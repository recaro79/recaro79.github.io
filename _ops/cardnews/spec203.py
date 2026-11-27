import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 203
SLUG = 'unreported-sales-deemed-bonus-representative'
CAT = '법인세'
DATE = '2026-11-27'
TITLE = '법인 매출을 빠뜨리거나 회삿돈을 대표님이 쓰셨다면 — 법인세에 더해 대표님 상여(인정상여)로 소득세까지 나옵니다, 쓴 사람이 불분명하면 대표자 귀속, 수정신고기한 안에 회수하면 사내유보'
DESC = '법인세 신고·결정·경정으로 익금산입된 금액이 회사 밖으로 나갔으면 귀속자에 따라 배당·상여·기타사외유출·기타소득으로 처분하고, 귀속이 불분명하면 대표자에게 귀속된 것으로 보아 상여로 처분합니다. 대표자는 근로소득으로 소득세를 추가로 내야 합니다. 수정신고기한 내에 사외유출 금액을 회수하고 스스로 익금산입하면 사내유보로 처분합니다(세무조사 통지 등 경정을 미리 안 경우 제외). 법인세법 제67조, 같은 법 시행령 제106조, 소득세법 시행령 제134조·제192조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '법인세법 제67조, 같은 법 시행령 제106조제1항·제4항, 소득세법 제135조제4항·제131조제2항, 같은 법 시행령 제134조제1항·제192조제1항'
TAGS = ['인정상여', '소득처분', '매출누락', '법인세', '대표자상여', '부산세무사']
ALTS = ['인정상여 소득처분 (표지)', '인정상여 소득처분 (상담 질문)', '인정상여 소득처분 (누구에게 처분)', '인정상여 소득처분 (O·X 퀴즈)', '인정상여 소득처분 (세금 합계)', '인정상여 소득처분 (스스로 바로잡기)', '인정상여 소득처분 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
법인을 운영하시는 대표님들께서 가장 조심하셔야 할 부분이 <b>회삿돈과 개인 돈의 구분</b>입니다. 현금 매출을 신고에서 빠뜨리거나, 실제로 쓰지 않은 비용을 넣어 회삿돈을 개인적으로 쓰시면 세무조사에서 <b>법인세</b>만 추징되는 것이 아닙니다. 그 돈이 대표님께 간 것으로 보아 <b>상여(인정상여)</b>로 처분되고, 대표님은 <b>근로소득세</b>까지 추가로 내셔야 합니다. 오늘은 이 "소득처분" 규정을 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>법인세 계산에서 익금에 더한 금액이 회사 밖으로 나갔으면 받은 사람에 따라 <b>배당·상여·기타사외유출·기타소득</b>으로 처분합니다.</li><li>누가 가져갔는지 <b>불분명하면 대표자</b>에게 간 것으로 보아 <b>상여</b>로 처분하므로, 대표님 근로소득세가 늘어납니다.</li><li>수정신고기한 안에 빠져나간 돈을 <b>회수</b>하고 스스로 익금산입해 신고하면 <b>사내유보</b>로 처분합니다(세무조사 통지 등을 받은 뒤는 제외).</li></ol>
<div class="small" style="margin-top:8px">(법인세법 제67조, 같은 법 시행령 제106조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"현금으로 받은 매출 일부를 신고하지 않고 운영비로 썼는데, 세무조사에서 걸리면 법인세만 더 내면 되는 거죠?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>(주)○○(가칭, 12월 결산)은 현금 매출 <b>1억 원</b>(공급가액)을 신고하지 않았고, 그 돈은 어디에 썼는지 장부로 확인되지 않습니다. 세무조사에서 이 사실이 드러나면, 법인세 과세표준에 1억 원이 더해지고(익금산입), 귀속이 불분명하므로 <b>대표자 상여</b>로 처분됩니다. 대표님의 기존 종합소득 과세표준은 1억 2천만 원, 법인의 기존 과세표준은 3억 원이라고 가정하겠습니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 소득처분 — 누구에게 무엇으로</h2>
<div class="tbl"><table>
<tr><th>빠져나간 돈이 간 곳</th><th>처분</th><th>근거</th></tr>
<tr><td>주주(임직원이 아닌 주주)</td><td><b>배당</b></td><td>시행령 제106조제1항제1호가목</td></tr>
<tr><td>임원 또는 직원</td><td><b>상여</b></td><td>같은 호 나목</td></tr>
<tr><td>법인이나 사업하는 개인(그의 사업소득 등을 구성하는 경우)</td><td>기타사외유출</td><td>같은 호 다목</td></tr>
<tr><td>그 밖의 사람</td><td>기타소득</td><td>같은 호 라목</td></tr>
<tr><td><b>귀속이 불분명</b></td><td><b>대표자 상여</b>(지분 30% 이상 임원이 사실상 경영을 지배하면 그 사람을 대표자로 봄)</td><td>같은 호 단서</td></tr>
<tr><td>회사 밖으로 나가지 않음</td><td>사내유보</td><td>같은 항 제2호</td></tr>
</table></div>

<h2>2. 상여 처분 뒤 이렇게 진행됩니다</h2>
<div class="tbl"><table>
<tr><th>단계</th><th>내용</th><th>근거</th></tr>
<tr><td>소득금액변동통지</td><td>세무서가 법인세를 결정·경정한 날부터 15일 안에 법인에 <b>소득금액변동통지서</b>를 보냄</td><td>소득세법 시행령 제192조제1항</td></tr>
<tr><td>원천징수</td><td>법인은 통지서를 받은 날에 상여를 지급한 것으로 보아 <b>근로소득세를 원천징수</b>해 납부</td><td>소득세법 제135조제4항·제131조제2항</td></tr>
<tr><td>대표자 추가신고</td><td>통지서를 받은 날이 속하는 달의 <b>다음다음 달 말일</b>까지 종합소득세를 추가신고·납부하면 기한 내 신고·납부로 봄</td><td>소득세법 시행령 제134조제1항·제6항·제7항</td></tr>
</table></div>

<h2>3. (주)○○ 사례 — 1억 원 매출 누락의 세금</h2>
<div class="tbl"><table>
<tr><th>세목</th><th>늘어나는 세금(지방세 포함)</th></tr>
<tr><td>법인세(과세표준 3억 → 4억, 20% 구간)</td><td>20,000,000 (법인지방소득세 포함 22,000,000)</td></tr>
<tr><td>대표자 근로소득세(과세표준 1.2억 → 2.2억)</td><td>37,100,000 (지방소득세 포함 40,810,000)</td></tr>
<tr><td>부가가치세(공급가액 1억 원 × 10%)</td><td>10,000,000</td></tr>
<tr><td><b>합계(가산세 제외)</b></td><td><b>72,810,000</b></td></tr>
</table></div>
<p>1억 원을 빠뜨리고 실제로는 <b>7,281만 원</b>의 세금이 생깁니다. 여기에 법인세·부가세·원천세의 <b>신고불성실·납부지연 가산세</b>가 따로 더해지고, 부정행위로 판단되면 가산세율도 높아집니다. 대표님이 상여 소득세를 법인 돈으로 대신 내주면 그 금액은 다시 법인 비용으로 인정되지 않습니다(시행령 제106조제1항제3호아목).</p>
<p class="small">※ python으로 계산·검산했습니다. 법인세는 2026년 1월 1일 이후 시작 사업연도 세율(법인세법 제55조), 소득세는 소득세법 제55조 기본세율을 적용했고, 지방소득세는 각 세액의 10%로 단순 가정했습니다. 가산세·세액공제·감면은 반영하지 않았습니다.</p>

<h2>4. 스스로 바로잡으면 — 사내유보</h2>
<p>법인이 <b>수정신고기한 안에</b> 매출누락·가공경비 등으로 빠져나간 금액을 <b>회수</b>하고, 세무조정으로 익금산입해 신고하면 대표자 상여가 아니라 <b>사내유보</b>로 처분합니다(시행령 제106조제4항). 다만 <b>세무조사 통지</b>를 받았거나, 세무조사 착수를 알게 되었거나, 과세자료 <b>해명 통지</b>를 받은 뒤 등 경정이 있을 것을 미리 알고 한 경우에는 적용되지 않습니다. 결국 <b>빨리 알아채고 먼저 바로잡는 것</b>이 가장 좋은 방법입니다.</p>

<h2>5. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 현금·계좌이체 매출이 <b>빠짐없이</b> 신고되었는지 매달 확인했다.</li>
<li>☐ 대표님 개인 지출이 법인 카드·법인 계좌로 처리되지 않았는지 확인했다(<a href="/column/47-household-expense-disallowance.html">칼럼 47</a>).</li>
<li>☐ 대표님이 가져간 돈은 <b>가지급금</b>으로 처리하고 이자·상환 계획을 세웠다(<a href="/column/10-provisional-payment-interest.html">칼럼 10</a>).</li>
<li>☐ 잘못을 발견했다면 세무조사 통지 <b>전에</b> 회수하고 수정신고를 검토했다.</li>
<li>☐ 소득금액변동통지서를 받았다면 원천세 납부와 대표자 추가신고 기한을 바로 달력에 표시했다.</li>
</ul>
<p>법인 돈의 흐름은 장부로 설명할 수 있어야 합니다. 걱정되는 거래가 있다면 문제가 커지기 전에 편하게 상담해 주세요. 수정신고 여부부터 세금 부담까지 함께 검토해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>법인 통장 거래내역·현금출납부</td><td>누락 매출, 대표자 인출</td></tr>
<tr><td>법인세·부가세 신고서</td><td>수정신고 대상, 기한</td></tr>
<tr><td>가지급금 명세·대여 약정서</td><td>사외유출 여부, 회수 계획</td></tr>
<tr><td>세무서 안내문·통지서(받은 경우)</td><td>사내유보 가능 여부, 대응 기한</td></tr>
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
<img class="ch" src="ch/wow-magnify-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">빠뜨린 매출, 대표님이 쓴 회삿돈</div><div class="t">법인세로<br>끝이 아닙니다</div><div class="series">법인세 절세 series 5편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">대표님들이 묻는 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">대표님</div><div class="say">빠뜨린 매출,<br>걸리면 <span class="mk">법인세만</span><br>더 내면 되죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">대표님 <span class="hl">상여</span>로<br>소득세까지<br>나와요!</div></div>
<img class="ch" src="ch/worry-calc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">왜 그럴까요? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">빠져나간 돈은 누구에게?</div><div class="h1" style="margin-top:8px">소득처분</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">주주에게 →<br><span style="color:#1f8a57">배당</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">임원·직원에게 →<br><span style="color:#1b5fa8">상여</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">모르면 →<br><span style="color:#c0392b">대표자 상여</span></div></div>
</div>
{FT(3, True, '법인세법 제67조·시행령 제106조①')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">조사 통지를 받은 뒤<br>돈을 돌려놓으면<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">상여 처분이 없다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 조사 통지 <b style="font-weight:900">전에</b><br>회수·수정신고해야 사내유보예요.</div>
{FT(4, True, '법인세법 시행령 제106조④')}</div>''',
# 5 타일
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4">매출 1억 원 누락 (가상 사례)</div><div style="font-size:96px;font-weight:900;letter-spacing:-4px;line-height:1.1;text-shadow:0 8px 20px rgba(120,0,40,.35)">세금 7,281만</div></div>
<div class="rows" style="top:420px">
 <div class="row"><div class="ic" style="background:#ff5c8a">법인</div><div class="tx">법인세 <span style="color:#e83e6f">2,200만 원</span></div></div>
 <div class="row"><div class="ic" style="background:#ff9a3c">대표</div><div class="tx">근로소득세 <span style="color:#e8761e">4,081만 원</span></div></div>
 <div class="row"><div class="ic" style="background:#7a5cff">부가</div><div class="tx">부가가치세 <span style="color:#5a3fd6">1,000만 원</span></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:1000px;font-size:30px">· 지방소득세 포함, <b style="color:#fff3c4">가산세는 별도</b>예요.</div>
{FT(5, True, '법인세법·소득세법 제55조')}</div>''',
# 6 바로잡기
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">먼저 바로잡으면</div><div class="h1" style="margin-top:8px">사내유보</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">수정신고기한 안에<br><span style="color:#1f8a57">돈을 회수</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">스스로<br><span style="color:#1b5fa8">익금산입 신고</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">조사 통지·해명 요구<br><span style="color:#c0392b">받기 전</span>이어야</div></div>
</div>
{FT(6, True, '법인세법 시행령 제106조④')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '문제가 커지기 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">먼저</span> 상담!'),
]
