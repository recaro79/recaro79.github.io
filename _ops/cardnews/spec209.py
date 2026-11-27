import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 209
SLUG = 'greenbelt-land-purchase-tax-reduction'
CAT = '양도소득세'
DATE = '2026-11-27'
TITLE = '개발제한구역(그린벨트) 땅을 매수청구·협의매수로 파신다면 — 지정 전부터 가진 땅은 양도세 40%, 20년 이상 가진 땅은 25% 감면, 땅 소재지 근처 거주 요건과 2028년 12월 31일 기한'
DESC = '개발제한구역 내 토지 등을 토지매수청구 또는 협의매수로 2028년 12월 31일까지 양도하면, 개발제한구역 지정일 이전에 취득해 계속 소재지(같은 시·군·구, 연접 시·군·구 또는 30km 이내)에 거주한 경우 양도세 40%, 매수청구일·협의매수일부터 20년 이전에 취득해 계속 거주한 경우 25%를 감면합니다. 해제 후 1년(경제자유구역 등 5년) 안에 사업인정고시되어 수용·협의매수되는 경우도 같습니다. 조세특례제한법 제77조의3, 같은 법 시행령 제74조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '조세특례제한법 제77조의3, 같은 법 시행령 제74조, 소득세법 제95조제2항'
TAGS = ['개발제한구역', '그린벨트', '매수청구', '협의매수', '양도세감면', '부산세무사']
ALTS = ['그린벨트 매수 감면 (표지)', '그린벨트 매수 감면 (상담 질문)', '그린벨트 매수 감면 (감면율)', '그린벨트 매수 감면 (O·X 퀴즈)', '그린벨트 매수 감면 (세금 계산)', '그린벨트 매수 감면 (거주 요건)', '그린벨트 매수 감면 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
부산에도 개발제한구역(그린벨트)으로 묶인 땅이 적지 않습니다. 오래전부터 그린벨트 안에 땅을 가지고 계신 분들이 <b>국가에 매수청구</b>를 하거나 <b>협의매수</b>로 땅을 넘기실 때 꼭 확인하셔야 할 감면이 있습니다. 요건을 갖추면 양도소득세를 <b>40% 또는 25%</b> 줄여 줍니다. 다만 <b>거주 요건</b>과 <b>2028년 12월 31일</b>이라는 기한이 있으니 미리 확인해 두세요.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>개발제한구역 안의 토지 등을 <b>토지매수청구</b> 또는 <b>협의매수</b>로 <b>2028년 12월 31일까지</b> 양도하면 양도세를 감면합니다.</li><li>개발제한구역 <b>지정일 이전</b>에 취득했으면 <b>40%</b>, 매수청구일·협의매수일부터 <b>20년 이전</b>에 취득했으면 <b>25%</b> 감면입니다.</li><li>취득일부터 매수청구일(협의매수일)까지 땅이 있는 시·군·구, <b>연접 시·군·구</b> 또는 <b>30km 이내</b>에 계속 거주해야 합니다(상속받은 땅은 피상속인 기간 통산).</li></ol>
<div class="small" style="margin-top:8px">(조세특례제한법 제77조의3, 같은 법 시행령 제74조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"25년 전에 산 그린벨트 땅을 국가에서 사 주겠다고 해요. 양도세 감면이 있다던데 저도 받을 수 있나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>부산에 사는 장○○ 님(가칭)은 <b>25년 전</b>(개발제한구역 지정 이후)에 부산 안의 개발제한구역 토지를 <b>1억 원</b>에 사서 지금까지 계속 부산에 살고 계십니다. 이 땅을 협의매수로 <b>5억 원</b>에 넘기면, 매수일부터 20년 이전에 취득했고 소재지 거주 요건도 갖추었으므로 양도세 <b>25% 감면</b> 대상입니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 감면 요건과 감면율</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>요건</th><th>감면율</th></tr>
<tr><td rowspan="2">개발제한구역 안의 토지 등을 <b>매수청구·협의매수</b>로 양도(제1항)</td><td>개발제한구역 <b>지정일 이전</b>에 취득 + 취득일부터 매수청구일(협의매수일)까지 소재지 거주</td><td><b>40%</b></td></tr>
<tr><td>매수청구일(협의매수일)부터 <b>20년 이전</b>에 취득 + 같은 기간 소재지 거주</td><td><b>25%</b></td></tr>
<tr><td rowspan="2">개발제한구역에서 <b>해제된</b> 토지 등을 협의매수·수용으로 양도(제2항) — 해제일부터 1년(경제자유구역·택지개발지구·산업단지 등 지정 지역은 5년) 안에 사업인정고시된 경우만</td><td>지정일 이전 취득 + 사업인정고시일까지 소재지 거주</td><td><b>40%</b></td></tr>
<tr><td>사업인정고시일부터 20년 이전 취득 + 같은 기간 소재지 거주</td><td><b>25%</b></td></tr>
</table></div>
<p class="small">근거: 조세특례제한법 제77조의3제1항·제2항, 시행령 제74조제2항. 양도 기한은 모두 <b>2028년 12월 31일</b>까지입니다.</p>

<h2>2. 거주 요건 — 어디에 살아야 할까요</h2>
<div class="tbl"><table>
<tr><th>인정되는 거주지</th><th>근거</th></tr>
<tr><td>토지가 있는 <b>시·군·구</b>(자치구) 안</td><td>시행령 제74조제1항제1호</td></tr>
<tr><td>그 시·군·구와 <b>연접한</b> 시·군·구 안</td><td>같은 항 제2호</td></tr>
<tr><td>토지로부터 <b>직선거리 30km 이내</b></td><td>같은 항 제3호</td></tr>
<tr><td>상속받은 토지: 피상속인의 취득일·거주기간을 이어서 계산</td><td>법 제77조의3제3항, 시행령 제74조제4항</td></tr>
<tr><td>취학·징집·질병 요양 등 부득이한 사유로 거주하지 못한 기간은 거주한 것으로 봄</td><td>시행령 제74조제4항</td></tr>
</table></div>

<h2>3. 장○○ 님 사례 계산</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>금액</th></tr>
<tr><td>양도가액 − 취득가액</td><td>500,000,000 − 100,000,000 = 400,000,000</td></tr>
<tr><td>장기보유 특별공제(15년 이상, 30%)</td><td>△120,000,000</td></tr>
<tr><td>양도소득 기본공제</td><td>△2,500,000</td></tr>
<tr><td>과세표준</td><td>277,500,000</td></tr>
<tr><td>산출세액</td><td>85,510,000</td></tr>
<tr><td>감면세액(25%)</td><td><b>△21,377,500</b></td></tr>
<tr><td>감면 후 양도소득세</td><td><b>64,132,500</b></td></tr>
</table></div>
<p>만약 장○○ 님이 개발제한구역 <b>지정 전부터</b> 그 땅을 가지고 계셨다면 40% 감면으로 약 <b>3,420만 원</b>이 줄어듭니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 필요경비·다른 양도 건은 없다고 가정했고, 세율은 소득세법 제55조제1항, 장기보유 특별공제는 제95조제2항 표 1을 적용했습니다. 감면받은 세액에는 조특법상 감면 종합한도(<a href="/column/162-capital-gains-reduction-overall-limit.html">칼럼 162</a>)와 농어촌특별세(<a href="/column/179-rural-special-tax-on-reduction.html">칼럼 179</a>) 적용 여부를 함께 확인해야 합니다. 지방소득세는 별도입니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 토지가 <b>개발제한구역</b> 안에 있는지, 지정일과 내 취득일을 확인했다(토지이용계획확인서).</li>
<li>☐ 양도 방식이 <b>토지매수청구</b> 또는 <b>협의매수</b>인지(일반 매매는 대상 아님) 확인했다.</li>
<li>☐ 취득일부터 매수청구일(협의매수일)까지 <b>주민등록상 거주지</b>가 요건 지역 안인지 확인했다.</li>
<li>☐ 상속받은 땅이라면 <b>피상속인의 취득일·거주기간</b> 자료를 준비했다.</li>
<li>☐ 양도세 신고(예정신고 포함) 때 <b>세액감면신청서</b>와 매수청구·협의매수 확인 서류를 함께 냈다(시행령 제74조제3항).</li>
</ul>
<p>그린벨트 토지는 보유 기간이 길고 상속받은 경우가 많아 요건 확인이 꼼꼼해야 합니다. 매수청구나 협의매수 안내를 받으셨다면 서류를 가지고 편하게 상담해 주세요. 감면 요건 확인부터 신고까지 함께 챙겨 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>토지이용계획확인서·등기부등본</td><td>개발제한구역 여부, 취득일</td></tr>
<tr><td>주민등록초본(주소 변동 이력)</td><td>거주 요건</td></tr>
<tr><td>매수청구·협의매수 관련 서류</td><td>양도 방식, 매수일, 보상가액</td></tr>
<tr><td>상속 관련 서류(상속받은 경우)</td><td>피상속인 취득일·거주기간</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-forest">{HD()}
<div class="bokeh" style="left:90px;top:200px;width:120px;height:120px;background:#bff0d0;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:250px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-magnify.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">그린벨트 땅 매수청구·협의매수</div><div class="t">양도세<br>최대 40% 감면</div><div class="series">양도세 절세 series 14편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">그린벨트 토지주 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">장○○ 님</div><div class="say">25년 전 산 땅,<br>국가가 사 준대요.<br><span class="mk">감면</span> 되나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">20년 넘었고 거주하면<br><span class="hl">25% 감면</span>이에요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">감면율은? →</div>
{FT(2, False)}</div>''',
# 3 타일
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">매수청구·협의매수 (2028.12.31.까지)</div><div class="h1" style="margin-top:8px">감면율</div></div>
<div class="tiles" style="top:360px">
 <div class="tile wide t-green"><div class="who" style="font-size:36px">지정일 이전 취득 + 거주</div><div class="amt">40<small>%</small></div></div>
 <div class="tile t-blue"><div class="who">20년 이전 취득</div><div class="amt">25<small>%</small></div></div>
 <div class="tile t-orange"><div class="who">일반 매매</div><div class="amt">대상 아님</div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:900px;font-size:30px;font-weight:600">· 해제 후 1년(경제자유구역 등 5년) 안 사업인정고시 →<br>  협의매수·수용도 같은 감면이에요.</div>
{FT(3, True, '조특법 제77조의3①②')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">땅이 있는 구에<br>꼭 살아야만<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">거주 요건이 된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/smile-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 연접 시·군·구나<br><b style="font-weight:900">30km 이내</b> 거주도 인정돼요.</div>
{FT(4, True, '조특법 시행령 제74조①')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">1억 원에 산 땅 5억 원에 협의매수 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">25% 감면 효과</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>산출세액</small><b style="color:#1b5fa8">8,551만</b></div><div class="op">−</div><div class="bx"><small>감면 25%</small><b style="color:#2fa36b">2,138만</b></div></div>
<div class="total" style="top:610px"><small>감면 후 양도세</small><b>6,413만 원</b><span>지정 전 취득이면 40% → 3,420만 원 감면</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 25년 보유, 장기보유 공제 30%<br>· 감면 한도·농특세 별도 확인</div>
{FT(5, True, '조특법 제77조의3·소득세법 제95조②')}</div>''',
# 6 거주
f'''<div class="c dk bg-lilac">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#5a3fd6;font-size:34px">거주 요건, 이렇게 봐요</div><div class="h1" style="margin-top:8px">어디 살아야 할까?</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">같은 <span style="color:#1f8a57">시·군·구</span><br>또는 연접 시·군·구</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">땅에서<br><span style="color:#1b5fa8">직선 30km 이내</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">상속받은 땅은<br><span style="color:#c0392b">부모님 기간 합산</span></div></div>
</div>
{FT(6, True, '조특법 시행령 제74조①④')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '그린벨트 땅 매수 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">감면</span> 확인!'),
]
