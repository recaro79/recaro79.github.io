import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 208
SLUG = 'housing-subscription-savings-deduction'
CAT = '종합소득세'
DATE = '2026-11-27'
TITLE = '12월 31일 전에 주택청약종합저축을 채우시면 — 총급여 7천만 원 이하 무주택 세대주(배우자 포함)는 연 300만 원 납입액의 40%를 소득공제, 무주택확인서는 다음 해 2월 말까지'
DESC = '총급여액 7천만 원 이하이고 과세기간 중 주택을 소유하지 않은 세대의 세대주 또는 세대주의 배우자가 2028년 12월 31일까지 주택청약종합저축에 납입한 금액(연 300만 원 한도)의 40%를 근로소득금액에서 공제합니다. 무주택 확인서를 다음 해 2월 말까지 저축 취급기관에 내야 하고, 가입 후 5년 안에 해지하면 납입액의 6%가 추징될 수 있습니다. 조세특례제한법 제87조제2항·제4항·제5항·제7항 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '조세특례제한법 제87조제2항·제4항·제5항·제7항'
TAGS = ['주택청약종합저축', '청약소득공제', '연말정산', '무주택세대주', '근로소득자', '부산세무사']
ALTS = ['주택청약 소득공제 (표지)', '주택청약 소득공제 (상담 질문)', '주택청약 소득공제 (요건)', '주택청약 소득공제 (O·X 퀴즈)', '주택청약 소득공제 (공제 계산)', '주택청약 소득공제 (추징 주의)', '주택청약 소득공제 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
연말이 다가오면 연금저축·IRP와 함께 꼭 챙기셔야 할 것이 <b>주택청약종합저축</b>입니다. 집이 없는 직장인이라면 올해 <b>12월 31일까지</b> 낸 금액 중 연 300만 원까지의 <b>40%</b>, 최대 <b>120만 원</b>을 소득에서 빼 줍니다. 요건과 함께 놓치기 쉬운 <b>무주택 확인서 제출</b>, <b>중도해지 추징</b>까지 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li><b>총급여 7천만 원 이하</b> 근로자로서 과세기간 중 <b>무주택 세대의 세대주 또는 세대주의 배우자</b>가 대상입니다(2028년 12월 31일 납입분까지).</li><li>그 해 납입액(연 <b>300만 원</b> 한도)의 <b>40%</b>를 근로소득금액에서 공제합니다(최대 120만 원).</li><li>다음 해 <b>2월 말까지 무주택 확인서</b>를 은행에 내야 하고, 가입 후 <b>5년 안에 해지</b>하면 공제 후 납입액 누계의 6%가 추징될 수 있습니다.</li></ol>
<div class="small" style="margin-top:8px">(조세특례제한법 제87조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"청약통장에 매달 10만 원씩 넣고 있어요. 연말에 더 넣으면 세금이 줄어든다던데 정말인가요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>총급여 5천만 원인 무주택 세대주 신○○ 님(가칭)은 올해 청약통장에 <b>120만 원</b>(월 10만 원)을 넣었습니다. 12월에 <b>180만 원</b>을 더 넣어 연 300만 원을 채우면, 소득공제액이 48만 원에서 <b>120만 원</b>으로 늘어납니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 누가, 얼마나 공제받을까요</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>대상</td><td>근로소득자(일용근로자 제외)로 해당 과세기간 <b>총급여 7천만 원 이하</b></td><td>조특법 제87조제2항</td></tr>
<tr><td>무주택 요건</td><td>해당 과세기간 중 <b>주택을 소유하지 않은 세대</b>의 <b>세대주 또는 세대주의 배우자</b>(세대주 여부는 과세기간 종료일 기준)</td><td>같은 조 제2항·제5항</td></tr>
<tr><td>공제액</td><td>주택청약종합저축 납입액(연 <b>300만 원</b> 한도)의 <b>40%</b></td><td>같은 조 제2항</td></tr>
<tr><td>적용 기한</td><td><b>2028년 12월 31일</b>까지 납입분</td><td>같은 조 제2항</td></tr>
<tr><td>합산 한도</td><td>주택임차차입금 원리금상환액 공제와 합해 연 400만 원, 장기주택저당차입금 이자 공제까지 합해 연 800만 원 등</td><td>같은 조 제5항(<a href="/column/191-mortgage-interest-deduction-year-end.html">칼럼 191</a>)</td></tr>
<tr><td>제출 서류</td><td>공제받을 과세기간의 <b>다음 연도 2월 말</b>까지 저축 취급기관에 <b>무주택 확인서</b> 제출</td><td>같은 조 제4항제1호</td></tr>
</table></div>
<p>과세기간 중에 주택 당첨 등 정해진 사유 외로 <b>중도해지</b>하면 그 해 납입액은 공제되지 않습니다(같은 조 제2항 단서).</p>

<h2>2. 신○○ 님 사례 계산</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>지금처럼(120만 원)</th><th>12월에 채우면(300만 원)</th></tr>
<tr><td>소득공제액(40%)</td><td>480,000</td><td><b>1,200,000</b></td></tr>
<tr><td>세금 감소(15% 구간 가정)</td><td>72,000</td><td><b>180,000</b></td></tr>
<tr><td>지방소득세 포함</td><td>79,200</td><td>198,000</td></tr>
</table></div>
<p>180만 원을 더 넣으면 세금이 약 <b>11만 8천 원</b>(지방소득세 포함) 더 줄어듭니다. 청약통장은 나중에 내 집 마련에도 쓰이니 여유가 되신다면 연말에 한도를 채워 보세요.</p>
<p class="small">※ python으로 계산·검산했습니다. 신○○ 님의 종합소득 과세표준이 공제 전후 모두 15% 구간(1,400만 원 초과 5,000만 원 이하)에 있다고 가정했습니다.</p>

<h2>3. 추징을 조심하세요</h2>
<div class="tbl"><table>
<tr><th>추징 사유</th><th>추징세액</th><th>근거</th></tr>
<tr><td>가입일부터 <b>5년 이내 해지</b>(사망·해외이주 등 정해진 사유 제외)</td><td>소득공제 적용 과세기간 이후 납입액(연 300만 원 한도) 누계 × <b>6%</b> — 실제 감면세액이 더 적다는 것을 증명하면 그 금액</td><td>조특법 제87조제7항제1호</td></tr>
<tr><td>국민주택규모를 <b>초과하는 주택</b>에 청약해 당첨</td><td>같음</td><td>같은 항 제2호</td></tr>
</table></div>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 올해 <b>총급여 7천만 원 이하</b>인지, 과세기간 중 세대원 모두 <b>무주택</b>인지 확인했다.</li>
<li>☐ 12월 31일 현재 <b>세대주 또는 세대주의 배우자</b>인지 확인했다.</li>
<li>☐ 올해 납입액을 확인하고 <b>300만 원</b>까지 채울지 정했다.</li>
<li>☐ 은행에 <b>무주택 확인서</b>를 냈는지(다음 해 2월 말까지) 확인했다.</li>
<li>☐ 5년 안에 해지할 계획이 있는지, 청약할 주택 규모는 어떤지 확인했다.</li>
</ul>
<p>연말정산은 12월 31일까지 무엇을 했느냐로 결정됩니다. 청약통장, 연금저축·IRP(<a href="/column/152-pension-account-tax-credit.html">칼럼 152</a>), 신용카드(<a href="/column/185-credit-card-deduction-2026-children.html">칼럼 185</a>)를 함께 점검해 보시고, 궁금하신 점은 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>청약통장 납입 내역</td><td>올해 납입액, 가입일</td></tr>
<tr><td>주민등록등본</td><td>세대주·세대원 확인</td></tr>
<tr><td>원천징수영수증·급여명세</td><td>총급여 7천만 원 이하 여부</td></tr>
<tr><td>주택 대출·월세 자료</td><td>주택자금 공제 합산 한도</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-night">{HD()}
<div class="bokeh" style="left:80px;top:190px;width:120px;height:120px;background:#8fb0ff;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:240px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wink-piggy.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">12월 31일까지 확인하세요</div><div class="t">청약통장으로<br>세금 줄이기</div><div class="series">종합소득세 절세 series 8편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">연말 직장인 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">신○○ 님</div><div class="say">청약통장에<br>연말에 더 넣으면<br><span class="mk">세금</span>이 줄어요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">300만 원까지<br><span class="hl">40%</span>를<br>소득공제해요!</div></div>
<img class="ch" src="ch/smile-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">요건은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">세 가지를 확인하세요</div><div class="h1" style="margin-top:8px">공제 요건</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">총급여<br><span style="color:#1f8a57">7천만 원 이하</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">과세기간 중<br><span style="color:#1b5fa8">무주택 세대</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx"><span style="color:#c0392b">세대주</span> 또는<br>세대주의 배우자</div></div>
</div>
{FT(3, True, '조특법 제87조②')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">청약통장에 넣기만 하면<br>무주택 확인서는<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">안 내도 된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-doc.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 다음 해 <b style="font-weight:900">2월 말까지</b><br>은행에 무주택 확인서를 내야 해요.</div>
{FT(4, True, '조특법 제87조④1호')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">총급여 5천만 원 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">300만 원 채우면</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>납입액</small><b style="color:#1b5fa8">300만</b></div><div class="op">×</div><div class="bx"><small>공제율</small><b style="color:#ff5c8a">40%</b></div></div>
<div class="total" style="top:610px"><small>소득공제</small><b>120만 원</b><span>세금 약 19만 8천 원 감소(지방세 포함·15% 구간)</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">포인트</b><br>· 월 25만 원이면 연 300만 원<br>· 2028년 납입분까지 적용</div>
{FT(5, True, '조특법 제87조②')}</div>''',
# 6 추징
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4">이럴 땐 돌려내야 해요</div><div style="font-size:100px;font-weight:900;letter-spacing:-4px;line-height:1.1;text-shadow:0 8px 20px rgba(120,0,40,.35)">추징 6%</div></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="right:30px;top:120px;width:360px">
<div class="rows" style="top:520px">
 <div class="row"><div class="ic" style="background:#ff5c8a">①</div><div class="tx">가입 <span style="color:#e83e6f">5년 안에</span> 해지</div></div>
 <div class="row"><div class="ic" style="background:#ff9a3c">②</div><div class="tx"><span style="color:#e8761e">국민주택규모 초과</span> 당첨</div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:900px;font-size:30px">· 공제 후 납입액(연 300만 원 한도) 누계의 6%<br>· 사망·해외이주 등은 <b style="color:#fff3c4">예외</b>예요.</div>
{FT(6, True, '조특법 제87조⑦')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '12월 31일 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">한도</span> 채우세요!'),
]
