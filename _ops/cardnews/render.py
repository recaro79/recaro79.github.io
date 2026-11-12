import sys
from playwright.sync_api import sync_playwright
src,outp=sys.argv[1],sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1400})
    pg.goto('file://'+src); pg.wait_for_timeout(600)
    for i in range(1,8):
        pg.locator(f'#s{i} .c').screenshot(path=f'{outp}_{i}.png')
    b.close()
