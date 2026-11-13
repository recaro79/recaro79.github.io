/* 연락처 저장 버튼: 휴대폰에서 파일 다운로드 대신 '연락처 추가' 화면이 바로 열리게 함
   연락처 내용은 /contact.vcf 한 곳에서만 관리합니다(이 파일은 고칠 필요 없음). */
(function(){
  var ua=navigator.userAgent;
  var and=/Android/i.test(ua);
  var ios=/iPhone|iPad|iPod/i.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
  var kakao=/KAKAOTALK/i.test(ua);
  var V=location.origin+'/contact.vcf';
  var e=encodeURIComponent;
  var AND=null;
  /* 안드로이드: contact.vcf 내용을 읽어 연락처 앱의 '새 연락처' 화면을 채운 채로 엶 (안 되면 vcf 파일로 대체) */
  if(and&&window.fetch){
    fetch(V).then(function(r){return r.text();}).then(function(t){
      function g(re){var m=t.match(re);return m?m[1].trim():'';}
      var x={name:g(/^FN:(.*)$/m),company:g(/^ORG:(.*)$/m),job_title:g(/^TITLE:(.*)$/m),
        phone:g(/^TEL;TYPE=CELL:(.*)$/m),email:g(/^EMAIL[^:]*:(.*)$/m),fax:g(/^TEL;TYPE=FAX[^:]*:(.*)$/m)};
      AND='intent:#Intent;action=android.intent.action.INSERT;type=vnd.android.cursor.dir/raw_contact'
        +';S.name='+e(x.name)+';S.company='+e(x.company)+';S.job_title='+e(x.job_title)
        +';S.phone='+e(x.phone)+';i.phone_type=2'
        +(x.email?';S.email='+e(x.email)+';i.email_type=2':'')
        +(x.fax?';S.secondary_phone='+e(x.fax)+';i.secondary_phone_type=4':'')
        +';S.browser_fallback_url='+e(V)+';end';
    }).catch(function(){});
  }
  [].forEach.call(document.querySelectorAll('a[href$="contact.vcf"]'),function(a){
    a.removeAttribute('download');
    a.addEventListener('click',function(ev){
      if(and&&AND){ev.preventDefault();location.href=AND;}
      else if(ios&&kakao){ev.preventDefault();location.href='kakaotalk://web/openExternal?url='+e(V);}
      /* 아이폰 사파리·PC: vcf를 그대로 열면 '연락처 추가' 화면이 뜸 */
    });
  });
})();
