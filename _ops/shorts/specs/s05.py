import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parts import *
NAME = "s05_배우자증여이월과세"; KEY = 0
BASIS = "상속세 및 증여세법 제53조, 소득세법 제97조의2 · 2026.11.26 현행 법령 기준"
SCENES = [
 cover("아내에게 증여하고 팔면", ["양도세가", "줄어들까?"], "양도세 절세 series 2편", "wow-none-sweat", bg="bg-night", glow="#ffd08a"),
 ox("배우자에게는<br>10년간 6억 원까지<br>증여세가 없다?", "O", "배우자 증여재산공제는<br><span class='hl'>10년 합산 6억 원</span>이에요", "wink-thumb", bg="bg-mint dk"),
 big("그런데 함정이 있어요!", "10년", "안에 팔면", [
   ("기준", "#ff5c8a", "증여받은 가격이 아니라<br><span style='color:#e83e6f'>처음 산 가격</span>으로 계산"),
   ("대상", "#ff9a3c", "토지·건물 등<br>(주식은 <span style='color:#e8761e'>1년</span>)")],
   "낸 증여세는<br>필요경비로 빼 줘요", "worry-none-sweat"),
 compare("남편이 3억에 산 땅 → 시가 6억에 증여 (가상 사례)", "아내가 8억에 판다면", ("10년 지나 매도", "2억", "#18b48a"), "vs", ("10년 안에 매도", "5억", "#ff5c72"),
   "양도차익 차이", "3억 원", "<span class='hl'>언제 파느냐</span>가 중요해요",
   "<b style='color:#e0463c'>꼭 확인!</b><br>세금이 더 적게 나오는 경우 등<br>예외가 있어 상담이 필요해요", "smile-calc"),
 ending("증여와 양도는 순서가 중요해요", "팔기 <span class='hl'>전에</span><br>물어보세요!"),
]
