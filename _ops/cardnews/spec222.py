import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 222
SLUG = 'amended-return-penalty-reduction'
CAT = '양도소득세'
DATE = '2026-11-27'
TITLE = '양도세를 적게 신고한 걸 뒤늦게 아셨다면 — 수정신고는 빠를수록 좋습니다, 신고기한 후 1개월 안이면 과소신고가산세 90% 감면, 2년 안까지 단계별 감면, 세무서가 먼저 찾으면 감면 없음'
DESC = '법정신고기한까지 신고했지만 세액을 적게 신고했다면, 세무서가 결정·경정하기 전에 수정신고할 수 있습니다. 수정신고하면 과소신고가산세(일반 10%)를 신고기한 후 1개월 이내 90%, 3개월 이내 75%, 6개월 이내 50%, 1년 이내 30%, 1년 6개월 이내 20%, 2년 이내 10% 감면합니다. 납부지연가산세는 하루 10만분의 22씩 붙으므로 빨리 낼수록 줄어듭니다. 국세기본법 제45조·제47조의3·제47조의4·제48조, 같은 법 시행령 제27조의4 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '국세기본법 제45조·제47조의3·제47조의4·제48조제2항, 같은 법 시행령 제27조의4'
TAGS = ['수정신고', '과소신고가산세', '가산세감면', '납부지연가산세', '양도소득세', '부산세무사']
ALTS = ['수정신고 가산세 감면 (표지)', '수정신고 가산세 감면 (상담 질문)', '수정신고 가산세 감면 (감면율)', '수정신고 가산세 감면 (O·X 퀴즈)', '수정신고 가산세 감면 (사례 비교)', '수정신고 가산세 감면 (확인할 점)', '수정신고 가산세 감면 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"양도세 예정신고를 했는데, 필요경비로 넣으면 안 되는 비용을 넣었더라고요. 그냥 두면 모르고 넘어가지 않을까요?" 이런 고민 상담을 받으면 저는 <b>"지금 바로 수정신고하시는 게 가장 싸게 끝나는 방법"</b>이라고 말씀드립니다. 세법은 스스로 바로잡는 분께 <b>가산세를 크게 깎아 주고</b>, 세무서가 먼저 찾아내면 <b>감면이 없기</b> 때문입니다. 오늘은 수정신고와 가산세 감면을 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>신고기한까지 신고했지만 세금을 적게 신고했다면, 세무서가 <b>결정·경정하기 전</b>까지 <b>수정신고</b>할 수 있습니다.</li><li>수정신고하면 과소신고가산세(일반 <b>10%</b>)를 신고기한 후 <b>1개월 이내 90%</b>, 3개월 이내 75%, 6개월 이내 50%, 1년 이내 30%, 1년 6개월 이내 20%, <b>2년 이내 10%</b> 감면합니다.</li><li>납부지연가산세는 <b>하루 10만분의 22</b>씩 늘어나므로, 수정신고와 함께 빨리 납부할수록 줄어듭니다. 세무서가 경정할 것을 <b>미리 알고</b> 수정신고하면 감면이 없습니다.</li></ol>
<div class="small" style="margin-top:8px">(국세기본법 제45조·제47조의3·제47조의4·제48조제2항, 같은 법 시행령 제27조의4 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"양도세 예정신고 때 경비를 잘못 넣어서 세금을 2천만 원 적게 냈어요. 지금 고쳐도 될까요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>장○○ 님(가칭)은 2026년 5월에 상가를 팔고 예정신고기한인 <b>7월 31일</b>까지 양도소득세를 신고·납부하셨습니다. 그런데 필요경비가 아닌 비용을 넣어 세금을 <b>2,000만 원</b> 적게 신고한 사실을 뒤늦게 알게 되셨습니다. 부정행위가 아닌 단순 착오라면 과소신고가산세는 2,000만 원의 <b>10%인 200만 원</b>이 기준입니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 수정신고와 가산세 기본 구조</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>수정신고</td><td>신고기한까지 신고한 사람(기한 후 신고한 사람 포함)이 세액을 적게 신고했을 때, 세무서가 <b>결정·경정해 통지하기 전</b>으로서 부과제척기간이 끝나기 전까지 제출</td><td>국기법 제45조</td></tr>
<tr><td>과소신고가산세</td><td>적게 신고한 세액의 <b>10%</b>(부정행위로 적게 신고한 부분은 <b>40%</b>)</td><td>국기법 제47조의3</td></tr>
<tr><td>납부지연가산세</td><td>덜 낸 세액 × 법정납부기한 다음 날부터 납부일(고지일) 전날까지 일수 × <b>1일 10만분의 22</b></td><td>국기법 제47조의4, 시행령 제27조의4</td></tr>
</table></div>

<h2>2. 수정신고 시기별 과소신고가산세 감면율</h2>
<div class="tbl"><table>
<tr><th>법정신고기한이 지난 후 수정신고 시기</th><th>감면율</th></tr>
<tr><td>1개월 이내</td><td><b>90%</b></td></tr>
<tr><td>1개월 초과 3개월 이내</td><td>75%</td></tr>
<tr><td>3개월 초과 6개월 이내</td><td>50%</td></tr>
<tr><td>6개월 초과 1년 이내</td><td>30%</td></tr>
<tr><td>1년 초과 1년 6개월 이내</td><td>20%</td></tr>
<tr><td>1년 6개월 초과 2년 이내</td><td>10%</td></tr>
</table></div>
<p>감면은 <b>과소신고가산세에만</b> 적용되고 납부지연가산세는 감면되지 않습니다. 또 세무서가 과세표준과 세액을 <b>경정할 것을 미리 알고</b> 수정신고한 경우는 감면에서 제외됩니다(국기법 제48조제2항제1호). 양도세 <b>예정신고</b>를 적게 했더라도 <b>확정신고기한까지</b> 수정신고하면, 6개월이 지났더라도 과소신고가산세의 <b>50%</b>를 감면받습니다(같은 항 제3호다목). 신고 자체를 하지 않은 경우의 기한 후 신고 감면은 <a href="/column/53-inheritance-tax-late-filing.html">칼럼 53</a>을 참고해 주세요.</p>

<h2>3. 장○○ 님 사례 — 언제 바로잡느냐에 따른 가산세 비교</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>8월 20일 수정신고·납부<br>(1개월 이내)</th><th>10월 30일 수정신고·납부<br>(3개월 이내)</th><th>세무서가 찾아 2027년 11월 30일 고지</th></tr>
<tr><td>과소신고가산세</td><td>200,000<br><span class="small">(200만 × 10%)</span></td><td>500,000<br><span class="small">(200만 × 25%)</span></td><td>2,000,000</td></tr>
<tr><td>납부지연가산세</td><td>83,600<br><span class="small">(19일)</span></td><td>396,000<br><span class="small">(90일)</span></td><td>2,138,400<br><span class="small">(486일)</span></td></tr>
<tr><td>가산세 합계</td><td><b>283,600</b></td><td>896,000</td><td><b>4,138,400</b></td></tr>
</table></div>
<p>같은 2,000만 원이라도 바로 고치면 가산세가 <b>약 28만 원</b>, 세무서가 먼저 찾으면 <b>약 414만 원</b>입니다. 늦어질수록 납부지연가산세가 날마다 붙는다는 점도 기억해 주세요.</p>
<p class="small">※ python으로 계산·검산했습니다. 부정행위가 없는 일반 과소신고로 가정했고, 납부지연가산세는 법정납부기한(7월 31일) 다음 날부터 납부일(고지일) 전날까지의 일수에 1일 10만분의 22를 적용했습니다. 지방소득세와 그 가산세는 별도이며 반영하지 않았습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 신고서의 양도가액·취득가액·필요경비를 증빙과 하나하나 다시 맞춰 봤다.</li>
<li>☐ 적게 신고한 사실을 알았다면 <b>신고기한 후 1개월</b>이 지나기 전인지 날짜를 확인했다.</li>
<li>☐ 수정신고와 함께 <b>추가 세액을 바로 납부</b>해 납부지연가산세를 줄였다.</li>
<li>☐ 예정신고분이라면 <b>확정신고기한</b>(다음 해 5월 31일)까지 고치는 방법도 확인했다.</li>
<li>☐ 지방소득세도 함께 수정신고했다.</li>
</ul>
<p>실수는 누구에게나 생길 수 있습니다. 중요한 것은 <b>먼저, 빨리</b> 바로잡는 것입니다. 신고 내용이 맞는지 걱정되신다면 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>당초 신고서·납부확인서</td><td>신고한 세액, 신고일</td></tr>
<tr><td>매매계약서·취득 관련 증빙</td><td>양도가액·취득가액</td></tr>
<tr><td>필요경비 영수증·세금계산서</td><td>인정되는 경비인지</td></tr>
<tr><td>세무서 안내문(받은 경우)</td><td>감면 가능 여부</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

_S217 = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec217.py'))

CARDS = [
# 1 표지
f'''<div class="c bg-night">{HD()}
<div class="bokeh" style="left:90px;top:220px;width:120px;height:120px;background:#9fc4ff;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:260px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">세금을 적게 신고했다면</div><div class="t">빨리 고칠수록<br>가산세 90% 감면</div><div class="series">양도세 절세 series 17편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#11684a">신고를 마친 분의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">장○○ 님</div><div class="say">경비를 잘못 넣었어요.<br><span class="mk">그냥 두면</span><br>모르지 않을까요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">지금 <span class="hl">수정신고</span>가<br>가장 싸게<br>끝나요!</div></div>
<img class="ch" src="ch/wink-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#11684a">얼마나 줄까요? →</div>
{FT(2, False)}</div>''',
# 3 목록(감면율)
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">신고기한이 지난 뒤</div><div class="h1" style="margin-top:8px">과소신고가산세 감면</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">90</div><div class="tx">1개월 이내<br><span style="color:#1f8a57">90% 감면</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">75</div><div class="tx">3개월 이내 75%<br><span style="color:#1b5fa8">6개월 이내 50%</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">30</div><div class="tx">1년 이내 30%<br><span style="color:#c0392b">2년 이내까지 10%</span></div></div>
</div>
{FT(3, True, '국세기본법 제48조②1')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">수정신고하면<br>납부지연가산세도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">90% 깎아 준다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 감면은 <b style="font-weight:900">과소신고가산세</b>만.<br>납부지연은 하루 10만분의 22씩 붙어요.</div>
{FT(4, True, '국세기본법 제47조의4·제48조')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">2천만 원 적게 신고 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">가산세 비교</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>1개월 내 수정</small><b style="color:#2fa36b">28만</b></div><div class="op">vs</div><div class="bx"><small>세무서 적발</small><b style="color:#ff5c8a">414만</b></div></div>
<div class="total" style="top:610px"><small>먼저 고치면 아끼는 가산세</small><b>약 385만 원</b><span>과소신고 + 납부지연 합계</span></div>
<img class="ch" src="ch/smile-piggy.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 부정행위 없는 단순 착오<br>· 지방소득세 별도</div>
{FT(5, True, '국세기본법 제47조의3·제47조의4')}</div>''',
# 6 확인
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">수정신고 전에 확인!</div><div class="h1" style="margin-top:8px">체크 포인트</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">세무서보다<br><span style="color:#c0392b">먼저 고치기</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">추가 세액<br><span style="color:#1b5fa8">바로 납부</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">③</div><div class="tx">예정신고분은<br><span style="color:#1f8a57">확정신고까지 50%</span></div></div>
</div>
{FT(6, True, '국세기본법 제45조·제48조②3')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '세무서보다 먼저').replace('<span class="hl">기한</span> 확인!', '<span class="hl">수정신고</span>!'),
]
