import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 212
SLUG = 'cadastral-resurvey-adjustment-money-tax'
CAT = '양도소득세'
DATE = '2026-11-27'
TITLE = '지적재조사로 땅 면적이 바뀌었다면 — 줄어든 면적으로 받은 조정금은 양도세 비과세, 늘어난 면적으로 낸 조정금은 나중에 팔 때 취득가액에 넣지 않습니다, 늘어난 땅의 취득시기는 원래 땅 취득일'
DESC = '지적재조사에 따른 경계 확정으로 지적공부상 면적이 줄어 받는 조정금은 양도소득세가 비과세됩니다. 반대로 면적이 늘어 납부한 조정금은 나중에 토지를 양도할 때 취득가액에서 제외되며, 늘어난 면적의 취득시기는 종전 토지를 취득한 날로 봅니다. 소득세법 제89조제1항제5호, 제97조제1항제1호, 같은 법 시행령 제162조제1항제9호의2 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제89조제1항제5호, 제97조제1항제1호, 같은 법 시행령 제162조제1항제9호의2'
TAGS = ['지적재조사', '조정금', '양도세비과세', '토지경계', '취득가액', '부산세무사']
ALTS = ['지적재조사 조정금 (표지)', '지적재조사 조정금 (상담 질문)', '지적재조사 조정금 (세법 처리)', '지적재조사 조정금 (O·X 퀴즈)', '지적재조사 조정금 (세금 차이)', '지적재조사 조정금 (확인할 점)', '지적재조사 조정금 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
요즘 동네마다 <b>지적재조사 사업</b>이 진행되면서 "우리 땅 면적이 줄어 조정금을 받게 됐다", "면적이 늘어 조정금을 내라고 한다"는 안내를 받으시는 분들이 많습니다. 조정금은 땅 일부를 사고파는 것과 비슷해 보여 세금 걱정을 하시는데, 세법은 이 조정금을 따로 정해 두었습니다. <b>받은 조정금은 비과세</b>, <b>낸 조정금은 취득가액에서 제외</b>가 핵심입니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>지적재조사로 경계가 확정되어 면적이 <b>줄어</b> 받는 <b>조정금</b>은 양도소득세 <b>비과세</b>입니다.</li><li>면적이 <b>늘어</b> 낸 조정금은 나중에 그 땅을 팔 때 <b>취득가액에 넣지 않습니다</b>.</li><li>늘어난 면적의 <b>취득시기</b>는 원래 땅을 취득한 날로 보므로, 보유기간(장기보유 특별공제·세율)은 원래 땅과 같이 계산합니다.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제89조제1항제5호, 제97조제1항제1호, 같은 법 시행령 제162조제1항제9호의2 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"지적재조사로 옆집과 경계를 다시 정했더니 우리 땅이 10㎡ 늘어서 조정금 1천만 원을 냈어요. 나중에 땅을 팔 때 이 돈도 산 값에 넣을 수 있죠?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>정○○ 님(가칭)은 2010년에 토지 100㎡를 <b>1억 원</b>에 샀습니다. 지적재조사로 면적이 110㎡로 늘어 조정금 <b>1천만 원</b>을 냈고, 2026년에 이 땅을 <b>3억 원</b>에 팔려고 합니다. 이때 양도세 취득가액은 1억 원이고, 낸 조정금 1천만 원은 <b>취득가액에 포함되지 않습니다</b>. 늘어난 10㎡도 2010년에 취득한 것으로 봅니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 지적재조사 조정금, 세법은 이렇게 봅니다</h2>
<div class="tbl"><table>
<tr><th>상황</th><th>세법 처리</th><th>근거</th></tr>
<tr><td>면적이 <b>줄어</b> 조정금을 받음</td><td>그 조정금은 양도소득세 <b>비과세</b></td><td>소득세법 제89조제1항제5호</td></tr>
<tr><td>면적이 <b>늘어</b> 조정금을 냄</td><td>나중에 양도할 때 그 조정금은 <b>취득가액에서 제외</b></td><td>소득세법 제97조제1항제1호 괄호</td></tr>
<tr><td>늘어난 면적의 취득시기</td><td>지적공부상 <b>종전 토지를 취득한 날</b></td><td>소득세법 시행령 제162조제1항제9호의2</td></tr>
</table></div>
<p>즉 받은 쪽은 세금이 없고, 낸 쪽은 그 돈을 나중에 비용으로 빼 주지 않는 대신 늘어난 땅을 처음부터 가지고 있던 것으로 보아 <b>보유기간을 길게</b> 인정해 줍니다. 경계 조정을 위한 토지 <b>교환</b>은 별도 규정으로 양도로 보지 않는 경우가 있습니다(<a href="/column/164-land-exchange-capital-gains.html">칼럼 164</a>).</p>

<h2>2. 정○○ 님 사례 — 조정금을 취득가액에 넣으면?</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>조정금을 넣었다고 착각한 경우</th><th>실제 계산</th></tr>
<tr><td>양도가액</td><td>300,000,000</td><td>300,000,000</td></tr>
<tr><td>취득가액</td><td>110,000,000</td><td><b>100,000,000</b></td></tr>
<tr><td>양도차익</td><td>190,000,000</td><td>200,000,000</td></tr>
<tr><td>장기보유 특별공제(15년 이상, 30%)</td><td>△57,000,000</td><td>△60,000,000</td></tr>
<tr><td>기본공제</td><td>△2,500,000</td><td>△2,500,000</td></tr>
<tr><td>과세표준</td><td>130,500,000</td><td>137,500,000</td></tr>
<tr><td>양도소득세 산출세액</td><td>30,235,000</td><td><b>32,685,000</b></td></tr>
</table></div>
<p>조정금을 취득가액에 넣어 신고하면 양도세가 <b>245만 원</b> 적게 계산되어, 나중에 과소신고 가산세와 함께 추징될 수 있습니다. 처음부터 정확히 신고하시는 것이 좋습니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 비사업용 토지가 아니고, 필요경비·다른 양도 건은 없다고 가정했으며, 세율은 소득세법 제55조제1항, 장기보유 특별공제는 제95조제2항 표 1을 적용했습니다. 지방소득세는 별도입니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 지적재조사 <b>조정금 통지서</b>와 받은(낸) 금액·날짜를 보관했다.</li>
<li>☐ 받은 조정금은 비과세이므로 따로 양도세 신고 대상이 아님을 확인했다.</li>
<li>☐ 낸 조정금은 나중에 땅을 팔 때 <b>취득가액에 넣지 않도록</b> 메모해 두었다.</li>
<li>☐ 늘어난 면적도 원래 땅과 <b>같은 취득일</b>로 보유기간을 계산했다.</li>
<li>☐ 농지·임야라면 비사업용 토지 판정(<a href="/column/29-non-business-land.html">칼럼 29</a>)도 함께 확인했다.</li>
</ul>
<p>지적재조사는 한 번 정리되면 오래 잊히기 쉬워, 땅을 팔 때 조정금을 어떻게 처리해야 할지 헷갈리는 경우가 많습니다. 관련 서류를 가지고 편하게 상담해 주세요. 양도세 계산까지 정확하게 도와 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>지적재조사 조정금 산정·통지서</td><td>면적 증감, 조정금 금액</td></tr>
<tr><td>조정금 수령·납부 영수증</td><td>받은(낸) 날짜와 금액</td></tr>
<tr><td>토지 등기부등본·토지대장</td><td>원래 취득일, 변경 전후 면적</td></tr>
<tr><td>원래 매매계약서</td><td>취득가액</td></tr>
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
<img class="ch" src="ch/wow-doc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">지적재조사로 땅 면적이 바뀌었어요</div><div class="t">조정금,<br>세금은요?</div><div class="series">양도세 절세 series 15편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">토지주분들의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">정○○ 님</div><div class="say">땅이 늘어 낸<br>조정금 1천만 원,<br><span class="mk">산 값</span>에 넣죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">취득가액에는<br><span class="hl">넣지 않아요</span>!</div></div>
<img class="ch" src="ch/smile-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">정리하면 →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">지적재조사 조정금</div><div class="h1" style="margin-top:8px">세법 처리</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">줄어서 받은 조정금<br><span style="color:#1f8a57">양도세 비과세</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">②</div><div class="tx">늘어서 낸 조정금<br><span style="color:#c0392b">취득가액 제외</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">늘어난 땅 취득일<br><span style="color:#1b5fa8">원래 땅 취득일</span></div></div>
</div>
{FT(3, True, '소득세법 제89조①5호·제97조①1호·시행령 제162조①')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">면적이 줄어 받은<br>조정금도 양도세를<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">신고해야 한다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 지적재조사 조정금은<br>양도세 <b style="font-weight:900">비과세</b>예요.</div>
{FT(4, True, '소득세법 제89조①5호')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">1억 원에 산 땅 3억 원에 양도 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">조정금 1천만 원</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>착각한 세금</small><b style="color:#2fa36b">3,024만</b></div><div class="op">vs</div><div class="bx"><small>실제 세금</small><b style="color:#ff5c8a">3,269만</b></div></div>
<div class="total" style="top:610px"><small>적게 신고하면 추징</small><b>245만 원 + 가산세</b><span>조정금은 취득가액에 넣지 않아요</span></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 16년 보유, 장기보유 공제 30%<br>· 비사업용 토지 아님</div>
{FT(5, True, '소득세법 제55조①·제95조②·제97조①')}</div>''',
# 6 확인
f'''<div class="c bg-orange">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">이것만 기억하세요</div><div class="h1" style="margin-top:8px">서류 보관</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">조정금<br><span style="color:#c0392b">통지서·영수증</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">변경 전후<br><span style="color:#b9770e">토지대장</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">원래 땅<br><span style="color:#1b5fa8">매매계약서</span></div></div>
</div>
{FT(6, True, '소득세법 제97조①')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '땅 파시기 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">조정금</span> 확인!'),
]
