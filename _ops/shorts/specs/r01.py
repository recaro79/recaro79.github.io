import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parts import *
NAME = "r01_인간은타고난러너"; KEY = 7
VER = "RUN TIP"
BASIS_LABEL = "참고"
BASIS = "Bramble·Lieberman, Nature(2004) · Bramble·Carrier, Science(1983) · Liebenberg, Current Anthropology(2006)"

# 비밀 ① 땀: 사람 vs 강아지 (전용 장면)
def sweat_vs():
    html = f"""
<div class="abs" style="left:56px;right:56px;top:190px"><div class="kick hl up" style="{d(.05)}">비밀 ①</div><div class="title up" style="font-size:96px;margin-top:6px;{d(.2)}">온몸으로 땀 쫙!</div></div>
<div class="abs pop" style="left:40px;top:470px;width:480px;background:rgba(255,255,255,.12);border-radius:40px;padding:20px 10px 30px;text-align:center;{d(.6)}">
 <img class="jog" src="ch/run-run-smile-sweat.svg" style="width:380px;display:block;margin:0 auto">
 <div style="font-size:48px;font-weight:900;margin-top:10px">사람</div><div style="font-size:36px;font-weight:700;color:#bff0ff;margin-top:6px">땀으로 온몸 식힘</div></div>
<div class="abs pop" style="right:40px;top:470px;width:480px;background:rgba(255,255,255,.12);border-radius:40px;padding:20px 10px 30px;text-align:center;{d(1.4)}">
 <img class="pant" src="ch/dog-pant.svg" style="width:360px;display:block;margin:0 auto">
 <div style="font-size:48px;font-weight:900;margin-top:10px">강아지</div><div style="font-size:36px;font-weight:700;color:#ffd0b0;margin-top:6px">헥헥! 혀·입으로만</div></div>
<div class="abs pop" style="left:600px;top:420px;font-size:64px;font-weight:900;color:#ffd84a;transform:rotate(12deg);{d(1.9)}">헥헥!</div>
<div class="note up" style="top:1180px;background:#fff;color:#16213e;{d(2.6)}">털 대신 땀샘이 많은 사람은<br><span style="color:#e05a24">더운 날 오래 달려도</span> 덜 지쳐요</div>"""
    return (6.0, "bg-night", html, [1.4])

_t = tiles("비밀 ② 숨쉬기", "걸음 vs 숨 리듬", [
   ("네 발로 뛰는 동물", "1:1", "고정", "#ff5c72", "#ffe3e7"),
   ("두 발로 뛰는 사람", "2:1", "자유", "#18b48a", "#dcf7ee")],
   "· 동물은 한 걸음에 숨 한 번으로 묶여 있어요<br>· 사람은 2:1, 3:1… 리듬을 골라 쓸 수 있어요", bg="bg-forest")
breath = (_t[0], _t[1], _t[2] + '<img class="ch jog" src="ch/run-run-focus-sweat.svg" style="left:290px;top:1020px;width:500px">', _t[3])

SCENES = [
 cover("달리기 좋아하세요?", ["인간은", "타고난 러너?"], "러닝 series 1편", "run-run-smile-sweat", bg="bg-orange", glow="#fff0b0", anim="jog"),
 ox("단거리는 동물에게 지지만<br><span style='background:linear-gradient(transparent 60%,#fff 60%)'>오래 달리기</span>는<br>사람이 강하다?", "O", "치타·말보다 느려도 오래 달리기는<br><span class='hl'>최상위권</span>! 비밀은 4가지", "run-cheer-wink", bg="bg-yellow dk"),
 sweat_vs(),
 breath,
 big("비밀 ③ 아킬레스건", "용수철", "역할을 해요", [
   ("착지", "#ff5c8a", "땅에 닿을 때<br><span style='color:#e83e6f'>힘을 모았다가</span>"),
   ("도약", "#ff9a3c", "다음 걸음에<br><span style='color:#e8761e'>튕겨 줘요</span>")],
   "그래서 오래 뛰어도<br>힘이 덜 들어요", "run-run-focus-sweat", bg="bg-pink"),
 ox("개는 달릴 때<br>머리를 잡아 주는<br>목덜미 인대가 없다?", "X", "개·말도 있어요! 없는 건 돼지·침팬지<br>유인원 중엔 <span class='hl'>사람만</span> 있어요", "run-run-wow", bg="bg-sky dk"),
 big("그래서 생긴 옛 사냥법", "끝까지", "쫓아가기!", [
   ("실제", "#2f7bff", "칼라하리 사막 사냥꾼들이<br>한낮에 영양을 <span style='color:#2f7bff'>지칠 때까지</span>"),
   ("핵심", "#18b48a", "더위 속에서 땀 흘리며<br><span style='color:#12936f'>버틴 쪽</span>이 이겨요")],
   "'지구력 사냥'이라고 불러요", "run-run-smile-sweat", bg="bg-orange", kc="#fff3c4"),
 ending("달리는 세무사의 러닝 상식", "세금도 달리기도<br><span class='hl'>꾸준함</span>이 이깁니다!", char="run-cheer-wink", sub="구독하고 <span class='hl'>러닝·절세 팁</span> 받아 가세요!"),
]
