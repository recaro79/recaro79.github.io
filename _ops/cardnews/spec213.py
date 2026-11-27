import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 213
SLUG = 'annuity-right-valuation-inheritance-gift'
CAT = '상속세·증여세'
DATE = '2026-11-27'
TITLE = '연금으로 나눠 받는 보험금·권리를 상속·증여받으셨다면 — 받을 총액이 아니라 해마다 받을 금액을 연 3%로 할인한 현재가치로 평가합니다(1년분 20배 한도), 해지하면 받을 일시금이 더 크면 그 금액'
DESC = '정기금을 받을 권리를 상속·증여받으면, 확정기간형(유기정기금)은 남은 기간 각 연도에 받을 금액을 연 3%로 할인한 현재가치 합계(1년분의 20배 한도), 기간이 정해지지 않은 무기정기금은 1년분의 20배, 종신정기금은 통계청 기대여명까지의 현재가치로 평가합니다. 평가기준일에 계약 해지 등으로 받을 수 있는 일시금이 더 크면 그 일시금으로 평가합니다. 상속세 및 증여세법 제65조제1항, 같은 법 시행령 제62조, 같은 법 시행규칙 제19조의2제3항 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '상속세 및 증여세법 제65조제1항, 같은 법 시행령 제62조, 같은 법 시행규칙 제19조의2제3항'
TAGS = ['정기금평가', '연금보험상속', '연금보험증여', '상속재산평가', '현재가치', '부산세무사']
ALTS = ['정기금 평가 (표지)', '정기금 평가 (상담 질문)', '정기금 평가 (평가 방법)', '정기금 평가 (O·X 퀴즈)', '정기금 평가 (사례 계산)', '정기금 평가 (확인할 점)', '정기금 평가 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
부모님이 연금보험을 남기셔서 자녀가 앞으로 <b>20년 동안 해마다 연금</b>을 받게 되는 경우가 있습니다. 이때 상속세는 "앞으로 받을 돈을 모두 더한 금액"으로 낼까요? 그렇지 않습니다. 세법은 이런 <b>정기금을 받을 권리</b>를 미래에 받을 금액을 <b>현재가치로 할인</b>해 평가합니다. 다만 계약을 해지하면 받을 수 있는 <b>일시금</b>이 더 크면 그 금액으로 평가한다는 점도 꼭 함께 보셔야 합니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li><b>기간이 정해진 정기금</b>(유기정기금): 남은 기간 각 연도에 받을 금액을 <b>연 3%</b>로 할인한 현재가치의 합계로 평가하되, <b>1년분의 20배</b>를 넘을 수 없습니다.</li><li>기간이 정해지지 않은 <b>무기정기금</b>은 1년분의 20배, 평생 받는 <b>종신정기금</b>은 받는 사람의 성별·연령별 <b>기대여명</b>까지의 현재가치로 평가합니다.</li><li>평가기준일에 계약을 <b>철회·해지·취소</b>해서 받을 수 있는 <b>일시금</b>이 더 크면 그 일시금이 평가액입니다.</li></ol>
<div class="small" style="margin-top:8px">(상속세 및 증여세법 제65조, 같은 법 시행령 제62조, 같은 법 시행규칙 제19조의2 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"아버지가 남기신 연금보험에서 제가 20년 동안 해마다 1,200만 원씩 받게 됐어요. 상속세는 2억 4천만 원을 기준으로 내야 하나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>강○○ 님(가칭)은 아버지가 돌아가시면서 연금보험의 수익자로서 앞으로 <b>20년간 매년 1,200만 원</b>(총 2억 4천만 원)을 받을 권리를 상속받았습니다. 첫 연금은 상속개시일부터 1년 뒤에 받고, 상속개시일 현재 계약을 해지하면 받을 수 있는 일시금은 <b>1억 6천만 원</b>이라고 가정하겠습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 정기금을 받을 권리, 이렇게 평가합니다</h2>
<div class="tbl"><table>
<tr><th>종류</th><th>평가 방법</th><th>근거</th></tr>
<tr><td><b>유기정기금</b>(기간 확정)</td><td>남은 기간 각 연도 정기금 ÷ (1 + 3%)<sup>n</sup>의 합계(n: 평가기준일부터 경과연수), <b>1년분 × 20배 한도</b></td><td>시행령 제62조제1호, 시행규칙 제19조의2제3항</td></tr>
<tr><td><b>무기정기금</b>(기간 미정)</td><td>1년분 정기금 × <b>20배</b></td><td>시행령 제62조제2호</td></tr>
<tr><td><b>종신정기금</b></td><td>받을 사람의 성별·연령별 <b>기대여명</b>(통계표, 소수점 이하 버림)까지 각 연도 정기금을 유기정기금과 같은 방식으로 할인한 합계</td><td>시행령 제62조제3호</td></tr>
<tr><td>일시금 비교</td><td>평가기준일에 계약 철회·해지·취소 등으로 받을 수 있는 <b>일시금이 더 크면 그 일시금</b></td><td>시행령 제62조 단서</td></tr>
</table></div>
<p>사망보험금이 상속재산으로 보는 재산(간주상속재산)에 해당하는지는 보험료를 누가 냈는지 등으로 먼저 판단합니다(<a href="/column/44-deemed-inheritance-insurance-retirement.html">칼럼 44</a>). 위 평가 방법은 그 권리가 <b>연금처럼 나눠 받는 형태</b>일 때의 가액 계산입니다.</p>

<h2>2. 강○○ 님 사례 계산</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>금액</th></tr>
<tr><td>앞으로 받을 총액(1,200만 원 × 20년)</td><td>240,000,000</td></tr>
<tr><td>연 3% 현재가치 합계(1~20년차 할인)</td><td><b>178,529,698</b></td></tr>
<tr><td>20배 한도(1,200만 원 × 20)</td><td>240,000,000 → 한도 이내</td></tr>
<tr><td>해지 시 일시금(가정)</td><td>160,000,000 → 현재가치보다 작음</td></tr>
<tr><td><b>평가액</b></td><td><b>178,529,698</b></td></tr>
</table></div>
<p>총액 2억 4천만 원이 아니라 약 <b>1억 7,853만 원</b>으로 평가합니다. 다른 상속재산이 많아 상속세 40% 구간이라면, 총액으로 잘못 계산했을 때보다 세금이 약 <b>2,459만 원</b> 적습니다. 반대로 해지 일시금이 현재가치보다 크다면 일시금으로 평가해야 하니 보험회사에서 <b>해지환급금 확인서</b>를 꼭 받아 두세요.</p>
<p class="small">※ python으로 계산·검산했습니다(원 미만 절사). 첫 정기금을 평가기준일부터 1년 뒤에 받는 것으로 보아 n = 1부터 할인했습니다. 실제 지급 시기·조건에 따라 계산이 달라질 수 있습니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 연금 지급이 <b>확정기간형</b>인지, <b>종신형</b>인지 약관과 지급 내역으로 확인했다.</li>
<li>☐ 평가기준일(상속개시일·증여일) 현재 <b>해지환급금(일시금)</b> 금액을 보험회사에서 확인했다.</li>
<li>☐ 보험료를 누가 냈는지 확인해 상속재산·증여재산 해당 여부를 먼저 판단했다(<a href="/column/65-insurance-proceeds-gift.html">칼럼 65</a>).</li>
<li>☐ 연금 외에 신탁 수익권처럼 나눠 받는 권리가 있다면 그 평가도 함께 확인했다(<a href="/column/134-trust-benefit-gift-tax.html">칼럼 134</a>).</li>
</ul>
<p>연금형 재산은 보험 약관, 지급 방식, 해지환급금에 따라 평가액이 크게 달라집니다. 상속·증여받으신 연금 권리가 있다면 보험증권과 지급 안내서를 가지고 편하게 상담해 주세요. 정확한 평가액부터 세금까지 함께 계산해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>보험증권·약관</td><td>계약자·피보험자·수익자, 지급 방식</td></tr>
<tr><td>연금 지급 안내서</td><td>연간 지급액, 지급 기간·시기</td></tr>
<tr><td>해지환급금 확인서(평가기준일 기준)</td><td>일시금과 현재가치 비교</td></tr>
<tr><td>보험료 납입 내역</td><td>상속·증여재산 해당 여부</td></tr>
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
<img class="ch" src="ch/wow-calc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">연금으로 받는 보험금 상속·증여</div><div class="t">총액이 아니라<br>현재가치로</div><div class="series">상속세 절세 series 7편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">상속인분들의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">강○○ 님</div><div class="say">20년간 1,200만 원씩,<br><span class="mk">2억 4천만 원</span>이<br>상속재산인가요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">연 3%로 할인한<br><span class="hl">현재가치</span>로<br>평가해요!</div></div>
<img class="ch" src="ch/smile-calc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">평가 방법은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">정기금을 받을 권리</div><div class="h1" style="margin-top:8px">평가 방법</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">기간 확정 → 3% 할인<br><span style="color:#1f8a57">1년분 20배 한도</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">기간 미정 →<br><span style="color:#1b5fa8">1년분 × 20배</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">종신 →<br><span style="color:#c0392b">기대여명</span>까지 할인</div></div>
</div>
{FT(3, True, '상증법 시행령 제62조·시행규칙 제19조의2③')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">해지환급금이 더 커도<br>현재가치로만<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">평가하면 된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 해지 시 받을 <b style="font-weight:900">일시금이</b><br><b style="font-weight:900">더 크면</b> 그 금액으로 평가해요.</div>
{FT(4, True, '상증법 시행령 제62조 단서')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">연 1,200만 원 × 20년 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">평가액은?</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>받을 총액</small><b style="color:#1b5fa8">2.4억</b></div><div class="op">→</div><div class="bx"><small>3% 현재가치</small><b style="color:#2fa36b">1.785억</b></div></div>
<div class="total" style="top:610px"><small>평가액</small><b>1억 7,853만 원</b><span>해지 일시금 1.6억 원보다 크므로</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 첫 연금은 1년 뒤 수령<br>· 해지 일시금 1억 6천만 원</div>
{FT(5, True, '상증법 시행령 제62조1호')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">신고 전에</div><div class="h1" style="margin-top:8px">꼭 확인하세요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx"><span style="color:#c0392b">확정형</span>인지<br>종신형인지</div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">평가기준일<br><span style="color:#b9770e">해지환급금</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">보험료를<br><span style="color:#1b5fa8">누가 냈는지</span></div></div>
</div>
{FT(6, True, '상증법 제65조①·시행령 제62조')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '연금형 재산 신고 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">평가액</span> 확인!'),
]
