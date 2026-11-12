# QR 명함 이미지 다시 만들기: python3 _ops/qrcard/build.py  (저장소 루트에서 실행)
# contact.vcf 내용으로 연락처 QR을 새로 만들고 card/qr-card.png 를 갱신합니다.
import qrcode, os
from qrcode.constants import ERROR_CORRECT_M
from playwright.sync_api import sync_playwright
d=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(os.path.dirname(d))
v=open(os.path.join(root,'contact.vcf'),encoding='utf-8').read()
for name,data in [('home','https://recaro79.github.io'),('vcard',v)]:
    q=qrcode.QRCode(error_correction=ERROR_CORRECT_M,border=0,box_size=16); q.add_data(data); q.make(fit=True)
    q.make_image(fill_color='#0f2448',back_color='white').save(os.path.join(d,name+'.png'))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1800,'height':1000})
    pg.goto('file://'+os.path.join(d,'card.html')); pg.wait_for_timeout(500)
    pg.screenshot(path=os.path.join(root,'card','qr-card.png')); b.close()
print('card/qr-card.png updated')
