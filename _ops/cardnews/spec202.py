import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 202
SLUG = 'inheritance-donated-to-state-tax-free'
CAT = '상속세'
DATE = '2026-11-27'
TITLE = '상속받은 땅을 시청·국가에 기부하신다면 — 상속세 신고기한 안에 증여하면 그 재산은 상속세가 없습니다, 국가·지자체·정당·사내근로복지기금 유증과 불우이웃 유증도 비과세'
DESC = '상속재산 중 상속인이 상속세 신고기한까지 국가·지방자치단체·공공단체에 증여한 재산, 피상속인이 국가·지자체·공공단체·정당·사내근로복지기금 등에 유증한 재산, 불우한 자를 돕기 위해 유증한 재산에는 상속세를 부과하지 않습니다. 상속세 및 증여세법 제12조, 같은 법 시행령 제8조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '상속세 및 증여세법 제12조제1호·제4호·제5호·제6호·제7호, 같은 법 시행령 제8조, 같은 법 제26조'
TAGS = ['상속세비과세', '국가기부', '유증', '상속재산기부', '상속세', '부산세무사']
ALTS = ['상속재산 국가 기부 비과세 (표지)', '상속재산 국가 기부 비과세 (상담 질문)', '상속재산 국가 기부 비과세 (비과세 재산)', '상속재산 국가 기부 비과세 (O·X 퀴즈)', '상속재산 국가 기부 비과세 (세금 차이)', '상속재산 국가 기부 비과세 (확인할 점)', '상속재산 국가 기부 비과세 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
상속재산 중에는 상속인이 쓰기 어려운 재산이 있습니다. 도로나 공원 부지로 쓰이고 있는 땅, 마을 공터처럼 사실상 공공용으로 쓰이는 땅이 대표적입니다. 이런 재산을 "아버지 뜻에 따라 시청에 기부하겠다"고 하시는 분들께 꼭 알려 드리는 규정이 있습니다. <b>상속세 신고기한 안에 국가·지방자치단체에 증여하면, 그 재산에는 상속세가 없습니다</b>. 기한이 지나서 기부하면 상속세는 그대로 내야 하니 시기가 중요합니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>상속인이 <b>상속세 신고기한까지</b> 국가·지방자치단체·공공단체에 증여한 상속재산은 <b>상속세 비과세</b>입니다.</li><li>돌아가신 분이 국가·지자체·공공단체·<b>정당</b>·<b>사내근로복지기금</b> 등에 <b>유증</b>한 재산, <b>불우한 이웃</b>을 돕기 위해 유증한 재산도 비과세입니다.</li><li>상속세 신고기한은 상속개시일이 속하는 달의 말일부터 <b>6개월</b>(국외 주소 9개월)이므로 그 안에 기부를 마쳐야 합니다.</li></ol>
<div class="small" style="margin-top:8px">(상속세 및 증여세법 제12조, 같은 법 시행령 제8조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"아버지 땅 중에 30년째 마을 도로로 쓰이는 땅이 있어요. 어차피 쓸 수도 없으니 시청에 기부하려고 하는데, 상속세는 내야 하나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>한○○ 님(가칭)의 아버지가 돌아가시면서 <b>30억 원</b>의 재산을 남기셨고, 상속인은 자녀들뿐입니다. 이 중 3억 원은 오래전부터 마을 도로로 쓰이고 있는 땅입니다. 자녀들은 상속세 신고기한 안에 이 땅을 <b>시청에 기부(증여)</b>하기로 했습니다. 이 경우 3억 원은 상속세 과세 대상에서 빠집니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 상속세가 없는 재산(비과세)</h2>
<div class="tbl"><table>
<tr><th>비과세 재산</th><th>근거</th></tr>
<tr><td>상속재산 중 상속인이 <b>신고기한까지</b> 국가·지방자치단체·공공단체에 <b>증여한 재산</b></td><td>법 제12조제7호</td></tr>
<tr><td>국가·지방자치단체·공공단체에 <b>유증</b>(사인증여 포함)한 재산 — 공공단체: 지방자치단체조합, 공공도서관·공공박물관 등</td><td>법 제12조제1호, 시행령 제8조제1항</td></tr>
<tr><td>「정당법」에 따른 <b>정당</b>에 유증한 재산</td><td>법 제12조제4호</td></tr>
<tr><td><b>사내근로복지기금</b>, 우리사주조합, 공동근로복지기금, 근로복지진흥기금에 유증한 재산</td><td>법 제12조제5호, 시행령 제8조제4항</td></tr>
<tr><td>사회통념상 인정되는 이재구호금품·치료비, <b>불우한 자를 돕기 위하여 유증한 재산</b></td><td>법 제12조제6호, 시행령 제8조제5항</td></tr>
<tr><td>금양임야·묘토(합계 2억 원)와 족보·제구(1천만 원) 등 제사용 재산</td><td>법 제12조제3호, 시행령 제8조제3항(<a href="/column/100-ancestral-ritual-property-exemption.html">칼럼 100</a>)</td></tr>
</table></div>
<p>장학재단·복지법인 같은 <b>공익법인</b>에 출연하는 것은 비과세가 아니라 별도의 <b>과세가액 불산입</b> 규정(요건·사후관리 있음)이 적용됩니다. 이 부분은 <a href="/column/80-public-interest-donation-inheritance.html">칼럼 80</a>에 정리해 두었습니다.</p>

<h2>2. 한○○ 님 사례 — 기부 여부에 따른 상속세</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>기부하지 않을 때</th><th>신고기한 안에 시청에 기부</th></tr>
<tr><td>상속재산가액</td><td>3,000,000,000</td><td>3,000,000,000</td></tr>
<tr><td>비과세(국가·지자체 증여)</td><td>−</td><td>△300,000,000</td></tr>
<tr><td>상속세 과세가액</td><td>3,000,000,000</td><td>2,700,000,000</td></tr>
<tr><td>상속공제(일괄공제)</td><td>△500,000,000</td><td>△500,000,000</td></tr>
<tr><td>과세표준</td><td>2,500,000,000</td><td>2,200,000,000</td></tr>
<tr><td>상속세 산출세액</td><td>840,000,000</td><td><b>720,000,000</b></td></tr>
</table></div>
<p>쓰기 어려운 땅 3억 원을 신고기한 안에 기부하면 상속세 산출세액이 <b>1억 2천만 원</b> 줄어듭니다. 반대로 기한이 지난 뒤 기부하면 이 땅까지 포함해 상속세를 내야 합니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 배우자 없이 자녀들만 상속하고, 채무·장례비·금융재산공제·사전증여재산은 없으며, 상속공제는 일괄공제 5억 원만 적용했다고 가정했습니다. 세율은 상속세 및 증여세법 제26조를 적용했고 신고세액공제는 반영하지 않았습니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 상속재산 중 도로·공원 등 <b>공공용으로 쓰이는 땅</b>이 있는지 확인했다.</li>
<li>☐ 기부받을 곳이 <b>국가·지방자치단체·공공단체</b>인지 확인했다(공익법인은 별도 규정).</li>
<li>☐ 상속세 <b>신고기한</b>(상속개시일이 속하는 달의 말일부터 6개월) 안에 기부 절차를 마칠 수 있도록 미리 담당 부서와 협의했다.</li>
<li>☐ 상속인이 여럿이면 기부할 재산을 누가 상속받아 기부할지 <b>분할 협의</b>를 먼저 정리했다.</li>
<li>☐ 유언으로 기부를 남기실 계획이라면 <b>유언장</b>에 받는 곳을 분명히 적어 두었다.</li>
</ul>
<p>기부는 좋은 뜻이지만, 시기와 절차를 놓치면 세금 혜택을 받지 못할 수 있습니다. 상속재산 중 기부를 생각하시는 재산이 있다면 신고기한 전에 편하게 상담해 주세요. 비과세 적용부터 상속세 신고까지 함께 챙겨 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>상속재산 목록·등기부등본·토지이용계획확인서</td><td>기부 대상 재산, 현황(도로·공원 등)</td></tr>
<tr><td>기부채납·증여 관련 지방자치단체 협의 서류</td><td>기부 완료 시기</td></tr>
<tr><td>유언장(있는 경우)</td><td>유증 여부, 받는 곳</td></tr>
<tr><td>가족관계증명서·상속재산 분할협의서</td><td>상속인, 기부할 상속인</td></tr>
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
<img class="ch" src="ch/smile-doc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">상속받은 땅, 시청에 기부하면</div><div class="t">상속세<br>안 내도 될까요?</div><div class="series">상속세 절세 series 6편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">상속인분들이 묻는 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">한○○ 님</div><div class="say">마을 도로로 쓰는 땅,<br><span class="mk">시청에 기부</span>하면<br>상속세는요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px"><span class="hl">신고기한 안에</span><br>기부하면<br>비과세예요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">비과세 재산은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">상속세가 없는 재산</div><div class="h1" style="margin-top:8px">이런 기부·유증</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">신고기한 안에<br><span style="color:#1f8a57">국가·지자체에 증여</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">국가·지자체·정당·<br><span style="color:#1b5fa8">사내근로복지기금</span> 유증</div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx"><span style="color:#c0392b">불우한 이웃</span>을 돕는<br>유증</div></div>
</div>
{FT(3, True, '상증법 제12조·시행령 제8조')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">상속세를 다 낸 뒤<br>1년 후에 기부해도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">상속세가 돌아온다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-calc.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 상속세 <b style="font-weight:900">신고기한까지</b><br>증여해야 비과세예요.</div>
{FT(4, True, '상증법 제12조제7호')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">상속재산 30억 원 · 자녀만 상속 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">도로 땅 3억 기부</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>기부 안 하면</small><b style="color:#ff5c8a">8.4억</b></div><div class="op">vs</div><div class="bx"><small>기한 내 기부</small><b style="color:#2fa36b">7.2억</b></div></div>
<div class="total" style="top:610px"><small>줄어드는 상속세(산출세액)</small><b>1억 2천만 원</b><span>40% 세율 구간에서 3억 원 제외</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 일괄공제 5억 원만 적용<br>· 신고세액공제 반영 전</div>
{FT(5, True, '상증법 제12조·제26조')}</div>''',
# 6 확인
f'''<div class="c bg-orange">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">기부 전에</div><div class="h1" style="margin-top:8px">꼭 확인하세요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">신고기한<br><span style="color:#c0392b">말일부터 6개월</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">받는 곳이<br><span style="color:#b9770e">국가·지자체</span>인지</div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">공익법인 출연은<br><span style="color:#1b5fa8">별도 규정</span></div></div>
</div>
{FT(6, True, '상증법 제12조·제16조·제67조')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '상속재산 기부 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">기한</span> 확인!'),
]
