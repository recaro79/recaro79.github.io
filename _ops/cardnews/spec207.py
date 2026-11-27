import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 207
SLUG = 'commercial-deposit-deemed-rent-vat'
CAT = '부가가치세'
DATE = '2026-11-27'
TITLE = '상가 임대보증금에도 부가세가 붙습니다 — 간주임대료 = 보증금 × 일수 × 3.1% ÷ 365, 세금계산서 없이 임대인이 부가세 신고 때 함께 신고·납부합니다'
DESC = '상가 등 부동산 임대용역을 공급하고 전세금이나 임대보증금을 받으면, 보증금에 과세대상 기간의 일수와 정기예금 이자율(연 3.1%)을 곱해 365로 나눈 금액(간주임대료)을 공급가액으로 보아 부가가치세를 냅니다. 간주임대료 부분은 세금계산서 발급의무가 없습니다. 부가가치세법 제29조제10항, 같은 법 시행령 제65조·제71조제1항제6호, 같은 법 시행규칙 제47조 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '부가가치세법 제29조제10항, 같은 법 시행령 제65조제1항·제2항·제3항, 제71조제1항제6호, 같은 법 시행규칙 제47조'
TAGS = ['간주임대료', '상가임대', '임대보증금', '부가가치세', '임대사업자', '부산세무사']
ALTS = ['보증금 간주임대료 부가세 (표지)', '보증금 간주임대료 부가세 (상담 질문)', '보증금 간주임대료 부가세 (계산식)', '보증금 간주임대료 부가세 (O·X 퀴즈)', '보증금 간주임대료 부가세 (사례 계산)', '보증금 간주임대료 부가세 (확인할 점)', '보증금 간주임대료 부가세 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
상가를 세 놓고 계신 사장님들께서 부가세 신고서를 보시고 "월세에 대한 부가세는 알겠는데, 보증금에도 부가세가 있나요?"라고 물으시는 경우가 많습니다. 네, 있습니다. 보증금은 돌려줄 돈이지만, 그 돈을 맡아 두는 동안 이자만큼의 이익을 얻는다고 보아 <b>간주임대료</b>를 계산해 부가세를 냅니다. 1월·7월 부가세 신고 전에 계산 방법을 알아 두시면 좋습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>상가 등 부동산을 임대하고 <b>보증금·전세금</b>을 받으면 <b>보증금 × 과세대상 기간 일수 × 3.1% ÷ 365</b>를 공급가액(간주임대료)으로 봅니다.</li><li>간주임대료의 <b>10%</b>가 부가세이고, 이 부분은 <b>세금계산서를 발급하지 않고</b> 임대인이 신고·납부합니다.</li><li>남의 건물을 빌려 다시 세 놓는(전대) 경우에는 내가 낸 보증금을 빼고 계산합니다.</li></ol>
<div class="small" style="margin-top:8px">(부가가치세법 제29조제10항, 같은 법 시행령 제65조·제71조, 같은 법 시행규칙 제47조 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"보증금 2억 원에 월세 300만 원으로 상가를 놓고 있어요. 월세 부가세는 세금계산서로 받는데, 보증금 부가세는 어떻게 하나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>일반과세자인 문○○ 님(가칭)은 상가를 <b>보증금 2억 원, 월세 300만 원</b>(부가세 별도)에 임대하고 있습니다. 2026년 7월 1일부터 12월 31일까지(<b>184일</b>) 계약 내용이 그대로라면, 2027년 1월 부가세 확정신고 때 월세분과 함께 보증금에 대한 <b>간주임대료</b>도 신고해야 합니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 간주임대료 계산 방법</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>내용</th><th>근거</th></tr>
<tr><td>계산식</td><td><b>해당 기간의 보증금 × 과세대상 기간의 일수 × 정기예금 이자율 ÷ 365</b>(윤년 366)</td><td>시행령 제65조제1항</td></tr>
<tr><td>정기예금 이자율</td><td>연 <b>3.1%</b>(1,000분의 31)</td><td>시행규칙 제47조</td></tr>
<tr><td>전대(빌려서 다시 임대)</td><td>받은 보증금 − 내가 임차할 때 낸 보증금(직접 사업에 쓰는 면적 비율만큼은 빼지 않음)</td><td>시행령 제65조제2항</td></tr>
<tr><td>보증금을 월세에 충당한 경우</td><td>충당한 금액을 뺀 보증금으로 계산</td><td>시행령 제65조제3항</td></tr>
<tr><td>세금계산서</td><td>간주임대료 부분은 <b>발급의무 면제</b></td><td>시행령 제71조제1항제6호</td></tr>
</table></div>
<p>주택 임대는 부가세 면세이므로 이 계산은 <b>상가·사무실 등 과세되는 부동산 임대</b>에 적용됩니다. 상가와 주택을 함께 임대하면서 구분이 불분명하면 토지·건물 가액과 면적 비율로 나누어 계산합니다(시행령 제65조제4항). 종합소득세에서 말하는 주택 임대 간주임대료(<a href="/column/23-housing-rental-income-tax.html">칼럼 23</a>)와는 별개의 계산입니다.</p>

<h2>2. 문○○ 님 사례 계산(2026년 2기, 184일)</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>공급가액</th><th>부가세(10%)</th></tr>
<tr><td>월세(300만 원 × 6개월)</td><td>18,000,000</td><td>1,800,000(세금계산서 발급)</td></tr>
<tr><td>간주임대료(2억 원 × 184일 × 3.1% ÷ 365)</td><td>3,125,479</td><td>312,547(세금계산서 없음)</td></tr>
<tr><td><b>합계</b></td><td>21,125,479</td><td><b>2,112,547</b></td></tr>
</table></div>
<p>보증금 2억 원이면 1년에 간주임대료 약 <b>620만 원</b>, 부가세 약 <b>62만 원</b>이 생깁니다. 보증금이 클수록 금액이 커지니 신고 때 빠뜨리지 않도록 주의하세요.</p>
<p class="small">※ python으로 계산·검산했습니다(원 미만 절사). 매입세액공제, 중도 계약 변경은 없는 것으로 가정했습니다.</p>

<h2>3. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ 신고기간 중 <b>보증금이 바뀐 날</b>이 있으면 기간을 나누어 계산했다.</li>
<li>☐ 보증금 일부를 밀린 월세로 <b>충당</b>했다면 그만큼 빼고 계산했다.</li>
<li>☐ 상가를 빌려 다시 세 놓는 경우 <b>내가 낸 보증금</b>을 빼고 계산했다.</li>
<li>☐ 간주임대료 부가세를 <b>누가 부담할지</b> 임대차계약서에 정해 두었다.</li>
<li>☐ 상가 건물을 팔 계획이라면 부가세 포괄양도 요건도 함께 검토했다(<a href="/column/147-commercial-building-business-transfer-vat.html">칼럼 147</a>).</li>
</ul>
<p>임대 부가세는 매번 반복되는 신고라 한 번 정리해 두시면 편합니다. 임대차계약서를 가지고 편하게 상담해 주세요. 간주임대료와 월세 부가세, 종합소득세까지 함께 정리해 드리겠습니다.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>임대차계약서(변경 계약 포함)</td><td>보증금·월세, 변경일</td></tr>
<tr><td>세금계산서 발행 내역</td><td>월세 공급가액</td></tr>
<tr><td>전대인 경우 내 임차계약서</td><td>내가 낸 보증금, 직접 사용 면적</td></tr>
<tr><td>보증금 충당 내역</td><td>충당액 차감</td></tr>
</table></div>
''' + _CTA

BASIS = '2026.11.27 현행 법령 기준'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True, law=''): return (f'<div class="basis">{law + " · " if law else ""}{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-orange">{HD()}
<div class="bokeh" style="left:90px;top:200px;width:120px;height:120px;background:#ffe3b0;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:250px;width:90px;height:90px;background:#fff;opacity:.3"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/wow-calc-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">상가 임대 사장님 필독</div><div class="t">보증금에도<br>부가세가 있어요</div><div class="series">부가세·기타 series 2편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-cream">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#8a5a00">부가세 신고 때 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">문○○ 님</div><div class="say">돌려줄 <span class="mk">보증금</span>에도<br>부가세를<br>내야 하나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">네, <span class="hl">간주임대료</span>로<br>계산해서<br>신고해요!</div></div>
<img class="ch" src="ch/smile-calc.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#8a5a00">계산식은? →</div>
{FT(2, False)}</div>''',
# 3 계산식
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">간주임대료 계산식</div><div class="h1" style="font-size:62px;margin-top:6px">보증금 × 일수 × 3.1%</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>보증금</small><b style="color:#1b5fa8">2억</b></div><div class="op">×</div><div class="bx"><small>일수 ÷ 365</small><b style="color:#ff5c8a">184일</b></div></div>
<div class="total" style="top:610px"><small>간주임대료 (× 3.1%)</small><b>312만 5,479원</b><span>부가세 10% = 31만 2,547원</span></div>
<img class="ch" src="ch/smile-magnify.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">포인트</b><br>· 이자율 3.1%는 시행규칙으로 정함<br>· 2026년 7~12월(184일) 예시</div>
{FT(3, True, '부가세법 시행령 제65조①·시행규칙 제47조')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">보증금 부가세도<br>월세처럼 세금계산서를<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">발급해야 한다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! 간주임대료 부분은<br>세금계산서 <b style="font-weight:900">발급의무가 없어요</b>.</div>
{FT(4, True, '부가세법 시행령 제71조①6호')}</div>''',
# 5 타일
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">보증금 2억 · 월세 300만 원 (가상 사례)</div><div class="h1" style="margin-top:8px">6개월 부가세</div></div>
<div class="tiles" style="top:360px">
 <div class="tile wide t-red"><div class="who" style="font-size:36px">2기 부가세 합계</div><div class="amt">211만<small>원</small></div></div>
 <div class="tile t-blue"><div class="who">월세분</div><div class="amt">180만<small>원</small></div></div>
 <div class="tile t-green"><div class="who">보증금분</div><div class="amt">31만<small>원</small></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:900px;font-size:30px;font-weight:600">· 보증금 2억 원이면 1년 간주임대료 약 620만 원<br>· 부가세로는 1년 약 62만 원이에요.</div>
{FT(5, True, '부가세법 제29조⑩·시행령 제65조')}</div>''',
# 6 확인
f'''<div class="c bg-forest">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:34px">신고 전에</div><div class="h1" style="margin-top:8px">꼭 확인하세요</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#e0463c">①</div><div class="tx">보증금 바뀐 날<br><span style="color:#c0392b">기간 나눠 계산</span></div></div>
 <div class="row"><div class="ic" style="background:#f39c12">②</div><div class="tx">밀린 월세에 충당한<br><span style="color:#b9770e">보증금은 빼기</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">③</div><div class="tx">전대라면<br><span style="color:#1b5fa8">내가 낸 보증금</span> 차감</div></div>
</div>
{FT(6, True, '부가세법 시행령 제65조②③')}</div>''',
# 7 상담 안내
_B['CARDS'][6].replace('상가 매각 전에', '부가세 신고 전에').replace('<span class="hl">양도세</span> 미리 계산!', '<span class="hl">보증금</span>도 챙기세요!'),
]
