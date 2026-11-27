import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 220
SLUG = 'inherited-deposit-valuation-accrued-interest'
CAT = '상속세'
DATE = '2026-11-27'
TITLE = '부모님이 남기신 정기예금·적금, 상속재산으로 얼마일까요 — 원금(예입총액)에 상속일까지 붙은 이자를 더하고 이자소득세 원천징수 상당액을 뺍니다, 금융재산 상속공제와 함께 확인'
DESC = '예금·저금·적금 등은 평가기준일(상속개시일) 현재 예입총액과 같은 날 현재 이미 지난 미수이자 상당액을 합친 금액에서 소득세법 제127조제1항에 따른 원천징수세액 상당 금액을 뺀 가액으로 평가합니다. 이렇게 평가한 금융재산에서 금융채무를 뺀 순금융재산에 대해 금융재산 상속공제(20%, 최대 2억 원)가 적용됩니다. 상속세 및 증여세법 제22조·제63조제4항, 소득세법 제129조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '상속세 및 증여세법 제63조제4항·제22조, 소득세법 제127조제1항·제129조제1항'
TAGS = ['상속예금평가', '미수이자', '정기예금상속', '금융재산상속공제', '상속세', '부산세무사']
ALTS = ['상속 예금 평가 (표지)', '상속 예금 평가 (상담 질문)', '상속 예금 평가 (계산식)', '상속 예금 평가 (O·X 퀴즈)', '상속 예금 평가 (사례 계산)', '상속 예금 평가 (확인할 점)', '상속 예금 평가 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"어머니 정기예금이 원금 3억 원인데, 상속세 신고할 때 3억 원만 적으면 되나요?" 상속 상담에서 아주 자주 받는 질문입니다. 정답은 <b>원금만으로는 부족합니다</b>. 세법은 예금·적금을 <b>상속개시일까지 이미 지난 기간의 이자</b>까지 더해 평가하고, 대신 그 이자에 대한 <b>원천징수세액 상당액은 빼 줍니다</b>. 오늘은 상속받은 예금의 평가 방법을 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>예금·저금·적금 등은 상속개시일 현재 <b>예입총액(넣은 돈)</b> + 그날까지 이미 지난 <b>미수이자 상당액</b> − <b>원천징수세액 상당액</b>으로 평가합니다.</li><li>일반 예금 이자의 원천징수세율은 <b>14%</b>이므로, 미수이자의 86% 정도가 더해진다고 보시면 됩니다.</li><li>이렇게 평가한 금융재산에서 금융채무를 뺀 순금융재산에는 <b>금융재산 상속공제</b>(20%, 최소 2천만 원·최대 2억 원)가 적용됩니다.</li></ol>
<div class="small" style="margin-top:8px">(상속세 및 증여세법 제63조제4항·제22조, 소득세법 제129조제1항 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"어머니 정기예금이 원금 3억 원이에요. 만기 전에 돌아가셨는데 상속재산은 3억 원으로 신고하면 되나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>박○○ 님(가칭)의 어머니는 원금 <b>3억 원</b>의 1년 만기 정기예금에 가입하신 지 8개월째에 돌아가셨습니다. 은행에서 상속개시일 기준 경과이자를 확인해 보니 <b>600만 원</b>이었습니다. 보통예금 잔액은 <b>2,000만 원</b>이었고, 이 계좌의 미수이자는 무시해도 될 만큼 적었습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다. 실제 미수이자는 금융회사에 상속개시일 기준으로 확인하셔야 합니다.</p>

<h2>1. 예금·적금 평가 방법</h2>
<div class="tbl"><table>
<tr><th>항목</th><th>내용</th><th>근거</th></tr>
<tr><td>① 예입총액</td><td>평가기준일(상속개시일) 현재 넣어 둔 원금 합계</td><td rowspan="3">상증법 제63조제4항</td></tr>
<tr><td>② 미수이자 상당액</td><td>같은 날 현재 <b>이미 지난 기간</b>에 해당하는 이자(아직 받지 않은 이자)</td></tr>
<tr><td>③ 원천징수세액 상당액</td><td>「소득세법」 제127조제1항에 따른 원천징수세액 상당 금액을 뺌(일반 이자소득 원천징수세율 14%, 소득세법 제129조제1항제1호라목)</td></tr>
<tr><td>평가액</td><td colspan="2"><b>① + ② − ③</b></td></tr>
</table></div>
<p>상속개시일 이후 예금을 해지하면서 실제로 받은 금액(중도해지 이율 적용 등)이 아니라, <b>상속개시일 현재</b>를 기준으로 위 방식에 따라 계산한다는 점이 중요합니다. 돌아가시기 전에 인출해 쓰신 예금은 별도의 추정 규정이 있으니 <a href="/column/189-pre-death-withdrawal-presumed-inheritance.html">칼럼 189</a>를 함께 보시면 좋습니다.</p>

<h2>2. 박○○ 님 사례 — 평가액과 금융재산 상속공제</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>금액(원)</th></tr>
<tr><td>정기예금 예입총액</td><td>300,000,000</td></tr>
<tr><td>+ 미수이자 상당액</td><td>6,000,000</td></tr>
<tr><td>− 원천징수세액 상당액(14%)</td><td>△840,000</td></tr>
<tr><td>정기예금 평가액</td><td><b>305,160,000</b></td></tr>
<tr><td>보통예금</td><td>20,000,000</td></tr>
<tr><td>금융재산 합계(금융채무 없음)</td><td>325,160,000</td></tr>
<tr><td>금융재산 상속공제(20%)</td><td><b>65,032,000</b></td></tr>
</table></div>
<p>원금 3억 원만 신고했다면 정기예금이 <b>516만 원 적게</b> 신고됩니다. 작은 금액 같아도 과소신고가 되면 가산세가 붙을 수 있으니 처음부터 정확히 계산하시는 것이 좋습니다. 금융재산 상속공제는 <a href="/column/17-financial-asset-deduction.html">칼럼 17</a>에서 자세히 다뤘습니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 순금융재산 가액이 2천만 원을 넘으면 그 20%와 2천만 원 중 큰 금액을 공제하고 2억 원을 넘으면 2억 원을 공제합니다(상속세 및 증여세법 제22조제1항). 상속세 신고기한까지 신고하지 않은 타인 명의 금융재산과 최대주주 등의 주식은 금융재산 상속공제 대상에서 빠집니다(같은 조 제2항).</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 상속인 금융거래 조회로 고인 명의 <b>예금·적금 계좌</b>를 빠짐없이 찾았다.</li>
<li>☐ 계좌마다 <b>상속개시일 기준 잔액</b>과 <b>경과이자</b>를 금융회사에서 확인했다.</li>
<li>☐ 미수이자에서 <b>원천징수세액 상당액(14%)</b>을 빼고 평가액을 계산했다.</li>
<li>☐ 대출 등 <b>금융채무</b>를 빼서 순금융재산을 구하고 금융재산 상속공제를 반영했다.</li>
<li>☐ 상속개시 전 1~2년 안에 큰돈이 인출된 적이 있는지 확인했다.</li>
</ul>
<p>예금은 숫자가 분명해 보여도 이자·원천징수·공제를 함께 따져야 정확한 신고가 됩니다. 상속세 신고를 준비하고 계시면 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>상속인 금융거래 조회 결과</td><td>고인 명의 계좌 전체</td></tr>
<tr><td>금융회사 잔액증명서(상속개시일 기준, 경과이자 포함)</td><td>예입총액·미수이자</td></tr>
<tr><td>대출 잔액증명서</td><td>금융채무</td></tr>
<tr><td>최근 2년 거래내역</td><td>상속개시 전 인출 내역</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

_S217 = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec217.py'))

CARDS = [
# 1 표지
f'''<div class="c bg-forest">{HD()}
<div class="bokeh" style="left:90px;top:220px;width:120px;height:120px;background:#bff0d0;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:260px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/smile-piggy.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">상속받은 정기예금·적금</div><div class="t">원금만 적으면<br>안 돼요</div><div class="series">상속세 절세 series 9편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-lilac">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#5b2f7a">상속인의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">박○○ 님</div><div class="say">정기예금 원금<br><span class="mk">3억 원</span>만<br>신고하면 되죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">그날까지 붙은<br><span class="hl">이자</span>도 더해요!</div></div>
<img class="ch" src="ch/wink-calc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#5b2f7a">계산법은? →</div>
{FT(2, False)}</div>''',
# 3 계산식
f'''<div class="c bg-night">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">상속개시일 기준</div><div class="h1" style="margin-top:8px">예금 평가 공식</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#3d8bff">＋</div><div class="tx">예입총액<br><span style="color:#1b5fa8">넣어 둔 원금</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">＋</div><div class="tx">미수이자<br><span style="color:#1f8a57">이미 지난 기간 이자</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">－</div><div class="tx">원천징수세액<br><span style="color:#c0392b">상당액(14%)</span></div></div>
</div>
{FT(3, True, '상증법 제63조④')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">상속 뒤 중도해지해<br>실제 받은 돈으로<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">평가하면 된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! <b style="font-weight:900">상속개시일 현재</b> 원금·<br>경과이자를 기준으로 계산해요.</div>
{FT(4, True, '상증법 제63조④')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">원금 3억 · 경과이자 600만 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">정기예금 평가액</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>원금만</small><b style="color:#ff5c8a">3억</b></div><div class="op">→</div><div class="bx"><small>세법 평가</small><b style="color:#2fa36b">3.05억</b></div></div>
<div class="total" style="top:610px"><small>3억 + 600만 − 84만</small><b>3억 516만 원</b><span>금융재산공제 20%도 함께</span></div>
<img class="ch" src="ch/smile-calc.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 원천징수세율 14%<br>· 미수이자는 은행 확인액</div>
{FT(5, True, '상증법 제63조④, 소득세법 제129조')}</div>''',
# 6 확인
f'''<div class="c bg-orange">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">신고 전에 확인!</div><div class="h1" style="margin-top:8px">체크 포인트</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#3d8bff">①</div><div class="tx">계좌 전체 조회<br><span style="color:#1b5fa8">빠진 계좌 없게</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">②</div><div class="tx">상속일 기준<br><span style="color:#1f8a57">잔액·경과이자</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">금융재산공제<br><span style="color:#c0392b">20%·최대 2억</span></div></div>
</div>
{FT(6, True, '상증법 제22조·제63조④')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '상속세 신고 전에').replace('<span class="hl">기한</span> 확인!', '<span class="hl">예금 평가</span> 확인!'),
]
