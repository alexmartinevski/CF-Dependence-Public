"use strict";
const COPY = {
 en: {
  papers:"Publications",updates:"What's new",about:"About",eyebrow:"EXTREMAL PROBABILITY · ANALYSIS · ALGEBRA",
  hero:"A research programme on dependence via characteristic functions, sharp inequalities, and the mathematical structures behind their extremizers.",
  areasNav:"By field",areasLabel:"RESEARCH MAP",areasHeading:"Publications by research area",
  areasIntro:"An overview of published articles grouped by their principal research topic. Each entry shows what it covers, the last verified release date and version DOI.",
  areasUnavailable:"The subject index is temporarily unavailable. See the complete research papers list below.",
  verifiedAsOf:"Catalogue curated on",zenodoUpdated:"Public Zenodo metadata refreshed on",missingDate:"Date not independently verified",releaseDate:"Publication date",
  versionIdentifier:"Verified version DOI",openLatest:"Open latest version",
  latestPublished:"Latest published record (Concept DOI)",lastVerifiedDate:"Last verified release date",
  verifiedVersionDOI:"Last verified version DOI (for citation)",
  doiExplanation:"The primary DOI follows the latest published Zenodo record; the version DOI identifies one specific release. Dates and version identifiers are from the last verified catalogue snapshot.",
  olderPdf:"Archived PDF",olderTex:"Archived TeX",zenodoPDF:"PDF on Zenodo",
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
  areasNav:"По областям",areasLabel:"КАРТА ИССЛЕДОВАНИЙ",areasHeading:"Публикации по научным областям",
  areasIntro:"Все опубликованные статьи сгруппированы по основной тематике. Для каждой приведены содержание, дата и DOI последней проверенной опубликованной версии.",
  areasUnavailable:"Тематический список временно недоступен. Полный список статей приведён ниже.",
  verifiedAsOf:"Каталог сверён по состоянию на",zenodoUpdated:"Публичные данные Zenodo обновлены",missingDate:"Дата не подтверждена",releaseDate:"Дата публикации",
  versionIdentifier:"DOI проверенной версии",openLatest:"Открыть актуальную версию",
  latestPublished:"Актуальная публикация (Concept DOI)",lastVerifiedDate:"Дата последней проверенной публикации",
  verifiedVersionDOI:"DOI проверенной версии (для цитирования)",
  doiExplanation:"Основной DOI ведёт к последней опубликованной версии Zenodo. DOI версии закреплён за конкретным выпуском. Даты и идентификаторы версии приводятся по последнему проверенному состоянию каталога.",
  olderPdf:"Архивный PDF",olderTex:"Архивный TeX",zenodoPDF:"PDF в Zenodo",
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
const RESEARCH_AREAS = [
  {id:"extremal",name:{en:"Extremal dependence and sharp inequalities",ru:"Экстремальная зависимость и точные неравенства"},
   description:{en:"Universal bounds, extremal profiles, stability and higher-order interaction measures.",
    ru:"Универсальные оценки, экстремальные профили, устойчивость и многомерные меры взаимодействия."}},
  {id:"transport",name:{en:"Prescribed marginals and optimal transport",ru:"Заданные маргинали и оптимальный транспорт"},
   description:{en:"Couplings, mixability, transport geometry and the construction of prescribed dependence.",
    ru:"Совместные распределения, смешиваемость, геометрия транспорта и синтез зависимости."}},
  {id:"algebra",name:{en:"Polynomial algebra, Galois theory and moments",ru:"Алгебра полиномов, теория Галуа и моменты"},
   description:{en:"Chebyshev–Lucas polynomials, critical points, resultants and arithmetic moment reconstruction.",
    ru:"Полиномы Чебышёва—Люкаса, критические точки, результанты и арифметика моментов."}},
  {id:"harmonic",name:{en:"Harmonic analysis and inverse problems",ru:"Гармонический анализ и обратные задачи"},
   description:{en:"Recovering hidden structures from Fourier, Walsh and finite-group observations.",
    ru:"Восстановление скрытых структур по наблюдениям Фурье, Уолша и конечных групп."}},
  {id:"statistics",name:{en:"Statistical tests and estimation",ru:"Статистические критерии и оценивание"},
   description:{en:"Independence tests, robust methods and estimating dependence functionals.",
    ru:"Критерии независимости, робастные методы и оценивание функционалов зависимости."}}
];
const DOI = /^10\.5281\/zenodo\.\d+$/;
let language = new URLSearchParams(location.search).get("lang") === "ru" ? "ru" : "en";
let papers = [];
let news = [];
let catalogueDate = "";
let zenodoCheckedDate = "";
let zenodoResolvedCount = 0;
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
  children(foot,detail,doiLink(p.concept_doi,COPY[language].openLatest));
  return children(card,top,title,desc,tags,foot);
}
function renderAreas() {
  const container=$("area-groups");
  if(!container)return;
  const note=$("area-snapshot");
  note.textContent=COPY[language].verifiedAsOf+": "+(catalogueDate||"—")+"."+(zenodoResolvedCount>0?" "+COPY[language].zenodoUpdated+": "+zenodoCheckedDate+" ("+zenodoResolvedCount+"/"+papers.length+").":"");
  container.replaceChildren();
  for(const area of RESEARCH_AREAS) {
    const members=papers.filter(p=>p.area===area.id);
    if(!members.length)continue;
    const group=node("section","area-group");
    const heading=node("div","area-group-heading");
    const title=node("h3",null,area.name[language]);
    const count=node("span","area-group-count",String(members.length));
    const description=node("p","area-group-description",area.description[language]);
    heading.append(title,count,description);
    const rows=node("div","area-rows");
    for(const p of members) {
      const item=node("article","area-row");
      const main=node("div","area-row-main");
      const headline=node("div","area-headline");
      const link=node("a","area-paper-link",p.title);
      link.href="paper.html?code="+encodeURIComponent(p.code)+"&lang="+language;
      headline.append(node("span","code",p.code),link);
      main.append(headline,node("p","area-paper-summary",p.summary[language]||p.summary.en));
      const meta=node("div","area-row-meta");
      const dateBlock=node("div","area-metadata-line");
      dateBlock.appendChild(node("span","area-meta-label",COPY[language].releaseDate));
      if(typeof p.published_on==="string" && /^\d{4}-\d{2}-\d{2}$/.test(p.published_on)) {
        const time=node("time","area-meta-value",p.published_on);
        time.dateTime=p.published_on;
        dateBlock.appendChild(time);
      } else dateBlock.appendChild(node("span","area-meta-value",COPY[language].missingDate));
      const versionBlock=node("div","area-metadata-line");
      versionBlock.append(node("span","area-meta-label",COPY[language].versionIdentifier),doiLink(p.version_doi,(p.version_label?p.version_label+" · ":"")+p.version_doi));
      const current=doiLink(p.concept_doi,COPY[language].openLatest);
      current.className="area-latest-link";
      meta.append(dateBlock,versionBlock,current);
      item.append(main,meta);
      rows.appendChild(item);
    }
    group.append(heading,rows);
    container.appendChild(group);
  }
  if(!container.children.length)
    container.appendChild(node("p","muted",COPY[language].areasUnavailable));
}
function renderIndex() {
  applyLanguage();
  try { renderAreas(); }
  catch (error) {
    // Never leave a permanent "Loading…" placeholder if only the optional
    // subject directory fails; the main paper catalogue must still render.
    const areaContainer=$("area-groups");
    if(areaContainer)areaContainer.replaceChildren(node("p","muted",COPY[language].areasUnavailable));
    console.error("Subject directory rendering failed",error);
  }
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
  $("paper-latest").replaceChildren(doiLink(p.concept_doi,COPY[language].openLatest));
  $("paper-version").replaceChildren(doiLink(p.version_doi,(p.version_label?p.version_label+" · ":"")+p.version_doi));
  $("paper-release-date").textContent=p.published_on||COPY[language].missingDate;
  const links=$("paper-downloads");links.replaceChildren();
  const downloads=[];
  // The current PDF must be retrieved from the Zenodo concept record, never
  // mistaken for an older GitHub snapshot or an exact-version record URL.
  downloads.push([COPY[language].zenodoPDF,"https://doi.org/"+p.concept_doi]);
  if (p.source_path) {
    downloads.push([COPY[language].olderPdf,publicRepoLink(p,"paper.pdf")]);
    downloads.push([COPY[language].olderTex,publicRepoLink(p,"paper.tex")]);
    downloads.push([COPY[language].source,publicRepoLink(p,null)]);
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
    const [a,b]=await Promise.all([fetch("data/papers.json",{cache:"no-store"}),fetch("data/news.json",{cache:"no-store"})]);
    if(!a.ok||!b.ok)throw new Error("Unable to load");
    const pdata=await a.json(), ndata=await b.json();
    papers=verifiedPapers(pdata.papers).sort((x,y)=>Number(x.code.slice(1))-Number(y.code.slice(1)));
    catalogueDate=typeof pdata.last_curated_on==="string"?pdata.last_curated_on:"";
    // Optional same-origin metadata generated by read-only Zenodo API at deploy time.
    // When unavailable, the explicitly dated curated catalogue remains the fallback.
    try {
      const r=await fetch("data/zenodo_latest.json",{cache:"no-store"});
      if(r.ok) {
        const latest=await r.json();
        if(latest.schema===1 && latest.records && typeof latest.records==="object") {
          let resolved=0;
          for(const p of papers) {
            const item=latest.records[p.code];
            if(!item || item.concept_doi!==p.concept_doi || !DOI.test(item.version_doi))continue;
            const changed=item.version_doi!==p.version_doi;
            p.version_doi=item.version_doi;
            if(typeof item.published_on==="string" && /^\d{4}-\d{2}-\d{2}$/.test(item.published_on))
              p.published_on=item.published_on;
            else if(changed) delete p.published_on;
            if(typeof item.version_label==="string" && /^[A-Za-z0-9][A-Za-z0-9._+\- ]{0,47}$/.test(item.version_label))
              p.version_label=item.version_label;
            else delete p.version_label;
            resolved++;
          }
          zenodoResolvedCount=resolved;
          if(typeof latest.checked_on==="string" && /^\d{4}-\d{2}-\d{2}$/.test(latest.checked_on))
            zenodoCheckedDate=latest.checked_on;
        }
      }
    }catch(error) {
      // No public metadata must never break the site's published catalogue.
    }
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
