import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 214
SLUG = 'retirement-pension-contribution-deduction'
CAT = '법인세'
DATE = '2026-11-27'
TITLE = '직원 퇴직금, 법인 비용은 언제 인정될까요 — 퇴직급여충당금은 2016년부터 손금 0%, 퇴직연금에 부담금을 내면 그 해 비용(DC형 전액, DB형은 퇴직금 추계액 한도), 임원 DC는 퇴직 때 한도 정산'
DESC = '2016년 1월 1일 이후 개시하는 사업연도부터 퇴직급여충당금은 손금 한도가 추계액의 0%라 결산에 쌓아도 비용으로 인정되지 않고, 실제 퇴직금을 지급할 때 손금이 됩니다. 반면 퇴직연금 부담금은 낸 사업연도에 손금으로 인정되며, 확정기여형(DC)은 전액, 확정급여형(DB)은 퇴직금 추계액에서 충당금과 이미 낸 부담금을 뺀 한도 내에서 손금입니다. 임원 DC 부담금은 퇴직 시 임원 퇴직금 한도로 정산합니다. 법인세법 시행령 제44조의2, 제60조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '법인세법 제33조, 같은 법 시행령 제44조의2제1항~제5항, 제60조제1항·제2항'
TAGS = ['퇴직연금', '퇴직급여충당금', 'DC형', 'DB형', '법인세', '부산세무사']
ALTS = ['퇴직연금 손금 (표지)', '퇴직연금 손금 (상담 질문)', '퇴직연금 손금 (DC·DB 비교)', '퇴직연금 손금 (O·X 퀴즈)', '퇴직연금 손금 (세금 효과)', '퇴직연금 손금 (임원 주의)', '퇴직연금 손금 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
연말 결산 때 "직원 퇴직금 충당금을 쌓았는데 비용으로 인정되나요?"라는 질문을 자주 받습니다. 결론부터 말씀드리면, <b>퇴직급여충당금은 2016년부터 법인세 비용(손금)으로 인정되지 않습니다</b>. 대신 <b>퇴직연금</b>에 부담금을 내면 그 해에 비용으로 인정받을 수 있습니다. 같은 퇴직금이라도 <b>언제 비용이 되느냐</b>가 달라지는 것이지요. DC형·DB형 차이와 임원 주의점까지 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li><b>퇴직급여충당금</b>은 2016년 이후 개시 사업연도부터 손금 한도가 <b>0%</b> — 장부에 쌓아도 비용이 아니고, 실제 퇴직금을 줄 때 비용이 됩니다.</li><li><b>퇴직연금 부담금</b>은 낸 사업연도에 손금: <b>DC형은 전액</b>, <b>DB형</b>은 퇴직금 추계액에서 충당금 잔액과 이미 낸 부담금을 뺀 금액이 한도입니다.</li><li><b>임원</b>의 DC 부담금은 퇴직할 때 그동안 낸 합계를 퇴직급여로 보아 <b>임원 퇴직금 한도</b>로 정산합니다.</li></ol>
<div class="small" style="margin-top:8px">(법인세법 시행령 제44조의2·제60조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"직원 퇴직금 추계액이 2억 원이라 결산에 퇴직급여충당금 2억 원을 잡았어요. 올해 법인세가 줄어들겠죠?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>(주)○○(가칭, 12월 결산)의 직원 전원 퇴직금 추계액은 <b>2억 원</b>이고 퇴직연금은 아직 없습니다. 결산에 퇴직급여충당금 2억 원을 비용으로 잡아도 법인세 계산에서는 <b>전액 손금불산입</b>됩니다. 반면 올해 DB형 퇴직연금에 가입해 <b>2억 원</b>을 부담금으로 내면, 추계액 한도 안이므로 <b>2억 원 전액</b>이 올해 손금이 됩니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 퇴직급여충당금 vs 퇴직연금</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>손금 인정</th><th>근거</th></tr>
<tr><td>퇴직급여충당금</td><td>누적 한도 = 퇴직금 추계액 × <b>0%</b>(2016.1.1. 이후 개시 사업연도) → 사실상 <b>불인정</b>, 실제 지급 시 손금</td><td>시행령 제60조제2항제7호</td></tr>
<tr><td><b>DC형</b>(확정기여형·IRP·중소기업퇴직연금기금 등) 부담금</td><td>낸 금액 <b>전액 손금</b>(임원은 퇴직 시 한도 정산)</td><td>시행령 제44조의2제3항</td></tr>
<tr><td><b>DB형</b>(확정급여형) 부담금</td><td>[퇴직금 추계액(또는 근로자퇴직급여 보장법상 금액 기준 중 큰 금액) − 기말 퇴직급여충당금(세무상 잔액) − 직전까지 낸 부담금] 한도 내 손금</td><td>시행령 제44조의2제4항</td></tr>
<tr><td>신고 서류</td><td>법인세 신고 때 <b>퇴직연금부담금조정명세서</b> 제출</td><td>시행령 제44조의2제5항</td></tr>
</table></div>

<h2>2. (주)○○ 사례 — 세금 효과</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>충당금만 설정</th><th>퇴직연금 2억 원 납입</th></tr>
<tr><td>올해 손금 인정액</td><td>0원</td><td>200,000,000</td></tr>
<tr><td>올해 법인세 감소(20% 구간 가정)</td><td>0원</td><td><b>40,000,000</b></td></tr>
<tr><td>법인지방소득세 포함</td><td>0원</td><td>44,000,000</td></tr>
</table></div>
<p>퇴직연금에 넣은 돈은 나중에 직원이 퇴직할 때 받는 돈이므로, 법인 입장에서는 <b>퇴직금 비용을 미리 인정</b>받아 법인세를 <b>앞당겨 줄이는</b> 효과가 있습니다. 다만 회사 자금이 외부 금융기관에 묶이므로 자금 사정도 함께 보셔야 합니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 과세표준이 손금 전후 모두 20% 구간(2억 원 초과 200억 원 이하, 2026년 시작 사업연도)이라고 가정했고, 법인지방소득세는 10%로 단순 가정했습니다.</p>

<h2>3. 임원 DC형은 이렇게 정산합니다</h2>
<p>임원에 대한 DC형 부담금도 낸 해에는 손금이지만, 임원이 <b>퇴직하는 해</b>에 그동안 낸 부담금 합계를 퇴직급여로 보아 <b>임원 퇴직금 한도</b>(정관 규정 또는 법정 산식, <a href="/column/27-executive-retirement-pay.html">칼럼 27</a>)와 비교합니다. 한도를 넘으면 퇴직 연도 부담금에서 초과액을 손금불산입하고, 초과액이 그해 부담금보다 크면 그 차액을 <b>익금산입</b>합니다(시행령 제44조의2제3항 단서).</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 결산에 잡은 퇴직급여충당금은 법인세에서 <b>손금불산입</b>(유보)으로 조정했다.</li>
<li>☐ 퇴직연금 유형(DC·DB)과 연내 <b>납입 일정</b>을 확인했다(12월 결산이면 12월 31일까지 납입분이 올해 손금).</li>
<li>☐ DB형은 <b>추계액 한도</b>를 계산해 초과 납입분이 없는지 확인했다.</li>
<li>☐ 임원 DC 부담금은 <b>퇴직금 지급규정</b>과 한도를 미리 점검했다.</li>
<li>☐ 법인세 신고 때 퇴직연금부담금조정명세서를 첨부했다.</li>
</ul>
<p>퇴직연금은 직원 복지와 법인세 절감을 함께 챙길 수 있는 제도입니다. 연말 결산 전에 퇴직금 추계액과 퇴직연금 납입 계획을 가지고 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>퇴직금 추계액 명세(직원별)</td><td>DB형 손금 한도</td></tr>
<tr><td>퇴직연금 계약서·납입 내역</td><td>DC·DB 유형, 납입액</td></tr>
<tr><td>퇴직급여충당금 명세</td><td>손금불산입 조정</td></tr>
<tr><td>정관·임원 퇴직금 지급규정</td><td>임원 퇴직금 한도</td></tr>
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
<img class="ch" src="ch/worry-doc-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">결산 때 쌓은 퇴직급여충당금</div><div class="t">비용으로<br>인정될까요?</div><div class="series">법인세 절세 series 6편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">연말 결산 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">대표님</div><div class="say">퇴직급여충당금<br><span class="mk">2억</span> 잡았으니<br>법인세 줄죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">충당금은 <span class="hl">0%</span>예요.<br>퇴직연금에<br>넣어야 비용!</div></div>
<img class="ch" src="ch/smile-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">DC·DB 차이는? →</div>
{FT(2, False)}</div>''',
# 3 타일
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">올해 손금으로 인정되는 금액</div><div class="h1" style="margin-top:8px">퇴직금 비용 인정</div></div>
<div class="tiles" style="top:360px">
 <div class="tile wide t-green"><div class="who" style="font-size:36px">DC형 퇴직연금 부담금</div><div class="amt">전액</div></div>
 <div class="tile t-blue"><div class="who">DB형 부담금</div><div class="amt">추계액 한도</div></div>
 <div class="tile t-red"><div class="who">퇴직급여충당금</div><div class="amt">0<small>%</small></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:900px;font-size:30px;font-weight:600">· 충당금은 실제 퇴직금을 지급할 때 비용이 돼요.<br>· 법인세 신고 때 퇴직연금부담금조정명세서 제출</div>
{FT(3, True, '법인세법 시행령 제44조의2·제60조')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">임원 DC형 부담금은<br>얼마를 내든 퇴직 때까지<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">모두 비용으로 끝?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 퇴직 때 <b style="font-weight:900">임원 퇴직금 한도</b>로<br>정산해 초과분은 다시 빼요.</div>
{FT(4, True, '법인세법 시행령 제44조의2③')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">퇴직금 추계액 2억 원 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">올해 법인세 차이</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>충당금만</small><b style="color:#ff5c8a">0원</b></div><div class="op">vs</div><div class="bx"><small>퇴직연금 납입</small><b style="color:#2fa36b">2억 손금</b></div></div>
<div class="total" style="top:610px"><small>법인세 감소(지방세 포함)</small><b>4,400만 원</b><span>20% 구간 가정 · 비용을 앞당겨 인정</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">포인트</b><br>· 12월 결산은 12/31까지 납입분<br>· DB형은 추계액 한도 확인</div>
{FT(5, True, '법인세법 시행령 제44조의2④')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">결산 전에</div><div class="h1" style="margin-top:8px">꼭 확인하세요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">충당금은<br><span style="color:#c0392b">손금불산입</span> 조정</div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">퇴직연금<br><span style="color:#b9770e">연내 납입</span> 계획</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">임원은<br><span style="color:#1b5fa8">퇴직금 규정</span> 점검</div></div>
</div>
{FT(6, True, '법인세법 시행령 제44조의2·제60조')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '연말 결산 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">퇴직연금</span> 점검!'),
]
