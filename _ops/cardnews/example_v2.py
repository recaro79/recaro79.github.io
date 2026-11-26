# 카드뉴스 v2 예시 (2026-11-26 기원님 승인 시안: 증여재산공제 7장)
# 새 spec을 만들 때 아래 HD()/FT() 와 CARDS 구조를 복사해 문구·색·캐릭터만 바꿔 씁니다.
# - 캐릭터: <img class="ch" src="ch/표정-소품[-sweat].svg" style="left:..;top:..;width:..">
#   표정 smile·worry·wow·wink / 소품 none·piggy·calc·doc·wave·thumb·magnify / 걱정 장면은 -sweat
# - 배경: bg-sunset·bg-night·bg-forest(표지용 어두운 배경), bg-mint·bg-yellow·bg-sky·bg-lilac·bg-cream(밝음 → class에 dk 추가),
#   bg-navy·bg-pink·bg-orange(흰 글씨)
# - 7장은 매번 형식을 섞습니다: 표지 / 대화(말풍선) / 숫자 타일 / O·X 퀴즈 / 목록 상자 / 계산식 / 상담 안내
# - 표지 아래 노란 글씨 'OO series N편'으로 시리즈를 이어 갑니다(log.md 시리즈 표 참고).

BASIS = '2026.11.26 현행 법령 기준 · 상속세 및 증여세법'
def HD(): return '<div class="ver">2026 Ver.</div><div class="brand"><img src="mark.png">세무법인 인성</div>'
def FT(n, basis=True): return (f'<div class="basis">{BASIS}</div>' if basis else '') + f'<div class="pg">{n} / 7</div>'

CARDS = [
# 1 표지
f'''<div class="c bg-sunset">{HD()}
<div class="bokeh" style="left:80px;top:190px;width:120px;height:120px;background:#ffd08a;opacity:.35"></div>
<div class="bokeh" style="left:860px;top:240px;width:90px;height:90px;background:#ffe3b0;opacity:.4"></div>
<div class="cv-glow"></div>
<img class="ch" src="ch/worry-piggy-sweat.svg" style="left:250px;top:150px;width:580px">
<div class="cv-shade"></div>
<div class="cv-txt"><div class="kick">부모님이 자녀에게 줄 때</div><div class="t">세금 없이<br>얼마까지 줄 수 있을까?</div><div class="series">증여세 절세 series 1편</div></div>
{FT(1, False)}</div>''',
# 2 대화
f'''<div class="c dk bg-mint">{HD()}
<div class="abs kick" style="left:60px;top:150px;font-size:40px;font-weight:900;color:#0f5a4c">상담실에서 정말 자주 듣는 질문</div>
<div class="bub" style="left:60px;top:240px;width:760px"><div class="who">고객님</div><div class="say">아들이 결혼하는데<br><span class="mk">1억 5천만 원</span> 보태주면<br>세금 많이 나오나요?</div></div>
<div class="bub r" style="right:60px;top:690px;width:620px"><div class="who">남기원 세무사</div><div class="say" style="font-size:50px">조건만 맞으면<br>증여세 <span class="hl">0원</span>일 수 있어요!</div></div>
<img class="ch" src="ch/wink-thumb.svg" style="left:10px;top:660px;width:400px">
<div class="abs" style="right:60px;top:1120px;font-size:36px;font-weight:900;color:#0f5a4c">어떻게요? 옆으로 넘겨 보세요 →</div>
{FT(2, False)}</div>''',
# 3 숫자 타일
f'''<div class="c bg-navy">{HD()}
<div class="abs" style="left:60px;top:140px;right:60px"><div class="kick hl" style="font-size:34px">10년 동안 세금 없이 받을 수 있는 금액</div><div class="h1" style="margin-top:8px">증여재산공제 한눈에!</div></div>
<div class="tiles" style="top:345px">
 <div class="tile wide t-red"><div class="who" style="font-size:36px">배우자에게</div><div class="amt">6억<small>원</small></div></div>
 <div class="tile t-blue"><div class="who">부모 → 성인 자녀</div><div class="amt">5천만<small>원</small></div></div>
 <div class="tile t-green"><div class="who">부모 → 미성년 자녀</div><div class="amt">2천만<small>원</small></div></div>
 <div class="tile t-violet"><div class="who">자녀 → 부모</div><div class="amt">5천만<small>원</small></div></div>
 <div class="tile t-orange"><div class="who">그 밖의 친족</div><div class="amt">1천만<small>원</small></div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:1090px;font-size:28px;font-weight:600">· '부모'에는 할아버지·할머니도 포함돼요.<br>· 미성년자는 만 19세 미만, '그 밖의 친족'은 4촌 이내 혈족·3촌 이내 인척이에요.</div>
{FT(3)}</div>''',
# 4 O·X 퀴즈
f'''<div class="c dk bg-yellow">{HD()}
<div class="abs" style="left:60px;top:150px"><span class="badge">O X 퀴즈</span></div>
<div class="abs" style="left:60px;right:60px;top:240px;font-size:66px;font-weight:900;line-height:1.3;letter-spacing:-2px">아빠한테 5천만 원,<br>엄마한테 5천만 원 받으면<br><span style="background:linear-gradient(transparent 60%,#fff 60%)">1억 원까지 세금 없다?</span></div>
<div class="ox x" style="left:60px;top:600px"></div>
<img class="ch" src="ch/wow-none-sweat.svg" style="left:430px;top:560px;width:560px">
<div class="note" style="top:1010px">정답은 <b class="hl" style="font-weight:900">X</b>! 부모님·조부모님은 <b class="hl">한 그룹</b>이라<br><b style="font-weight:900">10년 동안 합쳐서 5천만 원</b>까지만 공제돼요.</div>
{FT(4)}</div>''',
# 5 목록 상자
f'''<div class="c bg-pink">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#fff3c4">결혼·출산하는 자녀라면</div><div style="font-size:120px;font-weight:900;letter-spacing:-4px;line-height:1.1;text-shadow:0 8px 20px rgba(120,0,40,.35)">+1억 원<br><span style="font-size:76px">추가 공제!</span></div></div>
<img class="ch" src="ch/smile-wave.svg" style="right:30px;top:120px;width:380px">
<div class="rows" style="top:600px">
 <div class="row"><div class="ic" style="background:#ff5c8a">혼인</div><div class="tx">혼인신고일 <span style="color:#e83e6f">전후 2년</span> 안에<br>부모님께 받은 재산</div></div>
 <div class="row"><div class="ic" style="background:#ff9a3c">출산</div><div class="tx">자녀 출생일(입양일)부터 <span style="color:#e8761e">2년</span> 안에<br>부모님께 받은 재산</div></div>
</div>
<div class="abs small" style="left:60px;right:60px;top:1030px;font-size:31px">· 기본 공제(5천만 원)와 <b style="color:#fff3c4">따로</b> 받아요.<br>· 단, 혼인·출산 공제는 <b style="color:#fff3c4">합쳐서 1억 원</b>이 한도예요.</div>
{FT(5)}</div>''',
# 6 계산식
f'''<div class="c dk bg-sky">{HD()}
<div class="abs" style="left:60px;right:60px;top:150px"><div class="kick" style="color:#1b5fa8">그래서 결혼하는 성인 자녀는</div><div class="h1" style="font-size:66px;margin-top:6px">부모님께 최대 이만큼!</div></div>
<div class="eq" style="top:360px"><div class="bx"><small>기본 공제</small><b style="color:#3d8bff">5천만</b></div><div class="op">+</div><div class="bx"><small>혼인 공제</small><b style="color:#ff5c8a">1억</b></div></div>
<div class="total" style="top:610px"><small>합계</small><b>1억 5천만 원</b><span>까지 증여세 <span class="hl" style="display:inline;font-size:46px">0원</span></span></div>
<img class="ch" src="ch/smile-calc.svg" style="right:20px;top:880px;width:330px">
<div class="abs small" style="left:60px;width:640px;top:950px;color:#16213e"><b style="color:#e0463c">꼭 확인하세요</b><br>· 최근 10년 안에 부모님께 받으면서 이미 공제를 썼다면 그만큼 줄어요.<br>· 재산 종류·받는 방식에 따라 공제가 안 되는 경우도 있어요.</div>
{FT(6)}</div>''',
# 7 상담 안내
f'''<div class="c bg-navy">{HD()}
<div class="bokeh" style="left:930px;top:560px;width:110px;height:110px;background:#5c7dd6;opacity:.35"></div>
<div class="abs" style="left:0;right:0;top:130px;text-align:center"><div class="kick hl" style="font-size:40px">증여는 '주고 나서'보다</div><div style="font-size:84px;font-weight:900;letter-spacing:-3px;line-height:1.2">주기 <span class="hl">전에</span> 물어보세요!</div></div>
<img class="ch" src="ch/smile-wave.svg" style="left:360px;top:320px;width:360px">
<div class="end-box" style="top:740px">
 <div class="me"><img src="profile.jpg"><div><small>지점대표세무사</small><b>남기원</b><span>세무법인 인성 · 세무 경력 20년</span></div></div>
 <div class="ct"><img src="qr.png"><div><div class="tel">010-7741-4822</div><p>카카오톡 상담: QR을 찍어 주세요<br>평일 09:00~18:00 · recaro79.github.io<br>인스타그램·Threads @namsemu</p></div></div>
</div>
{FT(7)}</div>''',
]
