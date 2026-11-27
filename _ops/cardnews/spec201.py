import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 201
SLUG = 'rescinded-sale-capital-gains-refund'
CAT = '양도소득세'
DATE = '2026-11-27'
TITLE = '부동산을 판 뒤 매매계약이 해제됐다면 — 이미 낸 양도세는 해제 사실을 안 날부터 3개월 안에 경정청구로 돌려받습니다, 잔금 전 해제는 양도가 아니고 받은 위약금은 기타소득'
DESC = '양도소득세를 신고·납부한 뒤 그 매매계약이 해제권 행사로 해제되거나 계약 성립 후 부득이한 사유로 해제·취소되면, 그 사유가 발생한 것을 안 날부터 3개월 이내에 후발적 사유에 의한 경정청구를 할 수 있습니다. 잔금 청산(또는 먼저 한 등기) 전에 해제되면 양도 자체가 없고, 매수인에게서 받은 위약금·배상금은 기타소득입니다. 국세기본법 제45조의2제2항, 같은 법 시행령 제25조의2, 소득세법 제98조·제21조제1항제10호 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '국세기본법 제45조의2제2항, 같은 법 시행령 제25조의2, 소득세법 제98조, 같은 법 시행령 제162조제1항, 소득세법 제21조제1항제10호'
TAGS = ['계약해제', '양도세환급', '경정청구', '후발적사유', '위약금', '부산세무사']
ALTS = ['계약 해제와 양도세 (표지)', '계약 해제와 양도세 (상담 질문)', '계약 해제와 양도세 (언제 해제됐나)', '계약 해제와 양도세 (O·X 퀴즈)', '계약 해제와 양도세 (환급 사례)', '계약 해제와 양도세 (확인할 점)', '계약 해제와 양도세 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
부동산을 팔고 양도세까지 신고·납부했는데, 매수인이 남은 잔금을 끝내 주지 않아 계약을 해제하고 소유권을 되찾는 경우가 있습니다. 이럴 때 "이미 낸 양도세는 어떻게 되나요?"라는 질문을 받습니다. 결론부터 말씀드리면, 일정한 해제 사유에 해당하면 <b>해제 사실을 안 날부터 3개월 안에 경정청구</b>를 해서 돌려받을 수 있습니다. 기한이 짧으니 꼭 기억해 두세요.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>매매계약이 <b>해제권 행사</b>로 해제되거나 계약 후 생긴 <b>부득이한 사유</b>로 해제·취소되면, 낸 양도세는 <b>후발적 사유 경정청구</b> 대상입니다.</li><li>청구 기한은 그 사유가 발생한 것을 <b>안 날부터 3개월 이내</b>입니다(일반 경정청구 5년과 다릅니다).</li><li><b>잔금 청산 전</b>(먼저 등기한 경우는 등기접수일 전)에 해제되면 양도 자체가 없고, 매수인에게 받은 <b>위약금·배상금</b>은 기타소득입니다.</li></ol>
<div class="small" style="margin-top:8px">(국세기본법 제45조의2제2항, 같은 법 시행령 제25조의2, 소득세법 제98조·제21조제1항제10호 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"매수인 사정을 봐 드려 잔금 1억 원을 남기고 등기를 먼저 넘겨 드렸는데, 끝내 잔금을 안 줘서 계약을 해제했어요. 이미 낸 양도세 7천만 원은 어떻게 되나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>정○○ 님(가칭)은 2016년에 5억 원에 산 상가를 2026년 6월 <b>8억 원</b>에 팔기로 하고, 잔금 1억 원을 남긴 채 소유권이전등기를 먼저 해 주었습니다. 잔금 전에 등기를 했으므로 양도일은 <b>등기접수일</b>이 되어, 정○○ 님은 8월 말까지 양도세 <b>약 7,031만 원</b>을 예정신고·납부하셨습니다. 그런데 매수인이 끝내 잔금을 주지 않아 11월에 계약서의 해제 조항에 따라 <b>계약을 해제</b>하고 소유권을 되찾았습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 언제 해제되었는지가 중요합니다</h2>
<div class="tbl"><table>
<tr><th>상황</th><th>양도세 처리</th><th>근거</th></tr>
<tr><td>잔금 청산 <b>전</b>, 등기도 하기 전 해제</td><td>양도시기(대금 청산일)가 오지 않았으므로 <b>양도 없음</b> — 양도세 신고 대상 아님</td><td>소득세법 제98조, 시행령 제162조제1항</td></tr>
<tr><td>잔금 전 <b>등기를 먼저</b> 넘겨준 뒤 해제</td><td>등기접수일이 양도일 → 신고·납부 후 해제되면 <b>경정청구</b></td><td>시행령 제162조제1항제2호, 국세기본법 제45조의2제2항</td></tr>
<tr><td>잔금까지 받은 뒤 해제권 행사로 해제</td><td>신고·납부한 양도세 <b>경정청구</b></td><td>국세기본법 시행령 제25조의2제2호</td></tr>
</table></div>

<h2>2. 후발적 사유 경정청구, 이렇게 합니다</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>청구할 수 있는 사람</td><td>과세표준신고서를 법정신고기한까지 제출했거나 세무서의 결정을 받은 사람</td><td>국세기본법 제45조의2제2항</td></tr>
<tr><td>해당 사유</td><td>신고의 계산 근거가 된 거래의 효력과 관계되는 계약이 <b>해제권의 행사</b>로 해제되거나, 계약 성립 후 발생한 <b>부득이한 사유</b>로 해제·취소된 경우</td><td>같은 법 시행령 제25조의2제2호</td></tr>
<tr><td>기한</td><td>그 사유가 발생한 것을 <b>안 날부터 3개월 이내</b></td><td>같은 법 제45조의2제2항</td></tr>
<tr><td>처리</td><td>세무서는 청구를 받은 날부터 <b>2개월 이내</b>에 결과를 통지</td><td>같은 조 제3항</td></tr>
</table></div>
<p>조문은 <b>해제권 행사</b>(법정 해제권이나 계약서에 정한 약정 해제권)와 <b>계약 후 생긴 부득이한 사유</b>로 인한 해제를 사유로 정하고 있습니다. 당사자끼리 마음을 바꿔 하는 <b>단순 합의해제</b>는 이 사유에 바로 해당한다고 보기 어려울 수 있으므로, 해제 경위를 입증할 자료(내용증명, 해제 통지서, 판결문 등)를 꼭 남겨 두셔야 합니다.</p>

<h2>3. 정○○ 님 사례 — 돌려받을 수 있는 세금</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>금액</th></tr>
<tr><td>양도가액 − 취득가액</td><td>800,000,000 − 500,000,000 = 300,000,000</td></tr>
<tr><td>장기보유 특별공제(10년 이상, 20%)</td><td>△60,000,000</td></tr>
<tr><td>양도소득 기본공제</td><td>△2,500,000</td></tr>
<tr><td>과세표준</td><td>237,500,000</td></tr>
<tr><td>납부한 양도소득세(산출세액)</td><td><b>70,310,000</b></td></tr>
<tr><td>계약 해제 후 경정청구로 돌려받을 세액</td><td><b>70,310,000</b> (지방소득세 약 703만 원은 지방자치단체에 별도 청구)</td></tr>
</table></div>
<p>정○○ 님이 계약 해제 과정에서 매수인에게 받기로 한 계약금을 <b>위약금으로 몰취</b>했다면, 그 위약금은 양도소득이 아니라 <b>기타소득</b>으로 다음 해 5월 종합소득세 신고 대상이 될 수 있습니다(<a href="/column/142-contract-penalty-other-income.html">칼럼 142</a>).</p>
<p class="small">※ python으로 계산·검산했습니다. 필요경비·양도비는 없고, 2016년 6월 이전 취득·2026년 6월 양도(보유 10년 이상 11년 미만)로 가정했으며 다른 양도 건은 없는 것으로 했습니다. 세율은 소득세법 제55조제1항 기본세율, 장기보유 특별공제는 제95조제2항 표 1을 적용했습니다. 지방소득세는 양도소득세의 10%로 단순 가정했습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 계약이 해제된 날과 <b>그 사실을 안 날</b>을 확인하고, 3개월 기한을 달력에 표시했다.</li>
<li>☐ 해제 사유가 <b>해제권 행사</b>(잔금 미지급 등) 또는 <b>부득이한 사유</b>인지 계약서·내용증명으로 확인했다.</li>
<li>☐ 소유권 <b>말소등기</b> 등 원상회복 서류를 갖추었다.</li>
<li>☐ 받은 <b>위약금·배상금</b>이 있다면 기타소득 신고를 준비했다.</li>
<li>☐ 해제된 부동산을 다시 팔 때 취득시기·보유기간이 어떻게 되는지 함께 확인했다(<a href="/column/96-transfer-acquisition-date.html">칼럼 96</a>).</li>
</ul>
<p>계약 해제는 경위와 서류에 따라 결과가 달라질 수 있습니다. 해제를 검토하고 계시거나 이미 해제되셨다면 기한이 지나기 전에 서류를 가지고 편하게 상담해 주세요. 경정청구서 작성부터 지방소득세 환급까지 함께 챙겨 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>매매계약서(해제 조항)</td><td>약정 해제권, 위약금 약정</td></tr>
<tr><td>내용증명·해제 통지서·판결문</td><td>해제 사유와 해제일</td></tr>
<tr><td>등기부등본(말소등기 포함)</td><td>양도일, 원상회복 여부</td></tr>
<tr><td>양도세 신고서·납부영수증</td><td>환급받을 세액</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-pink">{HD()}
<div class="bokeh" style="left:80px;top:190px;width:120px;height:120px;background:#8fb0ff;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:240px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-doc-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">팔았는데 계약이 깨졌어요</div><div class="t">낸 양도세<br>돌려받을까요?</div><div class="series">양도세 절세 series 12편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">이런 일이 생겼다면</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">정○○ 님</div><div class="say">잔금을 안 줘서<br>계약을 <span class="mk">해제</span>했어요.<br>양도세는요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">안 날부터<br><span class="hl">3개월 안에</span><br>경정청구하세요!</div></div>
<img class="ch" src="ch/smile-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">경우별로 보면 →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">언제 해제됐나요?</div><div class="h1" style="margin-top:8px">경우별 처리</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">잔금·등기 전 해제<br><span style="color:#1f8a57">양도 아님</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">등기 먼저 넘긴 뒤 해제<br><span style="color:#1b5fa8">경정청구</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">잔금 받은 뒤 해제권 행사<br><span style="color:#c0392b">경정청구</span></div></div>
</div>
{FT(3, True, '소득세법 시행령 제162조①·국기법 제45조의2②')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">계약 해제 후 양도세<br>경정청구는 5년 안에만<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">하면 된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-calc.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 해제 같은 후발적 사유는<br>안 날부터 <b style="font-weight:900">3개월 이내</b>예요.</div>
{FT(4, True, '국세기본법 제45조의2②')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">상가 8억 원 양도 후 해제 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">돌려받는 세금</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>양도차익</small><b style="color:#1b5fa8">3억</b></div><div class="op">→</div><div class="bx"><small>낸 양도세</small><b style="color:#ff5c8a">7,031만</b></div></div>
<div class="total" style="top:610px"><small>경정청구로 환급</small><b>7,031만 원</b><span>지방소득세는 시·군·구에 따로 청구</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 10년 보유, 장기보유 공제 20%<br>· 해제권 행사로 해제</div>
{FT(5, True, '소득세법 제55조①·제95조②')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">해제했다면</div><div class="h1" style="margin-top:8px">꼭 챙기세요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">안 날부터<br><span style="color:#c0392b">3개월 기한</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">해제 사유 입증<br><span style="color:#b9770e">내용증명·판결문</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">받은 위약금은<br><span style="color:#1b5fa8">기타소득</span> 신고</div></div>
</div>
{FT(6, True, '국기법 시행령 제25조의2·소득세법 제21조①10호')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '계약이 해제됐다면').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">3개월</span> 안에!'),
]
