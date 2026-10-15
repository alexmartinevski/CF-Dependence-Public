"use strict";
/* Progressive enhancement only. Scientific abstracts and citation metadata
   remain visible in the original HTML, without JavaScript. */
(() => {
  let language=new URLSearchParams(window.location.search).get("lang")==="ru"?"ru":"en";
  function applyLanguage() {
    document.querySelectorAll("[data-en][data-ru]").forEach(el=>{
      el.textContent=el.getAttribute(language==="ru"?"data-ru":"data-en");
      el.setAttribute("lang",language);
    });
    document.querySelectorAll("[data-preserve-lang]").forEach(el=>{
      const href=el.getAttribute("data-base-href");
      if(!href)return;
      const url=new URL(href,document.baseURI);
      url.searchParams.set("lang",language);
      el.href=url.href;
    });
    document.querySelectorAll("[data-lang-toggle]").forEach(button=>{
      button.textContent=language==="ru"?"English":"Русский";
      button.setAttribute("aria-label",language==="ru"?"Switch interface to English":"Переключить интерфейс на русский");
    });
  }
  document.querySelectorAll("[data-lang-toggle]").forEach(button=>{
    button.addEventListener("click",()=>{
      language=language==="ru"?"en":"ru";
      const url=new URL(window.location.href);
      url.searchParams.set("lang",language);
      history.replaceState(null,"",url.href);
      applyLanguage();
    });
  });
  applyLanguage();
})();
