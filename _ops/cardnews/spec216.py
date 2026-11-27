import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 216
SLUG = 'insurance-premium-tax-credit'
CAT = '종합소득세'
DATE = '2026-11-27'
TITLE = '연말정산 보험료 세액공제 — 보장성보험·자동차보험은 물론 전세보증금 반환보증료(보증금 3억 원 이하)까지 연 100만 원 한도 12%, 장애인전용 보험은 별도 100만 원 한도 15%'
DESC = '근로소득자가 기본공제대상자를 피보험자로 하는 보장성보험료(만기환급금이 납입보험료 이하)를 내면 연 100만 원 한도로 12%를 세액공제하고, 장애인전용보장성보험료는 별도로 연 100만 원 한도 15%를 공제합니다. 생명·상해보험, 가계 손해보험(자동차·화재 등), 각종 공제, 보증대상 임차보증금 3억 원 이하 주택 임차보증금 반환보증 보험·보증료가 대상입니다. 소득세법 제59조의4제1항, 같은 법 시행령 제118조의4 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제59조의4제1항, 같은 법 시행령 제118조의4제1항·제2항'
TAGS = ['보험료세액공제', '연말정산', '전세보증보험', '보장성보험', '장애인전용보험', '부산세무사']
ALTS = ['보험료 세액공제 (표지)', '보험료 세액공제 (상담 질문)', '보험료 세액공제 (대상 보험)', '보험료 세액공제 (O·X 퀴즈)', '보험료 세액공제 (한도·공제율)', '보험료 세액공제 (사례 계산)', '보험료 세액공제 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
연말정산에서 보험료 공제는 "실손보험이나 종신보험만 되는 것"으로 아시는 분이 많습니다. 그런데 <b>자동차보험</b>, <b>화재보험</b> 같은 가계 손해보험과 <b>전세보증금 반환보증료</b>(보증금 3억 원 이하)도 공제 대상입니다. 다만 한도가 연 100만 원이라 이미 다른 보험료로 한도를 채우셨다면 추가 효과는 없습니다. 장애인 가족이 있다면 <b>장애인전용 보험</b>은 한도가 따로라는 점도 함께 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li><b>근로소득자</b>가 기본공제대상자를 피보험자로 낸 <b>보장성보험료</b>(만기환급금이 납입보험료 이하)는 연 <b>100만 원</b> 한도로 <b>12%</b> 세액공제됩니다.</li><li>생명·상해보험, 자동차·화재 등 <b>가계 손해보험</b>, 수협·신협·새마을금고 공제, <b>전세보증금 반환보증 보험·보증료</b>(보증금 3억 원 이하)가 대상입니다.</li><li><b>장애인전용 보장성보험료</b>는 별도로 연 100만 원 한도 <b>15%</b>입니다.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제59조의4제1항, 같은 법 시행령 제118조의4 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"전세 살면서 전세보증금 반환보증에 가입했는데, 그 보증료도 연말정산에서 공제가 되나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>직장인 염○○ 님(가칭)은 올해 본인 실손보험료 <b>50만 원</b>, 자동차보험료 <b>40만 원</b>, 전세보증금(2억 5천만 원) 반환보증료 <b>20만 원</b>을 냈고, 기본공제대상자인 장애인 자녀의 <b>장애인전용 보장성보험료 120만 원</b>을 냈습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 공제 대상 보험료</h2>
<div class="tbl"><table>
<tr><th>대상</th><th>내용</th><th>근거</th></tr>
<tr><td>생명보험·상해보험</td><td>만기환급금이 납입보험료를 초과하지 않는 보장성 보험</td><td>소득세법 제59조의4제1항, 시행령 제118조의4제2항제1호·제2호</td></tr>
<tr><td>가계 손해보험</td><td>화재·도난이나 그 밖의 손해를 담보하는 가계 손해보험(자동차보험 등)</td><td>시행령 제118조의4제2항제3호</td></tr>
<tr><td>각종 공제</td><td>수협·신협·새마을금고 공제, 군인·교직원·지방행정·경찰·소방 공제회 공제</td><td>같은 항 제4호·제5호</td></tr>
<tr><td><b>전세보증금 반환보증</b></td><td>주택 임차보증금 반환을 보증하는 보험·보증의 보험료·보증료 — 보증대상 임차보증금 <b>3억 원 초과</b>면 제외</td><td>같은 항 제6호</td></tr>
<tr><td><b>장애인전용</b> 보장성보험</td><td>계약서나 납입영수증에 장애인전용으로 표시된 보험·공제(장애인을 피보험자 또는 수익자로)</td><td>시행령 제118조의4제1항</td></tr>
</table></div>
<p class="small">구체적인 대상 보험료는 시행령 위임에 따라 시행규칙으로 정하므로, 연말정산 간소화 자료에 공제 대상으로 표시되는지 함께 확인하세요.</p>

<h2>2. 한도와 공제율</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>한도</th><th>공제율</th></tr>
<tr><td>일반 보장성보험료(위 대상 합계)</td><td>연 100만 원</td><td>12%</td></tr>
<tr><td>장애인전용 보장성보험료</td><td>연 100만 원(별도)</td><td><b>15%</b></td></tr>
</table></div>
<p>보험의 <b>피보험자</b>가 기본공제대상자(나이·소득 요건을 갖춘 부양가족)여야 하고, 근로소득자(일용근로자 제외)만 받을 수 있습니다(소득세법 제59조의4제1항).</p>

<h2>3. 염○○ 님 사례 계산</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>납입액</th><th>공제 대상</th><th>세액공제</th></tr>
<tr><td>실손 50만 + 자동차 40만 + 전세보증료 20만</td><td>1,100,000</td><td>1,000,000(한도)</td><td>120,000</td></tr>
<tr><td>장애인전용 보장성보험</td><td>1,200,000</td><td>1,000,000(한도)</td><td>150,000</td></tr>
<tr><td colspan="3"><b>합계</b></td><td><b>270,000</b></td></tr>
</table></div>
<p class="small">※ python으로 계산·검산했습니다. 산출세액이 공제액보다 충분히 크다고 가정했습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 보험의 <b>피보험자</b>가 본인 또는 기본공제대상자인지 확인했다.</li>
<li>☐ <b>저축성</b>(만기환급금이 납입보험료보다 큰) 보험은 제외된다는 점을 확인했다.</li>
<li>☐ 전세보증금 반환보증은 <b>보증대상 보증금 3억 원 이하</b>인지 확인했다.</li>
<li>☐ 장애인전용 보험은 증권·영수증에 <b>장애인전용</b> 표시가 있는지 확인했다(<a href="/column/206-disabled-dependent-deduction-medical-certificate.html">칼럼 206</a>).</li>
<li>☐ 맞벌이라면 계약자·피보험자와 기본공제 받는 사람을 맞춰 보았다(<a href="/column/153-dual-income-dependent-deduction.html">칼럼 153</a>).</li>
</ul>
<p>보험료 공제는 한도가 작지만 해마다 받을 수 있는 공제입니다. 연말정산 자료를 가지고 편하게 상담해 주세요. 빠진 공제가 없는지 함께 확인해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>연말정산 간소화 보험료 자료</td><td>공제 대상 여부, 납입액</td></tr>
<tr><td>보험증권</td><td>계약자·피보험자, 장애인전용 표시</td></tr>
<tr><td>전세보증 가입 증명·임대차계약서</td><td>보증대상 보증금 3억 원 이하 여부</td></tr>
<tr><td>가족관계·소득 자료</td><td>기본공제대상자 여부</td></tr>
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
<img class="ch" src="ch/smile-doc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">자동차보험·전세보증료도?</div><div class="t">보험료<br>세액공제 정리</div><div class="series">종합소득세 절세 series 10편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">연말정산 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">염○○ 님</div><div class="say"><span class="mk">전세보증료</span>도<br>보험료 공제<br>되나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">보증금 <span class="hl">3억 원 이하</span>면<br>공제돼요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">대상 보험은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">이런 보험료가 공제돼요</div><div class="h1" style="margin-top:8px">공제 대상</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">생명·상해<br><span style="color:#1f8a57">보장성 보험</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx"><span style="color:#1b5fa8">자동차·화재</span> 등<br>가계 손해보험</div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx"><span style="color:#c0392b">전세보증금</span> 반환보증<br>(3억 원 이하)</div></div>
</div>
{FT(3, True, '소득세법 시행령 제118조의4②')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">만기에 낸 돈보다 많이<br>돌려주는 저축성 보험도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">공제된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 만기환급금이 납입보험료<br><b style="font-weight:900">이하</b>인 보장성 보험만 돼요.</div>
{FT(4, True, '소득세법 제59조의4①')}</div>''',
# 5 타일
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4">연간 한도와 공제율</div><div style="font-size:100px;font-weight:900;letter-spacing:-4px;line-height:1.1;text-shadow:0 8px 20px rgba(120,0,40,.35)">100만 원씩</div></div>
<img class="ch" src="ch/smile-calc.svg" style="right:30px;top:120px;width:360px">
<div class="rows" style="top:520px">
 <div class="row"><div class="ic" style="background:#ff5c8a">일반</div><div class="tx">보장성보험 <span style="color:#e83e6f">12%</span></div></div>
 <div class="row"><div class="ic" style="background:#7a5cff">장애</div><div class="tx">장애인전용 <span style="color:#5a3fd6">15%</span></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:900px;font-size:30px">· 두 한도는 <b style="color:#fff3c4">따로</b> 적용돼요.<br>· 근로소득자만 받을 수 있어요.</div>
{FT(5, True, '소득세법 제59조의4①')}</div>''',
# 6 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">실손·자동차·전세보증 + 장애인전용 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">얼마나 돌려받나?</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>일반 100만 × 12%</small><b style="color:#1b5fa8">12만</b></div><div class="op">+</div><div class="bx"><small>장애인 100만 × 15%</small><b style="color:#ff5c8a">15만</b></div></div>
<div class="total" style="top:610px"><small>보험료 세액공제</small><b>27만 원</b><span>한도 넘은 금액은 공제 안 돼요</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">포인트</b><br>· 일반 110만 원 중 100만 원만<br>· 장애인전용 120만 원 중 100만 원만</div>
{FT(6, True, '소득세법 제59조의4①')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '연말정산 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">보험료</span> 확인!'),
]
