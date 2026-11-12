/* 카드뉴스·메뉴 공통 스크립트 (모든 페이지 공용) */
(function(){
  /* 1) 모바일 메뉴: 항목을 누르면 메뉴를 닫음 */
  var nav=document.querySelector('.nav');
  if(nav){[].forEach.call(nav.querySelectorAll('a'),function(a){a.addEventListener('click',function(){nav.classList.remove('open');});});}

  /* 2) 홈 '카드뉴스' 갤러리: 칼럼 목록에서 자동으로 만듦 */
  var g=document.getElementById('cnGallery');
  if(g){
    var seen={},html='';
    [].forEach.call(document.querySelectorAll('#column .col-card'),function(c){
      var href=c.getAttribute('href')||'';var m=href.match(/\/column\/(\d+)-/);if(!m||seen[m[1]])return;seen[m[1]]=1;
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

  /* 4) 칼럼 주소 끝이 #cn 이면 카드뉴스 위치로 이동 */
  if(location.hash==='#cn'){var c=document.querySelector('.cn');if(c)setTimeout(function(){c.scrollIntoView({block:'start'});},200);}
})();
