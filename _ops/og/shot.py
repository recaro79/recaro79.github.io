import sys,glob
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch()
  for f,w,h in [('home.html',1200,630)]+[(g,800,400) for g in sorted(glob.glob('g_*.html'))]:
    pg=b.new_page(viewport={'width':w,'height':h});pg.goto('file:///home/claude/ogh/'+f);pg.wait_for_timeout(400)
    pg.screenshot(path=f.replace('.html','.png'));pg.close()
