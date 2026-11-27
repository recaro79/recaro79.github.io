import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 226
SLUG = 'child-birth-adoption-tax-credit'
CAT = '종합소득세'
DATE = '2026-11-27'
TITLE = '올해 아기가 태어났거나 입양하셨다면 — 출산·입양 세액공제 첫째 30만·둘째 50만·셋째 이상 70만 원, 8세 이상 자녀·손자녀는 1명 25만·2명 55만·셋째부터 1명당 40만 원 자녀세액공제'
DESC = '기본공제대상자인 8세 이상 자녀(입양자·위탁아동 포함)와 손자녀가 있으면 1명 연 25만 원, 2명 연 55만 원, 3명 이상은 55만 원에 2명을 넘는 1명당 40만 원을 더한 금액을 세액에서 공제합니다. 해당 과세기간에 출산하거나 입양 신고한 자녀가 있으면 첫째 30만 원, 둘째 50만 원, 셋째 이상 70만 원을 추가로 공제합니다. 소득세법 제59조의2 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제59조의2제1항·제3항'
TAGS = ['자녀세액공제', '출산세액공제', '입양세액공제', '연말정산', '종합소득세', '부산세무사']
ALTS = ['자녀·출산 세액공제 (표지)', '자녀·출산 세액공제 (상담 질문)', '자녀·출산 세액공제 (출산·입양)', '자녀·출산 세액공제 (O·X 퀴즈)', '자녀·출산 세액공제 (8세 이상 자녀)', '자녀·출산 세액공제 (사례 계산)', '자녀·출산 세액공제 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"올해 셋째가 태어났는데 연말정산에서 뭘 더 받을 수 있나요?" 먼저 축하드립니다. 아이가 태어나거나 입양한 해에는 <b>출산·입양 세액공제</b>를 받을 수 있고, 8세 이상 자녀가 있으면 <b>자녀세액공제</b>도 받습니다. 둘 다 소득공제가 아니라 <b>세금에서 바로 빼 주는 세액공제</b>라 효과가 확실합니다. 오늘은 금액과 요건을 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>올해 출산하거나 <b>입양 신고</b>한 자녀가 있으면 <b>첫째 30만 원, 둘째 50만 원, 셋째 이상 70만 원</b>을 세액에서 공제합니다.</li><li>기본공제대상자인 <b>8세 이상 자녀·손자녀</b>(입양자·위탁아동 포함)는 <b>1명 25만 원, 2명 55만 원</b>, 3명부터는 1명당 <b>40만 원</b>씩 더해 공제합니다.</li><li>두 공제는 <b>함께</b> 받을 수 있고, 자녀를 <b>기본공제로 올린 사람</b>이 받습니다. 맞벌이라면 누가 공제받을지 미리 정하세요.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제59조의2 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"올해 셋째가 태어났고, 위로 9살·12살 아이가 있어요. 세금이 얼마나 줄까요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>한○○ 님(가칭)은 올해 <b>셋째</b>를 낳으셨고, 위로 <b>9살·12살</b> 두 자녀가 있습니다. 세 자녀 모두 한○○ 님의 기본공제대상자로 올리기로 했습니다. 막내는 8세 미만이라 자녀세액공제(8세 이상)에는 들어가지 않지만, 올해 태어났으므로 <b>출산 세액공제</b>를 받습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 출산·입양 세액공제</h2>
<div class="tbl"><table>
<tr><th>해당 과세기간에 출산·입양 신고한 자녀</th><th>공제액(연)</th></tr>
<tr><td>첫째</td><td><b>30만 원</b></td></tr>
<tr><td>둘째</td><td><b>50만 원</b></td></tr>
<tr><td>셋째 이상</td><td><b>70만 원</b></td></tr>
</table></div>
<p>입양은 <b>입양 신고한 과세기간</b>에 공제합니다. 몇째인지는 공제대상 자녀 중 순서로 판단합니다(소득세법 제59조의2제3항).</p>

<h2>2. 8세 이상 자녀세액공제</h2>
<div class="tbl"><table>
<tr><th>8세 이상 공제대상 자녀·손자녀 수</th><th>공제액(연)</th></tr>
<tr><td>1명</td><td><b>25만 원</b></td></tr>
<tr><td>2명</td><td><b>55만 원</b></td></tr>
<tr><td>3명</td><td><b>95만 원</b> (55만 + 40만)</td></tr>
<tr><td>4명</td><td><b>135만 원</b> (55만 + 40만 × 2)</td></tr>
</table></div>
<p>공제대상 자녀는 <b>기본공제대상자</b>여야 하므로, 원칙적으로 20세 이하이고 연 소득금액이 100만 원(근로소득만 있으면 총급여 500만 원) 이하여야 합니다. 맞벌이 부부의 부양가족 공제 배분은 <a href="/column/153-dual-income-dependent-deduction.html">칼럼 153</a>을 참고해 주세요.</p>

<h2>3. 한○○ 님 사례 — 올해 받는 공제</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>대상</th><th>공제액</th></tr>
<tr><td>자녀세액공제(8세 이상)</td><td>9살·12살 2명</td><td>550,000원</td></tr>
<tr><td>출산 세액공제</td><td>셋째 출산</td><td>700,000원</td></tr>
<tr><td colspan="2">합계(소득세에서 직접 공제)</td><td><b>1,250,000원</b></td></tr>
</table></div>
<p>세 자녀의 기본공제(1명당 150만 원 소득공제)와는 별도로, 세액에서 <b>125만 원</b>을 바로 뺍니다. 막내가 8살이 되는 해부터는 8세 이상 자녀가 3명이 되어 자녀세액공제가 <b>95만 원</b>으로 늘어납니다(그 사이 위 자녀의 나이·소득 요건이 유지된다고 가정).</p>
<p class="small">※ python으로 계산·검산했습니다. 세액공제는 납부할 소득세(산출세액) 범위에서 적용됩니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 올해 태어난 아이의 <b>출생신고</b>(입양은 <b>입양 신고</b>)를 마쳤다.</li>
<li>☐ 자녀를 <b>누구의 기본공제</b>로 올릴지 부부가 정했다(한 사람만 공제).</li>
<li>☐ 8세 이상 자녀의 <b>나이·소득 요건</b>(기본공제대상자)을 확인했다.</li>
<li>☐ 손자녀를 부양하고 계시다면 기본공제대상자로 올릴 수 있는지 확인했다.</li>
<li>☐ 연말정산(근로자)이나 5월 종합소득세 신고(사업자)에서 공제를 빠뜨리지 않았다.</li>
</ul>
<p>아이가 늘수록 챙길 공제도 늘어납니다. 연말정산이나 종합소득세 신고 전에 가족 공제를 한 번에 점검해 드리니 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>가족관계증명서·주민등록등본</td><td>자녀 수, 출생·입양 순서</td></tr>
<tr><td>입양관계증명서(입양한 경우)</td><td>입양 신고일</td></tr>
<tr><td>자녀의 소득 자료(있는 경우)</td><td>기본공제 소득 요건</td></tr>
<tr><td>배우자의 연말정산 자료</td><td>공제받을 사람 배분</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

_S217 = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec217.py'))

CARDS = [
# 1 표지
f'''<div class="c bg-pink">{HD()}
<div class="bokeh" style="left:90px;top:220px;width:120px;height:120px;background:#ffe3f0;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:260px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/smile-wave.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">올해 아기가 태어났다면</div><div class="t">출산 세액공제<br>최대 70만 원</div><div class="series">종합소득세 절세 series 12편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#11684a">세 아이 부모님의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">한○○ 님</div><div class="say">올해 <span class="mk">셋째</span>가 태어났어요.<br>세금 혜택이<br>있나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">축하드려요!<br>출산공제 <span class="hl">70만 원</span><br>받으세요</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#11684a">금액은? →</div>
{FT(2, False)}</div>''',
# 3 숫자 타일
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">올해 출산·입양 신고</div><div class="h1" style="margin-top:8px">출산·입양 세액공제</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#3d8bff">30</div><div class="tx">첫째<br><span style="color:#1b5fa8">30만 원</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">50</div><div class="tx">둘째<br><span style="color:#1f8a57">50만 원</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">70</div><div class="tx">셋째 이상<br><span style="color:#c0392b">70만 원</span></div></div>
</div>
{FT(3, True, '소득세법 제59조의2③')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">출산 세액공제와<br>자녀세액공제는<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">하나만 받는다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wow-none.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 요건이 맞으면 <b style="font-weight:900">둘 다</b><br>받을 수 있어요.</div>
{FT(4, True, '소득세법 제59조의2①③')}</div>''',
# 5 목록
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">8세 이상 자녀·손자녀</div><div class="h1" style="margin-top:8px">자녀세액공제</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#3d8bff">1</div><div class="tx">1명<br><span style="color:#1b5fa8">연 25만 원</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">2</div><div class="tx">2명<br><span style="color:#1f8a57">연 55만 원</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">3+</div><div class="tx">3명부터<br><span style="color:#c0392b">1명당 40만 원 추가</span></div></div>
</div>
{FT(5, True, '소득세법 제59조의2①')}</div>''',
# 6 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">9살·12살 + 올해 셋째 출산 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">올해 공제액</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>자녀(8세↑) 2명</small><b style="color:#1b5fa8">55만</b></div><div class="op">+</div><div class="bx"><small>셋째 출산</small><b style="color:#2fa36b">70만</b></div></div>
<div class="total" style="top:610px"><small>세금에서 바로 빼는 금액</small><b>125만 원</b><span>기본공제 150만 원(소득공제)과 별도</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">확인</b><br>· 세 자녀 모두 한 사람이 공제<br>· 산출세액 범위에서 공제</div>
{FT(6, True, '소득세법 제59조의2')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '연말정산 전에').replace('<span class="hl">기한</span> 확인!', '<span class="hl">가족 공제</span> 점검!'),
]
