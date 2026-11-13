/* 카드뉴스·메뉴 공통 스크립트 (모든 페이지 공용) */
(function(){
  /* 1) 모바일 메뉴: 항목을 누르면 메뉴를 닫음 */
  var nav=document.querySelector('.nav');
  if(nav){[].forEach.call(nav.querySelectorAll('a'),function(a){a.addEventListener('click',function(){nav.classList.remove('open');});});}

  /* 2) 홈 '카드뉴스' 갤러리: 칼럼 목록에서 자동으로 만듦 */
  var g=document.getElementById('cnGallery');
  if(g){
    var seen={},html='',lim=+(g.getAttribute('data-limit')||999),cnt=0;
    [].forEach.call(document.querySelectorAll('#column .col-card'),function(c){
      var href=c.getAttribute('href')||'';var m=href.match(/\/column\/(\d+)-/);if(!m||seen[m[1]]||cnt>=lim)return;seen[m[1]]=1;cnt++;
      var t=(c.querySelector('h3')||{}).textContent||'';var cat=(c.querySelector('.cat')||{}).textContent||'';
      html+='<a class="cg-item" href="'+href+'#cn"><span class="cg-img"><img src="/assets/cardnews/'+m[1]+'/1.jpg" alt="'+t.replace(/"/g,'')+' 카드뉴스" loading="lazy"><em>카드뉴스 7장 ›</em></span><span class="cg-cat">'+cat+'</span><b>'+t+'</b></a>';
    });
    g.innerHTML=html;
  }

  /* 3) 카드뉴스 넘김: 쪽수·점·안내 표시, 모바일에서도 화살표 */
  [].forEach.call(document.querySelectorAll('.cn'),function(cn){
    var tr=cn.querySelector('.cn-track');if(!tr)return;var imgs=tr.querySelectorAll('img');var n=imgs.length;if(!n)return;
    var ui=document.createElement('div');ui.className='cn-ui';
    var dots='';for(var i=0;i<n;i++)dots+='<i></i>';
    ui.innerHTML='<span class="cn-cnt"><b>1</b> / '+n+'</span><span class="cn-dots">'+dots+'</span><span class="cn-hint">옆으로 넘겨 보세요 ›</span>';
    cn.parentNode.insertBefore(ui,cn.nextSibling);
    var ds=ui.querySelectorAll('.cn-dots i');
    function upd(){var w=imgs[0].getBoundingClientRect().width+14;var k=Math.min(n-1,Math.round(tr.scrollLeft/w));
      ui.querySelector('.cn-cnt b').textContent=k+1;[].forEach.call(ds,function(d,j){d.className=j===k?'on':'';});
      cn.classList.toggle('at-start',tr.scrollLeft<5);cn.classList.toggle('at-end',tr.scrollLeft+tr.clientWidth>=tr.scrollWidth-5);}
    [].forEach.call(ds,function(d,j){d.addEventListener('click',function(){var w=imgs[0].getBoundingClientRect().width+14;tr.scrollTo({left:j*w,behavior:'smooth'});});});
    tr.addEventListener('scroll',function(){window.requestAnimationFrame(upd);});upd();
  });


  /* 5) 목록 줄이기: data-more="N" → 처음 N개만 보이고 '더 보기'로 펼침(data-nobtn 이면 버튼 없이 숨김만) */
  [].forEach.call(document.querySelectorAll('[data-more]'),function(box){
    var n=+box.getAttribute('data-more');var items=[].filter.call(box.children,function(e){return e.nodeType===1&&(e.tagName==='ARTICLE'||e.tagName==='A'||e.tagName==='LI');});
    if(items.length<=n)return;
    items.forEach(function(e,i){if(i>=n)e.classList.add('is-hidden');});
    if(box.hasAttribute('data-nobtn'))return;
    var unit=box.getAttribute('data-unit')||'개';var lb=box.getAttribute('data-label')||'더 보기';
    var b=document.createElement('button');b.type='button';b.className='more-btn';
    var open=false;function txt(){b.innerHTML=open?'접기 ▲':lb+' <small>('+(items.length-n)+unit+' 더)</small> ▼';}txt();
    b.addEventListener('click',function(){open=!open;items.forEach(function(e,i){if(i>=n)e.classList.toggle('is-hidden',!open);});txt();if(!open)box.scrollIntoView({block:'start',behavior:'smooth'});});
    box.parentNode.insertBefore(b,box.nextSibling);
  });

  /* 6) 칼럼 목록 페이지: 세목 탭 + 12편씩 더 보기 */
  var cl=document.querySelector('.col-list[data-filter]');
  if(cl){
    var cards=[].slice.call(cl.querySelectorAll('.col-card'));var page=+(cl.getAttribute('data-filter')||12);
    var tabs=[['전체',''],['양도소득세','양도'],['상속세','상속'],['증여세','증여'],['종합소득세','종합소득'],['법인세','법인'],['부가가치세·기타','부가|취득']];
    var cur='',shown=page,q='',idx=null,loading=false;
    /* 검색창: 제목·세목은 바로, 본문은 /assets/search.json 색인으로 찾음 */
    var sb=document.createElement('div');sb.className='csearch';
    sb.innerHTML='<span class="ic">🔍</span><input type="search" placeholder="검색어 입력 (예: 증여공제, 1주택)" aria-label="칼럼 검색"><button type="button" class="x" aria-label="지우기">✕</button>';
    cl.parentNode.insertBefore(sb,cl);
    var inp=sb.querySelector('input'),xb=sb.querySelector('.x');
    var info=document.createElement('p');info.className='csearch-info';cl.parentNode.insertBefore(info,cl);
    function norm(s){return (s||'').toLowerCase().replace(/[\s·・,.()"'“”‘’\-—~]/g,'');}
    function words(){return q.split(/\s+/).map(norm).filter(Boolean);}
    function loadIdx(){if(idx||loading||!window.fetch)return;loading=true;fetch('/assets/search.json').then(function(r){return r.json();}).then(function(j){idx={};j.forEach(function(o){idx[o.u]=norm(o.t+' '+o.d+' '+o.x);});render();}).catch(function(){});}
    function hit(x){var w=words();if(!w.length)return true;var h=x.getAttribute('href')||'';var txt=norm(x.textContent)+(idx&&idx[h]?idx[h]:'');return w.every(function(k){return txt.indexOf(k)>=0;});}
    var tmr;inp.addEventListener('input',function(){clearTimeout(tmr);tmr=setTimeout(function(){q=inp.value.trim();shown=page;loadIdx();render();},200);});
    xb.addEventListener('click',function(){inp.value='';q='';render();inp.focus();});
    var bar=document.createElement('div');bar.className='ftabs';
    tabs.forEach(function(t){var k=t[1];var c=cards.filter(function(x){return !k||new RegExp(k).test((x.querySelector('.cat')||{}).textContent||'');}).length;if(!c)return;
      var bt=document.createElement('button');bt.type='button';bt.innerHTML=t[0]+' <small>'+c+'</small>';if(!k)bt.className='on';
      bt.addEventListener('click',function(){cur=k;shown=page;[].forEach.call(bar.children,function(z){z.className='';});bt.className='on';render();});bar.appendChild(bt);});
    cl.parentNode.insertBefore(bar,cl);
    var mb=document.createElement('button');mb.type='button';mb.className='more-btn';cl.parentNode.insertBefore(mb,cl.nextSibling);
    mb.addEventListener('click',function(){shown+=page;render();});
    function render(){var k=0,tot=0;cards.forEach(function(x){var ok=(!cur||new RegExp(cur).test((x.querySelector('.cat')||{}).textContent||''))&&hit(x);if(ok)tot++;var vis=ok&&k<shown;if(ok)k++;x.classList.toggle('is-hidden',!vis);});
      var left=tot-Math.min(tot,shown);mb.style.display=left>0?'':'none';mb.innerHTML='칼럼 더 보기 <small>('+left+'편 더)</small> ▼';
      xb.style.display=q?'':'none';
      info.innerHTML=q?(tot?'‘<b>'+q.replace(/</g,'&lt;')+'</b>’ 검색 결과 <b>'+tot+'</b>편':'‘<b>'+q.replace(/</g,'&lt;')+'</b>’에 맞는 칼럼이 없습니다. 다른 낱말로 찾아보시거나 <a href="https://pf.kakao.com/_wdZNX/chat">카카오톡으로 물어봐 주세요</a>.')+(q&&!idx?' <small>(본문까지 찾는 중…)</small>':''):'';}
    var qs=(location.search.match(/[?&]q=([^&]*)/)||[])[1];if(qs){try{q=decodeURIComponent(qs.replace(/\+/g,' ')).trim();}catch(e){}inp.value=q;loadIdx();}
    render();
  }

  /* 7) 모바일: 업무분야 카드 눌러서 펼치기, 소식 본문 3줄 요약 + '자세히' */
  [].forEach.call(document.querySelectorAll('.svc-card'),function(c){c.addEventListener('click',function(){if(window.innerWidth<=600)c.classList.toggle('open');});});
  [].forEach.call(document.querySelectorAll('.nw-acc .nw'),function(a){a.addEventListener('click',function(e){if(e.target.closest('a'))return;a.classList.toggle('open');});});
  if(window.innerWidth<=600){[].forEach.call(document.querySelectorAll('#news .nw-list:not(.nw-acc) .nw p, #press-x .nw p'),function(p){
    p.classList.add('clamp');if(p.scrollHeight<=p.clientHeight+2){p.classList.remove('clamp');return;}
    var b=document.createElement('button');b.type='button';b.className='nw-more';b.textContent='자세히 보기 ▾';
    b.addEventListener('click',function(){var c=p.classList.toggle('clamp');b.textContent=c?'자세히 보기 ▾':'접기 ▴';});p.parentNode.insertBefore(b,p.nextSibling);});}

  /* 8) 홈 '정부 보도자료' 미니 목록: /press/ 페이지에서 최근 3건을 가져와 같은 아코디언으로 표시 */
  var pm=document.getElementById('pressMini');
  if(pm&&window.fetch){fetch('/press/').then(function(r){return r.text();}).then(function(h){
    var d=new DOMParser().parseFromString(h,'text/html');var arts=[].slice.call(d.querySelectorAll('.nw-list .nw')).slice(0,3);
    pm.innerHTML=arts.map(function(a){var id=a.id||'';var dt=a.querySelector('.nw-d');var tag=a.querySelector('.nw-tag');var h4=a.querySelector('h4');var p=a.querySelector('p');
      return '<article class="'+a.className+'">'+(dt?dt.outerHTML:'')+'<div>'+(tag?tag.outerHTML:'')+(h4?h4.outerHTML:'')+(p?p.outerHTML:'')+'<div class="nw-src"><a href="/press/'+(id?'#'+id:'')+'">자세히 보기(체크포인트·출처) ›</a></div></div></article>';}).join('');
    [].forEach.call(pm.querySelectorAll('.nw'),function(a){a.addEventListener('click',function(e){if(e.target.closest('a'))return;a.classList.toggle('open');});});
  }).catch(function(){});}

  /* 4) 칼럼 주소 끝이 #cn 이면 카드뉴스 위치로 이동 */
  if(location.hash==='#cn'){var c=document.querySelector('.cn');if(c)setTimeout(function(){c.scrollIntoView({block:'start'});},200);}
})();
