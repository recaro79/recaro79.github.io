# 칼럼 + 카드뉴스 게시 도우미: python3 _ops/cardnews/publish.py <spec.py>
# spec.py 에 NUM, SLUG, CAT(세목 표시), TITLE, DESC, OGDESC, BODY(본문 HTML: 인사말~상담자료표 직전까지),
# TAGS(list), CARDS(7장 슬라이드 HTML 문자열 list), ALTS(7개 alt 문구), DATE 를 정의합니다.
import sys, os, re, subprocess, runpy
from PIL import Image
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
S = runpy.run_path(sys.argv[1])
NUM, SLUG, CAT, TITLE, DATE = S['NUM'], S['SLUG'], S['CAT'], S['TITLE'], S['DATE']
fn = f'{NUM}-{SLUG}.html'
url = f'https://recaro79.github.io/column/{fn}'
# 기준 칼럼(직전 번호) 복사
prev = sorted([f for f in os.listdir(R + '/column') if re.match(r'\d+-', f)], key=lambda x: int(x.split('-')[0]))[-1]
src = open(R + '/column/' + prev, encoding='utf-8').read()
head, rest = src.split('<div class="crumb">', 1)
_, tail = rest.split('<div class="sign">', 1)
tail = '<div class="sign">' + tail
esc = lambda s: s.replace('&', '&amp;').replace('"', '&quot;')
head = re.sub(r'<title>.*?</title>', f'<title>{TITLE} | 세무법인 인성 남기원 세무사</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{esc(S["DESC"])}">', head)
head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{esc(TITLE)}">', head)
head = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{esc(S["OGDESC"])}">', head)
head = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{url}">', head)
head = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="https://recaro79.github.io/assets/img/col{NUM}-thumb.jpg">', head)
head = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{url}">', head)
tail = re.sub(r'※ 이 글은 \d{4}-\d\d-\d\d 현행', f'※ 이 글은 {DATE} 현행', tail)
tail = re.sub(r'<div class="tags-line">.*?</div>', '<div class="tags-line">' + ''.join(f'<span>#{t}</span>' for t in S['TAGS']) + '</div>', tail, flags=re.S)
cn = ''.join(f'<img src="/assets/cardnews/{NUM}/{i+1}.jpg" alt="{esc(a)}" loading="lazy">' for i, a in enumerate(S['ALTS']))
CN = f'''<p class="small" style="margin-top:6px">👉 카드뉴스로 먼저 훑어보세요 (옆으로 넘겨 보세요)</p>
<div class="cn" data-cn>
    <button class="cn-btn prev" aria-label="이전" onclick="cnMove(this,-1)">‹</button>
    <div class="cn-track">{cn}</div>
    <button class="cn-btn next" aria-label="다음" onclick="cnMove(this,1)">›</button>
  </div>
'''
body = S['BODY'].replace('{{CARDNEWS}}', CN)
mid = f'''<div class="crumb"><a href="/">홈</a> › <a href="/column/">세무 칼럼</a> › {CAT}</div>
<h1>{TITLE}</h1>
<div class="meta">{CAT} · {DATE} · 세무법인 인성 남기원 세무사</div>
{body}
'''
open(R + '/column/' + fn, 'w', encoding='utf-8').write(head + mid + tail)
# 카드뉴스
tpl = open(R + '/_ops/cardnews/template.html', encoding='utf-8').read()
style = tpl.split('<body>')[0]
slides = ''.join(f'<div id="s{i+1}" style="display:block">{c}</div>' for i, c in enumerate(S['CARDS']))
ch = R + f'/_ops/cardnews/c{NUM}.html'
open(ch, 'w', encoding='utf-8').write(style + '<body>' + slides + '</body></html>')
tmp = '/tmp/claude-0/-home-claude/64b84952-0c61-56e3-bb91-956bc6441653/scratchpad/cn'
os.makedirs(tmp, exist_ok=True)
subprocess.run(['python3', R + '/_ops/cardnews/render.py', ch, f'{tmp}/c{NUM}'], check=True)
od = R + f'/assets/cardnews/{NUM}'
os.makedirs(od, exist_ok=True)
for i in range(1, 8):
    im = Image.open(f'{tmp}/c{NUM}_{i}.png').convert('RGB')
    im.save(f'{od}/{i}.jpg', quality=86)
    if i == 1:
        w, h = im.size
        im.crop((0, 0, w, w)).resize((720, 720), Image.LANCZOS).save(R + f'/assets/img/col{NUM}-thumb.jpg', quality=86)
# 목록
card = f'''    <a class="col-card" href="/column/{fn}">
      <img src="/assets/img/col{NUM}-thumb.jpg" alt="{esc(TITLE)}">
      <div class="b"><div class="cat">{CAT}</div><h3>{TITLE}</h3><div class="d">{DATE}</div></div>
    </a>
'''
for p in ['index.html', 'column/index.html']:
    s = open(R + '/' + p, encoding='utf-8').read()
    if f'/column/{fn}' not in s:
        s = s.replace('<!-- COLUMNS:START -->\n', '<!-- COLUMNS:START -->\n' + card, 1)
        open(R + '/' + p, 'w', encoding='utf-8').write(s)
sm = open(R + '/sitemap.xml', encoding='utf-8').read()
if url not in sm:
    line = f'<url><loc>{url}</loc><lastmod>{DATE}</lastmod></url>\n'
    m = re.search(r'<url><loc>https://recaro79.github.io/column/' + prev.replace('.', r'\.'), sm)
    sm = sm[:m.start()] + line + sm[m.start():]
    open(R + '/sitemap.xml', 'w', encoding='utf-8').write(sm)
subprocess.run(['python3', R + '/_ops/search/build.py'], check=True)
print('OK', fn)
