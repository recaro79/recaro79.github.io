import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 198
SLUG = 'corporate-fines-penalties-nondeductible'
CAT = '법인세'
DATE = '2026-11-27'
TITLE = '법인이 낸 벌금·과태료·가산세, 비용이 될까요? — 법인세 계산에서는 빠집니다(손금불산입), 다만 거래처에 낸 지체상금·전기요금 연체가산금은 비용으로 인정'
DESC = '법인이 낸 벌금·과료·과태료·가산금·강제징수비, 세법상 의무 불이행으로 낸 가산세, 법인세·법인지방소득세는 법인세 계산 때 손금에 넣지 않습니다. 반면 계약상 지체상금, 전기요금 연체가산금, 산재보험료 연체금 등은 벌금이 아니어서 손금으로 인정됩니다. 법인세법 제21조, 법인세법 기본통칙 21-0…2·21-0…3 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '법인세법 제21조, 같은 법 시행령 제21조, 법인세법 기본통칙 21-0…1·21-0…2·21-0…3'
TAGS = ['법인세', '손금불산입', '벌금과태료', '가산세', '지체상금', '부산세무사']
ALTS = ['벌금·과태료 손금불산입 (표지)', '벌금·과태료 손금불산입 (상담 질문)', '벌금·과태료 손금불산입 (비용 안 되는 것)', '벌금·과태료 손금불산입 (O·X 퀴즈)', '벌금·과태료 손금불산입 (비용 되는 것)', '벌금·과태료 손금불산입 (세금 차이)', '벌금·과태료 손금불산입 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
연말 결산을 준비하다 보면 "직원이 업무 중에 받은 주차·속도위반 과태료", "부가세 신고를 늦게 해서 낸 가산세", "4대보험 연체금" 같은 지출이 꼭 보입니다. 회사 돈으로 냈으니 당연히 비용이라고 생각하시기 쉽지만, 법인세에서는 <b>비용(손금)으로 인정되지 않는 것</b>과 <b>인정되는 것</b>이 나뉩니다. 오늘은 그 구분을 알기 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li><b>벌금·과료·과태료·가산금·강제징수비</b>는 법인세 계산 때 손금에 넣지 않습니다.</li><li><b>법인세·법인지방소득세</b>, 세법상 의무 불이행으로 낸 세액(<b>가산세</b> 포함)도 손금이 아닙니다.</li><li>반면 계약을 지키지 못해 거래처에 낸 <b>지체상금</b>, <b>전기요금 연체가산금</b>, <b>산재보험료 연체금</b> 등은 벌금이 아니므로 손금으로 인정됩니다.</li></ol>
<div class="small" style="margin-top:8px">(법인세법 제21조, 법인세법 기본통칙 21-0…2·21-0…3 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"직원 업무용 차량 과태료, 부가세 가산세, 납품이 늦어 거래처에 물어 준 지체상금까지 모두 회사 비용으로 처리했는데 괜찮을까요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>(주)○○(가칭, 12월 결산 중소기업)은 2026년 장부에 다음 지출을 비용으로 처리했습니다. 업무 중 발생한 교통 과태료 <b>120만 원</b>, 부가가치세 신고불성실·납부지연 가산세 <b>80만 원</b>, 국민건강보험료 연체금 <b>30만 원</b>, 납품 지연으로 거래처에 낸 지체상금 <b>500만 원</b>, 전기요금 연체가산금 <b>10만 원</b>입니다. 이 중 법인세 계산에서 빠지는(손금불산입) 금액은 <b>230만 원</b>이고, 지체상금과 전기요금 연체가산금 510만 원은 그대로 비용으로 인정됩니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 손금에 넣지 않는 세금과 공과금</h2>
<div class="tbl"><table>
<tr><th>항목</th><th>예시</th><th>근거</th></tr>
<tr><td>법인세·법인지방소득세, 세법상 의무 불이행으로 낸 세액(가산세 포함)</td><td>법인세 본세, 신고불성실·납부지연 가산세, 간접국세 징수·납부 불이행 세액</td><td>법 제21조제1호, 시행령 제21조</td></tr>
<tr><td>벌금·과료·과태료·가산금·강제징수비</td><td>교통 과태료, 행정 과태료, 통고처분 벌금 상당액</td><td>법 제21조제3호</td></tr>
<tr><td>의무가 아닌 공과금, 법령 위반을 이유로 부과되는 공과금</td><td>임의로 낸 공과금, 위반 부과금</td><td>법 제21조제4호·제5호</td></tr>
<tr><td>통칙상 손금불산입 예시</td><td>업무 관련 교통사고 벌과금, 관세법 위반 벌과금, 국민건강보험료 연체금, 산재보험료 <b>가산금</b>, 외국에서 낸 벌과금</td><td>기본통칙 21-0…3</td></tr>
<tr><td>그 밖의 통칙 예시</td><td>원천징수하지 않고 회사가 대신 낸 원천세, 세금계산서 미제출로 공제받지 못한 매입세액</td><td>기본통칙 21-0…1</td></tr>
</table></div>

<h2>2. 벌금이 아니어서 손금으로 인정되는 것</h2>
<div class="tbl"><table>
<tr><th>항목</th><th>근거</th></tr>
<tr><td>사계약상 의무불이행으로 내는 <b>지체상금</b>(정부와의 납품계약 포함, 구상권 행사가 가능한 지체상금은 제외)</td><td>기본통칙 21-0…2 제1호</td></tr>
<tr><td>산업재해보상보험료의 <b>연체금</b></td><td>같은 통칙 제4호</td></tr>
<tr><td>국유지 사용료 납부지연 <b>연체료</b></td><td>같은 통칙 제5호</td></tr>
<tr><td>전기요금 납부지연 <b>연체가산금</b></td><td>같은 통칙 제6호</td></tr>
</table></div>
<p>같은 4대보험이라도 <b>국민건강보험료 연체금은 손금불산입</b>(21-0…3), <b>산재보험료 연체금은 손금</b>(21-0…2)으로 통칙이 다르게 정하고 있어 하나씩 확인해야 합니다.</p>

<h2>3. (주)○○ 사례 — 세금 차이</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>금액</th></tr>
<tr><td>손금불산입 합계(과태료 120만 + 가산세 80만 + 건강보험료 연체금 30만)</td><td>2,300,000</td></tr>
<tr><td>세무조정 전 과세표준(가정)</td><td>300,000,000</td></tr>
<tr><td>법인세(조정 전)</td><td>40,000,000</td></tr>
<tr><td>세무조정 후 과세표준</td><td>302,300,000</td></tr>
<tr><td>법인세(조정 후)</td><td>40,460,000</td></tr>
<tr><td>늘어나는 법인세</td><td><b>460,000</b> (법인지방소득세 포함 약 506,000)</td></tr>
</table></div>
<p>금액 자체는 크지 않지만, 과태료·가산세는 <b>낸 돈에 법인세까지 더 붙는</b> 구조입니다. 그리고 손금불산입 항목을 빠뜨리고 신고하면 나중에 수정신고와 가산세 부담이 생길 수 있습니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 2026년 1월 1일 이후 시작하는 사업연도의 법인세율(법인세법 제55조제1항: 2억 원 이하 10%, 2억 원 초과 200억 원 이하 20%)을 적용했고, 법인지방소득세는 법인세의 10%로 단순 가정했습니다. 세액공제·감면은 반영하지 않았습니다(<a href="/column/144-corporate-tax-rate-2026.html">칼럼 144</a> 참고).</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 세금과공과·잡손실 계정에서 <b>과태료·벌금·가산세</b>를 따로 골라냈다.</li>
<li>☐ 4대보험 연체금은 <b>건강보험(불산입)</b>과 <b>산재보험(손금)</b>을 구분했다.</li>
<li>☐ 거래처에 낸 <b>지체상금</b>은 계약서·청구서를 보관하고, 다른 사람에게 <b>구상권을 행사할 수 있는</b> 지체상금인지(이 경우 제외) 확인했다.</li>
<li>☐ 원천징수를 빠뜨려 회사가 대신 낸 원천세가 있는지 확인했다.</li>
<li>☐ 과태료가 반복된다면 차량 운행 관리·신고 일정 관리로 <b>지출 자체를 줄이는</b> 방법을 검토했다(<a href="/column/82-corporate-business-car.html">칼럼 82</a>).</li>
</ul>
<p>결산 때 세금과공과 계정만 한 번 훑어보셔도 신고 오류를 크게 줄일 수 있습니다. 결산을 앞두고 계시면 계정별 원장을 가지고 편하게 상담해 주세요. 손금 여부를 하나씩 확인해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>세금과공과·잡손실 계정별 원장</td><td>벌금·과태료·가산세·연체금 구분</td></tr>
<tr><td>과태료·가산세 고지서, 납부영수증</td><td>부과 사유와 근거 법령</td></tr>
<tr><td>지체상금 관련 계약서·청구서</td><td>계약상 지체상금 여부, 구상 가능 여부</td></tr>
<tr><td>4대보험 납부 내역</td><td>연체금·가산금 종류</td></tr>
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
<img class="ch" src="ch/worry-doc-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">회사가 낸 과태료·가산세</div><div class="t">비용으로<br>인정될까요?</div><div class="series">법인세 절세 series 4편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">결산 때 꼭 나오는 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">대표님</div><div class="say">과태료·가산세도<br>회사 돈으로 냈으니<br><span class="mk">비용</span> 맞죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">법인세에선<br><span class="hl">비용이 아니에요</span><br>(손금불산입)</div></div>
<img class="ch" src="ch/smile-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">무엇이 빠질까요? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">법인세 계산에서 빠지는 것</div><div class="h1" style="margin-top:8px">손금불산입</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">벌금·과료·<br><span style="color:#c0392b">과태료</span>·강제징수비</div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">법인세 본세와<br><span style="color:#b9770e">가산세</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">국민<span style="color:#1b5fa8">건강보험료</span><br>연체금</div></div>
</div>
{FT(3, True, '법인세법 제21조·통칙 21-0…3')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">납품이 늦어 거래처에<br>물어 준 지체상금도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">비용이 안 된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 계약상 지체상금은<br>벌금이 아니라서 <b style="font-weight:900">비용 인정</b>돼요.</div>
{FT(4, True, '통칙 21-0…2')}</div>''',
# 5 비용 되는 것
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4">벌금이 아니라서</div><div style="font-size:100px;font-weight:900;letter-spacing:-4px;line-height:1.1;text-shadow:0 8px 20px rgba(120,0,40,.35)">비용 OK!</div></div>
<img class="ch" src="ch/smile-thumb.svg" style="right:30px;top:120px;width:360px">
<div class="rows" style="top:520px">
 <div class="row"><div class="ic" style="background:#ff5c8a">①</div><div class="tx">계약상 <span style="color:#e83e6f">지체상금</span></div></div>
 <div class="row"><div class="ic" style="background:#ff9a3c">②</div><div class="tx">전기요금 <span style="color:#e8761e">연체가산금</span></div></div>
 <div class="row"><div class="ic" style="background:#7a5cff">③</div><div class="tx">산재보험료 <span style="color:#5a3fd6">연체금</span></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:1060px;font-size:30px">· <b style="color:#fff3c4">구상권을 행사할 수 있는</b> 지체상금은 제외예요.</div>
{FT(5, True, '통칙 21-0…2')}</div>''',
# 6 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">과세표준 3억 원 법인 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">과태료 등 230만 원</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>낸 돈</small><b style="color:#1b5fa8">230만</b></div><div class="op">+</div><div class="bx"><small>법인세 20%</small><b style="color:#ff5c8a">46만</b></div></div>
<div class="total" style="top:610px"><small>지방소득세 포함 추가 세금</small><b>약 50만 6천 원</b><span>비용으로 빼면 신고 오류!</span></div>
<img class="ch" src="ch/smile-calc.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 2026년 시작 사업연도 세율<br>· 감면·공제는 반영하지 않음</div>
{FT(6, True, '법인세법 제21조·제55조①')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '연말 결산 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">손금</span> 점검!'),
]
