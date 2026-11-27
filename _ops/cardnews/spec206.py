import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 206
SLUG = 'disabled-dependent-deduction-medical-certificate'
CAT = '종합소득세'
DATE = '2026-11-27'
TITLE = '희귀난치병 등으로 계속 치료받는 가족이 있다면 — 장애인등록이 없어도 병원 장애인증명서로 장애인 공제, 나이 제한 없이 기본공제 150만 원 + 추가공제 200만 원, 의료비는 한도 없이 공제'
DESC = '희귀성난치질환 등 또는 이와 유사한 질병·부상으로 중단 없이 주기적인 치료가 필요하고 의료기관의 장이 일상생활에 지장이 있다고 인정한 사람은 세법상 장애인입니다. 장애인 부양가족은 나이 제한 없이(소득 요건은 적용) 기본공제 150만 원과 장애인 추가공제 200만 원을 받고, 의료비 세액공제는 700만 원 한도가 적용되지 않습니다. 소득세법 제50조·제51조·제59조의4, 같은 법 시행령 제107조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제50조제1항제3호, 제51조제1항제2호, 제59조의4제2항, 같은 법 시행령 제107조제1항·제2항·제3항'
TAGS = ['장애인공제', '장애인증명서', '희귀난치질환', '연말정산', '의료비세액공제', '부산세무사']
ALTS = ['장애인 공제 (표지)', '장애인 공제 (상담 질문)', '장애인 공제 (세법상 장애인)', '장애인 공제 (O·X 퀴즈)', '장애인 공제 (공제 혜택)', '장애인 공제 (세금 차이)', '장애인 공제 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
연말정산에서 많이 놓치는 공제 중 하나가 <b>장애인 공제</b>입니다. "우리 가족은 장애인등록을 하지 않았으니 해당 없다"고 생각하시기 쉽지만, 세법상 장애인은 장애인복지법상 등록 장애인보다 범위가 넓습니다. <b>희귀난치성 질환 등으로 계속 치료를 받으며 일상생활이 어려운 가족</b>은 병원에서 <b>장애인증명서</b>를 받아 공제를 받을 수 있습니다. 부모님 연세가 60세가 안 되셔도 받을 수 있다는 점이 특히 중요합니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>희귀성난치질환 등 또는 <b>이와 유사한 질병·부상</b>으로 중단 없이 주기적인 치료가 필요하고, <b>의료기관의 장</b>이 일상생활에 지장이 있다고 인정한 사람은 세법상 <b>장애인</b>입니다.</li><li>장애인 부양가족은 <b>나이 제한 없이</b>(소득 100만 원 이하 요건은 적용) 기본공제 <b>150만 원</b> + 장애인 추가공제 <b>200만 원</b>을 받습니다.</li><li>장애인을 위해 낸 <b>의료비</b>는 연 700만 원 한도 없이 공제되고, 장애인전용보장성보험료·특수교육비 공제도 있습니다.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제50조·제51조·제59조의4, 같은 법 시행령 제107조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"아버지가 55세신데 희귀질환으로 몇 년째 치료를 받고 계세요. 60세가 안 되셔서 부양가족 공제는 안 된다고 들었는데 정말 방법이 없나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>직장인 권○○ 님(가칭, 총급여 7천만 원)은 함께 사는 아버지(55세, 소득 없음)의 치료비로 올해 <b>1,500만 원</b>을 내셨습니다. 아버지는 희귀질환으로 중단 없이 주기적인 치료를 받고 계시고, 담당 병원에서 일상생활에 지장이 있다는 <b>장애인증명서</b>를 발급받을 수 있습니다. 이 경우 아버지는 60세 미만이어도 <b>장애인 부양가족</b>으로 공제를 받을 수 있습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 세법상 장애인은 누구일까요</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>증빙</th></tr>
<tr><td>장애인복지법상 장애인 등</td><td>「장애인복지법」에 따른 장애인, 「장애아동 복지지원법」에 따른 장애아동 중 일정한 사람</td><td>장애인등록증 사본 등</td></tr>
<tr><td>국가유공자 상이자 등</td><td>상이자 및 이와 유사한 사람으로서 근로능력이 없는 사람</td><td>상이자 증명서 등</td></tr>
<tr><td><b>치료가 계속 필요한 사람</b></td><td>희귀성난치질환등 또는 이와 유사한 질병·부상으로 <b>중단 없이 주기적인 치료</b>가 필요한 사람으로서 <b>의료기관의 장</b>이 취업·취학 등 일상적인 생활에 지장이 있다고 인정하는 사람</td><td>의료기관 발급 <b>장애인증명서</b></td></tr>
</table></div>
<p class="small">근거: 소득세법 시행령 제107조제1항·제2항. 장애 상태가 1년 이상 지속될 것으로 예상되어 <b>장애기간이 적힌 증명서</b>를 낸 경우 그 기간 동안은 다시 내지 않아도 됩니다(다만 회사나 관할 세무서가 바뀌면 다시 제출, 시행령 제107조제3항).</p>

<h2>2. 장애인이면 받는 공제</h2>
<div class="tbl"><table>
<tr><th>공제</th><th>내용</th><th>근거</th></tr>
<tr><td>기본공제</td><td>1명당 150만 원 — 장애인 부양가족은 <b>나이 제한 없음</b>(연간 소득금액 100만 원 이하, 근로소득만 있으면 총급여 500만 원 이하 요건은 적용)</td><td>소득세법 제50조제1항제3호</td></tr>
<tr><td>장애인 추가공제</td><td>1명당 <b>200만 원</b></td><td>제51조제1항제2호</td></tr>
<tr><td>의료비 세액공제</td><td>장애인을 위해 지급한 의료비는 일반 가족의 <b>연 700만 원 한도 없이</b> 15% 공제(총급여 3% 기준 차감)</td><td>제59조의4제2항제2호</td></tr>
<tr><td>보험료 세액공제</td><td>장애인전용보장성보험료 연 100만 원 한도 15%</td><td>제59조의4제1항제1호</td></tr>
<tr><td>교육비 세액공제</td><td>장애인 재활교육 특수교육비 한도 없이 15%</td><td>제59조의4제3항제3호(<a href="/column/200-education-expense-tax-credit-2026.html">칼럼 200</a>)</td></tr>
</table></div>

<h2>3. 권○○ 님 사례 — 장애인 공제 전·후</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>장애인 공제 없이</th><th>장애인 공제 적용</th></tr>
<tr><td>인적공제(아버지)</td><td>0원(60세 미만)</td><td>350만 원(150만 + 200만)</td></tr>
<tr><td>인적공제에 따른 세금 감소(24% 구간 가정)</td><td>−</td><td>840,000</td></tr>
<tr><td>의료비 세액공제(1,500만 원 − 총급여 3% 210만 원)</td><td>1,050,000(700만 원 한도)</td><td>1,935,000(한도 없음)</td></tr>
<tr><td><b>장애인 공제로 늘어나는 혜택</b></td><td colspan="2"><b>1,725,000</b>(지방소득세 효과 별도)</td></tr>
</table></div>
<p class="small">※ python으로 계산·검산했습니다. 권○○ 님의 과세표준이 공제 전후 모두 24% 구간에 있고, 다른 의료비·실손보험금 수령액은 없으며, 산출세액이 세액공제액보다 충분히 크다고 가정했습니다. 의료비 세액공제는 기본공제대상자를 위한 의료비라면 나이·소득 제한이 없어 아버지가 장애인이 아니어도 700만 원 한도로 공제됩니다(소득세법 제59조의4제2항).</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 오랫동안 치료받는 가족이 있다면 담당 병원에 <b>소득세법상 장애인증명서</b> 발급이 가능한지 문의했다.</li>
<li>☐ 그 가족의 연간 <b>소득금액이 100만 원 이하</b>(근로소득만 있으면 총급여 500만 원 이하)인지 확인했다.</li>
<li>☐ 형제자매 중 <b>누가 공제받을지</b> 정해 한 사람만 신청했다(중복 공제 금지).</li>
<li>☐ 장애인증명서에 <b>장애기간</b>이 적혀 있는지 확인하고 보관했다.</li>
<li>☐ 지난 5년 동안 놓친 장애인 공제가 있다면 <b>경정청구</b>로 돌려받을 수 있는지 확인했다(<a href="/column/109-income-tax-refund-claim.html">칼럼 109</a>).</li>
</ul>
<p>장애인 공제는 증명서 한 장으로 해마다 수십만~수백만 원이 달라질 수 있는 공제입니다. 가족 중 해당하실 분이 있는지 궁금하시면 편하게 상담해 주세요. 지난 연도 환급 가능 여부까지 함께 확인해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>의료기관 발급 장애인증명서</td><td>장애 사유·장애기간</td></tr>
<tr><td>가족관계증명서·주민등록등본</td><td>부양 관계, 생계 같이 함</td></tr>
<tr><td>가족의 소득 자료</td><td>소득금액 100만 원 이하 여부</td></tr>
<tr><td>의료비 영수증·간소화 자료</td><td>의료비 세액공제 금액</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-pink">{HD()}
<div class="bokeh" style="left:90px;top:200px;width:120px;height:120px;background:#ffd3e0;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:250px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/smile-doc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">오래 치료받는 가족이 있다면</div><div class="t">장애인 공제<br>받으셨나요?</div><div class="series">종합소득세 절세 series 7편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">연말정산 상담 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">권○○ 님</div><div class="say">아버지가 <span class="mk">55세</span>라<br>부양가족 공제가<br>안 된대요</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px"><span class="hl">장애인증명서</span>가<br>있으면 나이와<br>상관없어요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">누가 해당될까? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">세법상 장애인</div><div class="h1" style="margin-top:8px">등록 장애인만이 아니에요</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx"><span style="color:#1f8a57">장애인복지법</span>상<br>장애인 등</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">국가유공자<br><span style="color:#1b5fa8">상이자</span> 등</div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">희귀난치질환 등 <span style="color:#c0392b">계속 치료</span><br>+ 병원장 인정</div></div>
</div>
{FT(3, True, '소득세법 시행령 제107조①')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">장애인 가족은<br>소득이 많아도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">기본공제가 된다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 나이 제한만 없어요.<br>소득 <b style="font-weight:900">100만 원 이하</b> 요건은 그대로예요.</div>
{FT(4, True, '소득세법 제50조①3호')}</div>''',
# 5 타일
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">장애인 부양가족 1명당</div><div class="h1" style="margin-top:8px">이런 공제가 있어요</div></div>
<div class="tiles" style="top:360px">
 <div class="tile wide t-red"><div class="who" style="font-size:36px">의료비 세액공제</div><div class="amt">한도 없음</div></div>
 <div class="tile t-blue"><div class="who">기본공제</div><div class="amt">150만<small>원</small></div></div>
 <div class="tile t-green"><div class="who">장애인 추가공제</div><div class="amt">200만<small>원</small></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:900px;font-size:30px;font-weight:600">· 장애인전용보장성보험 연 100만 원까지 15%<br>· 재활 특수교육비도 한도 없이 15%<br>· 기본공제는 나이 제한 없음(소득 요건 적용)</div>
{FT(5, True, '소득세법 제50조·제51조·제59조의4')}</div>''',
# 6 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">총급여 7천만 원 · 아버지 치료비 1,500만 원</div><div class="h1" style="font-size:62px;margin-top:6px">장애인 공제 효과</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>인적공제</small><b style="color:#1b5fa8">84만</b></div><div class="op">+</div><div class="bx"><small>의료비 추가</small><b style="color:#ff5c8a">88.5만</b></div></div>
<div class="total" style="top:610px"><small>늘어나는 세금 혜택</small><b>172만 5천 원</b><span>가상 사례 · 24% 구간 가정</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">포인트</b><br>· 의료비 700만 원 한도가 풀려요<br>· 지난 5년도 경정청구 가능</div>
{FT(6, True, '소득세법 제51조·제59조의4②')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '연말정산 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">증명서</span> 챙기세요!'),
]
