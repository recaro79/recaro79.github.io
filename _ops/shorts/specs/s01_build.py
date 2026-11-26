# 유튜브 쇼츠 제작기 (1080x1920, 30fps) — 장면 HTML(CSS 애니메이션) → 프레임 캡처 → 장면별 mp4 → 이어붙이기 → 소리
import os, sys, subprocess, json
from playwright.sync_api import sync_playwright

W, H, FPS = 1080, 1920, 30
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = r"""
@font-face{font-family:NM;src:url(NanumMyeongjo-800.woff2);font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;font-family:"Noto Sans CJK KR",sans-serif;color:#fff;word-break:keep-all}
.sc{position:absolute;inset:0;overflow:hidden}
.dk{color:#16213e}
.bg-sunset{background:linear-gradient(160deg,#ff9a62 0%,#d35d7a 38%,#5b2f7a 70%,#1c1238 100%)}
.bg-mint{background:linear-gradient(170deg,#c9f5e4 0%,#8fe0c5 100%)}
.bg-navy{background:linear-gradient(170deg,#1d2f63 0%,#0e1733 100%)}
.bg-yellow{background:linear-gradient(170deg,#ffe46b 0%,#ffc93a 100%)}
.bg-pink{background:linear-gradient(165deg,#ff7aa0 0%,#f2557f 55%,#c93a6a 100%)}
.bg-sky{background:linear-gradient(170deg,#dff0ff 0%,#a9d4ff 100%)}
.top{position:absolute;left:0;right:0;top:0;height:10px;background:rgba(255,255,255,.25);z-index:9}
.top i{display:block;height:100%;background:#ffd84a}
.ver{position:absolute;left:56px;top:70px;font-size:36px;font-weight:900;text-shadow:0 3px 10px rgba(0,0,0,.3);z-index:5}
.brand{position:absolute;right:56px;top:62px;display:flex;align-items:center;gap:12px;font-family:NM,serif;font-size:34px;font-weight:800;z-index:5;text-shadow:0 2px 8px rgba(0,0,0,.3)}
.brand img{width:54px;height:54px;border-radius:50%;background:#fff;padding:3px}
.dk .ver,.dk .brand{text-shadow:none}
.basis{position:absolute;left:56px;right:56px;top:1560px;font-size:26px;font-weight:600;opacity:.8}
.hl{color:#ffd84a}
.abs{position:absolute}
.ch{position:absolute;display:block}
.mk{background:linear-gradient(transparent 58%,#ffe066 58%)}
/* 움직임 */
@keyframes pop{0%{transform:scale(.2);opacity:0}60%{transform:scale(1.12);opacity:1}100%{transform:scale(1);opacity:1}}
@keyframes up{0%{transform:translateY(80px);opacity:0}100%{transform:none;opacity:1}}
@keyframes left{0%{transform:translateX(-120px);opacity:0}100%{transform:none;opacity:1}}
@keyframes right{0%{transform:translateX(120px);opacity:0}100%{transform:none;opacity:1}}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-22px)}}
@keyframes stamp{0%{transform:scale(3) rotate(-20deg);opacity:0}70%{transform:scale(.9) rotate(4deg);opacity:1}100%{transform:scale(1) rotate(0);opacity:1}}
@keyframes zoom{0%{transform:scale(1)}100%{transform:scale(1.06)}}
@keyframes wig{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}
.a{opacity:0;animation-fill-mode:both}
.pop{animation:pop .5s cubic-bezier(.2,.9,.3,1.2) both}
.up{animation:up .45s ease-out both}
.lf{animation:left .45s ease-out both}
.rt{animation:right .45s ease-out both}
.st{animation:stamp .45s ease-out both}
.bob{animation:bob 1.6s ease-in-out infinite}
.wig{animation:wig 1.2s ease-in-out infinite}
/* 부품 */
.title{font-size:112px;font-weight:900;line-height:1.15;letter-spacing:-4px;text-shadow:0 8px 22px rgba(0,0,0,.45)}
.kick{font-size:46px;font-weight:800}
.bub{position:absolute;background:#fff;color:#1d2433;border-radius:50px 50px 50px 10px;padding:44px 50px;box-shadow:0 16px 34px rgba(0,40,60,.2)}
.bub.r{background:#14254d;color:#fff;border-radius:50px 50px 10px 50px}
.bub .who{font-size:30px;font-weight:800;color:#7a8794;margin-bottom:12px}
.bub.r .who{color:#ffd84a}
.bub .say{font-size:58px;font-weight:900;line-height:1.35;letter-spacing:-1px}
.tile{position:absolute;left:56px;right:56px;height:190px;border-radius:40px;padding:0 50px;display:flex;align-items:center;justify-content:space-between}
.tile .w{font-size:46px;font-weight:800;color:#2a3142}
.tile .m{font-size:112px;font-weight:900;letter-spacing:-4px}
.tile .m small{font-size:44px;letter-spacing:0}
.note{position:absolute;left:56px;right:56px;background:#16213e;color:#fff;border-radius:36px;padding:42px 46px;font-size:48px;font-weight:800;line-height:1.45}
.row{position:absolute;left:56px;right:56px;background:#fff;color:#2a1a24;border-radius:36px;padding:36px 40px;display:flex;gap:30px;align-items:center}
.row .ic{flex:none;width:120px;height:120px;border-radius:28px;display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:900;color:#fff}
.row .tx{font-size:48px;font-weight:800;line-height:1.35}
"""

def head(dk=False):
    return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'

def d(t):  # 애니메이션 시작 시각
    return f'animation-delay:{t}s'

BASIS = '근거: 상속세 및 증여세법 제53조·제53조의2 · 2026.11.26 현행 법령 기준'

SCENES = [
# (길이초, 배경class, 내용)
(3.6, "bg-sunset", f"""
<img class="ch bob" src="ch/worry-piggy-sweat.svg" style="left:190px;top:260px;width:700px">
<div class="abs" style="left:0;right:0;top:820px;height:1100px;background:linear-gradient(to bottom,rgba(20,14,40,0),rgba(20,14,40,.9) 30%,#140e28)"></div>
<div class="abs" style="left:60px;right:60px;top:1010px">
 <div class="kick hl up" style="{d(.1)}">부모님이 자녀에게 줄 때</div>
 <div class="title pop" style="margin-top:24px;{d(.35)}">세금 없이</div>
 <div class="title pop" style="{d(.7)}">얼마까지</div>
 <div class="title pop" style="{d(1.05)}">줄 수 있을까?</div>
 <div class="kick hl up" style="margin-top:36px;font-size:40px;{d(1.5)}">증여세 절세 series 1편</div>
</div>"""),
(5.0, "bg-mint dk", f"""
<div class="abs kick up" style="left:56px;top:200px;color:#0f5a4c;font-weight:900;{d(.05)}">상담실에서 자주 듣는 질문</div>
<div class="bub lf" style="left:56px;top:300px;width:880px;{d(.2)}"><div class="who">고객님</div><div class="say">아들이 결혼하는데<br><span class="mk">1억 5천만 원</span> 보태주면<br>세금 많이 나오나요?</div></div>
<div class="bub r rt" style="right:56px;top:830px;width:820px;{d(1.8)}"><div class="who">남기원 세무사</div><div class="say" style="font-size:62px">조건만 맞으면<br>증여세 <span class="hl">0원</span>일 수<br>있어요!</div></div>
<img class="ch pop" src="ch/wink-thumb.svg" style="left:20px;top:1180px;width:480px;{d(2.2)}">"""),
(7.0, "bg-navy", f"""
<div class="abs" style="left:56px;right:56px;top:190px"><div class="kick hl up" style="{d(.05)}">10년 동안 세금 없이 받는 금액</div><div class="title up" style="font-size:88px;margin-top:10px;{d(.2)}">증여재산공제</div></div>
<div class="tile pop" style="top:470px;background:#ffe3e7;{d(.6)}"><div class="w">배우자에게</div><div class="m" style="color:#ff5c72">6억<small>원</small></div></div>
<div class="tile pop" style="top:690px;background:#e2eeff;{d(1.6)}"><div class="w">부모 → 성인 자녀</div><div class="m" style="color:#3d8bff">5천만<small>원</small></div></div>
<div class="tile pop" style="top:910px;background:#dcf7ee;{d(2.6)}"><div class="w">부모 → 미성년 자녀</div><div class="m" style="color:#18b48a">2천만<small>원</small></div></div>
<div class="tile pop" style="top:1130px;background:#ece4ff;{d(3.6)}"><div class="w">자녀 → 부모</div><div class="m" style="color:#9a6bff">5천만<small>원</small></div></div>
<div class="tile pop" style="top:1350px;background:#fff0dc;{d(4.6)}"><div class="w">그 밖의 친족</div><div class="m" style="color:#ff9f2e">1천만<small>원</small></div></div>
<div class="basis up" style="top:1580px;font-size:30px;opacity:.9;{d(5.4)}">· '부모'에는 할아버지·할머니도 포함돼요</div>"""),
(5.6, "bg-yellow dk", f"""
<div class="abs pop" style="left:56px;top:200px;background:#16213e;color:#ffd84a;font-size:44px;font-weight:900;padding:12px 34px;border-radius:50px;{d(.05)}">O X 퀴즈</div>
<div class="abs up" style="left:56px;right:56px;top:320px;font-size:80px;font-weight:900;line-height:1.3;letter-spacing:-2px;{d(.3)}">아빠한테 5천만 원,<br>엄마한테 5천만 원이면<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">1억까지 세금 없다?</span></div>
<img class="ch" src="ch/wow-none-sweat.svg" style="left:380px;top:700px;width:640px">
<div class="abs st" style="left:60px;top:760px;width:400px;height:400px;border-radius:50%;background:#fff;box-shadow:0 18px 40px rgba(120,80,0,.3);display:flex;align-items:center;justify-content:center;{d(2.0)}"><svg width="240" height="240" viewBox="0 0 100 100"><path d="M18 18 L82 82 M82 18 L18 82" stroke="#ef3f3f" stroke-width="16" stroke-linecap="round"/></svg></div>
<div class="note up" style="top:1280px;{d(2.7)}">정답은 <span class="hl">X!</span><br>부모님·조부모님은 한 그룹이라<br><span class="hl">10년 합쳐서 5천만 원</span>까지만</div>"""),
(5.4, "bg-pink", f"""
<div class="abs" style="left:56px;right:56px;top:200px"><div class="kick up" style="color:#fff3c4;{d(.05)}">결혼·출산하는 자녀라면</div>
<div class="pop" style="font-size:170px;font-weight:900;letter-spacing:-6px;line-height:1.05;margin-top:10px;text-shadow:0 10px 24px rgba(120,0,40,.35);{d(.3)}">+1억 원</div>
<div class="up" style="font-size:96px;font-weight:900;letter-spacing:-3px;{d(.7)}">추가 공제!</div></div>
<img class="ch pop" src="ch/smile-wave.svg" style="right:20px;top:330px;width:420px;{d(.9)}">
<div class="row lf" style="top:800px;{d(1.4)}"><div class="ic" style="background:#ff5c8a">혼인</div><div class="tx">혼인신고일 <span style="color:#e83e6f">전후 2년</span> 안에<br>부모님께 받은 재산</div></div>
<div class="row lf" style="top:1050px;{d(2.2)}"><div class="ic" style="background:#ff9a3c">출산</div><div class="tx">자녀 출생일부터<br><span style="color:#e8761e">2년</span> 안에 받은 재산</div></div>
<div class="abs up" style="left:56px;right:56px;top:1330px;font-size:44px;font-weight:800;line-height:1.5;{d(3.0)}">기본 공제와 <span style="color:#fff3c4">따로!</span><br>혼인·출산 합쳐서 <span style="color:#fff3c4">1억 원 한도</span></div>"""),
(5.6, "bg-sky dk", f"""
<div class="abs" style="left:56px;right:56px;top:200px"><div class="kick up" style="color:#1b5fa8;{d(.05)}">결혼하는 성인 자녀는</div><div class="title up" style="font-size:86px;text-shadow:none;margin-top:8px;{d(.2)}">부모님께 최대</div></div>
<div class="abs pop" style="left:56px;top:470px;width:420px;background:#fff;border-radius:36px;padding:34px;text-align:center;box-shadow:0 12px 26px rgba(20,60,120,.15);{d(.6)}"><div style="font-size:36px;font-weight:800;color:#5a6a80">기본 공제</div><div style="font-size:96px;font-weight:900;color:#3d8bff;letter-spacing:-3px">5천만</div></div>
<div class="abs pop" style="left:496px;top:540px;font-size:110px;font-weight:900;{d(1.0)}">+</div>
<div class="abs pop" style="right:56px;top:470px;width:420px;background:#fff;border-radius:36px;padding:34px;text-align:center;box-shadow:0 12px 26px rgba(20,60,120,.15);{d(1.3)}"><div style="font-size:36px;font-weight:800;color:#5a6a80">혼인 공제</div><div style="font-size:96px;font-weight:900;color:#ff5c8a;letter-spacing:-3px">1억</div></div>
<div class="abs pop" style="left:56px;right:56px;top:780px;background:#16213e;border-radius:40px;padding:46px;color:#fff;{d(2.1)}"><div style="font-size:40px;font-weight:800;color:#ffd84a">합계</div><div style="font-size:130px;font-weight:900;letter-spacing:-5px;line-height:1.05">1억 5천만 원</div><div style="font-size:52px;font-weight:900;margin-top:12px">까지 증여세 <span class="hl" style="font-size:72px">0원</span></div></div>
<img class="ch pop" src="ch/smile-calc.svg" style="right:30px;top:1180px;width:380px;{d(2.8)}">
<div class="abs up" style="left:56px;width:600px;top:1220px;font-size:36px;font-weight:700;line-height:1.5;{d(3.3)}"><b style="color:#e0463c">꼭 확인!</b><br>최근 10년 안에 이미 쓴<br>공제가 있으면 그만큼 줄어요</div>"""),
(5.2, "bg-navy", f"""
<div class="abs" style="left:0;right:0;top:200px;text-align:center"><div class="kick hl up" style="{d(.05)}">증여는 '주고 나서'보다</div><div class="title pop" style="font-size:100px;margin-top:10px;{d(.3)}">주기 <span class="hl">전에</span><br>물어보세요!</div></div>
<img class="ch bob" src="ch/smile-wave.svg" style="left:330px;top:520px;width:420px">
<div class="abs up" style="left:56px;right:56px;top:1010px;background:#fff;color:#16213e;border-radius:40px;padding:44px 48px;{d(.9)}">
 <div style="display:flex;gap:30px;align-items:center"><img src="profile.jpg" style="width:160px;height:160px;border-radius:50%;object-fit:cover;border:6px solid #ffd84a"><div><div style="font-size:28px;font-weight:800;color:#a27b3a;letter-spacing:4px">지점대표세무사</div><div style="font-family:NM,serif;font-size:72px;font-weight:800;letter-spacing:8px">남기원</div><div style="font-size:30px;font-weight:700;color:#5a6a80">세무법인 인성 · 세무 경력 20년</div></div></div>
 <div style="margin-top:28px;border-top:2px solid #eee3cd;padding-top:26px;font-size:62px;font-weight:900">010-7741-4822</div>
 <div style="font-size:34px;font-weight:700;color:#5a6a80;margin-top:6px">카카오톡 상담 · 평일 09:00~18:00</div>
</div>
<div class="abs pop" style="left:56px;right:56px;top:1530px;text-align:center;font-size:46px;font-weight:900;{d(1.8)}">구독하고 <span class="hl">절세 팁</span> 매일 받아 가세요!</div>
<div class="abs up" style="left:56px;right:56px;top:1640px;text-align:center;font-size:24px;font-weight:600;opacity:.75;{d(1.2)}">{BASIS}</div>"""),
]

def page(i, dur, cls, inner, start, total):
    bar = f'<div class="top"><i id="bar" style="width:{start/total*100:.2f}%"></i></div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="sc {cls}">{bar}{head()}{inner}</div>
<script>window.T0={start};window.TT={total};</script></body></html>"""

def main():
    os.chdir(D)
    total = sum(s[0] for s in SCENES)
    os.makedirs("out", exist_ok=True)
    start = 0.0
    parts = []
    only = set(int(x) for x in sys.argv[1:] if x.isdigit())
    preview = "--preview" in sys.argv
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": W, "height": H})
        for i, (dur, cls, inner) in enumerate(SCENES, 1):
            html = page(i, dur, cls, inner, start, total)
            p = f"_scene{i}.html"; open(p, "w").write(html)
            pg.goto("file://" + os.path.abspath(p)); pg.wait_for_timeout(300)
            pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
            n = int(round(dur * FPS))
            if preview:
                for t in (dur * 0.98,):
                    pg.evaluate(f"(t=>{{document.getAnimations().forEach(a=>a.currentTime=t*1000);document.getElementById('bar').style.width=((T0+t)/TT*100)+'%'}})({t})")
                    pg.screenshot(path=f"out/prev{i}.jpg", type="jpeg", quality=85)
                start += dur; continue
            if only and i not in only:
                parts.append(f"out/scene{i}.mp4"); start += dur; continue
            tmp = f"out/scene{i}.tmp.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp], stdin=subprocess.PIPE)
            for f in range(n):
                t = f / FPS
                pg.evaluate(f"(t=>{{document.getAnimations().forEach(a=>a.currentTime=t*1000);document.getElementById('bar').style.width=((T0+t)/TT*100)+'%'}})({t})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close(); assert ff.wait() == 0
            os.replace(tmp, f"out/scene{i}.mp4")
            parts.append(f"out/scene{i}.mp4")
            start += dur
            print("scene", i, "ok", flush=True)
        b.close()
    if preview:
        return
    open("out/list.txt", "w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "out/list.txt", "-c", "copy", "out/video.mp4"], check=True)
    json.dump({"total": total, "starts": [sum(s[0] for s in SCENES[:k]) for k in range(len(SCENES))]}, open("out/timing.json", "w"))
    print("video ok", total)

if __name__ == "__main__":
    main()
