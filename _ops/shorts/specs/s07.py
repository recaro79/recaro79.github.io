import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parts import *
NAME = "s07_생활비학비비과세"; KEY = -2
BASIS = "상속세 및 증여세법 제46조, 같은 법 시행령 제35조 · 2026.11.26 현행 법령 기준"
SCENES = [
 cover("부모님이 주신 등록금·생활비", ["이것도", "증여세 낼까?"], "증여세 절세 series 4편", "worry-calc-sweat", bg="bg-sunset", glow="#ffe3a0"),
 ox("부모님이 대신 내주신<br>대학 등록금,<br>증여세 낸다?", "X", "필요할 때 <span class='hl'>그 용도로 바로 쓴</span><br>교육비는 비과세예요", "wow-none", bg="bg-sky dk"),
 tiles("사회통념상 인정되는 범위라면", "이런 돈은 비과세", [
   ("피부양자 생활비·교육비", "OK", "", "#3d8bff", "#e2eeff"),
   ("치료비", "OK", "", "#18b48a", "#dcf7ee"),
   ("축하금·부의금 (통상 수준)", "OK", "", "#ff9f2e", "#fff0dc"),
   ("혼수용품 (통상 수준)", "OK", "", "#9a6bff", "#ece4ff")], ""),
 big("하지만 이렇게 쓰면", "과세!", "조심하세요", [
   ("저축", "#ef3f3f", "생활비로 받아<br><span style='color:#e0463c'>예금·적금</span>에 넣으면"),
   ("투자", "#ff9a3c", "받은 돈으로<br><span style='color:#e8761e'>주식·집</span>을 사면")],
   "'필요할 때마다, 그 용도에<br>직접' 쓰는 것이 핵심이에요", "worry-piggy-sweat", bg="bg-pink"),
 ending("애매하면 먼저 확인하세요", "증여 <span class='hl'>전에</span><br>물어보세요!"),
]
