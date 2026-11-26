// 세무 쇼츠 목록: /assets/shorts/list.json — 주차별로 최신 주가 맨 앞, 같은 주 안에서는 1편→7편 순서. 새 주의 7편은 목록 맨 앞에 순서대로 끼워 넣습니다.
(function(){
  var box=document.getElementById('shortsGallery'); if(!box) return;
  var limit=parseInt(box.getAttribute('data-limit')||'0',10);
  fetch('/assets/shorts/list.json?v='+Date.now().toString().slice(0,7)).then(function(r){return r.json()}).then(function(L){
    if(limit) L=L.slice(0,limit);
    box.innerHTML=L.map(function(s){
      return '<div class="sg-item"><div class="sg-v"><video src="/assets/shorts/'+s.id+'.mp4" poster="/assets/shorts/'+s.id+'.jpg" preload="none" playsinline controls></video></div>'+
        '<span class="cg-cat">'+s.cat+'</span><b>'+s.title+'</b>'+
        (s.col?'<a class="sg-col" href="'+s.col+'">관련 칼럼 읽기 ›</a>':'')+'</div>';
    }).join('');
    // 한 번에 하나만 재생
    var vs=box.querySelectorAll('video');
    vs.forEach(function(v){v.addEventListener('play',function(){vs.forEach(function(o){if(o!==v)o.pause()})})});
  });
})();
