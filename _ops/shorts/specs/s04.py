import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parts import *
NAME = "s04_증여신고기한"; KEY = 5
BASIS = "상속세 및 증여세법 제53조·제56조·제68조·제69조, 국세기본법 제47조의2 · 2026.11.26 현행 법령 기준"
SCENES = [
 cover("증여받고 그냥 두면?", ["증여세 신고,", "언제까지 해야 할까?"], "증여세 절세 series 2편", "wow-doc-sweat", bg="bg-sunset", glow="#ffc0c8"),
 big("증여받은 달 말일부터", "3개월", "안에 신고!", [
   ("예시", "#ff5c8a", "3월 10일에 받았다면<br><span style='color:#e83e6f'>6월 30일</span>까지"),
   ("혜택", "#ff9a3c", "기한 안에 신고하면<br>세금 <span style='color:#e8761e'>3%</span> 공제")],
   "산출세액에서 3%를<br>빼 주는 신고세액공제예요", "smile-doc"),
 compare("성인 자녀가 부모님께 1억 5천만 원", "신고하면 vs 안 하면", ("기한 내 신고", "970만", "#3d8bff"), "vs", ("신고 안 하면", "1,200만", "#ff5c72"),
   "차이", "230만 원 +", "납부지연가산세는 <span class='hl'>별도</span>",
   "<b style='color:#e0463c'>계산 기준 (가상 사례)</b><br>공제 5천만 원 뒤 과세표준 1억<br>산출세액 1,000만 원", "wow-calc"),
 ox("공제 한도 안이라<br>낼 세금이 0원이면<br>안 해도 가산세 없다?", "O", "낼 세금이 없으면 가산세도 0원<br>그래도 <span class='hl'>자금출처 대비</span>로<br>신고해 두면 좋아요", "wink-thumb"),
 ending("증여 신고, 어렵지 않아요", "기한 <span class='hl'>전에</span><br>연락 주세요!"),
]
