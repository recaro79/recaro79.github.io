import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 197
SLUG = 'actual-use-house-definition'
CAT = '양도소득세'
DATE = '2026-11-27'
TITLE = '서류상 상가·근린생활시설이라도 사람이 살면 주택입니다 — 양도세 주택 판정은 공부상 용도가 아니라 실제 쓰임새, 무허가 주택도 포함, 내 집 비과세가 흔들릴 수 있습니다'
DESC = '양도소득세에서 주택은 허가 여부나 건축물대장 등 공부상 용도와 관계없이 독립된 주거생활을 할 수 있는 구조(별도 출입문·화장실·취사시설)를 갖추고 사실상 주거용으로 쓰는 건물입니다. 용도가 분명하지 않을 때만 공부상 용도에 따릅니다. 근린생활시설 주거 사용, 무허가 주택이 있으면 1세대1주택 비과세 판정이 달라질 수 있습니다. 소득세법 제88조제7호, 같은 법 시행령 제152조의4 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제88조제7호, 같은 법 시행령 제152조의4, 소득세법 제95조제5항·제6항'
TAGS = ['주택판정', '근린생활시설', '근생빌라', '무허가주택', '1세대1주택비과세', '부산세무사']
ALTS = ['양도세 주택 판정 (표지)', '양도세 주택 판정 (상담 질문)', '양도세 주택 판정 (주택의 구조 요건)', '양도세 주택 판정 (O·X 퀴즈)', '양도세 주택 판정 (세금 차이)', '양도세 주택 판정 (이런 경우 주의)', '양도세 주택 판정 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"건축물대장에 근린생활시설(상가)로 되어 있으니 집이 아니죠?" 양도세 상담에서 정말 자주 듣는 질문입니다. 그런데 양도소득세에서는 <b>서류에 무엇이라고 적혀 있는지보다 실제로 어떻게 쓰고 있는지</b>가 먼저입니다. 상가로 등록된 공간에 세입자가 살고 있거나, 허가 없이 지은 집에 사람이 살고 있으면 그것도 <b>주택</b>이 됩니다. 이 때문에 내가 사는 집의 1세대1주택 비과세가 흔들리는 경우가 있어 오늘 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>양도세의 주택은 <b>허가 여부나 공부상 용도와 관계없이</b> 사실상 주거용으로 쓰는 건물입니다.</li><li>세대마다 <b>별도의 출입문·화장실·취사시설</b>을 갖춘 구조여야 하고, 용도가 분명하지 않을 때만 <b>공부상 용도</b>를 따릅니다.</li><li>근린생활시설을 주거로 임대하거나 무허가 주택이 있으면 <b>주택 수에 포함</b>되어 다른 집의 비과세가 안 될 수 있습니다.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제88조제7호, 같은 법 시행령 제152조의4 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"10년 살던 아파트를 팔려고 하는데, 따로 가진 건 근린생활시설로 된 빌라 한 칸뿐이에요. 거기엔 세입자가 살고 있지만 서류상 상가니까 저는 1주택 맞죠?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>최○○ 님(가칭)은 10년 동안 보유·거주한 아파트를 <b>9억 원</b>에 파실 계획입니다(취득가액 4억 원). 그 밖에 건축물대장상 <b>제2종 근린생활시설</b>인 빌라 한 칸을 가지고 계신데, 방·화장실·주방과 별도 출입문을 갖추고 있고 세입자가 <b>주거용</b>으로 살고 있습니다. 이 경우 빌라도 양도세에서는 주택이므로 최○○ 님은 <b>2주택자</b>가 되어 아파트 양도 시 1세대1주택 비과세를 받기 어렵습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 양도세에서 말하는 "주택"</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>정의</td><td><b>허가 여부나 공부상의 용도구분과 관계없이</b> 세대의 구성원이 독립된 주거생활을 할 수 있는 구조를 갖추어 <b>사실상 주거용</b>으로 사용하는 건물</td><td>소득세법 제88조제7호 전단</td></tr>
<tr><td>구조 요건</td><td>세대별로 구분된 각각의 공간마다 <b>별도의 출입문, 화장실, 취사시설</b>이 설치된 구조</td><td>시행령 제152조의4</td></tr>
<tr><td>용도가 불분명할 때</td><td>그 용도가 분명하지 아니하면 <b>공부상의 용도</b>에 따름</td><td>소득세법 제88조제7호 후단</td></tr>
</table></div>

<h2>2. 이런 경우를 조심하세요</h2>
<div class="tbl"><table>
<tr><th>상황</th><th>양도세에서 보는 방식</th></tr>
<tr><td>건축물대장상 근린생활시설인데 세입자가 <b>살고 있음</b>(이른바 근생빌라, 상가 2층 주거)</td><td>구조를 갖추고 사실상 주거용이면 <b>주택</b> → 주택 수에 포함</td></tr>
<tr><td>허가 없이 지은 집, 등기가 안 된 시골집에 사람이 살고 있음</td><td>허가 여부와 관계없으므로 <b>주택</b>이 될 수 있음</td></tr>
<tr><td>건축물대장상 주택인데 <b>사무실·창고</b>로만 쓰고 있음</td><td>사실상 주거용이 아니면 주택이 아닐 수 있음 — 실제 사용 사실을 입증할 자료가 중요</td></tr>
<tr><td>오래 비어 있어 쓰임새가 <b>분명하지 않음</b></td><td>공부상 용도에 따름(공부상 주택이면 주택)</td></tr>
</table></div>
<p>반대로 <b>상가를 주거용으로 바꿔 살다가</b> 그 건물이 1세대1주택이 되어 파시는 경우, 2025년 1월 1일 이후 양도분부터 장기보유 특별공제는 상가로 보유한 기간(표 1)과 주택으로 보유한 기간(표 2)을 나누어 계산하고, 보유기간 공제율은 40%를 넘지 못합니다(소득세법 제95조제5항·제6항, 부칙 제19933호 제7조). 주택으로 본 기간은 실제 주거용으로 쓰기 시작한 날(불분명하면 공부상 용도를 주택으로 바꾼 날)부터 셉니다.</p>

<h2>3. 최○○ 님 사례 — 빌라가 주택인지에 따른 차이</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>빌라가 주택이 아닐 때(1주택)</th><th>빌라가 주택일 때(2주택)</th></tr>
<tr><td>양도가액</td><td>900,000,000</td><td>900,000,000</td></tr>
<tr><td>취득가액</td><td>400,000,000</td><td>400,000,000</td></tr>
<tr><td>양도차익</td><td>비과세(12억 원 이하 1세대1주택)</td><td>500,000,000</td></tr>
<tr><td>장기보유 특별공제(10년, 표 1 20%)</td><td>−</td><td>△100,000,000</td></tr>
<tr><td>양도소득 기본공제</td><td>−</td><td>△2,500,000</td></tr>
<tr><td>과세표준</td><td>−</td><td>397,500,000</td></tr>
<tr><td>양도소득세 산출세액</td><td><b>0원</b></td><td><b>133,060,000</b></td></tr>
<tr><td>지방소득세 포함(10% 가정)</td><td>0원</td><td>146,366,000</td></tr>
</table></div>
<p>서류상 상가인 빌라 한 칸 때문에 세금이 <b>0원에서 약 1억 3,306만 원</b>(지방소득세 포함 약 1억 4,637만 원)으로 달라질 수 있습니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 아파트는 조정대상지역이 아닌 곳에 있어 다주택 중과가 없고, 일시적 2주택 등 다른 특례는 해당하지 않으며, 필요경비·양도비는 없는 것으로 가정했습니다. 세율은 소득세법 제55조제1항 기본세율, 장기보유 특별공제는 제95조제2항 표 1을 적용했습니다. 지방소득세는 양도소득세의 10%로 단순 가정했습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 세대원 모두가 가진 건물 중 <b>공부상 주택이 아니지만 사람이 살고 있는 곳</b>(근린생활시설, 상가 위층, 숙소 등)이 있는지 확인했다.</li>
<li>☐ 그 공간에 <b>별도 출입문·화장실·취사시설</b>이 모두 있는지 확인했다.</li>
<li>☐ 시골의 <b>무허가·미등기 주택</b>이나 부모님께 물려받은 빈집이 있는지 확인했다(<a href="/column/103-rural-house-one-house-exemption.html">칼럼 103</a>).</li>
<li>☐ 오피스텔이 있다면 실제 사용 용도를 따로 확인했다(<a href="/column/42-officetel-house-count.html">칼럼 42</a>).</li>
<li>☐ 실제 용도를 입증할 <b>임대차계약서·전입 현황·사업자등록·공과금 자료</b>를 정리해 두었다.</li>
</ul>
<p>주택 수 판단은 비과세·중과세를 가르는 첫 단추입니다. 집을 파시기 전에 세대가 가진 건물을 모두 펼쳐 놓고 한 번 점검해 보시는 것이 안전합니다. 건축물대장과 임대차계약서를 가지고 편하게 상담해 주세요. 주택 수부터 비과세 여부, 예상 세액까지 함께 확인해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>세대원 보유 건물의 건축물대장·등기부등본</td><td>공부상 용도, 소유자</td></tr>
<tr><td>임대차계약서·세입자 전입 여부</td><td>사실상 주거용 사용 여부</td></tr>
<tr><td>평면도·내부 사진</td><td>출입문·화장실·취사시설 구조</td></tr>
<tr><td>팔려는 집의 취득·양도 계약서</td><td>보유·거주기간, 예상 세액</td></tr>
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
<img class="ch" src="ch/wow-magnify-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">서류엔 상가, 실제론 집?</div><div class="t">사람이 살면<br>주택입니다</div><div class="series">양도세 절세 series 11편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">집 파실 분들이 묻는 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">최○○ 님</div><div class="say">근생빌라는<br>서류상 <span class="mk">상가</span>니까<br>저는 1주택이죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">세입자가 살면<br><span class="hl">주택</span>으로 봐서<br>2주택이에요!</div></div>
<img class="ch" src="ch/worry-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">기준은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">이 구조 + 실제 주거 사용</div><div class="h1" style="margin-top:8px">= 양도세상 주택</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">세대마다<br><span style="color:#1f8a57">별도 출입문</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">세대마다<br><span style="color:#1b5fa8">화장실</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">세대마다<br><span style="color:#c0392b">취사시설</span></div></div>
</div>
{FT(3, True, '소득세법 제88조7호·시행령 제152조의4')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">허가 없이 지은<br>시골집은 주택 수에<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">들어가지 않는다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 허가 여부와 관계없이<br>사람이 살면 <b style="font-weight:900">주택</b>이 될 수 있어요.</div>
{FT(4, True, '소득세법 제88조제7호')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">아파트 9억 원 양도 · 10년 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">근생빌라 한 칸 차이</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>1주택이면</small><b style="color:#2fa36b">0원</b></div><div class="op">vs</div><div class="bx"><small>2주택이면</small><b style="color:#ff5c8a">1.33억</b></div></div>
<div class="total" style="top:610px"><small>지방소득세 포함 시</small><b>약 1억 4,637만</b><span>양도차익 5억 원, 장기보유 공제 20%</span></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 조정대상지역 아님(중과 없음)<br>· 다른 비과세 특례 없음</div>
{FT(5, True, '소득세법 제55조①·제95조②')}</div>''',
# 6 주의
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">집 팔기 전에</div><div class="h1" style="margin-top:8px">이런 곳 확인!</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">세입자 사는<br><span style="color:#c0392b">근린생활시설</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">시골의<br><span style="color:#b9770e">무허가·미등기 집</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">주거용으로 쓰는<br><span style="color:#1b5fa8">오피스텔</span></div></div>
</div>
{FT(6, True, '소득세법 제88조제7호')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '집 파시기 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">주택 수</span> 점검!'),
]
