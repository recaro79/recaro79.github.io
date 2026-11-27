import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 204
SLUG = 'mortgaged-property-valuation-special'
CAT = '증여세·상속세'
DATE = '2026-11-27'
TITLE = '대출(근저당)이나 전세보증금이 걸린 땅·건물을 증여·상속하신다면 — 기준시가보다 담보된 채권액이 크면 그 금액으로 평가합니다, 대출을 그대로 둔 채 증여하면 증여세가 커질 수 있습니다'
DESC = '저당권·근저당권·질권이 설정되거나 전세권이 등기된 재산, 임대보증금을 받고 임대한 재산은 그 재산이 담보하는 채권액(근저당은 평가기준일 현재 채권액, 채권최고액 한도)과 시가·보충적 평가액 중 큰 금액으로 평가합니다. 같은 재산이 여러 채권을 담보하면 합계액으로 합니다. 상속세 및 증여세법 제66조, 같은 법 시행령 제63조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '상속세 및 증여세법 제66조, 같은 법 시행령 제63조제1항·제2항, 같은 법 제47조제1항·제53조·제56조'
TAGS = ['저당권평가특례', '근저당', '증여재산평가', '상속재산평가', '임대보증금', '부산세무사']
ALTS = ['저당권 설정 재산 평가 (표지)', '저당권 설정 재산 평가 (상담 질문)', '저당권 설정 재산 평가 (대상 재산)', '저당권 설정 재산 평가 (O·X 퀴즈)', '저당권 설정 재산 평가 (세금 차이)', '저당권 설정 재산 평가 (확인할 점)', '저당권 설정 재산 평가 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
매매사례가 없는 땅이나 상가를 증여하실 때 보통 <b>기준시가</b>(공시가격)로 신고하시는 경우가 많습니다. 그런데 그 땅에 <b>은행 대출(근저당)</b>이 잡혀 있거나 <b>임대보증금</b>을 받고 세를 놓은 건물이라면 이야기가 달라집니다. 세법은 "은행이 이 재산을 담보로 그만큼 빌려줬다면 적어도 그 금액의 가치는 있다"고 보아, <b>담보된 채권액이 기준시가보다 크면 그 금액으로 평가</b>합니다. 오늘은 이 평가 특례를 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>저당권·근저당권이 설정되거나 전세권이 등기된 재산, <b>임대보증금</b>을 받고 임대한 재산은 <b>담보된 채권액</b>과 시가(없으면 기준시가 등) 중 <b>큰 금액</b>으로 평가합니다.</li><li>근저당은 평가기준일 현재 <b>실제 채권액</b>(채권최고액이 더 적으면 채권최고액)으로 보고, 대출과 보증금이 함께 있으면 <b>합계액</b>으로 봅니다.</li><li>부모님 대출을 그대로 둔 채 땅만 자녀에게 증여하면, 평가액은 커지는데 채무는 빼 주지 않아 <b>증여세가 늘어날 수 있습니다</b>.</li></ol>
<div class="small" style="margin-top:8px">(상속세 및 증여세법 제66조, 같은 법 시행령 제63조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"기준시가 2억 원짜리 땅을 아들에게 주려고 해요. 제 사업자금 대출 3억 원 담보로 잡혀 있는데, 대출은 제가 계속 갚을 거니까 증여세는 2억 원 기준으로 내면 되죠?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>오○○ 님(가칭)은 매매사례가 없는 토지(기준시가 <b>2억 원</b>)를 성인 아들에게 증여하려고 합니다. 이 토지에는 오○○ 님의 사업자금 대출을 담보하는 근저당이 설정되어 있고, 증여일 현재 대출 잔액(담보된 채권액)은 <b>3억 원</b>(채권최고액 3억 6천만 원)입니다. 대출은 아들이 인수하지 않고 오○○ 님이 계속 갚습니다. 이 경우 토지의 평가액은 기준시가 2억 원이 아니라 <b>3억 원</b>이 됩니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 평가 특례가 적용되는 재산과 평가액</h2>
<div class="tbl"><table>
<tr><th>재산</th><th>채권액 기준 평가액</th><th>근거</th></tr>
<tr><td>저당권이 설정된 재산</td><td>그 재산이 담보하는 채권액</td><td>시행령 제63조제1항제1호</td></tr>
<tr><td>공동저당권이 설정된 재산</td><td>담보 채권액을 공동저당 재산들의 평가기준일 현재 가액으로 안분</td><td>같은 항 제2호</td></tr>
<tr><td><b>근저당권</b>이 설정된 재산</td><td>평가기준일 현재 그 재산이 담보하는 채권액(채권최고액이 더 적으면 채권최고액)</td><td>같은 항 제3호, 같은 조 제2항</td></tr>
<tr><td>질권 설정 재산·양도담보재산</td><td>담보하는 채권액</td><td>같은 항 제4호</td></tr>
<tr><td>전세권 등기 재산, <b>임대보증금</b>을 받고 임대한 재산</td><td>등기된 전세금 또는 임대보증금</td><td>같은 항 제5호</td></tr>
<tr><td>채무 담보 목적 신탁계약 재산</td><td>우선수익자인 채권자에 대해 담보하는 채권액</td><td>같은 항 제6호</td></tr>
</table></div>
<p>위 금액과 일반 평가 방법(시가, 시가가 없으면 기준시가 등 보충적 평가액)으로 계산한 금액 중 <b>큰 금액</b>이 평가액입니다(법 제66조). 한 재산이 대출과 보증금 등 <b>여러 채권</b>을 담보하면 그 <b>합계액</b>을 기준으로 하고, 신용보증기관의 보증이 함께 있으면 보증금액을 뺍니다(시행령 제63조제2항). 세를 놓은 건물이라면 임대료 환산가액과의 비교도 함께 해야 합니다(<a href="/column/116-rental-property-valuation.html">칼럼 116</a>).</p>

<h2>2. 오○○ 님 사례 — 증여세 비교</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>기준시가로 착각한 경우</th><th>실제(근저당 채권액 평가)</th></tr>
<tr><td>증여재산가액</td><td>200,000,000</td><td><b>300,000,000</b></td></tr>
<tr><td>인수한 채무</td><td>−</td><td>−(아들이 인수하지 않음)</td></tr>
<tr><td>증여재산공제(성인 자녀)</td><td>△50,000,000</td><td>△50,000,000</td></tr>
<tr><td>과세표준</td><td>150,000,000</td><td>250,000,000</td></tr>
<tr><td>증여세 산출세액</td><td>20,000,000</td><td><b>40,000,000</b></td></tr>
</table></div>
<p>같은 땅인데 근저당 때문에 증여세가 <b>2천만 원</b> 더 나옵니다. 만약 아들이 대출 3억 원을 실제로 인수하는 <b>부담부증여</b>라면 그 채무만큼은 증여재산에서 빠지지만, 그 부분은 오○○ 님의 <b>양도소득세</b> 대상이 됩니다(<a href="/column/09-burdened-gift.html">칼럼 09</a>). 증여 전에 대출을 줄이거나 담보를 다른 재산으로 옮기는 방법도 함께 비교해 보셔야 합니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 매매·감정·유사매매사례 등 시가가 없고, 10년 이내 다른 증여는 없다고 가정했습니다. 세율은 상속세 및 증여세법 제56조(제26조 세율)를 적용했고 신고세액공제는 반영하지 않았습니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 증여·상속할 재산의 <b>등기부등본</b>에서 근저당·전세권·질권 설정 여부를 확인했다.</li>
<li>☐ 은행에서 평가기준일 현재 <b>대출 잔액</b>(담보된 채권액)과 <b>채권최고액</b>을 확인했다.</li>
<li>☐ 세를 놓은 재산이라면 <b>임대보증금</b>을 더해 계산했다.</li>
<li>☐ 대출을 자녀가 인수할지(부담부증여), 부모가 계속 갚을지 정하고 세금을 각각 비교했다.</li>
<li>☐ 상속이라면 같은 대출·보증금이 <b>채무로 공제</b>되는지도 함께 확인했다(<a href="/column/48-funeral-debt-deduction.html">칼럼 48</a>).</li>
</ul>
<p>기준시가만 보고 세금을 예상하시면 대출이나 보증금 때문에 계산이 크게 달라질 수 있습니다. 증여를 계획하고 계시면 등기부등본과 대출 내역을 가지고 편하게 상담해 주세요. 평가액부터 세금까지 정확히 계산해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>등기부등본</td><td>근저당·전세권 설정, 채권최고액</td></tr>
<tr><td>대출 잔액 증명서</td><td>평가기준일 현재 담보된 채권액</td></tr>
<tr><td>임대차계약서</td><td>임대보증금·월세</td></tr>
<tr><td>공시가격(기준시가) 자료</td><td>보충적 평가액과 비교</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-lilac">{HD()}
<div class="bokeh" style="left:90px;top:200px;width:120px;height:120px;background:#c9b8ff;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:250px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/worry-piggy-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">대출 잡힌 땅을 증여할 때</div><div class="t">기준시가로<br>신고하면 될까요?</div><div class="series">증여세 절세 series 6편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">증여 상담에서 자주 듣는 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">오○○ 님</div><div class="say">기준시가 2억 땅,<br>대출이 <span class="mk">3억</span> 있어도<br>2억으로 신고죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">큰 금액인<br><span class="hl">3억 원</span>으로<br>평가해요!</div></div>
<img class="ch" src="ch/smile-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">어떤 재산이? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">채권액과 비교하는 재산</div><div class="h1" style="margin-top:8px">평가 특례 대상</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx"><span style="color:#1f8a57">근저당·저당권</span><br>설정 재산</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx"><span style="color:#1b5fa8">전세권</span> 등기<br>재산</div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx"><span style="color:#c0392b">임대보증금</span> 받고<br>세 놓은 재산</div></div>
</div>
{FT(3, True, '상증법 제66조·시행령 제63조')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">근저당은 등기부의<br>채권최고액으로<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">무조건 평가한다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 그날 <b style="font-weight:900">실제 채권액</b>으로 봐요.<br>(채권최고액이 더 적으면 최고액)</div>
{FT(4, True, '시행령 제63조①3호·②')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">성인 자녀에게 토지 증여 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">평가액이 바뀌면</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>기준시가</small><b style="color:#2fa36b">2억</b></div><div class="op">vs</div><div class="bx"><small>근저당 채권액</small><b style="color:#ff5c8a">3억</b></div></div>
<div class="total" style="top:610px"><small>증여세 산출세액</small><b>2천만 → 4천만</b><span>큰 금액(3억 원)으로 평가</span></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 대출은 부모가 계속 상환<br>· 시가 없음, 공제 5천만 원</div>
{FT(5, True, '상증법 제66조·제53조·제56조')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">증여 전에</div><div class="h1" style="margin-top:8px">꼭 확인하세요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">등기부의<br><span style="color:#c0392b">근저당·전세권</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">은행의<br><span style="color:#b9770e">대출 잔액</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">대출 인수하면<br><span style="color:#1b5fa8">부담부증여</span></div></div>
</div>
{FT(6, True, '상증법 제66조·제47조①')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '대출 낀 재산 증여 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">평가액</span> 확인!'),
]
