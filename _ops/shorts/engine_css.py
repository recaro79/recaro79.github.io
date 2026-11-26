CSS = r"""
@font-face{font-family:NM;src:url(NanumMyeongjo-800.woff2);font-weight:800}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;font-family:"Noto Sans CJK KR",sans-serif;color:#fff;word-break:keep-all}
.sc{position:absolute;inset:0;overflow:hidden}
.dk{color:#16213e}
.bg-sunset{background:linear-gradient(160deg,#ff9a62 0%,#d35d7a 38%,#5b2f7a 70%,#1c1238 100%)}
.bg-mint{background:linear-gradient(170deg,#c9f5e4 0%,#8fe0c5 100%)}
.bg-navy{background:linear-gradient(170deg,#1d2f63 0%,#0e1733 100%)}
.bg-yellow{background:linear-gradient(170deg,#ffe46b 0%,#ffc93a 100%)}
.bg-pink{background:linear-gradient(165deg,#ff7aa0 0%,#f2557f 55%,#c93a6a 100%)}
.bg-night{background:linear-gradient(165deg,#3a4fa0 0%,#22306b 45%,#0e1430 100%)}
.bg-forest{background:linear-gradient(165deg,#5fb98a 0%,#2c7a62 45%,#0f2e28 100%)}
.bg-lilac{background:linear-gradient(170deg,#ece4ff 0%,#c7b6ff 100%)}
.bg-orange{background:linear-gradient(165deg,#ffb15c 0%,#ff7a3d 100%)}
.bg-cream{background:linear-gradient(170deg,#fff8ea 0%,#f3e6cb 100%)}
.bg-sky{background:linear-gradient(170deg,#dff0ff 0%,#a9d4ff 100%)}
.top{position:absolute;left:0;right:0;top:0;height:10px;background:rgba(255,255,255,.25);z-index:9}
.top i{display:block;height:100%;background:#ffd84a}
.ver{position:absolute;left:56px;top:70px;font-size:36px;font-weight:900;text-shadow:0 3px 10px rgba(0,0,0,.3);z-index:5}
.brand{position:absolute;right:56px;top:62px;display:flex;align-items:center;gap:12px;font-family:NM,serif;font-size:34px;font-weight:800;z-index:5;text-shadow:0 2px 8px rgba(0,0,0,.3)}
.brand img{width:54px;height:54px;border-radius:50%;background:#fff;padding:3px}
.dk .ver,.dk .brand{text-shadow:none}
.basis{position:absolute;left:56px;right:56px;top:1560px;font-size:26px;font-weight:600;opacity:.8}
.hl{color:#ffd84a}
.abs{position:absolute}
.ch{position:absolute;display:block}
.mk{background:linear-gradient(transparent 58%,#ffe066 58%)}
/* 움직임 */
@keyframes pop{0%{transform:scale(.2);opacity:0}60%{transform:scale(1.12);opacity:1}100%{transform:scale(1);opacity:1}}
@keyframes up{0%{transform:translateY(80px);opacity:0}100%{transform:none;opacity:1}}
@keyframes left{0%{transform:translateX(-120px);opacity:0}100%{transform:none;opacity:1}}
@keyframes right{0%{transform:translateX(120px);opacity:0}100%{transform:none;opacity:1}}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-22px)}}
@keyframes stamp{0%{transform:scale(3) rotate(-20deg);opacity:0}70%{transform:scale(.9) rotate(4deg);opacity:1}100%{transform:scale(1) rotate(0);opacity:1}}
@keyframes zoom{0%{transform:scale(1)}100%{transform:scale(1.06)}}
@keyframes wig{0%,100%{transform:rotate(-3deg)}50%{transform:rotate(3deg)}}
.a{opacity:0;animation-fill-mode:both}
.pop{animation:pop .5s cubic-bezier(.2,.9,.3,1.2) both}
.up{animation:up .45s ease-out both}
.lf{animation:left .45s ease-out both}
.rt{animation:right .45s ease-out both}
.st{animation:stamp .45s ease-out both}
.bob{animation:bob 1.6s ease-in-out infinite}
@keyframes jog{0%,100%{transform:translateY(0) rotate(-2deg)}50%{transform:translateY(-26px) rotate(2deg)}}
.jog{animation:jog .5s ease-in-out infinite}
@keyframes pant{0%,100%{transform:scale(1)}50%{transform:scale(1.04,0.97)}}
.pant{animation:pant .35s ease-in-out infinite;transform-origin:50% 100%}
.wig{animation:wig 1.2s ease-in-out infinite}
/* 부품 */
.title{font-size:112px;font-weight:900;line-height:1.15;letter-spacing:-4px;text-shadow:0 8px 22px rgba(0,0,0,.45)}
.kick{font-size:46px;font-weight:800}
.bub{position:absolute;background:#fff;color:#1d2433;border-radius:50px 50px 50px 10px;padding:44px 50px;box-shadow:0 16px 34px rgba(0,40,60,.2)}
.bub.r{background:#14254d;color:#fff;border-radius:50px 50px 10px 50px}
.bub .who{font-size:30px;font-weight:800;color:#7a8794;margin-bottom:12px}
.bub.r .who{color:#ffd84a}
.bub .say{font-size:58px;font-weight:900;line-height:1.35;letter-spacing:-1px}
.tile{position:absolute;left:56px;right:56px;height:190px;border-radius:40px;padding:0 50px;display:flex;align-items:center;justify-content:space-between}
.tile .w{font-size:46px;font-weight:800;color:#2a3142}
.tile .m{font-size:112px;font-weight:900;letter-spacing:-4px}
.tile .m small{font-size:44px;letter-spacing:0}
.note{position:absolute;left:56px;right:56px;background:#16213e;color:#fff;border-radius:36px;padding:42px 46px;font-size:48px;font-weight:800;line-height:1.45}
.row{position:absolute;left:56px;right:56px;background:#fff;color:#2a1a24;border-radius:36px;padding:36px 40px;display:flex;gap:30px;align-items:center}
.row .ic{flex:none;width:120px;height:120px;border-radius:28px;display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:900;color:#fff}
.row .tx{font-size:48px;font-weight:800;line-height:1.35}
"""
