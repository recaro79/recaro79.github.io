# 쇼츠 엔진: python3 engine.py <spec.py>  → out/<NAME>/final.mp4
# spec.py: NAME, BASIS, SCENES = [parts.cover(...), parts.chat(...), ...]
import os, sys, subprocess, json, runpy, shutil
from playwright.sync_api import sync_playwright
from engine_css import CSS

W, H, FPS = 1080, 1920, 30
D = os.path.dirname(os.path.abspath(__file__))

def head(ver='2026 Ver.'):
    return f'<div class="ver">{ver}</div><div class="brand"><img src="mark.png">세무법인 인성</div>'

def page(cls, inner, start, total, ver='2026 Ver.'):
    bar = f'<div class="top"><i id="bar" style="width:{start/total*100:.2f}%"></i></div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="sc {cls}">{bar}{head(ver)}{inner}</div><script>window.T0={start};window.TT={total};</script></body></html>"""

SEEK = "(t=>{document.getAnimations().forEach(a=>a.currentTime=t*1000);document.getElementById('bar').style.width=((T0+t)/TT*100)+'%'})"

def render(spec_path, preview=False):
    S = runpy.run_path(spec_path)
    name, scenes, basis = S["NAME"], S["SCENES"], S["BASIS"]
    # 마지막 장면에 근거 문구 넣기
    dur, cls, inner, acc = scenes[-1]
    scenes[-1] = (dur, cls, inner + f'<div class="abs up" style="left:56px;right:56px;top:1615px;text-align:center;font-size:24px;font-weight:600;opacity:.75;animation-delay:1.2s">{S.get("BASIS_LABEL", "근거")}: {basis}</div>', acc)
    od = os.path.join(D, "out", name); os.makedirs(od, exist_ok=True)
    total = sum(s[0] for s in scenes)
    starts = [sum(s[0] for s in scenes[:k]) for k in range(len(scenes))]
    parts = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": W, "height": H})
        for i, (dur, cls, inner, acc) in enumerate(scenes, 1):
            p = os.path.join(D, f"_{name}_{i}.html")
            open(p, "w", encoding="utf-8").write(page(cls, inner, starts[i-1], total, S.get('VER', '2026 Ver.')))
            pg.goto("file://" + p); pg.wait_for_timeout(300)
            pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
            if preview:
                pg.evaluate(f"{SEEK}({dur*0.98})")
                pg.screenshot(path=f"{od}/prev{i}.jpg", type="jpeg", quality=85)
                os.remove(p); continue
            tmp = f"{od}/scene{i}.tmp.mp4"
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp], stdin=subprocess.PIPE)
            for f in range(int(round(dur * FPS))):
                pg.evaluate(f"{SEEK}({f/FPS})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close(); assert ff.wait() == 0
            os.replace(tmp, f"{od}/scene{i}.mp4"); parts.append(f"scene{i}.mp4"); os.remove(p)
        b.close()
    if preview:
        from PIL import Image
        ims = [Image.open(f"{od}/prev{i}.jpg") for i in range(1, len(scenes)+1)]
        w, h = 270, 480; sh = Image.new("RGB", (len(ims)*(w+10)+10, h+20), "#eee")
        for i, im in enumerate(ims): sh.paste(im.resize((w, h)), (10+i*(w+10), 10))
        sh.save(f"{od}/prev_sheet.jpg"); return
    open(f"{od}/list.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{od}/list.txt", "-c", "copy", f"{od}/video.mp4"], check=True)
    accents = [[i+1, t] for i, s in enumerate(scenes) for t in s[3]]
    json.dump({"total": total, "starts": starts}, open(f"{od}/timing.json", "w"))
    subprocess.run(["python3", os.path.join(D, "sound.py"), json.dumps(accents), od, str(S.get("KEY", 0))], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{od}/video.mp4", "-i", f"{od}/bgm.wav", "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", f"{od}/final.tmp.mp4"], check=True)
    os.replace(f"{od}/final.tmp.mp4", f"{od}/final.mp4")
    print("OK", name, round(total, 1), "s")

if __name__ == "__main__":
    render(sys.argv[1], preview="--preview" in sys.argv)
