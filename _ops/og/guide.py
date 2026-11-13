import json,subprocess
G=[('beopin','법인세<br>안내','결산 일정 · 준비서류 체크리스트'),
('bugase','부가가치세<br>안내','신고 일정 · 사업자 유형별 준비서류'),
('jeungyeo','증여세<br>안내','신고기한 · 간이계산기 · 혼인·출산 공제 확인'),
('jongso','종합소득세<br>안내','신고 일정 · 준비서류 체크리스트'),
('sangsok','상속세<br>안내','상속 일정 자동 계산 · 준비서류 체크리스트'),
('sugim','거래처<br>수임등록 안내','홈택스 수임동의 · 사업용 카드·계좌 · CMS 신청'),
('yangdo','양도소득세<br>안내','신고기한 계산 · 모의계산기 · 준비서류')]
css='''@font-face{font-family:NM;src:url(NanumMyeongjo-800.woff2);font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
body{width:800px;height:400px;background:linear-gradient(180deg,#fdfaf4 0%,#f3e9d6 100%);font-family:"Noto Sans CJK KR",sans-serif;color:#0f2448;position:relative;overflow:hidden}
.bar{position:absolute;left:0;top:0;bottom:0;width:14px;background:linear-gradient(180deg,#d9b871,#a27b3a)}
.c{position:absolute;right:-120px;top:-150px;width:440px;height:440px;border-radius:50%;border:3px solid rgba(201,169,97,.35)}
.w{position:absolute;left:60px;right:60px;top:72px}
.o{font-family:NM;font-size:24px;color:#a27b3a;font-weight:800;letter-spacing:2px}
.o img{width:30px;height:30px;vertical-align:-7px;margin-right:9px}
h1{font-size:46px;font-weight:900;line-height:1.25;margin-top:26px}
.l{height:2px;background:rgba(162,123,58,.45);margin-top:22px}
.s{font-size:22px;color:#3a4456;margin-top:18px}'''
for f,t,s in G:
  open(f'g_{f}.html','w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><div class="bar"></div><div class="w"><div class="o"><img src="kacta-mark.png">세무법인 인성</div><h1>{t}</h1><div class="l"></div><div class="s">{s}</div></div></body></html>')
