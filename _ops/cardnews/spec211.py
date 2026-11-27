import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 211
SLUG = 'hometown-love-donation-credit-2026'
CAT = '종합소득세'
DATE = '2026-11-27'
TITLE = '고향사랑기부금, 2026년부터 공제가 늘었습니다 — 10만 원까지 110분의 100, 10만~20만 원 구간은 40%(새로 신설), 20만 원 초과 2천만 원까지 15%, 12월 31일까지 기부분'
DESC = '거주자가 고향사랑 기부금을 지방자치단체에 기부하면 10만 원까지는 기부금의 110분의 100, 10만 원 초과 20만 원 이하 부분은 40%, 20만 원 초과 2천만 원 이하 부분은 15%(특별재난지역은 30%)를 종합소득산출세액에서 공제합니다. 10만~20만 원 구간 40%는 2026년 1월 1일 이후 기부분부터 적용됩니다. 사업자는 10만 원 초과분을 필요경비로 넣습니다. 조세특례제한법 제58조, 부칙(제21223호) 제13조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '조세특례제한법 제58조제1항·제2항·제3항, 부칙(법률 제21223호) 제13조'
TAGS = ['고향사랑기부금', '기부금세액공제', '연말정산', '2026세법개정', '근로소득자', '부산세무사']
ALTS = ['고향사랑기부금 공제 (표지)', '고향사랑기부금 공제 (상담 질문)', '고향사랑기부금 공제 (공제율)', '고향사랑기부금 공제 (O·X 퀴즈)', '고향사랑기부금 공제 (금액별 공제액)', '고향사랑기부금 공제 (확인할 점)', '고향사랑기부금 공제 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
연말이면 "고향사랑기부금 10만 원 하면 세금으로 거의 다 돌려받는다"는 이야기를 많이 들으셨을 겁니다. 그런데 <b>2026년부터는 공제가 더 늘었습니다</b>. 10만 원을 넘는 기부금 중 <b>20만 원까지는 40%</b>를 공제하는 구간이 새로 생겼습니다. 올해 <b>12월 31일까지</b> 기부하신 금액부터 적용되니, 얼마를 기부하면 얼마나 공제되는지 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li><b>10만 원 이하</b>: 기부금 × 110분의 100(10만 원이면 90,909원) 세액공제</li><li><b>10만 원 초과 20만 원 이하</b>: 그 부분의 <b>40%</b> — <b>2026년 기부분부터 신설</b></li><li><b>20만 원 초과 2천만 원 이하</b>: 그 부분의 <b>15%</b>(특별재난지역 지자체에 정해진 기간 내 기부하면 30%), 사업자는 10만 원 초과분을 필요경비로 처리</li></ol>
<div class="small" style="margin-top:8px">(조세특례제한법 제58조, 부칙 제21223호 제13조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"작년엔 고향사랑기부금 10만 원만 했는데, 올해는 20만 원 해도 괜찮을까요? 세금으로 얼마나 돌아오나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>직장인 노○○ 님(가칭)은 올해 고향 군청에 고향사랑기부금을 <b>20만 원</b> 기부하려고 합니다. 2025년까지라면 10만 원 초과분은 15%만 공제되어 세액공제액이 105,909원이었지만, 2026년 기부분부터는 10만~20만 원 구간이 <b>40%</b>로 올라 <b>130,909원</b>이 공제됩니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다. 2025년 기준 금액은 10만 원 × 100/110 + 10만 원 × 15%로 계산했습니다(개정 전 조세특례제한법 제58조제1항제2호).</p>

<h2>1. 기부 금액별 공제율</h2>
<div class="tbl"><table>
<tr><th>기부 금액 구간</th><th>세액공제</th><th>근거</th></tr>
<tr><td>10만 원 이하</td><td>기부금 × <b>110분의 100</b></td><td>조특법 제58조제1항제1호</td></tr>
<tr><td>10만 원 초과 20만 원 이하 부분</td><td><b>40%</b>(2026.1.1. 이후 기부분)</td><td>같은 항 제2호, 부칙 제13조</td></tr>
<tr><td>20만 원 초과 2천만 원 이하 부분</td><td><b>15%</b>(특별재난지역 선포 지자체에 정해진 기간 내 기부 시 30%)</td><td>같은 항 제3호</td></tr>
<tr><td>사업자인 거주자</td><td>10만 원 이하는 위 세액공제, 10만 원 초과분은 이월결손금을 뺀 소득금액 범위에서 <b>필요경비</b></td><td>같은 항 단서·제2항</td></tr>
<tr><td>한도</td><td>세액공제액은 종합소득산출세액이 한도</td><td>같은 조 제2항</td></tr>
</table></div>
<p>고향사랑기부금으로 공제받은 금액에는 일반 기부금 공제(소득세법 제59조의4제4항)를 다시 적용하지 않습니다(같은 조 제3항). 일반 기부금 공제는 <a href="/column/78-donation-tax-credit.html">칼럼 78</a>에 정리해 두었습니다.</p>

<h2>2. 금액별 세액공제액(2026년 기부분)</h2>
<div class="tbl"><table>
<tr><th>기부금</th><th>세액공제액</th></tr>
<tr><td>100,000원</td><td>90,909원</td></tr>
<tr><td><b>200,000원</b></td><td><b>130,909원</b></td></tr>
<tr><td>500,000원</td><td>175,909원</td></tr>
<tr><td>1,000,000원</td><td>250,909원</td></tr>
<tr><td>20,000,000원</td><td>3,100,909원</td></tr>
</table></div>
<p class="small">※ python으로 계산·검산했습니다(원 미만 절사). 소득세 세액공제액만 표시했고, 산출세액이 공제액보다 충분히 크다고 가정했습니다. 지방소득세와 답례품은 별도입니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 올해 기부분은 <b>12월 31일까지</b> 기부해야 올해 연말정산(종합소득세)에 반영됩니다.</li>
<li>☐ 기부처와 연간 한도, 답례품 기준은 「고향사랑 기부금에 관한 법률」과 공식 안내(고향사랑e음 등)로 확인했다.</li>
<li>☐ 기부 영수증이 연말정산 간소화 자료에 들어왔는지 확인했다.</li>
<li>☐ 사업자라면 10만 원 초과분은 <b>필요경비</b>로 처리된다는 점을 알고 장부에 반영했다.</li>
<li>☐ 산출세액이 적은 분은 공제를 다 못 받을 수 있으니 결정세액을 먼저 확인했다.</li>
</ul>
<p>연말정산은 12월 31일까지 무엇을 했느냐가 중요합니다. 고향사랑기부금과 함께 연금저축·IRP(<a href="/column/152-pension-account-tax-credit.html">칼럼 152</a>), 주택청약(<a href="/column/208-housing-subscription-savings-deduction.html">칼럼 208</a>)도 점검해 보시고, 궁금하신 점은 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>고향사랑기부금 영수증</td><td>기부일·금액·기부처</td></tr>
<tr><td>연말정산 간소화 자료</td><td>다른 기부금, 결정세액</td></tr>
<tr><td>원천징수영수증(전년도)</td><td>산출세액 규모</td></tr>
<tr><td>사업소득 장부(사업자)</td><td>필요경비 처리</td></tr>
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
<img class="ch" src="ch/smile-wave.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">2026년 달라진 고향사랑기부금</div><div class="t">20만 원 기부,<br>13만 원 공제</div><div class="series">종합소득세 절세 series 9편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">연말 기부 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">노○○ 님</div><div class="say">10만 원 넘게<br>기부하면 <span class="mk">손해</span><br>아닌가요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">올해부터<br>20만 원까지<br><span class="hl">40%</span> 공제돼요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">공제율은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">금액 구간별 세액공제</div><div class="h1" style="margin-top:8px">공제율</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">10만 원까지<br><span style="color:#1f8a57">110분의 100</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">②</div><div class="tx">10만~20만 원<br><span style="color:#c0392b">40%</span> (2026 신설)</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">20만~2천만 원<br><span style="color:#1b5fa8">15%</span> (재난지역 30%)</div></div>
</div>
{FT(3, True, '조특법 제58조①')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">2025년 12월에 한<br>기부도 40% 구간이<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">적용된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/smile-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! <b style="font-weight:900">2026년 1월 1일 이후</b><br>기부분부터 적용돼요.</div>
{FT(4, True, '조특법 부칙(제21223호) 제13조')}</div>''',
# 5 타일
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4">2026년 기부분 기준</div><div style="font-size:96px;font-weight:900;letter-spacing:-4px;line-height:1.1;text-shadow:0 8px 20px rgba(120,0,40,.35)">얼마 돌려받나?</div></div>
<div class="rows" style="top:420px">
 <div class="row"><div class="ic" style="background:#ff5c8a">10만</div><div class="tx">세액공제 <span style="color:#e83e6f">90,909원</span></div></div>
 <div class="row"><div class="ic" style="background:#ff9a3c">20만</div><div class="tx">세액공제 <span style="color:#e8761e">130,909원</span></div></div>
 <div class="row"><div class="ic" style="background:#7a5cff">50만</div><div class="tx">세액공제 <span style="color:#5a3fd6">175,909원</span></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:1000px;font-size:30px">· 지방소득세·답례품은 <b style="color:#fff3c4">별도</b>예요.</div>
{FT(5, True, '조특법 제58조①')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">기부 전에</div><div class="h1" style="margin-top:8px">꼭 확인하세요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">올해 공제는<br><span style="color:#c0392b">12월 31일까지</span> 기부</div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">사업자는 10만 원 초과분<br><span style="color:#b9770e">필요경비</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">공제는<br><span style="color:#1b5fa8">산출세액</span>이 한도</div></div>
</div>
{FT(6, True, '조특법 제58조①②')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '12월 31일 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">기부</span>도 챙기세요!'),
]
