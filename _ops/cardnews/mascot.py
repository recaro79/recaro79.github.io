# 사용법: python3 _ops/cardnews/mascot.py  → ch/ 폴더에 캐릭터 SVG 전체 생성 (표정-소품[-sweat].svg)
# 세무법인 인성 카드뉴스용 오리지널 캐릭터 (말랑한 3D 점토 느낌의 세무사 캐릭터)
# expr: smile / worry / wow / wink    prop: none / piggy / calc / doc / wave / thumb / magnify

def mascot(expr="smile", prop="none", sweat=False, glasses=True, uid="m"):
    u = uid
    defs = f'''
<defs>
 <radialGradient id="{u}skin" cx="38%" cy="30%" r="75%">
  <stop offset="0" stop-color="#fffdf7"/><stop offset=".55" stop-color="#f6eddc"/><stop offset="1" stop-color="#d9c6a6"/>
 </radialGradient>
 <radialGradient id="{u}skin2" cx="35%" cy="30%" r="80%">
  <stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#dcc9a8"/>
 </radialGradient>
 <linearGradient id="{u}suit" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2c4a86"/><stop offset="1" stop-color="#14254d"/>
 </linearGradient>
 <linearGradient id="{u}tie" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#ffd25a"/><stop offset="1" stop-color="#e0a21a"/>
 </linearGradient>
 <radialGradient id="{u}drop" cx="35%" cy="60%" r="70%">
  <stop offset="0" stop-color="#d6f1ff"/><stop offset=".6" stop-color="#6cc4f5"/><stop offset="1" stop-color="#2b8fd6"/>
 </radialGradient>
 <radialGradient id="{u}pig" cx="35%" cy="30%" r="80%">
  <stop offset="0" stop-color="#ffd3df"/><stop offset="1" stop-color="#f28aa6"/>
 </radialGradient>
 <radialGradient id="{u}shadow" cx="50%" cy="50%" r="50%">
  <stop offset="0" stop-color="#000" stop-opacity=".35"/><stop offset="1" stop-color="#000" stop-opacity="0"/>
 </radialGradient>
</defs>'''
    s = [f'<svg viewBox="0 0 400 470" xmlns="http://www.w3.org/2000/svg">', defs]
    s.append(f'<ellipse cx="200" cy="452" rx="135" ry="16" fill="url(#{u}shadow)"/>')
    # 몸통(정장)
    s.append(f'<path d="M95 455 C 88 360, 120 300, 200 298 C 280 300, 312 360, 305 455 Z" fill="url(#{u}suit)"/>')
    s.append('<path d="M168 300 L200 372 L232 300 Z" fill="#fbf7ef"/>')
    s.append(f'<path d="M193 312 L207 312 L214 330 L200 398 L186 330 Z" fill="url(#{u}tie)"/>')
    s.append('<path d="M150 304 L200 380 L176 400 Z" fill="#1d3466" opacity=".9"/><path d="M250 304 L200 380 L224 400 Z" fill="#1d3466" opacity=".9"/>')
    # 팔·소품
    left_arm = f'<ellipse cx="102" cy="388" rx="34" ry="46" fill="url(#{u}suit)" transform="rotate(18 102 388)"/><circle cx="96" cy="425" r="26" fill="url(#{u}skin2)"/>'
    right_arm = f'<ellipse cx="298" cy="388" rx="34" ry="46" fill="url(#{u}suit)" transform="rotate(-18 298 388)"/><circle cx="304" cy="425" r="26" fill="url(#{u}skin2)"/>'
    front = ''
    if prop == "wave":
        right_arm = f'<ellipse cx="318" cy="300" rx="30" ry="50" fill="url(#{u}suit)" transform="rotate(35 318 300)"/><circle cx="345" cy="250" r="27" fill="url(#{u}skin2)"/>' \
                    '<path d="M370 215 q14 -10 22 4 M378 240 q16 -4 18 10" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".9"/>'
    if prop == "thumb":
        right_arm = f'<ellipse cx="318" cy="330" rx="30" ry="48" fill="url(#{u}suit)" transform="rotate(30 318 330)"/><circle cx="340" cy="292" r="27" fill="url(#{u}skin2)"/>' \
                    f'<rect x="330" y="246" width="20" height="40" rx="10" fill="url(#{u}skin2)"/>'
    if prop == "piggy":
        front = f'''<g transform="translate(200 405)">
 <ellipse cx="0" cy="0" rx="78" ry="58" fill="url(#{u}pig)"/>
 <ellipse cx="70" cy="-2" rx="20" ry="17" fill="#f7a3b9"/><circle cx="64" cy="-3" r="4" fill="#b8576f"/><circle cx="76" cy="-3" r="4" fill="#b8576f"/>
 <path d="M-36 -50 l-10 -26 l26 10 Z" fill="#f28aa6"/><path d="M10 -56 l4 -26 l18 18 Z" fill="#f28aa6"/>
 <rect x="-22" y="-58" width="34" height="8" rx="4" fill="#9c3c58"/>
 <circle cx="38" cy="-18" r="6" fill="#3a2a2a"/><circle cx="40" cy="-20" r="2" fill="#fff"/>
 <ellipse cx="-30" cy="-22" rx="22" ry="12" fill="#fff" opacity=".35"/>
</g>
<g transform="translate(176 312)"><circle r="22" fill="#ffcf3f"/><circle r="16" fill="none" stroke="#d99a12" stroke-width="3"/><text x="0" y="8" text-anchor="middle" font-size="22" font-weight="900" fill="#b97f08" font-family="Noto Sans CJK KR,sans-serif">₩</text></g>'''
        left_arm = f'<ellipse cx="125" cy="395" rx="30" ry="40" fill="url(#{u}suit)" transform="rotate(40 125 395)"/>'
        right_arm = f'<ellipse cx="275" cy="395" rx="30" ry="40" fill="url(#{u}suit)" transform="rotate(-40 275 395)"/>'
        front += f'<circle cx="132" cy="420" r="24" fill="url(#{u}skin2)"/><circle cx="268" cy="420" r="24" fill="url(#{u}skin2)"/>'
    if prop in ("calc","doc"):
        left_arm = f'<ellipse cx="125" cy="395" rx="30" ry="40" fill="url(#{u}suit)" transform="rotate(40 125 395)"/>'
        right_arm = f'<ellipse cx="275" cy="395" rx="30" ry="40" fill="url(#{u}suit)" transform="rotate(-40 275 395)"/>'
    if prop == "calc":
        front = f'''<g transform="translate(200 400) rotate(-6)">
 <rect x="-62" y="-70" width="124" height="150" rx="18" fill="#3b3f4a"/><rect x="-50" y="-58" width="100" height="36" rx="8" fill="#c9f2c7"/>
 <text x="42" y="-31" text-anchor="end" font-size="24" font-weight="900" fill="#28502a" font-family="Noto Sans CJK KR,sans-serif">0원</text>
 {''.join(f'<rect x="{-50+c*35}" y="{-12+r*28}" width="28" height="22" rx="6" fill="{"#ffb43a" if c==2 else "#e9e9ef"}"/>' for r in range(3) for c in range(3))}
</g><circle cx="135" cy="430" r="25" fill="url(#{u}skin2)"/><circle cx="265" cy="430" r="25" fill="url(#{u}skin2)"/>'''
    if prop == "doc":
        front = f'''<g transform="translate(205 395) rotate(8)">
 <rect x="-60" y="-80" width="120" height="150" rx="10" fill="#fff"/>
 <rect x="-44" y="-58" width="88" height="10" rx="5" fill="#2c4a86"/>
 {''.join(f'<rect x="-44" y="{-36+i*20}" width="{88 if i%2 else 64}" height="8" rx="4" fill="#d5d9e4"/>' for i in range(4))}
 <circle cx="30" cy="48" r="16" fill="none" stroke="#e0463c" stroke-width="5"/>
</g><circle cx="140" cy="430" r="25" fill="url(#{u}skin2)"/><circle cx="270" cy="428" r="25" fill="url(#{u}skin2)"/>'''
    if prop == "magnify":
        right_arm = f'<ellipse cx="300" cy="380" rx="30" ry="44" fill="url(#{u}suit)" transform="rotate(-25 300 380)"/>'
        front = f'<g transform="translate(318 330)"><rect x="-9" y="30" width="18" height="70" rx="9" fill="#8a5a33" transform="rotate(-25)"/><circle r="48" fill="#dff3ff" fill-opacity=".55" stroke="#4a4f5e" stroke-width="12"/><ellipse cx="-16" cy="-16" rx="13" ry="7" fill="#fff" opacity=".85"/></g><circle cx="340" cy="415" r="25" fill="url(#{u}skin2)"/>'
    s.append(left_arm); s.append(right_arm)
    # 머리
    s.append(f'<circle cx="200" cy="165" r="150" fill="url(#{u}skin)"/>')
    s.append('<ellipse cx="150" cy="85" rx="48" ry="26" fill="#fff" opacity=".55" transform="rotate(-25 150 85)"/>')
    # 볼터치
    s.append('<ellipse cx="128" cy="205" rx="22" ry="12" fill="#ff9fae" opacity=".55"/><ellipse cx="272" cy="205" rx="22" ry="12" fill="#ff9fae" opacity=".55"/>')
    # 눈
    if expr == "wink":
        s.append('<ellipse cx="160" cy="175" rx="11" ry="15" fill="#2b2420"/><circle cx="163" cy="169" r="4" fill="#fff"/>')
        s.append('<path d="M226 176 q14 -14 28 0" stroke="#2b2420" stroke-width="7" fill="none" stroke-linecap="round"/>')
    elif expr == "wow":
        s.append('<ellipse cx="160" cy="172" rx="13" ry="18" fill="#2b2420"/><circle cx="164" cy="165" r="5" fill="#fff"/>')
        s.append('<ellipse cx="240" cy="172" rx="13" ry="18" fill="#2b2420"/><circle cx="244" cy="165" r="5" fill="#fff"/>')
    else:
        s.append('<ellipse cx="160" cy="175" rx="11" ry="15" fill="#2b2420"/><circle cx="163" cy="169" r="4" fill="#fff"/>')
        s.append('<ellipse cx="240" cy="175" rx="11" ry="15" fill="#2b2420"/><circle cx="243" cy="169" r="4" fill="#fff"/>')
    if expr == "worry":
        s.append('<path d="M140 140 l34 -8 M260 140 l-34 -8" stroke="#6b5a48" stroke-width="6" stroke-linecap="round"/>')
    # 안경
    if glasses:
        s.append('<g fill="none" stroke="#3a3130" stroke-width="6" opacity=".9"><circle cx="160" cy="175" r="34"/><circle cx="240" cy="175" r="34"/><path d="M194 172 q6 -6 12 0"/></g>')
        s.append('<ellipse cx="146" cy="160" rx="10" ry="5" fill="#fff" opacity=".6"/><ellipse cx="226" cy="160" rx="10" ry="5" fill="#fff" opacity=".6"/>')
    # 입
    mouth = {
        "smile": '<path d="M180 228 q20 22 40 0" stroke="#7a3b2e" stroke-width="7" fill="none" stroke-linecap="round"/>',
        "wink": '<path d="M176 226 q24 30 48 0 Z" fill="#a8412f"/><path d="M186 236 q14 10 28 0" fill="#ff8a8a"/>',
        "worry": '<path d="M182 238 q9 -10 18 0 q9 10 18 0" stroke="#7a3b2e" stroke-width="6" fill="none" stroke-linecap="round"/>',
        "wow": '<ellipse cx="200" cy="236" rx="14" ry="18" fill="#a8412f"/><ellipse cx="200" cy="244" rx="9" ry="7" fill="#ff8a8a"/>',
    }[expr]
    s.append(mouth)
    if sweat:
        s.append(f'<path d="M312 70 C 300 100, 288 118, 290 136 a 24 24 0 0 0 46 2 C 338 118, 326 100, 312 70 Z" fill="url(#{u}drop)"/>'
                 '<ellipse cx="303" cy="128" rx="5" ry="9" fill="#fff" opacity=".8"/>')
    s.append(front)
    s.append('</svg>')
    return "\n".join(s)


if __name__ == "__main__":
    import os
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ch")
    os.makedirs(d, exist_ok=True)
    n = 0
    for e in ["smile", "worry", "wow", "wink"]:
        for p in ["none", "piggy", "calc", "doc", "wave", "thumb", "magnify"]:
            for sw in (False, True):
                name = f"{e}-{p}{'-sweat' if sw else ''}.svg"
                open(os.path.join(d, name), "w", encoding="utf-8").write(mascot(e, p, sw, uid="m"))
                n += 1
    print(n, "files ->", d)
