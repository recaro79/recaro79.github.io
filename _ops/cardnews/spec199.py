import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 199
SLUG = 'gift-deduction-order-father-grandfather'
CAT = '증여세'
DATE = '2026-11-27'
TITLE = '아버지·할아버지께 함께 증여받으신다면 — 증여재산공제 5천만 원은 하나를 나눠 씁니다, 같은 날이면 금액대로 나누고 날짜가 다르면 먼저 받은 증여부터 공제, 순서에 따라 세금이 달라집니다'
DESC = '직계존속에게 받는 증여재산공제 5천만 원(미성년자 2천만 원)은 아버지·어머니·할아버지·할머니를 합쳐 10년간 한 번의 한도입니다. 2 이상의 증여가 동시에 있으면 각 과세가액에 안분해 공제하고, 증여시기가 다르면 최초의 증여부터 순차로 공제합니다. 손자녀는 세대생략 할증 30%가 붙어 순서에 따라 세액이 달라집니다. 상속세 및 증여세법 제53조, 제57조, 같은 법 시행령 제46조제1항 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '상속세 및 증여세법 제47조제2항, 제53조제2호, 제56조·제26조, 제57조제1항, 같은 법 시행령 제46조제1항'
TAGS = ['증여재산공제', '손자녀증여', '세대생략할증', '증여순서', '증여세', '부산세무사']
ALTS = ['증여재산공제 나누기 (표지)', '증여재산공제 나누기 (상담 질문)', '증여재산공제 나누기 (공제 규칙)', '증여재산공제 나누기 (O·X 퀴즈)', '증여재산공제 나누기 (세금 비교)', '증여재산공제 나누기 (확인할 점)', '증여재산공제 나누기 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"아버지께 1억, 할아버지께 1억을 받기로 했어요. 증여하는 분이 다르니 공제도 5천만 원씩 두 번 받겠죠?" 연말에 가족 증여를 준비하시는 분들이 자주 하시는 질문입니다. 결론부터 말씀드리면 <b>아닙니다</b>. 직계존속(부모·조부모)에게 받는 증여재산공제 <b>5천만 원은 모두 합쳐 10년에 한 번</b>이고, 여러 분께 받으면 그 한도를 <b>나눠 씁니다</b>. 그리고 어떻게 나누느냐에 따라 세금이 달라집니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>부모·조부모 등 <b>직계존속 전체</b>에게 받는 증여재산공제는 10년간 <b>5천만 원</b>(미성년자 2천만 원)이 한도입니다.</li><li>같은 날 여러 분께 받으면 각 증여금액에 <b>비례해 나눠(안분)</b> 공제하고, 날짜가 다르면 <b>먼저 받은 증여부터</b> 공제합니다.</li><li>할아버지·할머니께 받는 손자녀 증여는 산출세액에 <b>30% 할증</b>이 붙어, 공제를 어느 쪽에 쓰느냐에 따라 세금이 달라집니다.</li></ol>
<div class="small" style="margin-top:8px">(상속세 및 증여세법 제53조·제57조, 같은 법 시행령 제46조제1항 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"아버지께 1억 원, 할아버지께 1억 원을 받으려고 해요. 증여세를 어떻게 하면 줄일 수 있을까요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>성인인 윤○○ 님(가칭)은 아버지께 현금 <b>1억 원</b>, 할아버지께 현금 <b>1억 원</b>을 증여받을 계획입니다. 지난 10년 동안 부모님·조부모님께 증여받은 적은 없습니다. 아버지(어머니 포함)와 할아버지는 <b>다른 증여자</b>이므로 증여세는 각각 따로 계산하지만, 증여재산공제 5천만 원은 <b>하나의 한도</b>를 함께 씁니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 증여재산공제, 이렇게 나눕니다</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>공제 한도</td><td>직계존속(수증자의 직계존속과 혼인 중인 배우자 포함)으로부터 받은 증여: <b>5천만 원</b>(미성년자 2천만 원). 받기 전 10년 이내 공제받은 금액과 합쳐 한도를 넘으면 초과분은 공제하지 않음</td><td>법 제53조제2호</td></tr>
<tr><td>같은 날 여러 증여</td><td>2 이상의 증여가 <b>동시에</b> 있으면 각각의 증여세 과세가액에 대하여 <b>안분</b>하여 공제</td><td>시행령 제46조제1항제2호</td></tr>
<tr><td>날짜가 다른 증여</td><td>2 이상의 증여가 증여시기를 달리하면 <b>최초의 증여</b>세 과세가액부터 순차로 공제</td><td>시행령 제46조제1항제1호</td></tr>
<tr><td>합산 과세</td><td>10년 이내 <b>동일인</b>에게 받은 증여는 합산(증여자가 직계존속이면 그 배우자 포함 — 아버지·어머니는 합산, 할아버지는 따로)</td><td>법 제47조제2항</td></tr>
<tr><td>세대생략 할증</td><td>수증자가 증여자의 자녀가 아닌 직계비속이면 산출세액의 <b>30%</b> 가산(미성년자·증여재산 20억 원 초과는 40%). 부모가 사망해 손자녀가 받는 경우는 제외</td><td>법 제57조제1항</td></tr>
</table></div>

<h2>2. 윤○○ 님 사례 — 순서에 따른 증여세 비교</h2>
<div class="tbl"><table>
<tr><th>방법</th><th>아버지 증여분 세액</th><th>할아버지 증여분 세액(할증 30% 포함)</th><th>합계</th></tr>
<tr><td>① 같은 날 받음(공제 2,500만 원씩 안분)</td><td>7,500,000</td><td>9,750,000</td><td>17,250,000</td></tr>
<tr><td>② 아버지께 먼저 받음(아버지 증여에서 5천만 원 공제)</td><td>5,000,000</td><td>13,000,000</td><td>18,000,000</td></tr>
<tr><td>③ 할아버지께 먼저 받음(할아버지 증여에서 5천만 원 공제)</td><td>10,000,000</td><td>6,500,000</td><td><b>16,500,000</b></td></tr>
</table></div>
<p>같은 2억 원을 받아도 순서만으로 <b>최대 150만 원</b>(②와 ③의 차이) 세금이 달라집니다. 할증이 붙는 할아버지 증여분에서 공제를 쓰는 편이 세금이 적게 나오는 구조입니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 세율은 상속세 및 증여세법 제56조(제26조 세율: 1억 원 이하 10%)를 적용했고, 신고세액공제(3%)는 반영하지 않았습니다. 같은 날 받는 경우 공제는 증여금액 비율(1억 원 : 1억 원)로 안분했습니다. 10년 안에 다시 증여를 받으면 합산과 남은 공제 한도를 다시 따져야 합니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 최근 <b>10년 동안</b> 부모님·조부모님께 받은 증여와 공제받은 금액을 확인했다(<a href="/column/03-gift-deduction-10year-rule.html">칼럼 03</a>).</li>
<li>☐ 받는 사람이 <b>미성년자</b>라면 공제 한도가 2천만 원인지 확인했다.</li>
<li>☐ 여러 분께 받는다면 <b>증여일</b>(현금은 받은 날, 부동산은 등기접수일)을 정리했다(<a href="/column/178-gift-date-and-return-per-date.html">칼럼 178</a>).</li>
<li>☐ 손자녀 증여는 <b>30% 할증</b>과 할아버지·할머니의 상속 대비(5년 합산)를 함께 검토했다(<a href="/column/12-generation-skipping-gift.html">칼럼 12</a>, <a href="/column/190-split-gift-children-in-laws-grandchildren.html">칼럼 190</a>).</li>
<li>☐ 혼인·출산을 앞두고 있다면 별도의 <b>혼인·출산 증여재산공제 1억 원</b>도 함께 검토했다(<a href="/column/02-marriage-birth-gift-deduction.html">칼럼 02</a>).</li>
</ul>
<p>가족 증여는 누가, 언제, 얼마를 주느냐에 따라 세금이 달라집니다. 연말 증여를 계획하고 계시면 증여 전에 편하게 상담해 주세요. 순서와 금액을 함께 설계해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>최근 10년 증여 내역·증여세 신고서</td><td>합산 대상, 이미 쓴 공제</td></tr>
<tr><td>가족관계증명서</td><td>직계존속·손자녀 관계, 할증 여부</td></tr>
<tr><td>증여 예정 재산·금액·날짜</td><td>공제 순서, 예상 세액</td></tr>
<tr><td>혼인·출산 예정 여부</td><td>혼인·출산 공제 가능 여부</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-orange">{HD()}
<div class="bokeh" style="left:90px;top:200px;width:120px;height:120px;background:#ffe3b0;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:250px;width:90px;height:90px;background:#fff;opacity:.3"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-piggy-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">아버지·할아버지께 함께 받으면</div><div class="t">5천만 원 공제<br>두 번일까요?</div><div class="series">증여세 절세 series 5편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">연말 증여 상담 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">윤○○ 님</div><div class="say">주시는 분이 다르니<br>공제도 <span class="mk">5천만 원씩</span><br>두 번 받죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">부모·조부모 합쳐<br><span class="hl">5천만 원 하나</span>를<br>나눠 써요!</div></div>
<img class="ch" src="ch/wink-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">어떻게 나눌까요? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">직계존속 공제 5천만 원</div><div class="h1" style="margin-top:8px">나누는 규칙</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">같은 날 받으면<br><span style="color:#1f8a57">금액 비율로 안분</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">날짜가 다르면<br><span style="color:#1b5fa8">먼저 받은 것부터</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">10년간 합쳐<br><span style="color:#c0392b">한도 5천만 원</span></div></div>
</div>
{FT(3, True, '상증법 제53조·시행령 제46조①')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">아버지 증여와<br>할아버지 증여는<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">합쳐서 세금 계산?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/smile-thumb.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 세금은 <b style="font-weight:900">따로</b> 계산해요.<br>(아버지·어머니는 합산) 공제만 나눠 써요.</div>
{FT(4, True, '상증법 제47조②')}</div>''',
# 5 숫자 타일
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">아버지 1억 + 할아버지 1억 (가상 사례)</div><div class="h1" style="margin-top:8px">순서별 증여세</div></div>
<div class="tiles" style="top:360px">
 <div class="tile wide t-green"><div class="who" style="font-size:36px">할아버지께 먼저</div><div class="amt">1,650만<small>원</small></div></div>
 <div class="tile t-blue"><div class="who">같은 날</div><div class="amt">1,725만<small>원</small></div></div>
 <div class="tile t-red"><div class="who">아버지께 먼저</div><div class="amt">1,800만<small>원</small></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:900px;font-size:30px;font-weight:600">· 할아버지 증여분은 30% 할증이 붙어요.<br>· 할증 붙는 쪽에서 공제를 쓰면 세금이 줄어요.<br>· 신고세액공제 3% 반영 전 금액이에요.</div>
{FT(5, True, '상증법 제26조·제57조, 시행령 제46조')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">증여 전에</div><div class="h1" style="margin-top:8px">꼭 확인하세요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">10년 안에<br><span style="color:#c0392b">이미 쓴 공제</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">미성년자는<br><span style="color:#b9770e">2천만 원</span>까지</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">혼인·출산 공제<br><span style="color:#1b5fa8">1억 원</span>은 별도</div></div>
</div>
{FT(6, True, '상증법 제53조·제53조의2')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '가족 증여 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">순서</span> 설계!'),
]
