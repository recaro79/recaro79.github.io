import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 224
SLUG = 'vat-on-remaining-assets-at-closure'
CAT = '부가가치세'
DATE = '2026-11-27'
TITLE = '상가 임대사업을 폐업하신다면 — 부가세를 환급받았던 건물은 폐업할 때 나에게 판 것으로 보고 부가세를 냅니다, 취득가액 × (1 − 5% × 지난 과세기간 수), 10년(20과세기간)이 지나면 0원'
DESC = '사업자가 폐업할 때 매입세액을 공제받은 재화가 남아 있으면 자기에게 공급한 것으로 보아 부가가치세가 과세됩니다. 건물·구축물은 취득가액 × (1 − 5% × 경과된 과세기간 수), 그 밖의 감가상각자산은 취득가액 × (1 − 25% × 경과된 과세기간 수)가 공급가액이며, 경과 과세기간 수는 건물 20, 그 밖의 자산 4가 한도입니다. 사업양도에 해당하면 재화의 공급으로 보지 않습니다. 부가가치세법 제10조, 같은 법 시행령 제66조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '부가가치세법 제10조제1항·제6항·제9항제2호, 같은 법 시행령 제66조제2항·제4항·제5항'
TAGS = ['폐업부가세', '잔존재화', '상가임대', '간주공급', '부가가치세', '부산세무사']
ALTS = ['폐업 시 잔존재화 부가세 (표지)', '폐업 시 잔존재화 부가세 (상담 질문)', '폐업 시 잔존재화 부가세 (계산식)', '폐업 시 잔존재화 부가세 (O·X 퀴즈)', '폐업 시 잔존재화 부가세 (사례 계산)', '폐업 시 잔존재화 부가세 (확인할 점)', '폐업 시 잔존재화 부가세 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"상가 세입자가 나가서 임대사업을 접으려고 해요. 폐업 신고만 하면 되죠?" 상가를 분양받거나 사면서 <b>건물분 부가세를 환급받으셨던</b> 분이라면 꼭 확인하셔야 할 것이 있습니다. 폐업할 때 그 건물이 남아 있으면 세법은 <b>사업자가 자기에게 건물을 판 것</b>으로 보고 부가세를 매깁니다. 오늘은 이 '폐업 시 잔존재화' 부가세를 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>폐업할 때 <b>매입세액을 공제(환급)받은 재화</b>가 남아 있으면 자기에게 공급한 것으로 보아 <b>부가세</b>를 냅니다.</li><li>건물·구축물의 공급가액은 <b>취득가액 × (1 − 5% × 경과된 과세기간 수)</b>입니다. 과세기간은 6개월 단위이므로 <b>10년(20과세기간)</b>이 지나면 0원이 됩니다.</li><li>사업을 통째로 넘기는 <b>사업양도</b>에 해당하면 재화의 공급으로 보지 않으므로, 폐업 대신 다른 방법이 있는지도 따져 보셔야 합니다.</li></ol>
<div class="small" style="margin-top:8px">(부가가치세법 제10조제6항·제9항, 같은 법 시행령 제66조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"상가를 살 때 돌려받은 건물분 부가세, 폐업하면 다시 내야 하나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>오○○ 님(가칭)은 <b>2021년 3월</b>에 상가를 사면서 건물분 공급가액 <b>5억 원</b>에 대한 부가세 5천만 원을 환급받고 일반과세자로 임대해 오셨습니다. 세입자가 나간 뒤 다시 임대하지 않고 <b>2026년 11월</b>에 폐업하기로 하셨습니다. 상가는 팔지 않고 계속 소유합니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 폐업 시 잔존재화 과세의 기본</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>과세 대상</td><td>폐업할 때 남아 있는 <b>자기생산·취득재화</b>(매입세액을 공제받은 재화 등)</td><td>법 제10조제1항·제6항</td></tr>
<tr><td>공급가액(건물·구축물)</td><td>취득가액 × (1 − <b>5%</b> × 경과된 과세기간 수), 과세기간 수는 <b>20</b>이 한도</td><td>시행령 제66조제2항제1호</td></tr>
<tr><td>공급가액(그 밖의 감가상각자산)</td><td>취득가액 × (1 − <b>25%</b> × 경과된 과세기간 수), 과세기간 수는 <b>4</b>가 한도</td><td>같은 항 제2호</td></tr>
<tr><td>취득가액</td><td>매입세액을 공제받은 해당 재화의 가액</td><td>같은 조 제4항</td></tr>
<tr><td>과세기간 수 계산</td><td>과세기간 중간에 취득하거나 공급으로 보는 경우 그 과세기간 <b>개시일</b>에 취득·공급한 것으로 봄</td><td>같은 조 제5항</td></tr>
<tr><td>과세 제외</td><td>사업을 통째로 넘기는 <b>사업양도</b>(시행령으로 정하는 것)는 재화의 공급으로 보지 않음</td><td>법 제10조제9항제2호</td></tr>
</table></div>
<p>부가세 과세기간은 1월~6월(1기), 7월~12월(2기) 6개월 단위입니다. 그래서 건물은 대략 <b>10년</b>이 지나면 공급가액이 0원이 되어 폐업해도 부가세가 없습니다. 상가 임대보증금의 부가세는 <a href="/column/207-commercial-deposit-deemed-rent-vat.html">칼럼 207</a>, 상가를 사업양도로 넘기는 경우는 <a href="/column/147-commercial-building-business-transfer-vat.html">칼럼 147</a>을 참고해 주세요.</p>

<h2>2. 오○○ 님 사례 — 폐업 시 부가세 계산</h2>
<div class="tbl"><table>
<tr><th>항목</th><th>내용</th></tr>
<tr><td>건물 취득가액(매입세액 공제분)</td><td>500,000,000원</td></tr>
<tr><td>취득 시기 → 과세기간 개시일</td><td>2021년 3월 → 2021년 1기(1월 1일)</td></tr>
<tr><td>폐업 시기 → 과세기간 개시일</td><td>2026년 11월 → 2026년 2기(7월 1일)</td></tr>
<tr><td>경과된 과세기간 수</td><td>11 (2021년 1기 ~ 2026년 1기)</td></tr>
<tr><td>공급가액</td><td>5억 × (1 − 5% × 11) = <b>225,000,000원</b></td></tr>
<tr><td>부가가치세(10%)</td><td><b>22,500,000원</b></td></tr>
</table></div>
<p>세입자도 없는데 <b>2,250만 원</b>의 부가세를 내야 합니다. 만약 취득 후 20과세기간(약 10년)이 지난 뒤 폐업했다면 공급가액이 0원이 되어 부가세가 없습니다. 폐업 시점을 정하기 전에 꼭 계산해 보셔야 하는 이유입니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 건물분만 계산했고(토지는 면세), 일반과세자로서 취득 시 건물분 매입세액 전액을 공제받았다고 가정했습니다. 간이과세자는 계산 방법이 다를 수 있습니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 상가를 살 때 <b>건물분 부가세를 환급(공제)</b>받았는지 확인했다.</li>
<li>☐ 취득일과 폐업 예정일로 <b>경과된 과세기간 수</b>를 계산해 봤다.</li>
<li>☐ 폐업 대신 <b>새 임차인을 구해 계속 임대</b>하거나, 상가를 팔 때 <b>사업양도</b>로 넘길 수 있는지 검토했다.</li>
<li>☐ 폐업 후 부가세 확정신고 때 잔존재화를 <b>빠뜨리지 않고</b> 신고하도록 준비했다.</li>
<li>☐ 집기·비품 등 그 밖의 감가상각자산도 매입세액을 공제받았다면 함께 계산했다.</li>
</ul>
<p>상가 임대사업은 시작할 때 환급받은 부가세가 끝날 때 다시 돌아올 수 있습니다. 폐업이나 매각을 앞두고 계시면 시점과 방법을 정하기 전에 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>상가 분양·매매계약서, 세금계산서</td><td>건물분 취득가액·매입세액</td></tr>
<tr><td>부가세 신고서(취득 당시)</td><td>환급(공제) 여부</td></tr>
<tr><td>사업자등록증·임대차계약서</td><td>과세 유형, 임대 현황</td></tr>
<tr><td>폐업·매각 계획</td><td>시점, 사업양도 가능성</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

_S217 = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec217.py'))

CARDS = [
# 1 표지
f'''<div class="c bg-sunset">{HD()}
<div class="bokeh" style="left:90px;top:220px;width:120px;height:120px;background:#ffe3b0;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:260px;width:90px;height:90px;background:#ffd0e0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-doc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">상가 임대사업 폐업 전에</div><div class="t">남은 건물에<br>부가세가 나와요</div><div class="series">부가세·기타 series 3편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-lilac">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#5b2f7a">상가 주인의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">오○○ 님</div><div class="say">세입자가 나가서<br><span class="mk">폐업 신고</span>만<br>하면 되죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">환급받은 건물이면<br><span class="hl">부가세</span>를<br>내셔야 해요!</div></div>
<img class="ch" src="ch/worry-calc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#5b2f7a">얼마나요? →</div>
{FT(2, False)}</div>''',
# 3 계산식(목록)
f'''<div class="c bg-night">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">폐업할 때 남은 건물</div><div class="h1" style="margin-top:8px">공급가액 계산</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#3d8bff">①</div><div class="tx">건물 취득가액<br><span style="color:#1b5fa8">부가세 공제받은 금액</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">②</div><div class="tx">× (1 − 5% ×<br><span style="color:#c0392b">지난 과세기간 수)</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">③</div><div class="tx">20과세기간(약 10년)<br><span style="color:#1f8a57">지나면 0원</span></div></div>
</div>
{FT(3, True, '부가가치세법 시행령 제66조②')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">건물을 팔지 않고<br>갖고 있으면<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">부가세는 없다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 폐업하면 <b style="font-weight:900">자기에게 공급</b>한<br>것으로 보아 부가세를 매겨요.</div>
{FT(4, True, '부가가치세법 제10조⑥')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">건물 5억 · 2021년 취득 → 2026년 폐업</div><div class="h1" style="font-size:62px;margin-top:6px">폐업 부가세</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>취득가액</small><b style="color:#16213e">5억</b></div><div class="op">×</div><div class="bx"><small>1 − 5%×11</small><b style="color:#e0463c">45%</b></div></div>
<div class="total" style="top:610px"><small>공급가액 2.25억 × 10%</small><b>2,250만 원</b><span>세입자 없어도 내는 부가세</span></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정 (가상 사례)</b><br>· 일반과세자, 건물분만<br>· 경과 과세기간 11</div>
{FT(5, True, '부가가치세법 시행령 제66조②⑤')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">폐업 전에 검토!</div><div class="h1" style="margin-top:8px">줄이는 방법</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">새 임차인 구해<br><span style="color:#1f8a57">계속 임대</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">팔 때는<br><span style="color:#1b5fa8">사업양도 검토</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">폐업 시점<br><span style="color:#c0392b">과세기간 수 계산</span></div></div>
</div>
{FT(6, True, '부가가치세법 제10조⑨2')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '폐업 신고 전에').replace('<span class="hl">기한</span> 확인!', '<span class="hl">부가세</span> 확인!'),
]
