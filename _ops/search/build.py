# 칼럼 검색용 색인 만들기: python3 _ops/search/build.py  → assets/search.json
import glob,re,json,html,os
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
out=[]
for f in sorted(glob.glob(R+'/column/[0-9]*-*.html'),key=lambda x:int(os.path.basename(x).split('-')[0])):
  s=open(f,encoding='utf-8').read()
  t=re.search(r'<title>(.*?)</title>',s,re.S);t=html.unescape(t.group(1)).split(' | ')[0].strip() if t else ''
  d=re.search(r'<meta name="description" content="(.*?)"',s);d=html.unescape(d.group(1)) if d else ''
  b=re.search(r'<article.*?</article>',s,re.S);b=b.group(0) if b else s
  b=re.sub(r'<(script|style)[\s\S]*?</\1>','',b);b=re.sub(r'<[^>]+>',' ',b);b=html.unescape(b);b=re.sub(r'\s+',' ',b).strip()
  for z in ['홈 › 세무 칼럼 ›','안녕하세요. 세무법인 인성 남기원 세무사입니다.','세무법인 인성 남기원 세무사']: b=b.replace(z,' ')
  b=re.sub(r'\s+',' ',b)
  out.append({'u':'/column/'+os.path.basename(f),'t':t,'d':d,'x':b[:2500]})
open(R+'/assets/search.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,separators=(',',':')))
print(len(out),'편',os.path.getsize(R+'/assets/search.json')//1024,'KB')
