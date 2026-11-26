# 쇼츠 장면 부품 — 각 함수는 (길이초, 배경class, HTML, [강조음 시각]) 을 돌려줍니다.
def d(t): return f"animation-delay:{t}s"

def cover(kick, lines, series, char, bg="bg-sunset", glow="#ffd08a"):
    t = 0.35
    ls = ""
    for ln in lines:
        ls += f'<div class="title pop" style="{d(t)}">{ln}</div>'; t += 0.35
    html = f"""
<div class="abs" style="left:0;right:0;top:0;height:1000px;background:radial-gradient(ellipse at 50% 55%,{glow}88,transparent 60%)"></div>
<img class="ch bob" src="ch/{char}.svg" style="left:190px;top:260px;width:700px">
<div class="abs" style="left:0;right:0;top:820px;height:1100px;background:linear-gradient(to bottom,rgba(20,14,40,0),rgba(20,14,40,.9) 30%,#140e28)"></div>
<div class="abs" style="left:60px;right:60px;top:{1060 - 70*(len(lines)-3)}px">
 <div class="kick hl up" style="{d(.1)}">{kick}</div><div style="margin-top:24px"></div>{ls}
 <div class="kick hl up" style="margin-top:36px;font-size:40px;{d(t+.1)}">{series}</div>
</div>"""
    return (3.2 + 0.35 * len(lines), bg, html, [])

def chat(top, q, a, char, bg="bg-mint dk", topc="#0f5a4c"):
    html = f"""
<div class="abs kick up" style="left:56px;top:200px;color:{topc};font-weight:900;{d(.05)}">{top}</div>
<div class="bub lf" style="left:56px;top:300px;width:900px;{d(.2)}"><div class="who">고객님</div><div class="say">{q}</div></div>
<div class="bub r rt" style="right:56px;top:860px;width:820px;{d(1.8)}"><div class="who">남기원 세무사</div><div class="say" style="font-size:62px">{a}</div></div>
<img class="ch pop" src="ch/{char}.svg" style="left:20px;top:1200px;width:460px;{d(2.2)}">"""
    return (5.2, bg, html, [1.8])

def tiles(kick, title, items, foot="", bg="bg-navy"):
    # items: [(라벨, 큰글씨, 단위, 글자색, 배경색)]
    h = ""; t = 0.6
    top = 470
    gap = 220 if len(items) <= 5 else 190
    for lab, big, unit, c, bgc in items:
        h += f'<div class="tile pop" style="top:{top}px;background:{bgc};{d(t)}"><div class="w">{lab}</div><div class="m" style="color:{c}">{big}<small>{unit}</small></div></div>'
        top += gap; t += 0.9
    f = f'<div class="abs up" style="left:56px;right:56px;top:{top+20}px;font-size:34px;font-weight:700;line-height:1.5;{d(t)}">{foot}</div>' if foot else ""
    html = f"""<div class="abs" style="left:56px;right:56px;top:190px"><div class="kick hl up" style="{d(.05)}">{kick}</div><div class="title up" style="font-size:88px;margin-top:10px;{d(.2)}">{title}</div></div>{h}{f}"""
    return (t + 2.0, bg, html, [])

def ox(q, ans, note, char, bg="bg-yellow dk"):
    mark = ('<svg width="240" height="240" viewBox="0 0 100 100"><path d="M18 18 L82 82 M82 18 L18 82" stroke="#ef3f3f" stroke-width="16" stroke-linecap="round"/></svg>' if ans == "X"
            else '<svg width="240" height="240" viewBox="0 0 100 100"><circle cx="50" cy="50" r="34" fill="none" stroke="#2f7bff" stroke-width="14"/></svg>')
    html = f"""
<div class="abs pop" style="left:56px;top:200px;background:#16213e;color:#ffd84a;font-size:44px;font-weight:900;padding:12px 34px;border-radius:50px;{d(.05)}">O X 퀴즈</div>
<div class="abs up" style="left:56px;right:56px;top:320px;font-size:78px;font-weight:900;line-height:1.3;letter-spacing:-2px;{d(.3)}">{q}</div>
<img class="ch" src="ch/{char}.svg" style="left:380px;top:720px;width:640px">
<div class="abs st" style="left:60px;top:780px;width:400px;height:400px;border-radius:50%;background:#fff;box-shadow:0 18px 40px rgba(120,80,0,.3);display:flex;align-items:center;justify-content:center;{d(2.0)}">{mark}</div>
<div class="note up" style="top:1290px;{d(2.7)}">정답은 <span class="hl">{ans}!</span><br>{note}</div>"""
    return (6.0, bg, html, [2.0])

def big(kick, bigtxt, sub, rows, note, char, bg="bg-pink", kc="#fff3c4"):
    # rows: [(아이콘글자, 색, 내용html)]
    r = ""; t = 1.4; top = 800
    for ic, c, tx in rows:
        r += f'<div class="row lf" style="top:{top}px;{d(t)}"><div class="ic" style="background:{c}">{ic}</div><div class="tx">{tx}</div></div>'
        top += 250; t += 0.8
    html = f"""
<div class="abs" style="left:56px;right:56px;top:200px"><div class="kick up" style="color:{kc};{d(.05)}">{kick}</div>
<div class="pop" style="font-size:150px;font-weight:900;letter-spacing:-6px;line-height:1.05;margin-top:10px;text-shadow:0 10px 24px rgba(0,0,0,.25);{d(.3)}">{bigtxt}</div>
<div class="up" style="font-size:84px;font-weight:900;letter-spacing:-3px;{d(.7)}">{sub}</div></div>
<img class="ch pop" src="ch/{char}.svg" style="right:20px;top:330px;width:400px;{d(.9)}">
{r}<div class="abs up" style="left:56px;right:56px;top:{top+30}px;font-size:44px;font-weight:800;line-height:1.5;{d(t)}">{note}</div>"""
    return (t + 2.4, bg, html, [])

def compare(kick, title, left, op, right, tot_label, tot_big, tot_sub, warn, char, bg="bg-sky dk", kc="#1b5fa8"):
    # left/right: (라벨, 값, 색)
    box = lambda x, pos, t: f'<div class="abs pop" style="{pos}:56px;top:470px;width:420px;background:#fff;border-radius:36px;padding:34px;text-align:center;box-shadow:0 12px 26px rgba(20,60,120,.15);{d(t)}"><div style="font-size:36px;font-weight:800;color:#5a6a80">{x[0]}</div><div style="font-size:{x[3] if len(x)>3 else 96}px;font-weight:900;color:{x[2]};letter-spacing:-3px">{x[1]}</div></div>'
    html = f"""
<div class="abs" style="left:56px;right:56px;top:200px"><div class="kick up" style="color:{kc};{d(.05)}">{kick}</div><div class="title up" style="font-size:86px;text-shadow:none;margin-top:8px;{d(.2)}">{title}</div></div>
{box(left,'left',.6)}<div class="abs pop" style="left:0;right:0;text-align:center;top:545px;font-size:{90 if len(op)<2 else 60}px;font-weight:900;{d(1.0)}">{op}</div>{box(right,'right',1.3)}
<div class="abs pop" style="left:56px;right:56px;top:790px;background:#16213e;border-radius:40px;padding:46px;color:#fff;{d(2.1)}"><div style="font-size:40px;font-weight:800;color:#ffd84a">{tot_label}</div><div style="font-size:112px;font-weight:900;letter-spacing:-4px;line-height:1.08">{tot_big}</div><div style="font-size:50px;font-weight:900;margin-top:12px">{tot_sub}</div></div>
<img class="ch pop" src="ch/{char}.svg" style="right:30px;top:1190px;width:370px;{d(2.8)}">
<div class="abs up" style="left:56px;width:600px;top:1230px;font-size:36px;font-weight:700;line-height:1.5;{d(3.3)}">{warn}</div>"""
    return (6.0, bg, html, [2.1])

def ending(kick, title, bg="bg-navy", char="smile-wave"):
    html = f"""
<div class="abs" style="left:0;right:0;top:200px;text-align:center"><div class="kick hl up" style="{d(.05)}">{kick}</div><div class="title pop" style="font-size:96px;margin-top:10px;{d(.3)}">{title}</div></div>
<img class="ch bob" src="ch/{char}.svg" style="left:330px;top:520px;width:420px">
<div class="abs up" style="left:56px;right:56px;top:1010px;background:#fff;color:#16213e;border-radius:40px;padding:44px 48px;{d(.9)}">
 <div style="display:flex;gap:30px;align-items:center"><img src="profile.jpg" style="width:160px;height:160px;border-radius:50%;object-fit:cover;border:6px solid #ffd84a"><div><div style="font-size:28px;font-weight:800;color:#a27b3a;letter-spacing:4px">지점대표세무사</div><div style="font-family:NM,serif;font-size:72px;font-weight:800;letter-spacing:8px">남기원</div><div style="font-size:30px;font-weight:700;color:#5a6a80">세무법인 인성 · 세무 경력 20년</div></div></div>
 <div style="margin-top:28px;border-top:2px solid #eee3cd;padding-top:26px;font-size:62px;font-weight:900">010-7741-4822</div>
 <div style="font-size:34px;font-weight:700;color:#5a6a80;margin-top:6px">카카오톡 상담 · 평일 09:00~18:00</div>
</div>
<div class="abs pop" style="left:56px;right:56px;top:1530px;text-align:center;font-size:46px;font-weight:900;{d(1.8)}">구독하고 <span class="hl">절세 팁</span> 매일 받아 가세요!</div>"""
    return (5.2, bg, html, [0.3])
