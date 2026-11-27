import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 200
SLUG = 'education-expense-tax-credit-2026'
CAT = '종합소득세'
DATE = '2026-11-27'
TITLE = '연말정산 교육비 세액공제 — 지출액의 15%, 초·중·고 1명당 300만 원·대학생 900만 원, 본인은 한도 없음, 2026년부터 초등 1·2학년 예체능 학원·태권도장 수강료도 공제됩니다'
DESC = '근로소득자가 본인과 기본공제대상자를 위해 지급한 교육비는 15% 세액공제됩니다. 취학 전 아동·초중고생은 1명당 연 300만 원, 대학생은 연 900만 원 한도이고 본인 교육비는 한도가 없습니다. 2026년 1월 1일 이후 지급분부터 9세 미만 또는 2학년 이하 초등학생의 예능 학원·체육시설 수강료도 공제됩니다. 소득세법 제59조의4제3항, 같은 법 시행령 제118조의6 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제59조의4제3항, 같은 법 시행령 제118조의6, 소득세법 부칙(제21221호) 제5조'
TAGS = ['연말정산', '교육비세액공제', '학원비공제', '초등학원비', '근로소득자', '부산세무사']
ALTS = ['교육비 세액공제 (표지)', '교육비 세액공제 (상담 질문)', '교육비 세액공제 (한도)', '교육비 세액공제 (O·X 퀴즈)', '교육비 세액공제 (공제 계산)', '교육비 세액공제 (빠지는 것)', '교육비 세액공제 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
연말정산 시즌이 다가오면 자녀 학비·학원비가 얼마나 공제되는지 묻는 분들이 많습니다. 교육비 세액공제는 <b>낸 금액의 15%</b>를 세금에서 바로 빼 주는 제도인데, 대상과 한도가 정해져 있습니다. 특히 <b>2026년부터는 초등학교 1·2학년 자녀의 피아노·미술 같은 예능 학원과 태권도장 등 체육시설 수강료도 공제</b>받을 수 있게 바뀌었습니다. 올해 연말정산 전에 꼭 확인해 보세요.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>근로소득자가 본인·가족(기본공제대상자, 나이 제한 없음)을 위해 낸 교육비의 <b>15%</b>를 세액공제합니다.</li><li>한도는 1명당 취학 전·초중고 <b>연 300만 원</b>, 대학생 <b>연 900만 원</b>이고, <b>본인</b> 교육비(대학원 포함)는 한도가 없습니다.</li><li><b>2026년 지급분부터</b> 9세 미만 또는 2학년 이하 초등학생의 <b>예능 학원·체육시설</b> 수강료(월 단위, 주 1회 이상)도 공제됩니다.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제59조의4제3항, 같은 법 시행령 제118조의6 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"초등학교 2학년 아이 태권도 학원비, 고등학생 교복값, 대학생 아이 등록금까지 올해 연말정산에서 얼마나 돌려받을 수 있을까요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>직장인 강○○ 님(가칭)은 2026년에 세 자녀를 위해 다음 교육비를 냈습니다. 초등학교 2학년 자녀의 태권도장 수강료 <b>180만 원</b>(월 15만 원)과 방과후학교 수업료 <b>30만 원</b>, 고등학교 1학년 자녀의 교복 구입비 <b>60만 원</b>과 현장체험학습비 <b>40만 원</b>, 대학생 자녀의 등록금 <b>800만 원</b>(학교 장학금 200만 원 받음)입니다. 세 자녀 모두 강○○ 님의 기본공제대상자입니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 누구의 어떤 교육비가 공제될까요</h2>
<div class="tbl"><table>
<tr><th>대상</th><th>공제되는 교육비</th><th>1명당 한도</th></tr>
<tr><td><b>본인</b></td><td>학교·대학·<b>대학원</b> 교육비, 시간제 과정, 직업능력개발훈련 수강료(지원금 차감), 학자금 대출 원리금 상환액</td><td><b>한도 없음</b></td></tr>
<tr><td>취학 전 아동</td><td>유치원·어린이집 비용, 학원·체육시설 수강료(월 단위·주 1회 이상)</td><td>연 300만 원</td></tr>
<tr><td>초·중·고등학생</td><td>수업료·급식비·교과서대·방과후학교, 교복(중·고생 연 50만 원), 현장체험학습(연 30만 원)</td><td>연 300만 원</td></tr>
<tr><td><b>초등 1·2학년</b>(9세 미만 또는 2학년 이하) — 2026년 신설</td><td><b>예능 학원·체육시설</b> 수강료(월 단위·주 1회 이상)</td><td>초중고 한도 300만 원 안에서</td></tr>
<tr><td>대학생</td><td>등록금 등(대학원은 본인만)</td><td>연 900만 원</td></tr>
<tr><td>장애인</td><td>재활교육 특수교육비(국가·지자체 지원액 제외)</td><td>한도 없음</td></tr>
</table></div>
<p class="small">근거: 소득세법 제59조의4제3항, 시행령 제118조의6제1항·제7항·제10항. 초등 1·2학년 예능 학원·체육시설 수강료는 2026년 1월 1일 이후 지급분부터 적용됩니다(소득세법 부칙 제21221호 제5조).</p>

<h2>2. 공제되지 않는 것</h2>
<div class="tbl"><table>
<tr><th>항목</th><th>근거</th></tr>
<tr><td>초등 3학년 이상·중고생의 <b>학원비</b>(국어·영어·수학 학원 등)</td><td>법 제59조의4제3항제1호 라목·마목 대상 아님</td></tr>
<tr><td>학교·직장·사내근로복지기금 등에서 받은 <b>장학금</b>으로 낸 부분</td><td>법 제59조의4제3항 단서, 시행령 제118조의6제2항</td></tr>
<tr><td>자녀가 <b>학자금 대출</b>을 받아 낸 등록금(자녀가 나중에 상환할 때 본인 공제)</td><td>법 제59조의4제3항제1호 단서</td></tr>
<tr><td>배우자·자녀의 <b>대학원</b> 교육비</td><td>같은 호 단서</td></tr>
</table></div>

<h2>3. 강○○ 님 사례 계산</h2>
<div class="tbl"><table>
<tr><th>자녀</th><th>지출</th><th>공제 대상 금액</th></tr>
<tr><td>초등 2학년</td><td>태권도장 180만 원 + 방과후 30만 원</td><td>2,100,000</td></tr>
<tr><td>고등 1학년</td><td>교복 60만 원(한도 50만 원) + 체험학습 40만 원(한도 30만 원)</td><td>800,000</td></tr>
<tr><td>대학생</td><td>등록금 800만 원 − 장학금 200만 원</td><td>6,000,000</td></tr>
<tr><td colspan="2"><b>합계</b></td><td>8,900,000</td></tr>
<tr><td colspan="2"><b>교육비 세액공제(15%)</b></td><td><b>1,335,000</b></td></tr>
</table></div>
<p class="small">※ python으로 계산·검산했습니다. 강○○ 님의 산출세액이 공제액보다 충분히 크다고 가정했습니다(세액공제는 산출세액을 넘어 환급되지 않습니다). 태권도장은 시행령 제118조의6제6항의 체육시설에 해당하는 것으로 가정했습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 초등 1·2학년 자녀의 <b>예능 학원·태권도장 등</b> 수강료가 간소화 자료에 빠졌다면 학원에서 <b>교육비 납입증명서</b>를 받았다.</li>
<li>☐ 교복 구입 영수증, 현장체험학습비 납입증명서 등 간소화에 없는 자료를 챙겼다.</li>
<li>☐ 장학금 받은 금액을 빼고 계산했다.</li>
<li>☐ 맞벌이라면 자녀 기본공제를 받는 쪽에서 교육비 공제를 받는다는 점을 확인했다(<a href="/column/153-dual-income-dependent-deduction.html">칼럼 153</a>).</li>
<li>☐ 신용카드로 낸 학원비는 신용카드 소득공제와 교육비 세액공제를 함께 받을 수 있는지도 확인했다(<a href="/column/185-credit-card-deduction-2026-children.html">칼럼 185</a>).</li>
</ul>
<p>교육비는 증빙만 잘 챙기면 놓치지 않고 받을 수 있는 공제입니다. 지난해 빠뜨린 교육비가 있다면 5년 안에 경정청구로 돌려받을 수도 있습니다(<a href="/column/109-income-tax-refund-claim.html">칼럼 109</a>). 궁금하신 점은 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>연말정산 간소화 자료</td><td>학교 납입액, 장학금 반영 여부</td></tr>
<tr><td>학원·체육시설 교육비 납입증명서</td><td>초등 1·2학년 예체능, 취학 전 아동 수강료</td></tr>
<tr><td>교복 영수증·현장체험학습비 증명서</td><td>한도(50만 원·30만 원) 적용</td></tr>
<tr><td>가족관계증명서·자녀 소득 자료</td><td>기본공제대상자 여부</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-sunset">{HD()}
<div class="bokeh" style="left:90px;top:200px;width:120px;height:120px;background:#ffd38f;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:250px;width:90px;height:90px;background:#ffb3c7;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-calc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">2026 연말정산</div><div class="t">교육비<br>15% 돌려받기</div><div class="series">종합소득세 절세 series 6편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">학부모님들이 묻는 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">강○○ 님</div><div class="say">초2 아이<br><span class="mk">태권도 학원비</span>도<br>공제되나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px"><span class="hl">2026년부터</span><br>초등 1·2학년은<br>공제돼요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">한도는? →</div>
{FT(2, False)}</div>''',
# 3 타일
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">1명당 연간 한도 · 공제율 15%</div><div class="h1" style="margin-top:8px">교육비 한도</div></div>
<div class="tiles" style="top:360px">
 <div class="tile wide t-red"><div class="who" style="font-size:36px">본인 (대학원 포함)</div><div class="amt">한도 없음</div></div>
 <div class="tile t-blue"><div class="who">취학 전·초중고</div><div class="amt">300만<small>원</small></div></div>
 <div class="tile t-green"><div class="who">대학생</div><div class="amt">900만<small>원</small></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:900px;font-size:30px;font-weight:600">· 교복은 중·고생 1명당 50만 원까지<br>· 현장체험학습은 1명당 30만 원까지<br>· 장애인 특수교육비는 한도 없음</div>
{FT(3, True, '소득세법 제59조의4③·시행령 제118조의6')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">중학생 아이의<br>영어·수학 학원비도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">교육비 공제된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-doc.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 학원비는 취학 전 아동과<br><b style="font-weight:900">초등 1·2학년 예체능</b>만 돼요.</div>
{FT(4, True, '소득세법 제59조의4③1호')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">세 자녀 교육비 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">얼마나 돌려받을까?</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>공제 대상</small><b style="color:#1b5fa8">890만</b></div><div class="op">×</div><div class="bx"><small>공제율</small><b style="color:#ff5c8a">15%</b></div></div>
<div class="total" style="top:610px"><small>교육비 세액공제</small><b>133만 5천 원</b><span>초2 210만 + 고1 80만 + 대학 600만</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">포인트</b><br>· 교복 50만·체험학습 30만 한도<br>· 장학금 200만 원은 빼고 계산</div>
{FT(5, True, '소득세법 제59조의4③')}</div>''',
# 6 빠지는 것
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">이건 공제 안 돼요</div><div class="h1" style="margin-top:8px">빠지는 교육비</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">장학금으로<br><span style="color:#c0392b">낸 부분</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">자녀가 <span style="color:#b9770e">학자금 대출</span>로<br>낸 등록금</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">자녀·배우자의<br><span style="color:#1b5fa8">대학원</span> 학비</div></div>
</div>
{FT(6, True, '소득세법 제59조의4③')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '연말정산 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">교육비</span> 챙기세요!'),
]
