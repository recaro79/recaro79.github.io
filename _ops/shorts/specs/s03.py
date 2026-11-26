import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parts import *
NAME = "s03_상속공제10억"; KEY = -3
BASIS = "상속세 및 증여세법 제19조·제21조 · 2026.11.26 현행 법령 기준"
SCENES = [
 cover("부모님 재산이 10억이라면", ["상속세,", "우리 집도 낼까?"], "상속세 절세 series 1편", "worry-calc-sweat", bg="bg-forest", glow="#bff5d8"),
 tiles("배우자·자녀가 함께 상속받으면", "기본으로 빼 주는 금액", [
   ("일괄공제", "5억", "원", "#3d8bff", "#e2eeff"),
   ("배우자공제 (최소)", "5억", "원", "#ff5c72", "#ffe3e7"),
   ("합계", "10억", "원", "#18b48a", "#dcf7ee")],
   "· 배우자가 실제 많이 받으면 최대 30억까지 늘어요<br>· 사전 증여·채무 등에 따라 달라질 수 있어요"),
 ox("배우자 혼자<br>전부 상속받아도<br>일괄공제 5억?", "X", "배우자 <span class='hl'>단독 상속</span>이면<br>기초공제+인적공제만 돼요", "wow-none-sweat", bg="bg-lilac dk"),
 big("배우자공제 제대로 받으려면", "9개월", "안에 나누세요!", [
   ("기한", "#ff5c8a", "신고기한 다음 날부터<br><span style='color:#e83e6f'>9개월</span> 안에 분할"),
   ("등기", "#ff9a3c", "등기·명의개서까지<br><span style='color:#e8761e'>마쳐야</span> 인정")],
   "분할 사실도 세무서에<br>신고해야 해요", "smile-doc", bg="bg-orange"),
 ending("상속세는 준비한 만큼 줄어요", "미리 <span class='hl'>상담</span><br>받아 보세요!"),
]
