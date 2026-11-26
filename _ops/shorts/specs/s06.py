import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parts import *
NAME = "s06_세대생략할증"; KEY = 3
BASIS = "상속세 및 증여세법 제26조·제53조·제56조·제57조 · 2026.11.26 현행 법령 기준"
SCENES = [
 cover("할아버지가 손주에게 바로 주면", ["증여세가", "30% 더?"], "증여세 절세 series 3편", "wow-piggy-sweat", bg="bg-forest", glow="#ffe08a"),
 chat("상담실에서 자주 듣는 질문", "할아버지께서 손자에게<br><span class='mk'>1억 5천만 원</span>을<br>주신다는데 괜찮을까요?", "세금이 <span class='hl'>30%</span><br>더 붙어요!", "wow-none", bg="bg-cream dk", topc="#a2652a"),
 tiles("세대를 건너뛰면 할증", "얼마나 더 낼까?", [
   ("손주에게 증여", "+30", "%", "#ff5c72", "#ffe3e7"),
   ("미성년 손주 · 20억 초과", "+40", "%", "#9a6bff", "#ece4ff")],
   "· 산출세액에 그만큼 더해져요<br>· 조부모님도 '부모' 공제(5천만 원) 그룹이에요"),
 compare("성인에게 1억 5천만 원 (가상 사례)", "자녀 vs 손주", ("아버지 → 자녀", "1,000만", "#3d8bff", 84), "vs", ("할아버지 → 손주", "1,300만", "#ff5c72", 84),
   "할증", "+300만 원", "신고세액공제 <span class='hl'>전</span> 기준",
   "<b style='color:#e0463c'>계산 기준</b><br>공제 5천만 원 뒤 과세표준 1억<br>산출세액 1,000만 원", "smile-calc"),
 ox("손주의 부모(자녀)가<br>먼저 돌아가셨다면<br>그래도 할증?", "X", "자녀가 사망해 손주가 받으면<br><span class='hl'>할증하지 않아요</span>", "smile-none"),
 ending("대를 건너뛴 증여, 따져 볼 게 많아요", "주시기 <span class='hl'>전에</span><br>상담하세요!"),
]
