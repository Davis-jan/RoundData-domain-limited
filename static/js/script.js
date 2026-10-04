const nav=document.querySelector('.navwrap');
window.addEventListener('scroll',()=>nav?.classList.toggle('scrolled',window.scrollY>20));
const menuBtn=document.querySelector('.menu-btn'); const mainnav=document.querySelector('.mainnav');
menuBtn?.addEventListener('click',()=>{const open=mainnav.classList.toggle('open');menuBtn.setAttribute('aria-expanded',open);menuBtn.innerHTML=open?'<i class="fa-solid fa-xmark"></i>':'<i class="fa-solid fa-bars"></i>';});
document.querySelectorAll('.dropdown>button').forEach(btn=>btn.addEventListener('click',e=>{if(innerWidth<=900){e.preventDefault();btn.parentElement.classList.toggle('open')}}));
document.querySelectorAll('.faqitem button').forEach(btn=>btn.addEventListener('click',()=>{const item=btn.parentElement;document.querySelectorAll('.faqitem').forEach(x=>{if(x!==item)x.classList.remove('open')});item.classList.toggle('open')}));
const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target)}}),{threshold:.12});document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
