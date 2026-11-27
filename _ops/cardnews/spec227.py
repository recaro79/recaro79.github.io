import runpy, os
_B = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spec196.py'))
_CTA = _B['BODY'][_B['BODY'].index('<p class="small">※ 상담 요청 시'):]

NUM = 227
SLUG = 'self-managed-forest-land-tax-reduction'
CAT = '양도소득세'
DATE = '2026-11-27'
TITLE = '산림경영계획인가를 받고 10년 넘게 직접 가꾼 산을 파신다면 — 직접 경영한 기간에 따라 양도소득세 10%~50% 감면, 보전산지·임업인·산 근처 거주 요건, 감면 종합한도는 연 1억 원'
DESC = '산지 소재지(같은 시·군·구, 연접 시·군·구 또는 30km 이내)에 거주하는 임업인이 산림경영계획인가를 받아 10년 이상 직접 경영한 보전산지를 양도하면 직접 경영 기간에 따라 양도소득세를 10년 이상 10%, 20년 이상 20%, 30년 이상 30%, 40년 이상 40%, 50년 이상 50% 감면합니다. 감면세액은 자경농지 등 다른 감면과 합쳐 과세기간별 1억 원, 5년간 2억 원 한도입니다. 조세특례제한법 제69조의4·제133조, 같은 법 시행령 제66조의4 기준. 2026-11-27 현행 법령 기준.'
OGDESC = '조세특례제한법 제69조의4·제133조제1항, 같은 법 시행령 제66조의4'
TAGS = ['자경산지', '임야양도', '산림경영계획', '양도세감면', '양도소득세', '부산세무사']
ALTS = ['자경산지 양도세 감면 (표지)', '자경산지 양도세 감면 (상담 질문)', '자경산지 양도세 감면 (감면율)', '자경산지 양도세 감면 (O·X 퀴즈)', '자경산지 양도세 감면 (요건)', '자경산지 양도세 감면 (세금 계산)', '자경산지 양도세 감면 (상담 안내)']

BODY = '''<p>안녕하세요. 세무법인 인성 남기원 세무사입니다.<br>
"아버지 때부터 나무를 심고 가꿔 온 산이 있는데, 이번에 팔게 됐습니다. 산도 감면이 있나요?" 농지의 자경 감면, 축사용지 감면처럼 <b>직접 가꾼 산</b>에도 양도세 감면이 있습니다. 바로 <b>자경산지 감면</b>입니다. 다만 <b>산림경영계획인가</b>를 받고 직접 경영한 기간을 따지므로, 인가 서류가 가장 중요합니다. 오늘은 그 요건과 감면율을 쉽게 정리해 드리겠습니다.</p>

<div class="sum">
<div class="t">📌 핵심 3줄 요약</div>
<ol><li>산 근처에 사는 <b>임업인</b>이 <b>산림경영계획인가</b>를 받아 <b>10년 이상 직접 경영</b>한 <b>보전산지</b>를 팔면 양도세를 감면합니다.</li><li>감면율은 직접 경영 기간에 따라 <b>10년 10% · 20년 20% · 30년 30% · 40년 40% · 50년 이상 50%</b>입니다.</li><li>감면세액은 자경농지·축사용지 등 다른 감면과 합쳐 <b>과세기간별 1억 원, 5년간 2억 원</b>이 한도입니다.</li></ol>
<div class="small" style="margin-top:8px">(조세특례제한법 제69조의4·제133조, 같은 법 시행령 제66조의4 / 2026-11-27 현행 법령 기준)</div>
</div>

{{CARDNEWS}}
<div class="quote">"산림경영계획인가를 받고 25년 동안 직접 나무를 가꾼 산을 팝니다. 감면이 얼마나 되나요?"</div>

<h2>사례로 먼저 보겠습니다</h2>
<p>문○○ 님(가칭)은 <b>25년 전 2억 원</b>에 보전산지를 사서 곧바로 산림경영계획인가를 받고, 같은 군에 살면서 임업인으로 직접 나무를 가꿔 오셨습니다. 이번에 이 산을 <b>6억 원</b>에 팔게 되었습니다. 직접 경영한 기간이 <b>20년 이상 30년 미만</b>이므로 감면율은 <b>20%</b>입니다.</p>
<p class="small">※ 이해를 돕기 위해 구성한 가상 사례입니다.</p>

<h2>1. 직접 경영 기간별 감면율</h2>
<div class="tbl"><table>
<tr><th>직접 경영한 기간</th><th>감면율</th></tr>
<tr><td>10년 이상 20년 미만</td><td>양도소득세의 <b>10%</b></td></tr>
<tr><td>20년 이상 30년 미만</td><td><b>20%</b></td></tr>
<tr><td>30년 이상 40년 미만</td><td><b>30%</b></td></tr>
<tr><td>40년 이상 50년 미만</td><td><b>40%</b></td></tr>
<tr><td>50년 이상</td><td><b>50%</b></td></tr>
</table></div>
<p>경영 기간은 산지를 취득하고 <b>산림경영계획인가를 받은 날부터</b> 양도할 때까지 직접 임업에 사용한 기간으로 계산합니다(시행령 제66조의4제3항).</p>

<h2>2. 감면 요건</h2>
<div class="tbl"><table>
<tr><th>요건</th><th>내용</th><th>근거</th></tr>
<tr><td>사람</td><td>「임업 및 산촌 진흥촉진에 관한 법률」에 따른 <b>임업인</b>으로, 감면 기간 이상 산지가 있는 시·군·구, 연접 시·군·구, 또는 직선거리 <b>30km 이내</b>에 거주</td><td>시행령 제66조의4제1항</td></tr>
<tr><td>직접 경영</td><td>소유 산지에서 임업에 상시 종사하거나, 임작업의 <b>2분의 1 이상</b>을 자기 노동력으로 수행</td><td>같은 조 제2항</td></tr>
<tr><td>대상 산지</td><td>「산지관리법」에 따른 <b>보전산지</b>(시 지역 주거·상업·공업지역 편입 후 3년이 지난 산지 등은 제외)</td><td>같은 조 제3항</td></tr>
<tr><td>인가</td><td>「산림자원의 조성 및 관리에 관한 법률」 제13조에 따른 <b>산림경영계획인가</b></td><td>법 제69조의4제1항</td></tr>
<tr><td>신청</td><td>양도세 예정·확정신고 때 <b>세액감면신청서</b> 제출</td><td>시행령 제66조의4제9항</td></tr>
</table></div>
<p>상속받은 산지는 상속인이 1년 이상 계속 임업에 사용하면 피상속인이 경영한 기간을 합칠 수 있습니다(같은 조 제6항). 감면 종합한도는 <a href="/column/162-capital-gains-reduction-overall-limit.html">칼럼 162</a>, 축사용지 감면은 <a href="/column/225-livestock-barn-land-transfer-tax-exemption.html">칼럼 225</a>를 참고해 주세요.</p>

<h2>3. 문○○ 님 사례 — 감면 전후 비교</h2>
<div class="tbl"><table>
<tr><th>구분</th><th>금액(원)</th></tr>
<tr><td>양도차익(6억 − 2억)</td><td>400,000,000</td></tr>
<tr><td>장기보유특별공제(15년 이상 30%)</td><td>△120,000,000</td></tr>
<tr><td>양도소득기본공제</td><td>△2,500,000</td></tr>
<tr><td>과세표준</td><td>277,500,000</td></tr>
<tr><td>양도소득세 산출세액</td><td>85,510,000</td></tr>
<tr><td>감면세액(20%)</td><td>△17,102,000</td></tr>
<tr><td>납부할 양도소득세</td><td><b>68,408,000</b></td></tr>
</table></div>
<p>직접 가꾼 기간 덕분에 <b>1,710만 원</b>이 줄어듭니다. 경영 기간이 30년이 되면 감면율이 30%로 오르니, 매각 시점을 정할 때 경영 기간도 함께 따져 보시면 좋습니다.</p>
<p class="small">※ python으로 계산·검산했습니다. 필요경비는 없고, 비사업용 토지 중과세율은 적용되지 않는 경우로 가정했습니다. 장기보유특별공제는 소득세법 제95조제2항 표 1, 세율은 같은 법 제55조를 적용했습니다. 지방소득세와 감면에 따른 농어촌특별세 등은 반영하지 않았습니다.</p>

<h2>4. 이렇게 점검하세요</h2>
<ul class="check">
<li>☐ <b>산림경영계획인가서</b>와 인가일을 확인했다(경영 기간의 시작).</li>
<li>☐ 산지가 <b>보전산지</b>인지 토지이용계획확인서로 확인했다.</li>
<li>☐ 임업인 확인서 등 <b>임업인</b>임을 증명할 자료가 있다.</li>
<li>☐ 경영 기간 동안 산 근처(같은·연접 시군구 또는 30km 이내)에 거주했는지 주민등록초본으로 확인했다.</li>
<li>☐ 조림·숲가꾸기 등 <b>직접 임작업</b>을 한 기록을 모아 두었다.</li>
<li>☐ 최근 5년간 다른 감면을 받았는지 확인해 한도를 계산했다.</li>
</ul>
<p>산은 대대로 물려받아 오래 가꾸는 경우가 많아 서류가 흩어져 있기 쉽습니다. 매각을 앞두고 계시면 인가 서류부터 함께 확인해 드리겠습니다. 편하게 상담해 주세요.</p>

<h2>상담 때 준비하시면 좋은 자료</h2>
<div class="tbl"><table>
<tr><th>자료</th><th>확인 내용</th></tr>
<tr><td>산림경영계획인가서</td><td>인가일·경영 기간</td></tr>
<tr><td>토지 등기사항증명서·토지이용계획확인서</td><td>취득일, 보전산지 여부</td></tr>
<tr><td>임업인 확인 자료·임작업 기록</td><td>직접 경영 여부</td></tr>
<tr><td>주민등록초본(주소 이력)</td><td>거주 요건</td></tr>
<tr><td>매매계약서</td><td>양도가액</td></tr>
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
<div class="bokeh" style="left:860px;top:260px;width:90px;height:90px;background:#e8ffd0;opacity:.35"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/smile-doc.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">10년 넘게 직접 가꾼 산</div><div class="t">팔 때 양도세<br>최대 50% 감면</div><div class="series">양도세 절세 series 19편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-lilac">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#5b2f7a">임업인의 질문</div>
<div class="bub" style="left:60px;top:240px;width:820px"><div class="who">문○○ 님</div><div class="say">25년 가꾼 산,<br><span class="mk">감면</span>이<br>있을까요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:660px"><div class="who">남기원 세무사</div><div class="say" style="font-size:44px">인가 받고 가꾸셨다면<br><span class="hl">20% 감면</span>이에요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:700px;width:380px">
<div class="abs" style="right:60px;top:1140px;font-size:36px;font-weight:900;color:#5b2f7a">감면율은? →</div>
{FT(2, False)}</div>''',
# 3 숫자
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick hl" style="font-size:36px">직접 경영한 기간에 따라</div><div class="h1" style="margin-top:8px">감면율</div></div>
<div class="rows" style="top:400px">
 <div class="row"><div class="ic" style="background:#3d8bff">10</div><div class="tx">10년 이상<br><span style="color:#1b5fa8">10% 감면</span></div></div>
 <div class="row"><div class="ic" style="background:#2fa36b">20</div><div class="tx">20년 20% · 30년 30%<br><span style="color:#1f8a57">40년 40%</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">50</div><div class="tx">50년 이상<br><span style="color:#c0392b">50% 감면</span></div></div>
</div>
{FT(3, True, '조특법 제69조의4①')}</div>''',
# 4 OX
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:62px;font-weight:900;line-height:1.3;letter-spacing:-2px">산을 산 날부터<br>경영 기간을<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">무조건 센다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/worry-magnify.svg" style="left:470px;top:580px;width:480px">
<div class="note" style="top:1000px">정답은 <b class="hl" style="font-weight:900">X</b>! <b style="font-weight:900">산림경영계획인가</b>를<br>받은 날부터 직접 경영한 기간이에요.</div>
{FT(4, True, '조특법 시행령 제66조의4③')}</div>''',
# 5 목록(요건)
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4;font-size:34px">이 요건을 갖추세요</div><div class="h1" style="margin-top:8px">감면 요건</div></div>
<div class="rows" style="top:390px">
 <div class="row"><div class="ic" style="background:#2fa36b">①</div><div class="tx">임업인 · 산 근처<br><span style="color:#1f8a57">30km 이내 거주</span></div></div>
 <div class="row"><div class="ic" style="background:#3d8bff">②</div><div class="tx">보전산지<br><span style="color:#1b5fa8">산림경영계획인가</span></div></div>
 <div class="row"><div class="ic" style="background:#e0463c">③</div><div class="tx">직접 임업<br><span style="color:#c0392b">10년 이상</span></div></div>
</div>
{FT(5, True, '조특법 시행령 제66조의4①~③')}</div>''',
# 6 계산
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">2억에 사서 6억에 양도 · 25년 경영 (가상 사례)</div><div class="h1" style="font-size:62px;margin-top:6px">양도세 비교</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>감면 전</small><b style="color:#ff5c8a">8,551만</b></div><div class="op">→</div><div class="bx"><small>20% 감면 후</small><b style="color:#2fa36b">6,841만</b></div></div>
<div class="total" style="top:610px"><small>줄어드는 양도소득세</small><b>1,710만 원</b><span>연 1억·5년 2억 원 한도 안</span></div>
<img class="ch" src="ch/smile-calc.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">가정</b><br>· 장기보유특별공제 30%<br>· 비사업용 토지 중과 없음</div>
{FT(6, True, '조특법 제69조의4·제133조')}</div>''',
# 7 상담 안내
_S217['CARDS'][6].replace('공익 출연 전에', '산 매각 전에').replace('<span class="hl">기한</span> 확인!', '<span class="hl">인가 서류</span> 확인!'),
]
