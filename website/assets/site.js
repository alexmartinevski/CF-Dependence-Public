"use strict";
const COPY = {
 en: {
  papers:"Publications",updates:"What's new",about:"About",eyebrow:"EXTREMAL PROBABILITY · ANALYSIS · ALGEBRA",
  hero:"A research programme on dependence via characteristic functions, sharp inequalities, and the mathematical structures behind their extremizers.",
  publishedLabel:"PUBLISHED RESEARCH",papersHeading:"Research papers",publishedCount:"published records",
  searchLabel:"Search publications",noMatches:"No publications match your search.",
  newsLabel:"RELEASE HISTORY",updatesHeading:"What's new",
  updatesInfo:"Verified public-release notes only. DOI reservations and private reviews do not appear as publications.",
  aboutLabel:"THE PROJECT",aboutHeading:"About CF Dependence",
  aboutText:"An evolving mathematical research programme bringing together extremal probability, fixed-marginal dependence, and algebraic methods. This catalogue links to published versions and their public research materials.",
  footer:"Only verified published works are listed. Draft DOI ≠ publication.",
  back:"← All papers",researchSummary:"RESEARCH SUMMARY",summary:"Overview",topics:"Research areas",
  versionHistory:"What changed in published versions",bibliography:"BIBLIOGRAPHY",author:"Author",
  versionDOI:"Published version DOI",conceptDOI:"All versions (Concept DOI)",
  published:"Published",details:"View paper",pdf:"PDF",tex:"TeX",source:"Repository",
  emptyHistory:"No verified public version-change notes are available yet.",
  newsEmpty:"No verified public-release notes are available yet.",error:"Unable to load the public catalogue.",
  searchPlaceholder:"Search by title, code or topic",otherLang:"Русский"
 },
 ru: {
  papers:"Работы",updates:"Что изменилось",about:"О проекте",eyebrow:"ЭКСТРЕМАЛЬНАЯ ВЕРОЯТНОСТЬ · АНАЛИЗ · АЛГЕБРА",
  hero:"Исследовательская программа по зависимости через характеристические функции, точным неравенствам и математической структуре экстремалей.",
  publishedLabel:"ОПУБЛИКОВАННЫЕ РАБОТЫ",papersHeading:"Научные статьи",publishedCount:"опубликованные работы",
  searchLabel:"Поиск работ",noMatches:"Ничего не найдено.",
  newsLabel:"ИСТОРИЯ ВЫПУСКОВ",updatesHeading:"Что изменилось",
  updatesInfo:"Только подтверждённые публичные изменения. Резервирование DOI и внутреннее ревью не означают публикацию.",
  aboutLabel:"ПРОЕКТ",aboutHeading:"О CF Dependence",
  aboutText:"Развивающаяся математическая программа, объединяющая экстремальную вероятность, зависимость при фиксированных маргиналях и алгебраические методы. Каталог ведёт к опубликованным версиям и общедоступным научным материалам.",
  footer:"Только подтверждённые опубликованные работы. Зарезервированный DOI ≠ публикация.",
  back:"← Все работы",researchSummary:"СОДЕРЖАНИЕ",summary:"Обзор",topics:"Области исследований",
  versionHistory:"Изменения в опубликованных версиях",bibliography:"БИБЛИОГРАФИЯ",author:"Автор",
  versionDOI:"DOI опубликованной версии",conceptDOI:"Все версии (Concept DOI)",
  published:"Опубликовано",details:"Открыть статью",pdf:"PDF",tex:"TeX",source:"Репозиторий",
  emptyHistory:"Пока нет подтверждённых заметок об изменениях опубликованных версий.",
  newsEmpty:"Пока нет подтверждённых публичных обновлений.",error:"Не удалось загрузить каталог.",
  searchPlaceholder:"Поиск по названию, коду или теме",otherLang:"English"
 }
};
const DOI = /^10\.5281\/zenodo\.\d+$/;
let language = new URLSearchParams(location.search).get("lang") === "ru" ? "ru" : "en";
let papers = [];
let news = [];
const $ = (id) => document.getElementById(id);
function node(tag, className, text) {
  const el = document.createElement(tag);
  if (className) el.className = className;
  if (text !== undefined) el.textContent = text;
  return el;
}
function children(parent, ...nodes) { for(const n of nodes) parent.appendChild(n); return parent; }
function applyLanguage() {
  document.documentElement.lang = language;
  for (const el of document.querySelectorAll("[data-i18n]")) {
    const key=el.dataset.i18n;
    if(COPY[language][key])el.textContent=COPY[language][key];
  }
  const search=$("search"); if(search) search.placeholder=COPY[language].searchPlaceholder;
  for (const btn of document.querySelectorAll("[data-lang-switch]")) btn.textContent=COPY[language].otherLang;
  const url=new URL(location.href); url.searchParams.set("lang",language);
  history.replaceState(null,"",url);
}
function doiLink(doi, label=doi) {
  const el=node("a",null,label+" ↗");
  if (!DOI.test(doi)) { el.removeAttribute("href"); return el; }
  el.href="https://doi.org/"+doi;
  el.target="_blank";el.rel="noopener noreferrer";return el;
}
function publicRepoLink(p, file) {
  if (!/^papers\/[a-z0-9-]+$/.test(p.source_path)) return "#";
  return "https://github.com/alexmartinevski/CF-Dependence-Public/blob/main/"+p.source_path+(file?"/"+file:"");
}
function verifiedPapers(input) {
  if(!Array.isArray(input))throw new Error("Invalid catalogue");
  return input.filter(p=>p.status==="published" && DOI.test(p.version_doi) && DOI.test(p.concept_doi));
}
function renderCard(p) {
  const card=node("article","card");
  const top=node("div","card-top");
  children(top,node("span","code",p.code),node("span","pill",COPY[language].published));
  const title=node("h3",null,p.title);
  const desc=node("p",null,p.summary[language]||p.summary.en);
  const tags=node("div","tags");
  for(const subject of p.topics || [])tags.appendChild(node("span","tag",subject));
  const foot=node("div","card-bottom");
  const detail=node("a",null,COPY[language].details+" ↗");
  detail.href="paper.html?code="+encodeURIComponent(p.code)+"&lang="+language;
  children(foot,detail,node("span","tiny",p.version_doi));
  return children(card,top,title,desc,tags,foot);
}
function renderIndex() {
  applyLanguage();
  const query=($("search")?.value||"").trim().toLocaleLowerCase();
  const matching=papers.filter(p=>[p.code,p.title,p.summary.en,p.summary.ru,...(p.topics||[])].join(" ").toLocaleLowerCase().includes(query));
  const list=$("paper-list"); list.replaceChildren(...matching.map(renderCard));
  $("paper-count").textContent=String(matching.length);
  $("no-matches").classList.toggle("hidden",matching.length!==0);
  renderUpdates($("news-items"),true);
}
function story(date, title, summary, source) {
  const article=node("article","news-item");
  const time=node("time",null,date); time.dateTime=date;
  const h=node("h3",null,title);
  const p=node("p",null,summary);
  article.append(time,h,p);
  if(source && source.startsWith("https://doi.org/")) {
    const a=node("a",null,source.slice("https://doi.org/".length)+" ↗");
    a.href=source;a.target="_blank";a.rel="noopener noreferrer";article.append(a);
  }
  return article;
}
function allUpdates() {
  const items=[...news.map(x=>({date:x.date,title:x.title[language],summary:x.summary[language],source:x.source||null}))];
  for (const p of papers) for (const c of p.changes||[]) {
    if (!DOI.test(c.doi) || !c.date) continue;
    items.push({date:c.date,title:p.code+" · "+p.title,summary:c.summary[language]||c.summary.en,source:"https://doi.org/"+c.doi});
  }
  return items.sort((a,b)=>b.date.localeCompare(a.date));
}
function renderUpdates(parent, includeSiteNews) {
  const events=includeSiteNews?allUpdates():[];
  parent.replaceChildren();
  if(!events.length){parent.appendChild(node("p","muted",COPY[language].newsEmpty));return;}
  for(const e of events)parent.appendChild(story(e.date,e.title,e.summary,e.source));
}
function renderDetail() {
  applyLanguage();
  const code=new URLSearchParams(location.search).get("code");
  const p=papers.find(x=>x.code===code);
  if(!p){$("paper-title").textContent=COPY[language].error;return;}
  document.title=p.title+" — CF Dependence";
  $("paper-code").textContent=p.code+" · "+COPY[language].published;
  $("paper-title").textContent=p.title;
  $("paper-summary").textContent=p.summary[language]||p.summary.en;
  $("paper-description").textContent=p.summary[language]||p.summary.en;
  const tags=$("paper-topics");tags.replaceChildren(...(p.topics||[]).map(x=>node("span","tag",x)));
  $("paper-doi").replaceChildren(doiLink(p.version_doi));
  $("paper-concept").replaceChildren(doiLink(p.concept_doi));
  const links=$("paper-downloads");links.replaceChildren();
  const downloads=[];
  if (p.source_path) {
    downloads.push(["PDF",publicRepoLink(p,"paper.pdf")]);
    downloads.push(["TeX",publicRepoLink(p,"paper.tex")]);
    downloads.push([COPY[language].source,publicRepoLink(p,null)]);
  } else if (typeof p.record_url==="string" && /^https:\/\/zenodo\.org\/records\/\d+$/.test(p.record_url)) {
    downloads.push([COPY[language].pdf+" · Zenodo",p.record_url]);
  }
  for(const [name,url] of downloads){const a=node("a",null,name+" ↗");a.href=url;a.target="_blank";a.rel="noopener noreferrer";links.appendChild(a);}
  const history=$("paper-history");history.replaceChildren();
  const changes=(p.changes||[]).filter(x=>DOI.test(x.doi)).sort((a,b)=>b.date.localeCompare(a.date));
  if(!changes.length)history.appendChild(node("p","muted",COPY[language].emptyHistory));
  else for(const c of changes)history.appendChild(story(c.date,c.version||p.title,c.summary[language]||c.summary.en,"https://doi.org/"+c.doi));
}
async function init() {
  const buttons=document.querySelectorAll("[data-lang-switch]");
  for(const b of buttons)b.addEventListener("click",()=>{language=language==="en"?"ru":"en";if(document.body.dataset.page==="index")renderIndex();else renderDetail();});
  applyLanguage();
  try{
    const [a,b]=await Promise.all([fetch("data/papers.json"),fetch("data/news.json")]);
    if(!a.ok||!b.ok)throw new Error("Unable to load");
    const pdata=await a.json(), ndata=await b.json();
    papers=verifiedPapers(pdata.papers).sort((x,y)=>Number(x.code.slice(1))-Number(y.code.slice(1)));
    news=Array.isArray(ndata.entries)?ndata.entries:[];
    if(document.body.dataset.page==="index") {
      $("search").addEventListener("input",renderIndex);
      renderIndex();
    } else renderDetail();
  }catch(error) {
    const target=$("paper-list")||$("paper-title");
    if(target)target.textContent=COPY[language].error;
  }
}
document.addEventListener("DOMContentLoaded",init);
