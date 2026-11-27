import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 219
SLUG = 'non-business-asset-expense-disallowance'
CAT = '법인세'
DATE = '2026-11-27'
TITLE = '법인 이름으로 사 둔 땅을 놀리고 계신다면 — 업무에 쓰지 않는 부동산·자산의 유지비·관리비는 법인 비용으로 인정되지 않습니다, 취득 후 2년(신축용 토지 5년) 유예기간과 관련 차입금 이자까지'
DESC = '법인이 업무에 직접 사용하지 않는 부동산(유예기간 경과 후), 업무에 쓰지 않는 서화·골동품·자동차·선박·항공기 등 업무무관자산을 취득·관리하면서 생기는 비용, 유지비, 수선비와 관련 비용은 손금에 산입하지 않습니다. 유예기간은 건축물 신축용 토지 5년, 그 밖의 부동산 2년이며, 업무무관자산을 가진 법인의 차입금 이자 일부도 손금불산입됩니다. 법인세법 제27조·제28조, 같은 법 시행령 제49조·제50조, 같은 법 시행규칙 제26조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '법인세법 제27조·제28조제1항제4호, 같은 법 시행령 제49조·제50조, 같은 법 시행규칙 제26조'
TAGS = ['업무무관자산', '업무무관부동산', '손금불산입', '법인세', '법인부동산', '부산세무사']
ALTS = ['업무무관자산 비용 손금불산입 (표지)', '업무무관자산 비용 손금불산입 (상담 질문)', '업무무관자산 비용 손금불산입 (O·X 퀴즈)', '업무무관자산 비용 손금불산입 (유예기간)', '업무무관자산 비용 손금불산입 (세금 차이)', '업무무관자산 비용 손금불산입 (대상 자산)', '업무무관자산 비용 손금불산입 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"나중에 공장 지으려고 회사 이름으로 땅을 사 뒀는데, 관리비랑 수선비는 당연히 회사 비용이죠?" 법인 대표님들께 자주 듣는 질문입니다. 그런데 그 땅을 <b>업무에 쓰지 않은 채 유예기간이 지나면</b> 세법은 <b>업무무관 부동산</b>으로 보고, 그 땅을 관리하느라 쓴 돈을 <b>법인 비용(손금)으로 인정하지 않습니다</b>. 오늘은 어떤 자산이 해당되는지, 유예기간은 얼마인지 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>법인 업무에 직접 쓰지 않는 <b>부동산</b>, 업무에 쓰지 않는 <b>서화·골동품·자동차·선박·항공기</b> 등은 <b>업무무관자산</b>입니다.</li><li>이 자산을 취득·관리하면서 생기는 <b>비용·유지비·수선비</b>와 관련 비용은 <b>손금불산입</b>되고, 업무무관자산을 가진 법인의 <b>차입금 이자 일부</b>도 비용으로 인정되지 않습니다.</li><li>부동산은 취득 후 <b>유예기간</b>(신축용 토지 <b>5년</b>, 그 밖의 부동산 <b>2년</b>) 안에 업무에 쓰기 시작하면 업무무관 부동산이 되지 않습니다.</li></ol>
<div class="small" style="margin-top:8px">(법인세법 제27조·제28조, 같은 법 시행령 제49조, 같은 법 시행규칙 제26조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"회사 이름으로 사 둔 땅이 3년째 비어 있어요. 관리비랑 수선비를 회사 비용으로 처리해도 되나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>(주)○○(가칭, 제조업)은 3년 전 창고를 짓겠다며 땅과 낡은 건물을 샀지만 아직 착공하지 못하고 비워 두었습니다. 이 땅은 건축물 신축용 토지가 아니라 기존 건물이 있는 부동산이어서 유예기간이 <b>취득일부터 2년</b>이고, 그 기간이 지났습니다. 2026 사업연도에 이 부동산의 유지비·수선비·관리 용역비로 <b>3,000만 원</b>을 비용 처리했다면, 세무조정으로 <b>전액 손금불산입</b>해야 합니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다. 정당한 사유로 업무에 쓰지 못하는 경우 등 예외(시행규칙 제26조제5항)가 있는지는 별도로 확인해야 합니다.</p>

<h2>1. 업무무관자산과 손금불산입되는 비용</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>업무무관 부동산</td><td>① 법인의 업무에 직접 사용하지 않는 부동산(유예기간 중인 것은 제외)<br>② 유예기간 중에 업무에 쓰지 않고 양도하는 부동산(부동산매매업이 주업인 법인 제외)</td><td>시행령 제49조제1항제1호</td></tr>
<tr><td>업무무관 동산</td><td>서화·골동품(사무실·복도 등 여러 사람이 보는 곳에 늘 두는 장식용은 제외), 업무에 쓰지 않는 자동차·선박·항공기, 그 밖의 비슷한 자산</td><td>시행령 제49조제1항제2호</td></tr>
<tr><td>손금불산입 비용</td><td>위 자산을 <b>취득·관리하면서 생기는 비용, 유지비, 수선비</b> 및 관련 비용</td><td>법 제27조제1호, 시행령 제49조제3항</td></tr>
<tr><td>관련 이자</td><td>업무무관자산을 취득·보유한 법인이 낸 차입금 이자 중 시행령으로 정한 금액(해당 자산가액 상당 차입금 이자 한도)</td><td>법 제28조제1항제4호</td></tr>
<tr><td>그 밖의 업무무관 지출</td><td>법인이 직접 쓰지 않고 다른 사람(주주가 아닌 임원·소액주주 임원·직원은 제외)이 주로 쓰는 장소·건축물·물건의 유지비·관리비·사용료 등</td><td>시행령 제50조제1항제1호</td></tr>
</table></div>

<h2>2. 부동산 유예기간과 '업무'의 뜻</h2>
<div class="tbl"><table>
<tr><th>부동산 종류</th><th>유예기간</th></tr>
<tr><td>건축물·시설물 <b>신축용 토지</b></td><td>취득일부터 <b>5년</b>(공장용 부지로 승인받은 공장건설계획기간이 5년을 넘으면 그 기간)</td></tr>
<tr><td>부동산매매업이 주업인 법인의 <b>매매용 부동산</b></td><td>취득일부터 <b>5년</b></td></tr>
<tr><td><b>그 밖의 부동산</b></td><td>취득일부터 <b>2년</b></td></tr>
</table></div>
<p>여기서 '법인의 업무'는 법령에서 정한 업무 또는 <b>사업연도 종료일 현재 법인등기부에 적힌 목적사업</b>(인허가가 필요한 사업은 인허가를 받은 경우)입니다(시행규칙 제26조제2항). 토지를 사서 업무용 건물 공사를 <b>착공</b>하면 업무에 직접 사용한 것으로 보고, 반대로 <b>건물 없는 땅을 임대</b>하면(업무에 쓰던 공장·건물 부속토지를 임대하는 경우 제외) 업무에 직접 쓰지 않는 부동산으로 봅니다(같은 조 제3항·제4항).</p>
<p>법령으로 사용이 금지·제한된 부동산, 경매·공매 진행 중인 부동산, 휴업·폐업·이전으로 쓰지 않게 된 지 5년이 안 된 부동산, 도시계획 변경 등 정당한 사유로 쓰지 못하는 부동산 등은 <b>부득이한 사유</b>가 있는 부동산으로 업무무관 부동산에서 제외됩니다(같은 조 제5항). 가지급금 인정이자는 <a href="/column/10-provisional-payment-interest.html">칼럼 10</a>, 임원 사택 비용은 <a href="/column/161-executive-company-housing-expense.html">칼럼 161</a>에서 다뤘습니다.</p>

<h2>3. (주)○○ 사례 — 법인세 비교</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>비용으로 처리한 그대로</th><th>업무무관 비용 손금불산입 후</th></tr>
<tr><td>조정 전 과세표준</td><td>180,000,000</td><td>180,000,000</td></tr>
<tr><td>손금불산입(유지비·수선비 등)</td><td>-</td><td>+30,000,000</td></tr>
<tr><td>과세표준</td><td>180,000,000</td><td>210,000,000</td></tr>
<tr><td>법인세 산출세액</td><td>18,000,000</td><td><b>22,000,000</b></td></tr>
<tr><td>지방소득세 포함 합계</td><td>19,800,000</td><td><b>24,200,000</b></td></tr>
</table></div>
<p>3,000만 원의 비용이 인정되지 않으면서 세금이 <b>440만 원</b> 늘어납니다. 신고 때 빠뜨렸다가 나중에 확인되면 가산세까지 붙을 수 있으니 미리 점검하시는 것이 좋습니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 2026년 1월 1일 이후 개시하는 사업연도에 적용되는 법인세율(법인세법 제55조제1항제1호: 2억 원 이하 10%, 2억 원 초과 200억 원 이하 20%)을 적용했고, 차입금 이자 손금불산입·세액공제·감면은 없다고 가정했습니다. 지방소득세는 법인세의 10%로 계산했습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 법인 명의 부동산마다 <b>취득일</b>과 <b>실제 업무 사용 시작일</b>을 정리했다.</li>
<li>☐ 신축용 토지(5년)인지, 그 밖의 부동산(2년)인지 <b>유예기간</b>을 확인했다.</li>
<li>☐ 사용하려는 용도(임대 등)가 <b>법인등기부 목적사업</b>에 들어 있는지 확인했다.</li>
<li>☐ 사용하지 못한 데 <b>부득이한 사유</b>(사용 제한, 경매, 휴업·이전 등)가 있다면 증빙을 모아 두었다.</li>
<li>☐ 대표 자택 등에 둔 그림·골동품, 업무에 쓰지 않는 차량·선박의 비용을 회사 비용으로 처리하지 않았다.</li>
<li>☐ 업무무관자산이 있다면 차입금 이자 손금불산입 금액도 함께 계산했다.</li>
</ul>
<p>법인 부동산은 사 두는 시점보다 <b>언제부터 어떻게 쓰는지</b>가 세금을 가릅니다. 법인 명의로 부동산을 사셨거나 살 계획이 있으시면 결산 전에 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>법인 부동산 등기사항증명서·매매계약서</td><td>취득일, 유예기간</td></tr>
<tr><td>건축허가·착공신고서, 임대차계약서</td><td>업무 사용 시작일, 사용 형태</td></tr>
<tr><td>법인등기부등본</td><td>목적사업</td></tr>
<tr><td>계정별 원장(유지비·수선비·이자)</td><td>손금불산입 대상 금액</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

_S217 = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec217.py'))

CARDS = [
# 1 표지
f'''<div class="c bg-navy">{HD()}
<div class="bokeh" style="left:90px;top:220px;width:120px;height:120px;background:#9fc4ff;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:260px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/worry-doc-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">법인 명의로 사 둔 땅</div><div class="t">놀리면 관리비<br>비용 불인정</div><div class="series">법인세 절세 series 7편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">법인 대표님의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">○○ 대표님</div><div class="say">3년째 비어 있는 땅,<br><span class="mk">관리비</span>는 회사<br>비용이죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">업무에 안 쓰면<br><span class="hl">비용 불인정</span>이에요!</div></div>
<img class="ch" src="ch/wink-magnify.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">왜 그럴까요? →</div>
{FT(2, False)}</div>''',
# 3 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">대표님 집 거실에 둔<br>골동품 관리비도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">회사 비용이다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-none.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 사무실·복도 등에 늘 두는<br><b style="font-weight:900">장식용만</b> 업무무관자산에서 빠져요.</div>
{FT(3, True, '법인세법 시행령 제49조①')}</div>''',
# 4 숫자 타일(목록)
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">이 기간 안에 쓰기 시작하세요</div><div class="h1" style="margin-top:8px">부동산 유예기간</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">5</div><div class="tx">건물 신축용 토지<br><span style="color:#1f8a57">취득 후 5년</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">5</div><div class="tx">매매업 법인 매매용<br><span style="color:#1b5fa8">취득 후 5년</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">2</div><div class="tx">그 밖의 부동산<br><span style="color:#c0392b">취득 후 2년</span></div></div>
</div>
{FT(4, True, '법인세법 시행규칙 제26조①')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">유지비·수선비 3천만 원 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">법인세 비교</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>비용 인정 시</small><b style="color:#2fa36b">1,980만</b></div><div class="op">vs</div><div class="bx"><small>손금불산입</small><b style="color:#ff5c8a">2,420만</b></div></div>
<div class="total" style="top:610px"><small>늘어나는 세금(지방세 포함)</small><b>440만 원</b><span>과세표준 1.8억 → 2.1억</span></div>
<img class="ch" src="ch/worry-calc.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 2026년 개시 사업연도 세율<br>· 이자 손금불산입·공제 없음</div>
{FT(5, True, '법인세법 제27조·제55조')}</div>''',
# 6 목록
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">비용 불인정 범위</div><div class="h1" style="margin-top:8px">이것도 빠져요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">유지비·수선비<br><span style="color:#c0392b">관리 비용</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">관련 차입금<br><span style="color:#1b5fa8">이자 일부</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">③</div><div class="tx">안 쓰는 차량·<br><span style="color:#1f8a57">선박·골동품</span></div></div>
</div>
{FT(6, True, '법인세법 제27조·제28조①4')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '결산 전에').replace('<span class="hl">기한</span> 확인!', '<span class="hl">법인 자산</span> 점검!'),
]
