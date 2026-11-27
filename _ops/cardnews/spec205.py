import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 205
SLUG = 'real-estate-rich-company-shares-transfer'
CAT = '양도소득세'
DATE = '2026-11-27'
TITLE = '부동산이 많은 가족 법인 주식을 파신다면 — 부동산 비율 50% 이상 법인의 과점주주가 50% 이상 넘기면 주식 세율(20~25%)이 아니라 부동산처럼 기본세율 6~45%, 비사업용 토지가 많으면 10%p 더'
DESC = '자산총액 중 부동산 등 비율이 50% 이상인 법인의 과점주주(주주 1인과 특수관계인 지분 합계 50% 초과)가 3년 내 합산해 주식 50% 이상을 과점주주 외의 자에게 양도하거나, 골프장·스키장·휴양시설·부동산업 법인으로 부동산 비율 80% 이상인 법인의 주식을 양도하면 기타자산으로 보아 기본세율(6~45%)을 적용합니다. 비사업용 토지 비율 50% 이상 법인이면 10%p를 더합니다. 장기보유 특별공제는 없습니다. 소득세법 제94조제1항제4호다목·라목, 제104조제1항, 같은 법 시행령 제158조·제167조의7 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '소득세법 제94조제1항제4호다목·라목·제2항, 제104조제1항제1호·제9호·제11호, 같은 법 시행령 제158조, 제167조의7'
TAGS = ['특정주식', '부동산과다보유법인', '과점주주', '기타자산', '주식양도세', '부산세무사']
ALTS = ['부동산 과다보유 법인 주식 (표지)', '부동산 과다보유 법인 주식 (상담 질문)', '부동산 과다보유 법인 주식 (요건)', '부동산 과다보유 법인 주식 (O·X 퀴즈)', '부동산 과다보유 법인 주식 (세금 차이)', '부동산 과다보유 법인 주식 (확인할 점)', '부동산 과다보유 법인 주식 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
건물·토지를 가진 가족 법인을 운영하시다가 "건물을 파는 대신 법인 주식을 통째로 넘기면 세금이 줄지 않을까?" 생각하시는 분들이 계십니다. 비상장주식 대주주 양도세율은 20~25%이니 부동산 세율(최고 45%)보다 낮아 보이기 때문입니다. 그런데 세법은 이런 경우를 미리 막아 두었습니다. <b>부동산이 대부분인 법인의 주식을 과점주주가 대량으로 넘기면</b>, 주식이 아니라 <b>부동산과 같은 "기타자산"</b>으로 보아 기본세율 6~45%로 과세합니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>자산총액 중 <b>부동산 등이 50% 이상</b>인 법인의 <b>과점주주</b>(본인+특수관계인 지분 50% 초과)가 주식 <b>50% 이상</b>을 넘기면(3년 내 합산) <b>기타자산</b>으로 과세합니다.</li><li>골프장·스키장·휴양시설·부동산업 등 법인으로 부동산 비율 <b>80% 이상</b>이면 지분율과 관계없이 그 주식은 기타자산입니다.</li><li>세율은 주식 세율(20~25%)이 아니라 <b>기본세율 6~45%</b>, 비사업용 토지 비율이 50% 이상인 법인이면 <b>10%p 가산</b>, 장기보유 특별공제는 없습니다.</li></ol>
<div class="small" style="margin-top:8px">(소득세법 제94조제1항제4호다목·라목, 제104조제1항, 같은 법 시행령 제158조·제167조의7 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"가족 법인이 가진 건물을 파는 것보다 법인 주식을 넘기는 게 세금이 적다고 들었어요. 맞나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>윤○○ 님(가칭)은 가족과 함께 부동산임대 법인 주식 100%를 가지고 있습니다. 법인 자산의 대부분(90%)은 상가 건물입니다. 윤○○ 님이 가진 주식 <b>60%</b>를 가족이 아닌 사람에게 <b>30억 원</b>에 팔려고 합니다(취득가액 3억 원). 법인은 부동산 비율 50% 이상, 윤○○ 님 가족은 과점주주, 넘기는 주식은 50% 이상이므로 이 주식은 <b>기타자산</b>으로 과세됩니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 기타자산으로 보는 주식(특정주식)</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>요건</th><th>근거</th></tr>
<tr><td rowspan="3">부동산 과다보유 법인 주식</td><td>법인 자산총액 중 부동산 등(토지·건물·부동산에 관한 권리 + 다른 부동산 과다 법인 주식 환산액) 비율이 <b>50% 이상</b></td><td>법 제94조제1항제4호다목</td></tr>
<tr><td><b>과점주주</b>: 주주 1인과 특수관계인 등의 지분 합계가 <b>50% 초과</b></td><td>시행령 제158조제1항</td></tr>
<tr><td>과점주주가 과점주주 외의 자에게 <b>50% 이상</b> 양도(양도일부터 소급 3년 내 과점주주들이 양도한 주식 합산)</td><td>법 제94조제1항제4호다목, 시행령 제158조제2항</td></tr>
<tr><td>특정업종 법인 주식</td><td>골프장·스키장 등 체육시설업, 휴양시설관련업, 부동산업·부동산개발업 법인으로 부동산 등 비율 <b>80% 이상</b>(지분율·양도 비율 요건 없음)</td><td>법 제94조제1항제4호라목, 시행령 제158조제8항</td></tr>
<tr><td>자산총액 계산</td><td>장부가액(토지·건물은 기준시가가 더 크면 기준시가), 양도일 전 1년 내 차입·증자로 늘어난 현금·금융재산 등은 제외</td><td>시행령 제158조제4항</td></tr>
</table></div>
<p>주식(제3호)에도 해당하고 기타자산(제4호)에도 해당하면 <b>기타자산</b>으로 봅니다(법 제94조제2항).</p>

<h2>2. 세율 비교</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>세율</th><th>근거</th></tr>
<tr><td>일반 비상장주식(대주주)</td><td>과세표준 3억 원 이하 20%, 초과분 25%</td><td>법 제104조제1항제11호가목</td></tr>
<tr><td><b>기타자산(특정주식)</b></td><td><b>기본세율 6~45%</b></td><td>같은 항 제1호</td></tr>
<tr><td>비사업용 토지 비율 50% 이상 법인의 특정주식</td><td>기본세율 + <b>10%p</b>(16~55%)</td><td>같은 항 제9호, 시행령 제167조의7</td></tr>
</table></div>
<p>기타자산에는 <b>장기보유 특별공제</b>가 적용되지 않습니다(법 제95조제2항은 토지·건물 등만 대상). 오래 보유하셨어도 공제가 없다는 점을 꼭 기억하세요.</p>

<h2>3. 윤○○ 님 사례 — 세금 차이</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>일반 주식으로 착각한 경우</th><th>실제(기타자산)</th></tr>
<tr><td>양도가액 − 취득가액</td><td>2,700,000,000</td><td>2,700,000,000</td></tr>
<tr><td>양도소득 기본공제</td><td>△2,500,000</td><td>△2,500,000</td></tr>
<tr><td>과세표준</td><td>2,697,500,000</td><td>2,697,500,000</td></tr>
<tr><td>세율</td><td>20%·25%</td><td>기본세율 6~45%</td></tr>
<tr><td>양도소득세 산출세액</td><td>659,375,000</td><td><b>1,147,935,000</b></td></tr>
</table></div>
<p>같은 주식인데 기타자산으로 보면 양도세가 <b>약 4억 8,856만 원</b> 더 나옵니다(지방소득세 별도). 주식으로 넘기면 무조건 유리하다고 생각하시면 안 되는 이유입니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 비사업용 토지 과다보유 법인이 아니고, 증권거래세·필요경비·다른 양도 건은 없는 것으로 가정했습니다. 세율은 소득세법 제55조제1항(기본세율)과 제104조제1항제11호가목을 적용했습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 법인 재무상태표로 <b>부동산 등 비율</b>(기준시가가 장부가액보다 크면 기준시가)을 계산했다.</li>
<li>☐ 본인과 가족 등 <b>특수관계인 지분 합계</b>가 50%를 넘는지 확인했다.</li>
<li>☐ 최근 <b>3년 동안</b> 과점주주들이 넘긴 주식을 합산해 50% 이상인지 확인했다.</li>
<li>☐ 법인에 <b>비사업용 토지</b>가 많은지(50% 이상이면 10%p 가산) 확인했다(<a href="/column/29-non-business-land.html">칼럼 29</a>).</li>
<li>☐ 법인이 건물을 직접 파는 경우의 법인세·배당 세금과 <b>함께 비교</b>했다(<a href="/column/118-corporate-land-gain-surcharge.html">칼럼 118</a>, <a href="/column/133-unlisted-stock-transfer-tax.html">칼럼 133</a>).</li>
</ul>
<p>부동산 법인의 출구 전략은 주식 양도, 건물 매각 후 배당, 청산 등 여러 방법을 숫자로 비교해야 합니다. 법인 정리나 지분 매각을 검토하고 계시면 재무제표와 주주명부를 가지고 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>최근 재무상태표·법인세 신고서</td><td>자산총액, 부동산 등 비율</td></tr>
<tr><td>주주명부·주식변동상황명세서</td><td>과점주주 여부, 3년 내 양도 주식</td></tr>
<tr><td>법인 보유 부동산 등기부·공시가격</td><td>기준시가 비교, 비사업용 토지 여부</td></tr>
<tr><td>주식 취득 자료(출자·매입)</td><td>취득가액</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-sunset">{HD()}
<div class="bokeh" style="left:90px;top:200px;width:120px;height:120px;background:#ffd38f;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:250px;width:90px;height:90px;background:#ffb3c7;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-calc-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">건물 대신 법인 주식을 팔면?</div><div class="t">주식 세율이<br>아닐 수 있어요</div><div class="series">양도세 절세 series 13편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">법인 대표님들의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">윤○○ 님</div><div class="say">건물 말고<br><span class="mk">법인 주식</span>을 넘기면<br>세금이 적죠?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">부동산 법인이면<br><span class="hl">부동산 세율</span>로<br>과세돼요!</div></div>
<img class="ch" src="ch/worry-doc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#0f5a4c">요건은? →</div>
{FT(2, False)}</div>''',
# 3 목록
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">세 가지가 모두 맞으면</div><div class="h1" style="margin-top:8px">기타자산 과세</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">법인 자산 중<br><span style="color:#1f8a57">부동산 50% 이상</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">가족 지분 합계<br><span style="color:#1b5fa8">50% 초과</span>(과점주주)</div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">3년 내 합산<br><span style="color:#c0392b">50% 이상</span> 양도</div></div>
</div>
{FT(3, True, '소득세법 제94조①4호다목·시행령 제158조')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">10년 넘게 가진 주식이면<br>기타자산도 장기보유<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">특별공제를 받는다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 기타자산은<br>장기보유 특별공제가 <b style="font-weight:900">없어요</b>.</div>
{FT(4, True, '소득세법 제95조②')}</div>''',
# 5 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">주식 60%를 30억 원에 양도 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">양도차익 27억 원</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>주식 세율</small><b style="color:#2fa36b">6.59억</b></div><div class="op">vs</div><div class="bx"><small>기타자산</small><b style="color:#ff5c8a">11.48억</b></div></div>
<div class="total" style="top:610px"><small>늘어나는 양도세</small><b>약 4억 8,856만</b><span>20~25% 대신 기본세율 6~45%</span></div>
<img class="ch" src="ch/worry-calc-sweat.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 비사업용 토지 과다 법인 아님<br>· 지방소득세 별도</div>
{FT(5, True, '소득세법 제104조①1호·11호')}</div>''',
# 6 확인
f'''<div class="c bg-orange">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">이것도 기억하세요</div><div class="h1" style="margin-top:8px">추가 체크</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">비사업용 토지 50%↑<br><span style="color:#c0392b">+10%p 가산</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">골프장·부동산업 등<br><span style="color:#b9770e">80%↑면 지분 무관</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">부동산 비율은<br><span style="color:#1b5fa8">기준시가</span>도 비교</div></div>
</div>
{FT(6, True, '소득세법 제94조①4호라목·시행령 제158조④·제167조의7')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '법인 지분 매각 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">세율</span> 먼저 확인!'),
]
