import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 223
SLUG = 'ceo-loan-to-company-interest'
CAT = '법인세·종합소득세'
DATE = '2026-11-27'
TITLE = '대표님이 회사에 빌려준 돈(가수금), 이자를 받아도 될까요 — 회사는 이자를 비용으로, 대표님은 이자의 25%(지방세 포함 27.5%)를 원천징수, 시가(당좌대출이자율 연 4.6% 등)보다 높으면 초과분은 비용 불인정'
DESC = '법인이 대표이사 등 특수관계인에게서 돈을 빌리고 이자를 지급하면 법인은 이자를 손금으로 처리하고, 대표는 비영업대금의 이익으로 25% 원천징수됩니다. 다만 시가(가중평균차입이자율, 특정한 경우 당좌대출이자율 연 4.6%)보다 높은 이율로 빌리고 그 차이가 시가의 5% 이상이거나 3억 원 이상이면 부당행위계산 부인으로 초과분은 손금에 산입되지 않습니다. 법인세법 제52조, 같은 법 시행령 제88조·제89조, 같은 법 시행규칙 제43조, 소득세법 제14조·제129조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '법인세법 제52조, 같은 법 시행령 제88조제1항제7호·제3항, 제89조제3항, 같은 법 시행규칙 제43조, 소득세법 제14조제3항제6호·제129조제1항제1호나목'
TAGS = ['가수금', '대표이사이자', '비영업대금', '부당행위계산', '법인세', '부산세무사']
ALTS = ['가수금 이자 (표지)', '가수금 이자 (상담 질문)', '가수금 이자 (세금 구조)', '가수금 이자 (O·X 퀴즈)', '가수금 이자 (이율별 비교)', '가수금 이자 (확인할 점)', '가수금 이자 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"회사 운영자금이 모자라 제 돈 3억 원을 넣었는데, 은행처럼 이자를 받아도 되나요?" 법인 대표님들께 자주 받는 질문입니다. 대표님이 회사에 빌려준 돈(장부상 <b>가수금</b>)에 이자를 받는 것은 가능합니다. 회사는 그 이자를 <b>비용</b>으로 처리하고, 대표님은 이자소득에 대해 <b>25%를 원천징수</b>당합니다. 다만 이율을 너무 높게 정하면 초과분은 <b>회사 비용으로 인정되지 않습니다</b>. 오늘은 그 기준을 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>법인이 대표님께 지급한 이자는 원칙적으로 <b>법인 비용</b>입니다. 대표님이 받는 이자는 <b>비영업대금의 이익</b>으로 <b>25%</b>(지방소득세 포함 27.5%)를 원천징수합니다.</li><li>이율의 기준(시가)은 <b>가중평균차입이자율</b>이 원칙이고, 회사에 특수관계인이 아닌 곳에서 빌린 돈이 없는 경우 등에는 <b>당좌대출이자율 연 4.6%</b>입니다.</li><li>시가보다 높은 이율로 빌려 그 차이가 <b>시가의 5% 이상이거나 3억 원 이상</b>이면 초과 이자는 <b>손금불산입</b>됩니다.</li></ol>
<div class="small" style="margin-top:8px">(법인세법 제52조, 같은 법 시행령 제88조·제89조, 같은 법 시행규칙 제43조, 소득세법 제129조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"회사에 3억 원을 빌려줬는데, 이자를 연 10%로 받으면 안 될까요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>(주)○○(가칭)의 최○○ 대표님은 회사에 <b>3억 원</b>을 빌려주셨습니다. 회사에는 은행 등 특수관계인이 아닌 곳에서 빌린 돈이 없어, 이자율의 시가는 <b>당좌대출이자율 연 4.6%</b>입니다. 대표님은 연 4.6%와 연 10% 중 어느 이율로 이자를 받을지 고민하고 계십니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 가수금 이자의 세금 구조</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>회사(법인)</td><td>지급한 이자는 원칙적으로 손금(비용). 이자를 지급할 때 <b>원천징수</b>해 납부</td><td>소득세법 제127조</td></tr>
<tr><td>대표(개인)</td><td>사업이 아닌 개인 간 금전 대여 이자는 <b>비영업대금의 이익</b> → 원천징수세율 <b>25%</b></td><td>소득세법 제129조제1항제1호나목</td></tr>
<tr><td>금융소득 종합과세</td><td>이자·배당 합계가 연 <b>2천만 원 이하</b>이고 원천징수되었다면 분리과세로 끝나고, 넘으면 종합과세</td><td>소득세법 제14조제3항제6호</td></tr>
<tr><td>이율의 시가</td><td>가중평균차입이자율 원칙. 특수관계인이 아닌 자로부터의 차입금이 없는 경우 등에는 <b>당좌대출이자율 연 4.6%</b></td><td>시행령 제89조제3항, 시행규칙 제43조</td></tr>
<tr><td>부당행위 기준</td><td>시가보다 <b>높은 이율로 차용</b>하고, 차이가 시가의 <b>5% 이상</b> 또는 <b>3억 원 이상</b>이면 초과분 손금불산입</td><td>시행령 제88조제1항제7호·제3항</td></tr>
</table></div>
<p>반대로 회사가 대표님께 돈을 빌려준 <b>가지급금</b>은 이자를 받지 않으면 인정이자가 생깁니다(<a href="/column/10-provisional-payment-interest.html">칼럼 10</a>). 금융소득 종합과세는 <a href="/column/60-financial-income-comprehensive-tax.html">칼럼 60</a>에서 다뤘습니다.</p>

<h2>2. 최○○ 대표님 사례 — 이율에 따른 비교(1년분)</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>연 4.6%</th><th>연 10%</th></tr>
<tr><td>회사가 지급하는 이자</td><td>13,800,000</td><td>30,000,000</td></tr>
<tr><td>회사 비용(손금) 인정</td><td>13,800,000</td><td>13,800,000</td></tr>
<tr><td>손금불산입(시가 초과분)</td><td>-</td><td><b>16,200,000</b></td></tr>
<tr><td>대표님 원천징수(지방소득세 포함 27.5%)</td><td>3,795,000</td><td>8,250,000</td></tr>
<tr><td>금융소득 종합과세 여부<br><span class="small">(다른 금융소득 없을 때)</span></td><td>2천만 원 이하 → 분리과세</td><td>2천만 원 초과 → 종합과세</td></tr>
</table></div>
<p>연 10%로 정하면 회사는 시가를 넘는 <b>1,620만 원</b>을 비용으로 인정받지 못하고, 대표님은 금융소득이 2천만 원을 넘어 종합과세 대상이 됩니다. 시가 수준의 이율로 정하고 <b>금전소비대차계약서</b>를 써 두시는 것이 안전합니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 회사에 특수관계인이 아닌 자로부터의 차입금이 없어 당좌대출이자율(시행규칙 제43조제3항제1호)을 시가로 보고, 차입금 잔액이 1년 내내 3억 원이라고 가정했습니다. 연 10%의 경우 시가와의 차이(1,620만 원)가 시가(1,380만 원)의 5% 이상이므로 부당행위계산 부인 대상입니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 대표님이 회사에 넣은 돈이 <b>가수금(차입금)</b>인지, 자본금(증자)인지 장부에서 구분했다.</li>
<li>☐ 이자율·상환 조건을 정한 <b>금전소비대차계약서</b>와 이사회 등 내부 결의를 남겼다.</li>
<li>☐ 회사의 <b>가중평균차입이자율</b>을 계산했거나, 당좌대출이자율(연 4.6%) 적용 대상인지 확인했다.</li>
<li>☐ 이자를 지급할 때 <b>25% + 지방소득세</b>를 원천징수해 신고·납부했다.</li>
<li>☐ 대표님의 이자·배당 합계가 <b>연 2천만 원</b>을 넘는지 확인했다.</li>
</ul>
<p>대표님 돈과 회사 돈의 흐름은 장부와 계약서로 깔끔하게 정리될수록 세무 위험이 줄어듭니다. 가수금 정리나 이자 지급을 계획하고 계시면 결산 전에 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>가수금·차입금 계정별 원장</td><td>입금일·잔액·상환 내역</td></tr>
<tr><td>금전소비대차계약서(있는 경우)</td><td>이율·기간</td></tr>
<tr><td>회사의 금융기관 차입금 명세</td><td>가중평균차입이자율 계산</td></tr>
<tr><td>대표님의 다른 금융소득 내역</td><td>금융소득 종합과세 여부</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

_S217 = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec217.py'))

CARDS = [
# 1 표지
f'''<div class="c bg-forest">{HD()}
<div class="bokeh" style="left:90px;top:220px;width:120px;height:120px;background:#bff0d0;opacity:.3"></div>
<div class="bokeh" style="left:860px;top:260px;width:90px;height:90px;background:#ffe3b0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/smile-doc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">회사에 빌려준 대표님 돈</div><div class="t">가수금 이자<br>받아도 될까요?</div><div class="series">법인세 절세 series 8편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">법인 대표님의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">최○○ 대표님</div><div class="say">회사에 3억 빌려줬는데<br><span class="mk">이자 10%</span><br>받아도 되죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">이자는 OK!<br>다만 <span class="hl">시가 이율</span>로<br>정하세요</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">왜 그럴까요? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">이자를 주고받으면</div><div class="h1" style="margin-top:8px">세금은 이렇게</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">회사는<br><span style="color:#1f8a57">이자 = 비용 인정</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">대표님은<br><span style="color:#1b5fa8">25% 원천징수</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">연 2천만 원 넘으면<br><span style="color:#c0392b">종합과세</span></div></div>
</div>
{FT(3, True, '소득세법 제14조·제129조')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">대표님께 주는 이자는<br>이율이 높아도<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">전부 비용이다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-calc.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! <b style="font-weight:900">시가를 넘는 이자</b>는<br>부당행위로 비용에서 빠질 수 있어요.</div>
{FT(4, True, '법인세법 시행령 제88조①7·③')}</div>''',
# 5 계산
f'''<div class="c dk bg-lilac">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#5b2f7a">가수금 3억 원 · 1년 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">이율별 비교</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>연 4.6%</small><b style="color:#2fa36b">1,380만</b></div><div class="op">vs</div><div class="bx"><small>연 10%</small><b style="color:#ff5c8a">3,000만</b></div></div>
<div class="total" style="top:610px"><small>연 10%일 때 비용 불인정</small><b>1,620만 원</b><span>시가(4.6%) 초과분</span></div>
<img class="ch" src="ch/worry-magnify.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 외부 차입금 없음(4.6% 시가)<br>· 잔액 1년 내내 3억 원</div>
{FT(5, True, '법인세법 시행령 제89조③, 시행규칙 제43조')}</div>''',
# 6 확인
f'''<div class="c bg-orange">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">이자 주기 전에 확인!</div><div class="h1" style="margin-top:8px">체크 포인트</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#3d8bff">①</div><div class="tx">금전소비대차<br><span style="color:#1b5fa8">계약서 작성</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">②</div><div class="tx">시가 이율<br><span style="color:#1f8a57">가중평균·4.6%</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">지급할 때<br><span style="color:#c0392b">27.5% 원천징수</span></div></div>
</div>
{FT(6, True, '법인세법 시행령 제89조, 소득세법 제129조')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '결산 전에').replace('<span class="hl">기한</span> 확인!', '<span class="hl">가수금</span> 정리!'),
]
