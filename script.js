(function(){
  "use strict";
  var $=function(s,c){return (c||document).querySelector(s)};
  var $$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};

  // year
  // hydrate embedded images from registry (keeps each base64 stored once)
  var IMG=window.__IMG__||{};
  $$('[data-img]').forEach(function(el){ var k=el.getAttribute('data-img'); if(IMG[k]) el.src=IMG[k]; });

  var yr=$('#yr'); if(yr) yr.textContent=new Date().getFullYear();

  // nav bg on scroll
  var nav=$('#nav');
  var onScroll=function(){ nav.classList.toggle('scrolled', window.scrollY>40); };
  onScroll(); window.addEventListener('scroll',onScroll,{passive:true});

  // mobile menu
  var toggle=$('.nav__toggle'), menu=$('#menu');
  function setMenu(open){
    menu.hidden=!open; toggle.classList.toggle('open',open);
    toggle.setAttribute('aria-expanded',open?'true':'false');
    document.body.classList.toggle('noscroll',open);
  }
  toggle.addEventListener('click',function(){ setMenu(menu.hidden); });
  $$('#menu a').forEach(function(a){a.addEventListener('click',function(){setMenu(false);});});

  // reveal on scroll
  var io;
  if('IntersectionObserver' in window){
    io=new IntersectionObserver(function(ents){
      ents.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} });
    },{threshold:.14, rootMargin:'0px 0px -8% 0px'});
    $$('.reveal').forEach(function(el){io.observe(el);});
  } else { $$('.reveal').forEach(function(el){el.classList.add('in');}); }

  // ---- PROJECT MODALS ----
  var overlay=$('#overlay'), lastFocus=null;
  function openProject(id){
    var art=$('#project-'+id); if(!art) return;
    lastFocus=document.activeElement;
    overlay.hidden=false; document.body.classList.add('noscroll');
    $$('.project',overlay).forEach(function(p){p.hidden=(p!==art);});
    art.scrollTop=0; overlay.scrollTop=0;
    var c=$('.project__close',art); if(c) c.focus();
    initSliders(art);
  }
  function closeProject(){
    overlay.hidden=true; document.body.classList.remove('noscroll');
    if(lastFocus&&lastFocus.focus) lastFocus.focus();
  }
  $$('.work-card').forEach(function(btn){
    btn.addEventListener('click',function(){ openProject(btn.getAttribute('data-project')); });
  });
  $$('[data-close]').forEach(function(b){b.addEventListener('click',closeProject);});
  overlay.addEventListener('click',function(e){ if(e.target===overlay) closeProject(); });

  // ---- LIGHTBOX ----
  var lb=$('#lightbox'), lbImg=$('#lightboxImg');
  function openLightbox(src){ lbImg.src=src; lb.hidden=false; document.body.classList.add('noscroll'); $('.lightbox__close').focus(); }
  function closeLightbox(){ lb.hidden=true; lbImg.src=''; if(!overlay.hidden){document.body.classList.add('noscroll');} else {document.body.classList.remove('noscroll');} }
  document.addEventListener('click',function(e){
    var g=e.target.closest?e.target.closest('.g-item'):null;
    if(g){ var k=g.getAttribute('data-full'); openLightbox(IMG[k]||k); }
  });
  $('.lightbox__close').addEventListener('click',closeLightbox);
  lb.addEventListener('click',function(e){ if(e.target===lb) closeLightbox(); });

  // ESC handling
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape'){
      if(!lb.hidden){ closeLightbox(); }
      else if(!overlay.hidden){ closeProject(); }
      else if(!menu.hidden){ setMenu(false); }
    }
  });

  // ---- BEFORE / AFTER SLIDERS ----
  function initSliders(scope){
    $$('.ba',scope).forEach(function(ba){
      if(ba.dataset.init) return; ba.dataset.init='1';
      var before=$('.ba-before',ba), line=$('.ba-line',ba), handle=$('.ba-handle',ba);
      var pos=50, dragging=false;
      function set(p){
        pos=Math.max(2,Math.min(98,p));
        before.style.clipPath='inset(0 '+(100-pos)+'% 0 0)';
        line.style.left=pos+'%'; handle.style.left=pos+'%';
        handle.setAttribute('aria-valuenow',Math.round(pos));
      }
      function fromEvent(e){
        var r=ba.getBoundingClientRect();
        var x=(e.touches?e.touches[0].clientX:e.clientX)-r.left;
        set(x/r.width*100);
      }
      ba.addEventListener('pointerdown',function(e){ dragging=true; ba.setPointerCapture&&ba.setPointerCapture(e.pointerId); fromEvent(e); });
      ba.addEventListener('pointermove',function(e){ if(dragging) fromEvent(e); });
      window.addEventListener('pointerup',function(){ dragging=false; });
      handle.addEventListener('keydown',function(e){
        if(e.key==='ArrowLeft'){ set(pos-3); e.preventDefault(); }
        if(e.key==='ArrowRight'){ set(pos+3); e.preventDefault(); }
      });
      set(50);
    });
  }

  // ---- CONTACT FORM ----
  // Paste your Zapier "Catch Hook" webhook URL between the quotes to enable
  // real delivery (Zap sends an SMS text to Rocío + optional Google Sheet log).
  // While empty, the form falls back to opening the visitor's email app.
  var FORM_ENDPOINT='https://hooks.zapier.com/hooks/catch/28252800/4dpqtys/';
  var form=$('#contactForm'), note=$('#formNote');
  // Preferred-contact toggle: show only the field they choose
  var fEmail=$('#field-email'), fPhone=$('#field-phone');
  function pref(){ var r=form.querySelector('input[name=contactpref]:checked'); return r?r.value:'Email'; }
  function syncPref(){ var call=pref()==='Call / Text'; if(fEmail){fEmail.hidden=call;} if(fPhone){fPhone.hidden=!call;} }
  $$('input[name=contactpref]',form).forEach(function(r){ r.addEventListener('change',syncPref); });
  syncPref();
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var name=$('#cf-name').value.trim(), type=$('#cf-type').value, msg=$('#cf-msg').value.trim();
    var p=pref(), email=$('#cf-email').value.trim(), phone=$('#cf-phone').value.trim(), contact;
    if(!name){ note.textContent='Please add your name.'; return; }
    if(p==='Call / Text'){ if(!phone){ note.textContent='Please add a phone number so Rocío can reach you.'; return; } contact=phone; }
    else { if(!email){ note.textContent='Please add your email so Rocío can reach you.'; return; } contact=email; }
    if(!msg){ note.textContent='Please add a short note about your project.'; return; }
    if(!FORM_ENDPOINT){
      var subject=encodeURIComponent('Project inquiry — '+name+' ('+type+')');
      var body=encodeURIComponent('Name: '+name+'\nPreferred contact: '+p+'\n'+(p==='Call / Text'?'Phone: '+phone:'Email: '+email)+'\nProject type: '+type+'\n\n'+msg);
      window.location.href='mailto:zurcfuhrmeister@gmail.com?subject='+subject+'&body='+body;
      note.textContent='Opening your email app… if nothing happens, email zurcfuhrmeister@gmail.com directly.';
      return;
    }
    var btn=form.querySelector('button[type=submit]');
    note.textContent='Sending…'; if(btn){ btn.disabled=true; }
    var params=new URLSearchParams({name:name,preferred:p,email:email,phone:phone,contact:contact,
      type:type,message:msg,source:'rociohomerefresh website'});
    fetch(FORM_ENDPOINT,{method:'POST',mode:'no-cors',
      headers:{'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'},
      body:params.toString()})
      .then(function(){ form.reset(); syncPref(); note.textContent='Thank you — your message is on its way to Rocío. She’ll be in touch soon.'; })
      .catch(function(){ note.textContent='Sorry — something went wrong sending your message. Please email zurcfuhrmeister@gmail.com directly.'; })
      .finally(function(){ if(btn){ btn.disabled=false; } });
  });
})();
