import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 218
SLUG = 'heritage-house-general-house-exemption'
CAT = '양도소득세'
DATE = '2026-11-27'
TITLE = '문화유산(국가유산)으로 지정된 한옥과 내 집을 함께 가지고 계신다면 — 일반주택을 팔 때 1세대1주택 비과세, 지정·등록문화유산·천연기념물등 주택은 주택 수에서 빼고 판단합니다'
DESC = '지정문화유산, 국가등록문화유산, 천연기념물등에 해당하는 주택과 그 밖의 일반주택을 국내에 각각 1개씩 가진 1세대가 일반주택을 양도하면 1주택을 가진 것으로 보아 1세대1주택 비과세를 적용합니다. 일반주택은 2년 보유(취득 당시 조정대상지역이면 2년 거주) 요건을 갖춰야 하고, 양도가액 12억 원 초과분은 과세됩니다. 소득세법 제89조, 같은 법 시행령 제154조·제155조제6항·제160조·제167조의3 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제89조제1항제3호, 같은 법 시행령 제154조제1항·제155조제6항·제160조·제167조의3제1항제6호'
TAGS = ['국가유산주택', '문화유산주택', '1세대1주택', '양도소득세', '비과세특례', '부산세무사']
ALTS = ['국가유산주택 비과세 특례 (표지)', '국가유산주택 비과세 특례 (상담 질문)', '국가유산주택 비과세 특례 (대상 주택)', '국가유산주택 비과세 특례 (O·X 퀴즈)', '국가유산주택 비과세 특례 (세금 차이)', '국가유산주택 비과세 특례 (확인할 점)', '국가유산주택 비과세 특례 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"할아버지 때부터 내려온 고택이 문화유산으로 지정돼 있어요. 그럼 저는 2주택자라서 지금 사는 아파트를 팔면 양도세를 내야 하나요?" 이런 질문을 받으면 먼저 반가운 소식부터 전해 드립니다. 세법은 <b>문화유산·천연기념물등으로 지정·등록된 주택</b>을 함께 가지고 있어도, <b>일반주택을 팔 때는 1주택을 가진 것으로 보아</b> 비과세를 적용합니다. 오늘은 그 요건과 주의할 점을 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li><b>지정문화유산·국가등록문화유산·천연기념물등</b>에 해당하는 주택과 일반주택을 <b>각각 1개씩</b> 가진 1세대가 <b>일반주택</b>을 팔면 1주택자로 보아 비과세를 적용합니다.</li><li>일반주택은 따로 <b>2년 이상 보유</b>(취득 당시 조정대상지역이면 <b>2년 이상 거주</b>도) 요건을 갖춰야 하고, 양도가액 <b>12억 원 초과분</b>은 과세됩니다.</li><li>상속주택·일시적 2주택 특례와 달리 <b>언제까지 팔아야 한다는 기한이 따로 없습니다</b>.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제89조제1항제3호, 같은 법 시행령 제154조제1항·제155조제6항 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"문화유산으로 지정된 시골 고택이 있는데, 서울 아파트를 팔면 2주택자로 양도세를 내야 하나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>한○○ 님(가칭)은 아버지께 물려받은 고택(지정문화유산인 주택)을 가지고 계시고, <b>10년 전 6억 원</b>에 산 아파트에서 <b>10년째</b> 살고 계십니다. 이 아파트를 <b>15억 원</b>에 팔기로 하셨습니다. 고택은 문화유산 주택이므로 아파트를 팔 때 한○○ 님 세대는 <b>1주택을 가진 것</b>으로 봅니다. 아파트는 2년 보유·거주 요건을 갖췄으니 1세대1주택 비과세가 적용되고, 12억 원을 넘는 부분만 과세됩니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 특례가 적용되는 주택</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>특례 대상 주택</td><td>「문화유산의 보존 및 활용에 관한 법률」에 따른 <b>지정문화유산</b>, 「근현대문화유산의 보존 및 활용에 관한 법률」에 따른 <b>국가등록문화유산</b>, 「자연유산의 보존 및 활용에 관한 법률」에 따른 <b>천연기념물등</b>에 해당하는 주택</td><td>시행령 제155조제6항제1호</td></tr>
<tr><td>보유 형태</td><td>위 주택과 그 밖의 주택(일반주택)을 국내에 <b>각각 1개씩</b> 소유한 1세대</td><td>시행령 제155조제6항</td></tr>
<tr><td>비과세되는 주택</td><td><b>일반주택</b>을 양도하는 경우 1주택을 가진 것으로 보아 1세대1주택 비과세 적용</td><td>같은 항</td></tr>
<tr><td>일반주택 요건</td><td>보유기간 <b>2년 이상</b>, 취득 당시 조정대상지역이었다면 보유기간 중 <b>거주 2년 이상</b></td><td>시행령 제154조제1항</td></tr>
<tr><td>고가주택</td><td>양도가액이 <b>12억 원을 넘으면</b> 넘는 비율만큼 양도차익에 과세</td><td>법 제89조제1항제3호, 시행령 제160조</td></tr>
<tr><td>양도 기한</td><td>시행령 제155조제6항에는 일반주택을 언제까지 팔아야 한다는 <b>기한 규정이 없습니다</b></td><td>시행령 제155조제6항</td></tr>
</table></div>
<p>참고로 1세대 3주택 이상 중과세를 판단할 때도 국가유산주택 자체는 <b>중과 대상 주택에서 제외</b>됩니다(시행령 제167조의3제1항제6호). 다만 이 규정은 주택 수 계산에서 빼 주는 규정(같은 항 제1호·제12호)과는 다르니, 다주택이시라면 꼭 따로 확인하셔야 합니다(<a href="/column/111-multi-home-surcharge-resumed.html">칼럼 111</a>).</p>
<p>비슷한 구조의 특례로 상속받은 주택(<a href="/column/08-inherited-house-exemption.html">칼럼 08</a>), 일시적 2주택(<a href="/column/04-temporary-two-house.html">칼럼 04</a>)이 있는데, 이들은 순위·기한 요건이 따로 있다는 점이 다릅니다.</p>

<h2>2. 한○○ 님 사례 — 양도소득세 비교</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>특례가 없다면(일반 2주택 가정)</th><th>국가유산주택 특례 적용</th></tr>
<tr><td>양도가액 / 취득가액</td><td>15억 / 6억</td><td>15억 / 6억</td></tr>
<tr><td>과세 대상 양도차익</td><td>900,000,000</td><td>180,000,000<br><span class="small">(9억 × (15억−12억) ÷ 15억)</span></td></tr>
<tr><td>장기보유특별공제</td><td>△180,000,000 (보유 10년 20%)</td><td>△144,000,000 (보유 40% + 거주 40%)</td></tr>
<tr><td>양도소득기본공제</td><td>△2,500,000</td><td>△2,500,000</td></tr>
<tr><td>과세표준</td><td>717,500,000</td><td>33,500,000</td></tr>
<tr><td>양도소득세</td><td>265,410,000</td><td><b>3,765,000</b></td></tr>
<tr><td>지방소득세 포함 합계</td><td>291,951,000</td><td><b>4,141,500</b></td></tr>
</table></div>
<p>특례 덕분에 세금이 약 <b>2억 8,781만 원</b> 줄어듭니다. 고택을 지키시는 가족에게는 꼭 챙기셔야 할 규정입니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 필요경비는 없고, 아파트는 10년 보유·10년 거주, 다주택 중과는 적용되지 않는 경우로 가정했습니다. 세율은 소득세법 제55조, 장기보유특별공제는 같은 법 제95조제2항(표 1·표 2)을 적용했습니다. 지방소득세는 양도소득세의 10%로 계산했습니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 고택이 <b>지정문화유산·국가등록문화유산·천연기념물등</b> 중 어디에 해당하는지 지정·등록 문서로 확인했다.</li>
<li>☐ 우리 세대가 가진 주택이 <b>문화유산 주택 1개 + 일반주택 1개</b>인지 확인했다(일반주택이 2개 이상이면 다른 특례 검토).</li>
<li>☐ 일반주택의 <b>보유기간 2년</b>, 취득 당시 조정대상지역이었다면 <b>거주 2년</b>을 채웠다.</li>
<li>☐ 양도가액이 <b>12억 원</b>을 넘는지, 넘는다면 장기보유특별공제(보유·거주)를 계산해 봤다.</li>
<li>☐ 양도소득세 신고 때 문화유산 지정·등록 사실을 확인할 자료를 준비했다.</li>
</ul>
<p>문화유산 주택은 세대가 바뀌어도 쉽게 팔 수 없는 경우가 많습니다. 그만큼 세법도 배려하고 있으니, 집을 파시기 전에 요건을 미리 점검해 보시길 권해 드립니다. 궁금하신 점은 편하게 문의해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>문화유산 지정·등록 문서, 건축물대장·등기사항증명서</td><td>특례 대상 주택 여부</td></tr>
<tr><td>세대원 전원의 주택 보유 현황</td><td>문화유산 주택 1개 + 일반주택 1개 여부</td></tr>
<tr><td>일반주택 매매계약서(취득·양도)</td><td>보유기간, 12억 원 초과 여부</td></tr>
<tr><td>주민등록표 초본(주소 이력)</td><td>거주기간</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

_S217 = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec217.py'))

CARDS = [
# 1 표지
f'''<div class="c bg-sunset">{HD()}
<div class="bokeh" style="left:90px;top:220px;width:120px;height:120px;background:#ffe3b0;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:260px;width:90px;height:90px;background:#ffd0e0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-none.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">문화유산 고택 + 내 집</div><div class="t">2주택이어도<br>내 집은 비과세</div><div class="series">양도세 절세 series 16편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#11684a">고택을 물려받은 분의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">한○○ 님</div><div class="say">문화유산 고택이<br>있으면 <span class="mk">2주택자</span>라<br>세금 내나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">일반주택 팔 때는<br><span class="hl">1주택</span>으로<br>봐 드려요!</div></div>
<img class="ch" src="ch/smile-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#11684a">대상은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-night">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">이런 주택이면 해당돼요</div><div class="h1" style="margin-top:8px">특례 대상 주택</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx"><span style="color:#c0392b">지정문화유산</span><br>주택</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx"><span style="color:#1b5fa8">국가등록문화유산</span><br>주택</div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">③</div><div class="tx"><span style="color:#1f8a57">천연기념물등</span><br>주택</div></div>
</div>
{FT(3, True, '소득세법 시행령 제155조⑥')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">일반주택은 산 지<br>2년이 안 돼도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">바로 비과세된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 일반주택도 <b style="font-weight:900">2년 보유</b><br>(조정지역 취득분은 2년 거주)가 필요해요.</div>
{FT(4, True, '소득세법 시행령 제154조①')}</div>''',
# 5 계산
f'''<div class="c dk bg-lilac">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#5b2f7a">15억 아파트 · 10년 보유·거주 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">세금 비교</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>특례 없다면</small><b style="color:#ff5c8a">2.92억</b></div><div class="op">vs</div><div class="bx"><small>특례 적용</small><b style="color:#2fa36b">414만</b></div></div>
<div class="total" style="top:610px"><small>줄어드는 세금(지방세 포함)</small><b>약 2.88억 원</b><span>12억 원 초과분만 과세</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 취득 6억 원, 필요경비 없음<br>· 다주택 중과 미적용</div>
{FT(5, True, '소득세법 제55조·제95조, 시행령 제160조')}</div>''',
# 6 확인
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">팔기 전에 확인!</div><div class="h1" style="margin-top:8px">체크 포인트</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">문화유산 1채<br><span style="color:#1f8a57">+ 일반주택 1채</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">일반주택<br><span style="color:#1b5fa8">2년 보유(거주)</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">양도가액<br><span style="color:#c0392b">12억 초과분 과세</span></div></div>
</div>
{FT(6, True, '소득세법 제89조, 시행령 제154조·제155조')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '집 팔기 전에').replace('<span class="hl">기한</span> 확인!', '<span class="hl">비과세</span> 확인!'),
]
