# 러닝 쇼츠용 캐릭터: 러닝복 입은 세무사 캐릭터(runner) + 헥헥 강아지(dog)
# python3 runner.py → ch/run-*.svg, ch/dog-*.svg 생성
import os

def _head(u, expr, sweat, extra_drops=False):
    s = [f'<circle cx="200" cy="165" r="150" fill="url(#{u}skin)"/>',
         '<ellipse cx="150" cy="85" rx="48" ry="26" fill="#fff" opacity=".55" transform="rotate(-25 150 85)"/>',
         '<ellipse cx="128" cy="205" rx="22" ry="12" fill="#ff8f9f" opacity=".7"/><ellipse cx="272" cy="205" rx="22" ry="12" fill="#ff8f9f" opacity=".7"/>']
    if expr == "wink":
        s.append('<ellipse cx="160" cy="175" rx="11" ry="15" fill="#2b2420"/><circle cx="163" cy="169" r="4" fill="#fff"/><path d="M226 176 q14 -14 28 0" stroke="#2b2420" stroke-width="7" fill="none" stroke-linecap="round"/>')
    elif expr == "focus":
        s.append('<path d="M146 170 q14 10 28 0 M226 170 q14 10 28 0" stroke="#2b2420" stroke-width="8" fill="none" stroke-linecap="round"/>')
    else:
        s.append('<ellipse cx="160" cy="175" rx="11" ry="15" fill="#2b2420"/><circle cx="163" cy="169" r="4" fill="#fff"/><ellipse cx="240" cy="175" rx="11" ry="15" fill="#2b2420"/><circle cx="243" cy="169" r="4" fill="#fff"/>')
    s.append('<g fill="none" stroke="#3a3130" stroke-width="6" opacity=".9"><circle cx="160" cy="175" r="34"/><circle cx="240" cy="175" r="34"/><path d="M194 172 q6 -6 12 0"/></g>')
    s.append({"smile": '<path d="M176 226 q24 30 48 0 Z" fill="#a8412f"/>',
              "wink": '<path d="M176 226 q24 30 48 0 Z" fill="#a8412f"/><path d="M186 236 q14 10 28 0" fill="#ff8a8a"/>',
              "focus": '<ellipse cx="200" cy="234" rx="16" ry="12" fill="#a8412f"/>',
              "wow": '<ellipse cx="200" cy="236" rx="14" ry="18" fill="#a8412f"/>'}[expr])
    # 머리띠
    s.append(f'<path d="M58 118 Q200 40 342 118 L338 150 Q200 76 62 150 Z" fill="url(#{u}band)"/><path d="M336 128 q36 -6 54 18 q-30 -2 -46 10 Z" fill="#e8402f"/><path d="M340 140 q28 18 40 46 q-26 -14 -46 -22 Z" fill="#ff6a3d"/>')
    if sweat:
        drop = lambda x, y, k: f'<g transform="translate({x} {y}) scale({k})"><path d="M0 0 C -12 30, -24 48, -22 66 a 24 24 0 0 0 46 2 C 26 48, 12 30, 0 0 Z" fill="url(#{u}drop)"/><ellipse cx="-9" cy="58" rx="5" ry="9" fill="#fff" opacity=".8"/></g>'
        s.append(drop(318, 78, 1))
        if extra_drops:
            s.append(drop(70, 120, .6) + drop(350, 200, .5) + drop(40, 240, .45))
    return s

def runner(expr="smile", sweat=False, pose="run", uid="r"):
    u = uid
    defs = f'''<defs>
 <radialGradient id="{u}skin" cx="38%" cy="30%" r="75%"><stop offset="0" stop-color="#fffdf7"/><stop offset=".55" stop-color="#f6eddc"/><stop offset="1" stop-color="#d9c6a6"/></radialGradient>
 <radialGradient id="{u}skin2" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#dcc9a8"/></radialGradient>
 <linearGradient id="{u}shirt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff8a3d"/><stop offset="1" stop-color="#f05a24"/></linearGradient>
 <linearGradient id="{u}band" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ff5a4a"/><stop offset="1" stop-color="#e8402f"/></linearGradient>
 <radialGradient id="{u}drop" cx="35%" cy="60%" r="70%"><stop offset="0" stop-color="#d6f1ff"/><stop offset=".6" stop-color="#6cc4f5"/><stop offset="1" stop-color="#2b8fd6"/></radialGradient>
 <radialGradient id="{u}shadow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#000" stop-opacity=".35"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
</defs>'''
    s = ['<svg viewBox="0 0 400 470" xmlns="http://www.w3.org/2000/svg">', defs,
         f'<ellipse cx="200" cy="452" rx="135" ry="16" fill="url(#{u}shadow)"/>']
    # 팔(뒤쪽)
    if pose == "run":
        s.append(f'<g><rect x="70" y="320" width="56" height="90" rx="28" fill="url(#{u}skin2)" transform="rotate(-40 98 330)"/><circle cx="52" cy="290" r="26" fill="url(#{u}skin2)"/></g>')
    else:  # 만세
        s.append(f'<rect x="60" y="230" width="52" height="100" rx="26" fill="url(#{u}skin2)" transform="rotate(25 86 330)"/><circle cx="56" cy="215" r="27" fill="url(#{u}skin2)"/>')
    # 몸통(싱글렛) + 배번
    s.append(f'<path d="M95 455 C 88 360, 120 300, 200 298 C 280 300, 312 360, 305 455 Z" fill="url(#{u}shirt)"/>')
    s.append('<path d="M150 302 q50 40 100 0" fill="none" stroke="#fff" stroke-width="8" opacity=".85"/>')
    s.append('<rect x="148" y="350" width="104" height="72" rx="8" fill="#fff"/><rect x="148" y="350" width="104" height="14" rx="6" fill="#2c4a86"/>'
             '<text x="200" y="410" text-anchor="middle" font-size="40" font-weight="900" fill="#14254d" font-family="Noto Sans CJK KR,sans-serif">42</text>')
    for x, y in ((156, 357), (244, 357), (156, 414), (244, 414)):
        s.append(f'<circle cx="{x}" cy="{y}" r="3" fill="#c9a96a"/>')
    # 팔(앞쪽)
    if pose == "run":
        s.append(f'<rect x="276" y="300" width="56" height="96" rx="28" fill="url(#{u}skin2)" transform="rotate(35 304 310)"/><circle cx="326" cy="390" r="27" fill="url(#{u}skin2)"/>')
    else:
        s.append(f'<rect x="288" y="230" width="52" height="100" rx="26" fill="url(#{u}skin2)" transform="rotate(-25 314 330)"/><circle cx="344" cy="215" r="27" fill="url(#{u}skin2)"/>')
    s += _head(u, expr, sweat, extra_drops=sweat)
    # 속도선
    if pose == "run":
        s.append('<g stroke="#fff" stroke-width="7" stroke-linecap="round" opacity=".75"><path d="M8 150 h40"/><path d="M0 200 h56"/><path d="M14 250 h34"/></g>')
    s.append('</svg>')
    return "\n".join(s)

def dog(uid="d", hot=True):
    u = uid
    return f'''<svg viewBox="0 0 400 420" xmlns="http://www.w3.org/2000/svg"><defs>
 <radialGradient id="{u}fur" cx="40%" cy="30%" r="80%"><stop offset="0" stop-color="#ffe2b8"/><stop offset="1" stop-color="#e3a564"/></radialGradient>
 <radialGradient id="{u}shadow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#000" stop-opacity=".3"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient></defs>
<ellipse cx="200" cy="402" rx="130" ry="14" fill="url(#{u}shadow)"/>
<path d="M90 400 C 80 300, 120 260, 200 258 C 280 260, 320 300, 310 400 Z" fill="url(#{u}fur)"/>
<path d="M70 70 C 30 90, 30 200, 80 220 C 100 170, 100 110, 70 70 Z" fill="#b8733a"/>
<path d="M330 70 C 370 90, 370 200, 320 220 C 300 170, 300 110, 330 70 Z" fill="#b8733a"/>
<ellipse cx="200" cy="160" rx="135" ry="125" fill="url(#{u}fur)"/>
<ellipse cx="200" cy="215" rx="70" ry="52" fill="#fff4e4"/>
<ellipse cx="150" cy="140" rx="13" ry="17" fill="#2b2420"/><circle cx="154" cy="134" r="5" fill="#fff"/>
<ellipse cx="250" cy="140" rx="13" ry="17" fill="#2b2420"/><circle cx="254" cy="134" r="5" fill="#fff"/>
<ellipse cx="200" cy="188" rx="22" ry="15" fill="#3a2a2a"/>
<path d="M176 212 q24 22 48 0" fill="#7a2e2e"/>
<path d="M186 220 C 184 270, 216 270, 214 220 Z" fill="#ff7a8a"/><path d="M200 224 v28" stroke="#e0566a" stroke-width="3"/>
{'<g fill="#ff6a3d" opacity=".9"><path d="M60 40 q10 -24 20 0 q-10 14 -20 0Z"/><path d="M330 30 q10 -24 20 0 q-10 14 -20 0Z"/></g>' if hot else ''}
</svg>'''

if __name__ == "__main__":
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ch")
    os.makedirs(d, exist_ok=True)
    for e in ["smile", "wink", "focus", "wow"]:
        for sw in (False, True):
            for pose in ("run", "cheer"):
                open(os.path.join(d, f"run-{pose}-{e}{'-sweat' if sw else ''}.svg"), "w").write(runner(e, sw, pose))
    open(os.path.join(d, "dog-pant.svg"), "w").write(dog())
    print("ok")
