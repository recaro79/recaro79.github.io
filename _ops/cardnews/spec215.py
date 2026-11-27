import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 215
SLUG = 'business-opportunity-deemed-gift'
CAT = '증여세'
DATE = '2026-11-27'
TITLE = '아버지 회사가 자녀 회사에 매장·대리점·프랜차이즈 사업을 넘겨주면 — 사업기회 제공 증여의제, 첫해 이익으로 3년 치를 미리 과세하고 2년 뒤 실제 이익으로 정산, 넘겨준 회사가 중소기업이면 제외'
DESC = '지배주주와 친족의 지분이 30% 이상인 수혜법인이 지배주주와 특수관계에 있는 법인으로부터 임대차·입점·대리점·프랜차이즈 계약 등으로 사업기회를 제공받으면, 개시사업연도 이익을 기준으로 [(이익 × 지분율 − 법인세 상당액) ÷ 월수 × 12] × 3을 지배주주등이 증여받은 것으로 보고, 사업기회제공일 이후 2년이 지난 사업연도에 실제 이익으로 정산합니다. 사업기회를 제공한 법인이 중소기업이거나 수혜법인 지분 50% 이상 법인이면 제외됩니다. 상속세 및 증여세법 제45조의4, 같은 법 시행령 제34조의4 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '상속세 및 증여세법 제45조의4, 제47조제1항, 같은 법 시행령 제34조의3·제34조의4, 같은 법 시행규칙 제10조의9'
TAGS = ['사업기회제공', '일감떼어주기', '증여의제', '가족법인', '수혜법인', '부산세무사']
ALTS = ['사업기회 제공 증여의제 (표지)', '사업기회 제공 증여의제 (상담 질문)', '사업기회 제공 증여의제 (요건)', '사업기회 제공 증여의제 (O·X 퀴즈)', '사업기회 제공 증여의제 (계산)', '사업기회 제공 증여의제 (정산)', '사업기회 제공 증여의제 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
회사를 운영하시는 대표님들께서 자녀가 세운 회사에 "우리 회사가 하던 매장 운영을 넘겨주자", "대리점 계약을 자녀 회사로 돌리자"고 생각하시는 경우가 있습니다. 세법은 이런 거래를 <b>사업기회 제공</b>으로 보아, 자녀 회사가 그 사업으로 벌게 될 이익을 자녀가 <b>증여받은 것으로 의제</b>합니다. 흔히 "일감 떼어주기"라고 부르는 규정입니다. 다만 사업기회를 넘겨준 회사가 <b>중소기업</b>이면 적용되지 않으니, 요건부터 차근차근 보셔야 합니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>지배주주와 친족 지분이 <b>30% 이상</b>인 회사(수혜법인)가 지배주주와 특수관계인 법인에게서 <b>임대차·입점·대리점·프랜차이즈 계약</b> 등으로 사업기회를 받으면 대상입니다.</li><li>첫 사업연도 이익으로 <b>[(이익 × 지분율 − 법인세 상당액) ÷ 월수 × 12] × 3</b>을 미리 증여로 보고, 사업기회제공일 이후 <b>2년이 지난 사업연도</b>에 실제 이익으로 <b>정산</b>합니다.</li><li>사업기회를 준 법인이 <b>중소기업</b>이거나 수혜법인이 지분 <b>50% 이상</b>을 가진 법인이면 <b>제외</b>됩니다.</li></ol>
<div class="small" style="margin-top:8px">(상속세 및 증여세법 제45조의4, 같은 법 시행령 제34조의4 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"제가 운영하는 회사의 직영 매장 하나를 딸이 세운 회사가 운영하도록 입점계약을 바꾸려고 해요. 세금 문제가 있을까요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>허○○ 대표님(가칭)이 지배하는 A법인(<b>중소기업이 아닌</b> 중견기업)이 직영하던 매장을, 딸이 지분 100%를 가진 B법인과 <b>입점계약</b>을 맺어 넘겨주었습니다. B법인의 첫 사업연도(12개월) 동안 그 매장 사업부문에서 생긴 이익(세무조정 반영)은 <b>3억 원</b>, 이에 해당하는 법인세 상당액은 <b>4천만 원</b>이라고 가정하겠습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 적용 요건</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>수혜법인</td><td>지배주주와 그 친족(지배주주등)의 주식보유비율이 <b>30% 이상</b>인 법인</td><td>법 제45조의4제1항</td></tr>
<tr><td>사업기회를 준 법인</td><td>지배주주와 특수관계에 있는 법인 — 단, <b>중소기업</b>(조특법상)과 수혜법인 지분 <b>50% 이상</b> 법인은 <b>제외</b></td><td>같은 항, 시행령 제34조의4제1항·제7항·제8항</td></tr>
<tr><td>제공 방법</td><td>특수관계법인이 직접 하거나 다른 사업자가 하던 사업기회를 <b>임대차계약, 입점계약, 대리점계약, 프랜차이즈계약</b> 등 명칭과 관계없는 약정으로 제공</td><td>시행령 제34조의4제2항, 시행규칙 제10조의9제1항</td></tr>
<tr><td>증여시기·신고</td><td>개시사업연도 종료일에 증여받은 것으로 보고, 법인세 신고기한이 속하는 달의 말일부터 <b>3개월</b> 안에 신고</td><td>법 제45조의4제1항·제2항</td></tr>
<tr><td>정산</td><td>사업기회제공일 이후 <b>2년이 지난 날이 속하는 사업연도</b>까지 실제 이익으로 다시 계산해 차액 납부 또는 환급</td><td>같은 조 제3항·제5항</td></tr>
</table></div>
<p>이 증여의제이익은 다른 증여와 <b>합산하지 않는</b> 재산(합산배제증여재산)입니다(법 제47조제1항). 수혜법인에서 받은 배당이 있으면 일정 금액을 증여의제이익에서 뺍니다(시행령 제34조의4제5항·제6항).</p>

<h2>2. 허○○ 대표님 사례 — 증여의제이익 계산</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>금액</th></tr>
<tr><td>사업기회로 생긴 개시사업연도 이익 × 딸의 지분율(100%)</td><td>300,000,000</td></tr>
<tr><td>법인세 납부세액 중 상당액</td><td>△40,000,000</td></tr>
<tr><td>÷ 개시사업연도 월수(12) × 12</td><td>260,000,000</td></tr>
<tr><td><b>× 3 = 증여의제이익</b></td><td><b>780,000,000</b></td></tr>
</table></div>
<p>첫해 이익만으로 <b>3년 치(7억 8천만 원)</b>를 미리 증여로 보아 딸이 증여세를 내고, 2년 뒤 실제 3개 사업연도 이익을 반영해 정산합니다. 실제 이익이 더 적으면 차액만큼 환급받을 수 있습니다(법 제45조의4제3항 단서). 만약 A법인이 <b>중소기업</b>이었다면 이 규정은 적용되지 않습니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 법인세 상당액은 수혜법인 산출세액(감면 차감)에 그 사업부문 이익이 각 사업연도 소득금액에서 차지하는 비율을 곱해 계산하는데(시행령 제34조의4제4항), 사례에서는 4천만 원으로 단순 가정했습니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 사업기회를 넘겨주는 회사가 조특법상 <b>중소기업</b>인지 먼저 확인했다(중소기업이면 제외).</li>
<li>☐ 받는 회사의 <b>지배주주·친족 지분율</b>이 30% 이상인지 확인했다.</li>
<li>☐ 넘겨받는 사업부문의 <b>회계를 구분</b>해 이익을 따로 계산할 수 있게 했다.</li>
<li>☐ 증여세 신고기한(법인세 신고기한이 속한 달 말일부터 3개월)과 <b>2년 뒤 정산</b> 일정을 표시했다.</li>
<li>☐ 일감몰아주기(<a href="/column/95-related-company-trade-deemed-gift.html">칼럼 95</a>), 특정법인 거래(<a href="/column/126-specific-corporation-deemed-gift.html">칼럼 126</a>) 규정과 겹치는지도 함께 검토했다.</li>
</ul>
<p>가족 법인 사이 거래는 규모와 기업 구분에 따라 결과가 크게 달라집니다. 사업 재편을 계획하고 계시면 실행 전에 편하게 상담해 주세요. 적용 여부부터 세금까지 함께 검토해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>두 회사 주주명부</td><td>지배주주·친족 지분율, 특수관계</td></tr>
<tr><td>중소기업 해당 여부 자료(제공 법인)</td><td>적용 제외 여부</td></tr>
<tr><td>임대차·입점·대리점·프랜차이즈 계약서</td><td>사업기회 제공 방법, 제공일</td></tr>
<tr><td>사업부문별 손익 자료</td><td>수혜법인 이익 계산</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-pink">{HD()}
<div class="bokeh" style="left:90px;top:200px;width:120px;height:120px;background:#ffd3e0;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:250px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-doc-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">아버지 회사 사업을 자녀 회사로?</div><div class="t">사업기회도<br>증여입니다</div><div class="series">증여세 절세 series 8편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">법인 대표님 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">허○○ 대표님</div><div class="say">직영 매장을<br>딸 회사에 <span class="mk">입점계약</span>으로<br>넘겨도 되나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">중소기업이 아니면<br><span class="hl">증여세</span> 대상일<br>수 있어요!</div></div>
<img class="ch" src="ch/worry-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">요건은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">이럴 때 적용돼요</div><div class="h1" style="margin-top:8px">사업기회 제공</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">받는 회사<br><span style="color:#1f8a57">가족 지분 30%↑</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">임대차·입점·대리점·<br><span style="color:#1b5fa8">프랜차이즈 계약</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">주는 회사가<br><span style="color:#c0392b">중소기업이 아님</span></div></div>
</div>
{FT(3, True, '상증법 제45조의4①·시행령 제34조의4')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">사업기회를 준 회사가<br>중소기업이어도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">증여의제가 된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 제공 법인이 <b style="font-weight:900">중소기업</b>이면<br>이 규정에서 제외돼요.</div>
{FT(4, True, '상증법 시행령 제34조의4⑦')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">첫해 이익 3억 · 지분 100% (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">3년 치 미리 과세</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>이익 − 법인세 상당</small><b style="color:#1b5fa8">2.6억</b></div><div class="op">×</div><div class="bx"><small>3년 치</small><b style="color:#ff5c8a">3</b></div></div>
<div class="total" style="top:610px"><small>증여의제이익</small><b>7억 8천만 원</b><span>2년 뒤 실제 이익으로 정산</span></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 제공 법인은 중견기업<br>· 법인세 상당액 4천만 원</div>
{FT(5, True, '상증법 제45조의4①')}</div>''',
# 6 정산
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">끝이 아니에요</div><div class="h1" style="margin-top:8px">2년 뒤 정산</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">실제 이익이 크면<br><span style="color:#c0392b">추가 납부</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">②</div><div class="tx">실제 이익이 작으면<br><span style="color:#1f8a57">환급</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">받은 배당은<br><span style="color:#1b5fa8">일정액 공제</span></div></div>
</div>
{FT(6, True, '상증법 제45조의4③·시행령 제34조의4⑤⑥')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '사업 재편 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">먼저</span> 검토!'),
]
