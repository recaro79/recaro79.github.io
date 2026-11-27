import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 221
SLUG = 'artwork-antique-sale-other-income-tax'
CAT = '종합소득세'
DATE = '2026-11-27'
TITLE = '집에 있던 그림·고미술품을 파신다면 — 한 점 6천만 원 이상이면 기타소득으로 세금을 냅니다, 받은 금액의 80~90%는 필요경비로 빼 주고 20% 세율로 분리과세, 생존 국내 작가 작품은 제외'
DESC = '양도가액이 개당·점당·조당 6천만 원 이상인 회화·판화·100년 넘은 골동품 등 서화·골동품을 양도하면 기타소득으로 과세됩니다. 양도일 현재 생존한 국내 원작자의 작품은 제외됩니다. 받은 금액이 1억 원 이하이면 90%, 1억 원 초과분은 80%(10년 이상 보유 시 90%)를 필요경비로 인정하고, 분리과세기타소득으로 20% 세율이 적용됩니다. 소득세법 제14조·제21조·제129조, 같은 법 시행령 제41조·제87조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제14조제3항제8호다목·제21조제2항·제129조제1항제6호라목, 같은 법 시행령 제41조제14항·제18항, 제87조제2호'
TAGS = ['서화골동품', '미술품양도', '기타소득', '분리과세', '종합소득세', '부산세무사']
ALTS = ['서화·골동품 양도 기타소득 (표지)', '서화·골동품 양도 기타소득 (상담 질문)', '서화·골동품 양도 기타소득 (대상)', '서화·골동품 양도 기타소득 (O·X 퀴즈)', '서화·골동품 양도 기타소득 (세금 계산)', '서화·골동품 양도 기타소득 (필요경비)', '서화·골동품 양도 기타소득 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"아버지가 오래 모으신 고서화를 경매에 내놓으려는데, 그림 팔아도 세금이 있나요?" 요즘 미술품 거래가 늘면서 이런 질문이 많아졌습니다. 그림이나 골동품은 부동산이 아니라 양도소득세 대상은 아니지만, <b>한 점에 6천만 원 이상</b>으로 팔면 <b>기타소득</b>으로 세금을 냅니다. 다행히 받은 금액의 <b>80~90%를 필요경비</b>로 빼 주기 때문에 실제 세 부담은 생각보다 크지 않습니다. 오늘은 그 계산 방법을 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>회화·판화·<b>100년 넘은 골동품</b> 등을 개당·점당·조당 <b>6천만 원 이상</b>에 팔면 기타소득입니다. 단, <b>양도일 현재 살아 계신 국내 작가</b>의 작품은 제외됩니다.</li><li>받은 금액 <b>1억 원까지 90%</b>, 1억 원 초과분은 <b>80%</b>(10년 이상 보유하면 <b>90%</b>)를 필요경비로 빼 줍니다. 실제 경비가 더 많으면 실제 경비를 뺍니다.</li><li>다른 소득과 합치지 않는 <b>분리과세</b>이며 세율은 <b>20%</b>입니다. 사업장을 갖추거나 사업자등록을 하고 거래하면 사업소득이 됩니다.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제14조제3항제8호·제21조제2항·제129조, 같은 법 시행령 제41조·제87조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"15년 동안 갖고 있던 고서화를 2억 원에 팔게 됐어요. 세금이 얼마나 나올까요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>윤○○ 님(가칭)은 <b>15년 전</b> 3천만 원에 산 조선시대 서화를 <b>2억 원</b>에 팔게 되었습니다. 제작된 지 100년이 넘은 골동품이고 원작자는 이미 고인이므로 과세 대상입니다. 윤○○ 님은 미술품 거래를 사업으로 하지 않는 개인입니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 과세 대상 서화·골동품</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>대상 물품</td><td>① 회화·데생·파스텔(손으로 그린 것) 및 콜라주와 유사한 장식판<br>② 오리지널 판화·인쇄화·석판화<br>③ 골동품(<b>제작 후 100년이 넘은 것</b>)<br>④ 그 밖에 역사상·예술상 가치가 있는 것으로 시행규칙에서 정한 것</td><td>시행령 제41조제14항</td></tr>
<tr><td>금액 기준</td><td>개당·점당 또는 조(짝을 이루어 거래되는 것)당 양도가액 <b>6천만 원 이상</b></td><td>같은 항</td></tr>
<tr><td>제외</td><td>양도일 현재 <b>생존해 있는 국내 원작자</b>의 작품</td><td>같은 항 단서</td></tr>
<tr><td>사업소득이 되는 경우</td><td>거래를 위해 사업장 등 물적 시설(온라인 가상 사업장 포함)을 갖추거나, 거래 목적으로 <b>사업자등록</b>을 한 경우</td><td>시행령 제41조제18항</td></tr>
</table></div>

<h2>2. 필요경비와 세율</h2>
<div class="tbl"><table>
<tr><th>받은 금액(양도가액)</th><th>필요경비</th></tr>
<tr><td>1억 원 이하</td><td>받은 금액의 <b>90%</b></td></tr>
<tr><td>1억 원 초과</td><td>9천만 원 + (받은 금액 − 1억 원) × <b>80%</b><br>보유기간 <b>10년 이상</b>이면 초과분도 <b>90%</b></td></tr>
<tr><td colspan="2">실제 들어간 필요경비가 위 금액보다 크면 실제 경비를 뺍니다(시행령 제87조제2호).</td></tr>
</table></div>
<p>이렇게 구한 기타소득금액은 <b>분리과세기타소득</b>으로 다른 종합소득과 합치지 않으며(소득세법 제14조제3항제8호다목), 원천징수세율은 <b>20%</b>입니다(같은 법 제129조제1항제6호라목). 지방소득세는 별도입니다.</p>

<h2>3. 윤○○ 님 사례 — 보유기간에 따른 세금 비교</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>15년 보유(실제)</th><th>만약 5년 보유였다면</th></tr>
<tr><td>받은 금액</td><td>200,000,000</td><td>200,000,000</td></tr>
<tr><td>필요경비</td><td>△180,000,000<br><span class="small">(9천만 + 1억 × 90%)</span></td><td>△170,000,000<br><span class="small">(9천만 + 1억 × 80%)</span></td></tr>
<tr><td>기타소득금액</td><td>20,000,000</td><td>30,000,000</td></tr>
<tr><td>소득세(20%)</td><td><b>4,000,000</b></td><td>6,000,000</td></tr>
<tr><td>지방소득세 포함 합계</td><td><b>4,400,000</b></td><td>6,600,000</td></tr>
</table></div>
<p>2억 원에 팔아도 세금은 <b>440만 원</b>입니다. 실제 취득가액 3천만 원보다 법정 필요경비(1억 8천만 원)가 훨씬 크기 때문입니다. 10년 이상 보유하면 1억 원 초과분의 필요경비율이 90%로 올라가 세금이 더 줄어듭니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 실제 필요경비(취득가액 3천만 원)가 법정 필요경비보다 적어 법정 필요경비를 적용했습니다. 지방소득세는 소득세의 10%로 계산했습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 파는 작품 한 점(또는 한 조)의 가격이 <b>6천만 원 이상</b>인지 확인했다.</li>
<li>☐ 원작자가 <b>생존한 국내 작가</b>인지, 골동품이면 <b>제작 후 100년</b>이 넘었는지 확인했다.</li>
<li>☐ <b>취득일</b>을 증명할 자료(구입 영수증·경매 낙찰 확인서 등)로 10년 보유 여부를 확인했다.</li>
<li>☐ 실제 취득가액·수선비 등이 법정 필요경비보다 큰지 비교했다.</li>
<li>☐ 미술품 거래를 반복하면서 사업장이나 사업자등록을 갖추고 있지 않은지(사업소득 해당 여부) 확인했다.</li>
</ul>
<p>미술품은 상속·증여 때도 감정이 필요한 재산입니다. 팔기 전에 세금과 신고 방법을 함께 점검해 보시면 좋겠습니다. 상속·증여 시 감정평가수수료 공제는 <a href="/column/158-appraisal-fee-deduction.html">칼럼 158</a>을 참고해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>작품 정보(작가·제작 연도·감정서)</td><td>과세 대상 여부</td></tr>
<tr><td>구입 영수증·낙찰 확인서·상속·증여 서류</td><td>취득일·취득가액(보유기간)</td></tr>
<tr><td>매매(위탁)계약서·경매 정산서</td><td>받은 금액, 원천징수 여부</td></tr>
<tr><td>최근 거래 내역</td><td>사업성(반복 거래) 여부</td></tr>
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
<img class="ch" src="ch/wow-magnify.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">그림·고미술품을 파신다면</div><div class="t">6천만 원 이상<br>기타소득 과세</div><div class="series">종합소득세 절세 series 11편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">소장가의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">윤○○ 님</div><div class="say">고서화를<br><span class="mk">2억 원</span>에 팔면<br>세금 많이 나오죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">경비를 <span class="hl">90%</span>까지<br>빼 줘서 생각보다<br>적어요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">대상은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">한 점 6천만 원 이상이면</div><div class="h1" style="margin-top:8px">과세 대상</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">손으로 그린<br><span style="color:#c0392b">회화·데생·파스텔</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">오리지널<br><span style="color:#1b5fa8">판화·석판화</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">③</div><div class="tx">제작 후 100년 넘은<br><span style="color:#1f8a57">골동품</span></div></div>
</div>
{FT(3, True, '소득세법 시행령 제41조⑭')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">살아 계신 국내 작가<br>그림을 1억에 팔면<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">기타소득 과세?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/smile-none.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 양도일 현재 <b style="font-weight:900">생존한 국내<br>원작자</b>의 작품은 과세 대상에서 빠져요.</div>
{FT(4, True, '소득세법 시행령 제41조⑭ 단서')}</div>''',
# 5 계산
f'''<div class="c dk bg-mint">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#11684a">15년 보유 고서화 2억 원 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">세금 계산</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>받은 금액</small><b style="color:#16213e">2억</b></div><div class="op">−</div><div class="bx"><small>필요경비</small><b style="color:#2fa36b">1.8억</b></div></div>
<div class="total" style="top:610px"><small>2천만 원 × 20% (지방세 포함)</small><b>440만 원</b><span>다른 소득과 합치지 않아요</span></div>
<img class="ch" src="ch/smile-calc.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">계산</b><br>· 9천만 + 1억 × 90%(10년↑)<br>· 실제 경비 3천만 원보다 커서 적용</div>
{FT(5, True, '소득세법 제129조, 시행령 제87조')}</div>''',
# 6 숫자 타일
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">받은 금액에 따라</div><div class="h1" style="margin-top:8px">필요경비 비율</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">90</div><div class="tx">1억 원까지<br><span style="color:#1f8a57">90% 인정</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">80</div><div class="tx">1억 원 초과분<br><span style="color:#1b5fa8">80% 인정</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">90</div><div class="tx">10년 이상 보유 시<br><span style="color:#c0392b">초과분도 90%</span></div></div>
</div>
{FT(6, True, '소득세법 시행령 제87조제2호')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '작품 팔기 전에').replace('<span class="hl">기한</span> 확인!', '<span class="hl">세금</span> 확인!'),
]
