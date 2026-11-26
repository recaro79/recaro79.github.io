import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parts import *
NAME = "s02_1주택비과세"; KEY = 2
BASIS = "소득세법 제89조, 같은 법 시행령 제154조·제160조 · 2026.11.26 현행 법령 기준"
SCENES = [
 cover("집 팔기 전에 꼭!", ["2년만 갖고 있으면", "양도세 0원?"], "양도세 절세 series 1편", "worry-doc-sweat", bg="bg-night", glow="#9fb6ff"),
 chat("상담실에서 자주 듣는 질문", "집 산 지 2년 넘었으니<br>팔아도 세금<br><span class='mk'>없는 거죠?</span>", "<span class='hl'>살 때</span> 어떤 지역이었는지<br>먼저 확인해야 해요!", "smile-magnify"),
 tiles("1세대1주택 비과세 기본 조건", "3가지 체크!", [
   ("양도일 현재", "1주택", "", "#3d8bff", "#e2eeff"),
   ("보유 기간", "2년", "이상", "#18b48a", "#dcf7ee"),
   ("파는 가격", "12억", "이하", "#ff9f2e", "#fff0dc")],
   "· 살 때 조정대상지역이었다면 <span class='hl'>2년 거주</span>도 필요해요"),
 ox("살 때 조정대상지역이던 집,<br>2년 보유만 하면<br>비과세?", "X", "보유기간 중 <span class='hl'>2년 이상 거주</span>까지<br>해야 비과세예요", "wow-none-sweat"),
 big("12억 넘는 집이라면?", "초과분만", "비율만큼 과세!", [
   ("공식", "#ff5c8a", "양도차익 × <span style='color:#e83e6f'>(양도가액−12억)</span><br>÷ 양도가액"),
   ("예시", "#ff9a3c", "15억에 팔면<br>차익의 <span style='color:#e8761e'>20%</span>에만 과세")],
   "장기보유특별공제도<br>같은 비율로 계산해요", "smile-calc"),
 ending("집 팔기 전 1분 체크", "계약 <span class='hl'>전에</span><br>물어보세요!"),
]
