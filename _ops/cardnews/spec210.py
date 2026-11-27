import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 210
SLUG = 'pre-ipo-stock-gift-listing-gain'
CAT = '증여세'
DATE = '2026-11-27'
TITLE = '상장 전 회사 주식을 자녀에게 증여하셨다면 — 5년 안에 코스피·코스닥에 상장되어 오른 이익도 증여세로 정산합니다, 상장 3개월 뒤 가격 기준, 기업가치가 실제로 늘어난 몫은 제외'
DESC = '최대주주등(최대주주 또는 특수관계인 포함 25% 이상 주주)의 특수관계인이 최대주주등으로부터 주식을 증여받거나 취득한 날부터 5년 이내에 그 주식이 유가증권시장·코스닥시장에 상장되어 가치가 오르면, 상장일부터 3개월이 되는 날의 평가액에서 증여 당시 가액과 기업가치의 실질적 증가분을 뺀 이익이 기준금액(30%와 3억 원 중 적은 금액) 이상일 때 증여재산가액으로 보아 증여세를 정산합니다. 상속세 및 증여세법 제41조의3, 같은 법 시행령 제31조의3 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '상속세 및 증여세법 제41조의3, 같은 법 시행령 제31조의3, 같은 법 시행규칙 제10조의4'
TAGS = ['상장차익증여', '비상장주식증여', '가업승계', '최대주주', '증여세정산', '부산세무사']
ALTS = ['상장 이익 증여 (표지)', '상장 이익 증여 (상담 질문)', '상장 이익 증여 (요건)', '상장 이익 증여 (O·X 퀴즈)', '상장 이익 증여 (이익 계산)', '상장 이익 증여 (확인할 점)', '상장 이익 증여 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
회사를 키워 오신 대표님들께서 상장(IPO)을 앞두고 "상장되면 주가가 오를 테니 그 전에 자녀에게 주식을 미리 넘겨 두자"고 생각하시는 경우가 있습니다. 비상장 상태의 낮은 가격으로 증여세를 내고, 상장 후 오른 이익은 자녀 몫이 되도록 하려는 것이지요. 그런데 세법은 이런 경우를 위해 <b>상장에 따른 이익의 증여</b> 규정을 두고 있습니다. <b>5년 안에 상장되면</b> 오른 이익을 다시 계산해 증여세를 추가로 매깁니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>최대주주등의 특수관계인(자녀 등)이 최대주주등에게서 주식을 <b>증여받거나 사들인 날부터 5년 이내</b>에 그 회사가 <b>유가증권시장·코스닥</b>에 상장되면 대상입니다.</li><li>이익 = (상장일부터 <b>3개월 되는 날</b>의 1주당 평가액 − 증여 당시 1주당 가액 − 1주당 <b>기업가치 실질 증가분</b>) × 주식 수입니다.</li><li>이익이 (증여 당시 가액 + 기업가치 증가분)의 <b>30%</b>와 <b>3억 원</b> 중 적은 금액 이상이면 당초 증여에 더해 증여세를 <b>정산</b>합니다.</li></ol>
<div class="small" style="margin-top:8px">(상속세 및 증여세법 제41조의3, 같은 법 시행령 제31조의3 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"내년쯤 코스닥 상장을 준비하고 있어요. 지금 비상장일 때 아들에게 주식을 증여하면 증여세가 훨씬 적겠죠?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>최대주주인 서○○ 대표님(가칭)은 비상장 주식 <b>10만 주</b>(1주당 증여세 과세가액 1만 원, 총 10억 원)를 성인 아들에게 증여하고 증여세를 냈습니다. 3년 뒤 회사가 <b>코스닥에 상장</b>했고, 상장일부터 3개월이 되는 날 1주당 평가액은 <b>4만 원</b>이었습니다. 그 사이 회사 실적으로 늘어난 기업가치(실질 증가분)는 1주당 5천 원으로 확인되었습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 적용 요건</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>누가</td><td>최대주주등(최대주주·최대출자자, 또는 특수관계인 지분을 합해 <b>25% 이상</b> 주주)의 <b>특수관계인</b></td><td>법 제41조의3제1항, 시행령 제31조의3제4항</td></tr>
<tr><td>어떻게 받았나</td><td>① 최대주주등에게서 주식을 <b>증여받거나 유상 취득</b> ② 최대주주등에게 3년 내 <b>증여받은 재산</b>으로 다른 사람에게서 주식 취득(증여 후 유상증자 신주 포함)</td><td>법 제41조의3제2항·제7항</td></tr>
<tr><td>언제</td><td>증여·취득일부터 <b>5년 이내</b> 유가증권시장·코스닥시장 <b>상장</b>(첫 매매거래일)</td><td>같은 조 제1항·제5항, 시행령 제31조의3제2항</td></tr>
<tr><td>정산기준일</td><td>상장일부터 <b>3개월</b>이 되는 날(그 전에 사망·증여·양도하면 그날)</td><td>같은 조 제3항</td></tr>
<tr><td>기준금액</td><td>(증여 당시 가액 + 기업가치 실질 증가분) × 주식 수의 <b>30%</b>와 <b>3억 원</b> 중 적은 금액 — 이익이 이보다 적으면 과세 제외</td><td>시행령 제31조의3제3항</td></tr>
</table></div>
<p>반대로 정산기준일 평가액이 당초 증여 가액보다 크게 떨어지면(차액이 기준금액 이상) 당초 낸 증여세 중 그 차액에 해당하는 금액을 <b>환급</b>받을 수 있습니다(법 제41조의3제4항 단서). 전환사채를 받아 5년 안에 주식으로 바꾼 경우도 같은 방식으로 봅니다(같은 조 제8항).</p>

<h2>2. 서○○ 대표님 사례 계산</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>금액</th></tr>
<tr><td>1주당 이익: 40,000 − 10,000 − 5,000(기업가치 실질 증가분)</td><td>25,000</td></tr>
<tr><td>상장 이익(× 10만 주)</td><td><b>2,500,000,000</b></td></tr>
<tr><td>기준금액: Min[(10,000 + 5,000) × 10만 주 × 30% = 4.5억, 3억]</td><td>300,000,000 → 이익이 기준 이상이므로 과세</td></tr>
<tr><td>당초 증여세 산출세액(10억 원 − 공제 5천만 원)</td><td>225,000,000</td></tr>
<tr><td>정산 후 증여세 산출세액(35억 원 − 공제 5천만 원)</td><td>1,265,000,000</td></tr>
<tr><td><b>추가로 내는 증여세</b></td><td><b>1,040,000,000</b></td></tr>
</table></div>
<p>비상장일 때 증여하면 10억 원에 대한 세금만 내면 될 것 같지만, 5년 안에 상장되면 오른 이익 25억 원까지 더해 <b>약 10억 4천만 원</b>을 추가로 내야 합니다. 상장 이익 증여세 신고기한은 <b>정산기준일이 속하는 달의 말일부터 3개월</b>입니다(법 제68조).</p>
<p class="small">※ python으로 계산·검산했습니다. 10년 내 다른 증여는 없고, 세율은 상속세 및 증여세법 제56조(제26조 세율)를 적용했으며 신고세액공제·가업승계 특례는 반영하지 않았습니다. 기업가치 실질 증가분은 재무제표 등으로 확인되는 1주당 순손익액을 바탕으로 계산합니다(시행령 제31조의3제5항).</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 상장 계획이 있다면 증여·양도 시점부터 <b>5년</b> 안에 상장될 가능성을 함께 따져 보았다.</li>
<li>☐ 증여 후 <b>유상증자</b>로 받은 신주도 포함된다는 점을 확인했다.</li>
<li>☐ 회사의 실적으로 늘어난 <b>기업가치 실질 증가분</b>을 입증할 재무제표를 준비했다.</li>
<li>☐ 가업승계 증여세 과세특례(<a href="/column/22-family-business-succession-gift.html">칼럼 22</a>), 최대주주 할증(<a href="/column/195-largest-shareholder-premium-valuation.html">칼럼 195</a>)과 함께 비교했다.</li>
<li>☐ 정산기준일과 신고기한을 달력에 표시했다.</li>
</ul>
<p>상장 전 주식 이전은 평가, 증여 시점, 상장 일정이 모두 맞물리는 문제입니다. 상장을 준비하고 계시다면 증여 전에 편하게 상담해 주세요. 시점별 세금을 함께 계산해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>주주명부·주식변동상황명세서</td><td>최대주주등 여부, 증여·취득일</td></tr>
<tr><td>증여세 신고서(당초)</td><td>1주당 증여세 과세가액</td></tr>
<tr><td>최근 사업연도 재무제표</td><td>기업가치 실질 증가분</td></tr>
<tr><td>상장 일정·공모가 자료</td><td>정산기준일, 예상 평가액</td></tr>
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
<img class="ch" src="ch/wow-none-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">상장 전에 자녀에게 주식 증여?</div><div class="t">5년 안 상장이면<br>다시 계산해요</div><div class="series">증여세 절세 series 7편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">상장 준비 대표님 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">서○○ 대표님</div><div class="say">상장 전에 주면<br>증여세가<br><span class="mk">훨씬 적죠</span>?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">5년 안 상장되면<br><span class="hl">오른 이익</span>까지<br>정산해요!</div></div>
<img class="ch" src="ch/worry-calc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">요건은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">이렇게 되면 과세</div><div class="h1" style="margin-top:8px">상장 이익 증여</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">최대주주등에게서<br><span style="color:#1f8a57">주식 증여·취득</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx"><span style="color:#1b5fa8">5년 안에</span><br>코스피·코스닥 상장</div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">이익이 <span style="color:#c0392b">30%·3억 원</span><br>중 적은 금액 이상</div></div>
</div>
{FT(3, True, '상증법 제41조의3·시행령 제31조의3')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">아버지에게 돈을 받아<br>남에게서 주식을 사면<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">적용되지 않는다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 3년 내 증여받은 돈으로<br>산 주식도 <b style="font-weight:900">적용 대상</b>이에요.</div>
{FT(4, True, '상증법 제41조의3②2호')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">10만 주 증여 · 3년 뒤 코스닥 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">1주당 이익</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>상장 3개월 후</small><b style="color:#ff5c8a">4만 원</b></div><div class="op">−</div><div class="bx"><small>증여가+실질증가</small><b style="color:#1b5fa8">1.5만 원</b></div></div>
<div class="total" style="top:610px"><small>추가 증여세</small><b>약 10억 4천만 원</b><span>상장 이익 25억 원을 더해 정산</span></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 당초 증여 10억 원, 성인 자녀<br>· 신고세액공제 반영 전</div>
{FT(5, True, '상증법 제41조의3④·제56조')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">이것도 알아 두세요</div><div class="h1" style="margin-top:8px">확인할 점</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">증여 후 <span style="color:#c0392b">유상증자</span><br>신주도 포함</div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">값이 크게 떨어지면<br><span style="color:#b9770e">증여세 환급</span> 가능</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">정산기준일이 속한 달<br>말일부터 <span style="color:#1b5fa8">3개월</span> 신고</div></div>
</div>
{FT(6, True, '상증법 제41조의3④⑦·제68조')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '상장 전 주식 이전 때').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">시점</span> 설계!'),
]
