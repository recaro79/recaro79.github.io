import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 217
SLUG = 'public-interest-trust-inheritance-exclusion'
CAT = '상속세'
DATE = '2026-11-27'
TITLE = '상속재산 일부를 공익신탁으로 장학·자선에 쓰신다면 — 상속세 신고기한까지 신탁하면 그 재산은 상속세 과세가액에서 빠집니다, 중도해지 금지와 잔여재산 국가 귀속 등 요건'
DESC = '상속재산 중 피상속인이나 상속인이 「공익신탁법」에 따른 공익신탁을 통해 공익법인등에 출연하는 재산은 상속세 과세가액에 산입하지 않습니다. 수익자가 공익법인등이나 그 수혜자일 것, 만기까지 중도해지·취소되지 않을 것, 중도해지·종료 시 잔여재산이 국가·지방자치단체·다른 공익신탁에 귀속될 것이 요건이며, 상속세 신고기한까지 신탁을 이행해야 합니다. 상속세 및 증여세법 제17조, 같은 법 시행령 제14조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '상속세 및 증여세법 제17조, 같은 법 시행령 제14조제1항·제2항, 같은 법 제26조'
TAGS = ['공익신탁', '상속세', '과세가액불산입', '장학기금', '기부', '부산세무사']
ALTS = ['공익신탁 상속세 (표지)', '공익신탁 상속세 (상담 질문)', '공익신탁 상속세 (요건)', '공익신탁 상속세 (O·X 퀴즈)', '공익신탁 상속세 (세금 차이)', '공익신탁 상속세 (확인할 점)', '공익신탁 상속세 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"아버지께서 생전에 모교 후배들을 위한 장학금을 늘 말씀하셨어요." 상속 상담을 하다 보면 고인의 뜻을 기려 재산 일부를 공익에 쓰고 싶어 하시는 가족을 자주 뵙습니다. 재단을 직접 세우기 부담스럽다면 <b>공익신탁</b>이라는 방법이 있습니다. 요건을 갖춰 <b>상속세 신고기한까지</b> 신탁하면 그 재산은 <b>상속세 과세가액에서 빠집니다</b>. 오늘은 요건을 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>상속재산 중 피상속인이나 상속인이 「공익신탁법」에 따른 <b>공익신탁</b>을 통해 공익법인등에 출연하는 재산은 상속세 과세가액에 <b>넣지 않습니다</b>.</li><li>수익자가 <b>공익법인등이나 그 수혜자</b>, 만기까지 <b>중도해지·취소 없음</b>, 중도해지·종료 시 잔여재산은 <b>국가·지자체·다른 공익신탁</b>에 귀속되어야 합니다.</li><li><b>상속세 신고기한까지</b> 신탁을 이행해야 하고, 법령·행정상 사유로 늦어지면 그 사유가 끝난 달의 말일부터 6개월 안에 이행합니다.</li></ol>
<div class="small" style="margin-top:8px">(상속세 및 증여세법 제17조, 같은 법 시행령 제14조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"아버지 뜻대로 상속재산 중 2억 원으로 장학금을 만들고 싶어요. 재단을 세우지 않아도 상속세 혜택이 있나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>문○○ 님(가칭) 가족은 아버지가 남기신 상속재산 <b>20억 원</b> 중 <b>2억 원</b>을 「공익신탁법」에 따른 장학 목적 공익신탁에 맡기기로 했습니다. 상속인은 자녀들뿐이고, 상속세 신고기한 안에 신탁을 마쳤습니다. 이 2억 원은 상속세 과세가액에 들어가지 않습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 공익신탁 과세가액 불산입 요건</h2>
<div class="tbl"><table>
<tr><th>요건</th><th>내용</th><th>근거</th></tr>
<tr><td>신탁 종류</td><td>「공익신탁법」에 따른 공익신탁으로서 종교·자선·학술 그 밖의 공익 목적</td><td>법 제17조제1항</td></tr>
<tr><td>수익자</td><td>공익법인등이거나 그 공익법인등의 <b>수혜자</b></td><td>시행령 제14조제1항제1호</td></tr>
<tr><td>중도해지 금지</td><td>만기일까지 신탁계약이 <b>중도해지·취소되지 않을 것</b></td><td>같은 항 제2호</td></tr>
<tr><td>잔여재산 귀속</td><td>중도해지·종료 시 잔여 신탁재산이 <b>국가·지방자치단체·다른 공익신탁</b>에 귀속</td><td>같은 항 제3호</td></tr>
<tr><td>이행 기한</td><td><b>상속세 신고기한까지</b> 신탁 이행(법령·행정상 사유로 늦어지면 사유 종료일이 속하는 달의 말일부터 6개월 이내)</td><td>시행령 제14조제2항</td></tr>
</table></div>
<p>장학재단·복지법인 같은 공익법인에 <b>직접 출연</b>하는 방법은 별도 규정(상증법 제16조)이 적용됩니다(<a href="/column/80-public-interest-donation-inheritance.html">칼럼 80</a>). 국가·지방자치단체에 증여하는 경우는 비과세입니다(<a href="/column/202-inheritance-donated-to-state-tax-free.html">칼럼 202</a>).</p>

<h2>2. 문○○ 님 사례 — 상속세 비교</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>공익신탁 없이</th><th>2억 원 공익신탁</th></tr>
<tr><td>상속세 과세가액</td><td>2,000,000,000</td><td>1,800,000,000</td></tr>
<tr><td>상속공제(일괄공제)</td><td>△500,000,000</td><td>△500,000,000</td></tr>
<tr><td>과세표준</td><td>1,500,000,000</td><td>1,300,000,000</td></tr>
<tr><td>상속세 산출세액</td><td>440,000,000</td><td><b>360,000,000</b></td></tr>
</table></div>
<p>2억 원을 공익신탁하면 상속세 산출세액이 <b>8천만 원</b> 줄어듭니다. 고인의 뜻을 기리면서 세금 부담도 덜 수 있는 방법입니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 배우자 없이 자녀들만 상속하고, 채무·금융재산공제·사전증여재산은 없으며, 상속공제는 일괄공제 5억 원만 적용했다고 가정했습니다. 세율은 상속세 및 증여세법 제26조를 적용했고 신고세액공제는 반영하지 않았습니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 「공익신탁법」에 따른 <b>인가</b>를 받는 공익신탁인지 신탁회사와 확인했다.</li>
<li>☐ 수익자·중도해지 금지·잔여재산 귀속 조항이 신탁계약서에 들어 있는지 확인했다.</li>
<li>☐ <b>상속세 신고기한</b>(상속개시일이 속하는 달의 말일부터 6개월) 안에 신탁 이행이 가능하도록 일정을 잡았다.</li>
<li>☐ 상속인들 사이에 어떤 재산을 신탁할지 <b>분할 협의</b>를 먼저 정리했다.</li>
<li>☐ 공익법인 직접 출연, 국가·지자체 기부와 비교해 가장 맞는 방법을 골랐다.</li>
</ul>
<p>고인의 뜻을 세금 걱정 없이 이어가시려면 방법과 기한을 미리 정하셔야 합니다. 상속재산 일부를 공익에 쓰실 계획이 있다면 신고기한 전에 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>상속재산 목록·상속인 현황</td><td>신탁할 재산, 분할 협의</td></tr>
<tr><td>공익신탁 계약서(안)·인가 자료</td><td>수익자·중도해지·잔여재산 조항</td></tr>
<tr><td>유언장(있는 경우)</td><td>고인의 공익 출연 의사</td></tr>
<tr><td>상속세 신고 일정표</td><td>신탁 이행 기한</td></tr>
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
<img class="ch" src="ch/smile-wave.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">고인의 뜻을 장학금으로</div><div class="t">공익신탁하면<br>상속세 제외</div><div class="series">상속세 절세 series 8편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">상속인 가족의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">문○○ 님</div><div class="say">재단 없이도<br><span class="mk">장학금</span>으로 쓰면<br>혜택이 있나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px"><span class="hl">공익신탁</span>으로<br>신고기한까지<br>맡기시면 돼요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">요건은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">세 가지를 지켜야 해요</div><div class="h1" style="margin-top:8px">공익신탁 요건</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">수익자는<br><span style="color:#1f8a57">공익법인·그 수혜자</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">②</div><div class="tx">만기까지<br><span style="color:#c0392b">중도해지 금지</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">남은 재산은<br><span style="color:#1b5fa8">국가·지자체 등</span> 귀속</div></div>
</div>
{FT(3, True, '상증법 시행령 제14조①')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">상속세를 신고한 뒤<br>1년 안에만 신탁하면<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">혜택을 받는다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-calc.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 원칙적으로 상속세<br><b style="font-weight:900">신고기한까지</b> 신탁해야 해요.</div>
{FT(4, True, '상증법 시행령 제14조②')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">상속재산 20억 원 · 자녀만 상속 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">2억 원 공익신탁</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>신탁 없이</small><b style="color:#ff5c8a">4.4억</b></div><div class="op">vs</div><div class="bx"><small>2억 신탁</small><b style="color:#2fa36b">3.6억</b></div></div>
<div class="total" style="top:610px"><small>줄어드는 상속세(산출세액)</small><b>8천만 원</b><span>40% 세율 구간에서 2억 원 제외</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 일괄공제 5억 원만 적용<br>· 신고세액공제 반영 전</div>
{FT(5, True, '상증법 제17조·제26조')}</div>''',
# 6 확인
f'''<div class="c bg-orange">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">다른 방법과 비교</div><div class="h1" style="margin-top:8px">공익 출연 방법</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx"><span style="color:#1f8a57">공익신탁</span><br>과세가액 불산입</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx"><span style="color:#1b5fa8">공익법인 출연</span><br>불산입(사후관리)</div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx"><span style="color:#c0392b">국가·지자체</span><br>증여 비과세</div></div>
</div>
{FT(6, True, '상증법 제12조·제16조·제17조')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '공익 출연 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">기한</span> 확인!'),
]
