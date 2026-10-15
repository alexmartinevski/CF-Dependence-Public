"use strict";
const COPY = {
 en: {
  papers:"Publications",updates:"What's new",about:"About",eyebrow:"EXTREMAL PROBABILITY · ANALYSIS · ALGEBRA",
  hero:"A research programme on dependence via characteristic functions, sharp inequalities, and the mathematical structures behind their extremizers.",
  programmeLabel:"THE SCIENTIFIC PROGRAMME",programmeHeading:"What CF Dependence studies",
  programmeLead:"The programme originated in characteristic-function measures of dependence and now investigates mathematical interactions through their observations, constraints and extremal properties.",
  programmeObjectHeading:"Research object",
  programmeObject:"For a joint probability law P with marginals P₁, …, P_d, the central object is the signed interaction measure: the difference between the joint law and the product of its marginals.",
  programmeObjectNote:"The Fourier factorization defect is the original observable—not the boundary of the project. Other norms, harmonic representations, transport and interaction observables open different extremal questions.",
  programmeGoalHeading:"Research goal",
  programmeGoal:"Discover new mathematical laws, prove them analytically where possible, and identify common mechanisms that explain entire classes of results rather than isolated examples.",
  programmeMethodHeading:"How the project works",
  programmeMethod:"Explore examples, numerical experiments and counterexamples; extract invariants and essential coordinates; formulate an explicit law, prove it rigorously and test whether the mechanism transfers to other problems. Exact bounds, extremizers, equality and stability are central questions.",
  programmeBridge:"The publications below develop connected parts of this programme: sharp inequalities, prescribed marginals and transport, algebra, harmonic reconstruction and statistics.",
  areasNav:"By field",areasLabel:"RESEARCH MAP",areasHeading:"Publications by research area",
  keyResultsHeading:"Key results",resultsLabel:"Key results",
  resultsFromVersion:"Results described from published version",areasIntro:"An annotated scientific guide: each published article has a short overview and three selected results from its verified text.",
  areasUnavailable:"The publication catalogue could not be displayed. Reload this page and try again.",
  firstPublished:"First publication",lastChanged:"Latest published revision",
  latestVersionNumber:"Latest version",unknownVersion:"Version not verified",zenodoOrdinal:"Zenodo release",
  publicationDateNote:"Dates refer to published Zenodo versions, not edits of this website.",
  verifiedAsOf:"Catalogue curated on",zenodoUpdated:"Public Zenodo metadata refreshed on",missingDate:"Date not independently verified",releaseDate:"Publication date",
  versionIdentifier:"Verified version DOI",openLatest:"Open latest version",
  latestPublished:"Latest published record (Concept DOI)",lastVerifiedDate:"Last verified release date",
  verifiedVersionDOI:"Last verified version DOI (for citation)",
  doiExplanation:"Dates refer to the first and latest published Zenodo releases, not website edits. The concept DOI follows the latest version; the version DOI fixes one release.",
  olderPdf:"Archived PDF",olderTex:"Archived TeX",zenodoPDF:"PDF on Zenodo",
  publishedLabel:"PUBLISHED RESEARCH",papersHeading:"Research papers",publishedCount:"published records",
  searchLabel:"Search publications",noMatches:"No publications match your search.",
  newsLabel:"RELEASE HISTORY",updatesHeading:"What's new",
  updatesInfo:"Verified public-release notes only. DOI reservations and private reviews do not appear as publications.",
  authorNav:"Author",authorLabel:"RESEARCHER",authorHeading:"About the author",
  authorRole:"Independent Researcher",
  aiDisclosureLabel:"RESEARCH TRANSPARENCY",aiDisclosureHeading:"AI collaboration disclosure",
  aiDisclosureText:"CF Dependence research was conducted by the author in collaboration with artificial intelligence (AI) systems. AI assisted with mathematical exploration, developing and critically examining ideas and proofs, and preparing manuscripts. AI systems are not listed as co-authors. The author is responsible for the published mathematical statements, proofs, and conclusions.",
  aboutLabel:"THE PROJECT",aboutHeading:"About CF Dependence",
  aboutText:"An evolving mathematical research programme bringing together extremal probability, fixed-marginal dependence, and algebraic methods. This catalogue links to published versions and their public research materials.",
  footer:"Only verified published works are listed. Draft DOI ≠ publication.",
  back:"← All papers",researchSummary:"RESEARCH SUMMARY",summary:"Overview",topics:"Research areas",
  versionHistory:"What changed in published versions",bibliography:"BIBLIOGRAPHY",author:"Author",
  versionDOI:"Published version DOI",conceptDOI:"All versions (Concept DOI)",
  published:"Published",details:"View paper",pdf:"PDF",tex:"TeX",source:"Repository",
  emptyHistory:"No verified public version-change notes are available yet.",
  newsEmpty:"No verified public-release notes are available yet.",error:"Unable to load the public catalogue.",
  searchPlaceholder:"Search by title, code, result or topic",otherLang:"Русский"
 },
 ru: {
  papers:"Работы",updates:"Что изменилось",about:"О проекте",eyebrow:"ЭКСТРЕМАЛЬНАЯ ВЕРОЯТНОСТЬ · АНАЛИЗ · АЛГЕБРА",
  hero:"Исследовательская программа по зависимости через характеристические функции, точным неравенствам и математической структуре экстремалей.",
  programmeLabel:"НАУЧНАЯ ПРОГРАММА",programmeHeading:"Что исследует CF Dependence",
  programmeLead:"Проект возник из исследования зависимости через характеристические функции и теперь изучает математические структуры взаимодействия, их наблюдения, ограничения и экстремальные свойства.",
  programmeObjectHeading:"Объект исследования",
  programmeObject:"Пусть P — совместное распределение с маргиналями P₁, …, P_d. Основной объект — знаковая мера взаимодействия: разность совместного распределения и произведения его маргиналей.",
  programmeObjectNote:"Дефект факторизации характеристических функций — исходный способ наблюдения, но не граница проекта. Другие нормы, гармонические представления, транспорт и меры взаимодействия открывают новые экстремальные задачи.",
  programmeGoalHeading:"Цель исследования",
  programmeGoal:"Открывать новые математические законы, доказывать их аналитически там, где это возможно, и выявлять общие механизмы, объясняющие целые классы результатов, а не отдельные примеры.",
  programmeMethodHeading:"Как ведётся исследование",
  programmeMethod:"Исследуем примеры, вычислительные эксперименты и контрпримеры; выделяем инварианты и существенные координаты; формулируем явный закон, строго доказываем его и проверяем перенос механизма на другие задачи. В центре внимания — точные границы, экстремизаторы, случаи равенства и устойчивость.",
  programmeBridge:"Публикации ниже раскрывают связанные части программы: точные неравенства, заданные маргинали и транспорт, алгебру, гармонические методы восстановления и статистику.",
  areasNav:"По областям",areasLabel:"КАРТА ИССЛЕДОВАНИЙ",areasHeading:"Публикации по научным областям",
  keyResultsHeading:"Основные результаты",resultsLabel:"Что доказано или установлено",
  resultsFromVersion:"Результаты изложены по опубликованной версии",areasIntro:"Аннотированный научный каталог: для каждой статьи приведены краткий обзор и три выбранных результата из проверенного опубликованного текста.",
  areasUnavailable:"Не удалось отобразить каталог публикаций. Перезагрузите страницу и попробуйте ещё раз.",
  firstPublished:"Первая публикация",lastChanged:"Последнее обновление",
  latestVersionNumber:"Последняя версия",unknownVersion:"Номер версии не подтверждён",zenodoOrdinal:"Выпуск Zenodo",
  publicationDateNote:"Даты относятся к опубликованным версиям Zenodo, а не к изменениям сайта.",
  verifiedAsOf:"Каталог сверён по состоянию на",zenodoUpdated:"Публичные данные Zenodo обновлены",missingDate:"Дата не подтверждена",releaseDate:"Дата публикации",
  versionIdentifier:"DOI проверенной версии",openLatest:"Открыть актуальную версию",
  latestPublished:"Актуальная публикация (Concept DOI)",lastVerifiedDate:"Дата последней проверенной публикации",
  verifiedVersionDOI:"DOI проверенной версии (для цитирования)",
  doiExplanation:"Даты относятся к первой и последней опубликованным версиям Zenodo, а не к правкам сайта. Concept DOI ведёт к актуальной версии, DOI версии фиксирует конкретный выпуск.",
  olderPdf:"Архивный PDF",olderTex:"Архивный TeX",zenodoPDF:"PDF в Zenodo",
  publishedLabel:"ОПУБЛИКОВАННЫЕ РАБОТЫ",papersHeading:"Научные статьи",publishedCount:"опубликованные работы",
  searchLabel:"Поиск работ",noMatches:"Ничего не найдено.",
  newsLabel:"ИСТОРИЯ ВЫПУСКОВ",updatesHeading:"Что изменилось",
  updatesInfo:"Только подтверждённые публичные изменения. Резервирование DOI и внутреннее ревью не означают публикацию.",
  authorNav:"Об авторе",authorLabel:"ИССЛЕДОВАТЕЛЬ",authorHeading:"Об авторе",
  authorRole:"Независимый исследователь",
  aiDisclosureLabel:"ПРОЗРАЧНОСТЬ ИССЛЕДОВАНИЙ",aiDisclosureHeading:"Участие искусственного интеллекта",
  aiDisclosureText:"Исследования CF Dependence выполнялись автором совместно с системами искусственного интеллекта (ИИ). ИИ участвовал в математическом поиске, разработке и критическом анализе идей и доказательств, а также в подготовке рукописей. Системы ИИ не указаны в качестве соавторов. За опубликованные утверждения, доказательства и выводы отвечает автор.",
  aboutLabel:"ПРОЕКТ",aboutHeading:"О CF Dependence",
  aboutText:"Развивающаяся математическая программа, объединяющая экстремальную вероятность, зависимость при фиксированных маргиналях и алгебраические методы. Каталог ведёт к опубликованным версиям и общедоступным научным материалам.",
  footer:"Только подтверждённые опубликованные работы. Зарезервированный DOI ≠ публикация.",
  back:"← Все работы",researchSummary:"СОДЕРЖАНИЕ",summary:"Обзор",topics:"Области исследований",
  versionHistory:"Изменения в опубликованных версиях",bibliography:"БИБЛИОГРАФИЯ",author:"Автор",
  versionDOI:"DOI опубликованной версии",conceptDOI:"Все версии (Concept DOI)",
  published:"Опубликовано",details:"Открыть статью",pdf:"PDF",tex:"TeX",source:"Репозиторий",
  emptyHistory:"Пока нет подтверждённых заметок об изменениях опубликованных версий.",
  newsEmpty:"Пока нет подтверждённых публичных обновлений.",error:"Не удалось загрузить каталог.",
  searchPlaceholder:"Поиск по названию, коду, результатам или теме",otherLang:"English"
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
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/;
function versionName(p) {
  if (typeof p.version_label === "string" && /^[A-Za-z0-9][A-Za-z0-9._+\- ]{0,47}$/.test(p.version_label))
    return p.version_label;
  if (Number.isInteger(p.version_index) && p.version_index > 0)
    return COPY[language].zenodoOrdinal+" №"+p.version_index;
  return COPY[language].unknownVersion;
}
function metadataValueLine(label, value, date=false) {
  const line=node("div","area-metadata-line");
  line.appendChild(node("span","area-meta-label",label));
  if(date && typeof value==="string" && ISO_DATE.test(value)) {
    const stamp=node("time","area-meta-value",value);
    stamp.dateTime=value;
    line.appendChild(stamp);
  } else {
    line.appendChild(node("span","area-meta-value",value || COPY[language].missingDate));
  }
  return line;
}
function lastVersionDate(p) { return p.last_version_on || p.published_on || ""; }
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
function renderAreas(visiblePapers=papers) {
  const container=$("area-groups");
  if(!container)return;
  const note=$("area-snapshot");
  note.textContent=COPY[language].verifiedAsOf+": "+(catalogueDate||"—")+"."+(zenodoResolvedCount>0?" "+COPY[language].zenodoUpdated+": "+zenodoCheckedDate+" ("+zenodoResolvedCount+"/"+papers.length+").":"")+" "+COPY[language].publicationDateNote;
  container.replaceChildren();
  for(const area of RESEARCH_AREAS) {
    const members=visiblePapers.filter(p=>p.area===area.id);
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
      const highlights=node("ul","area-highlights");
      for(const fact of p.highlights||[]) {
        const li=node("li",null,fact[language]||fact.en);
        highlights.appendChild(li);
      }
      const resultHeading=node("p","area-results-label",COPY[language].resultsLabel);
      main.append(resultHeading,highlights);
      const meta=node("div","area-row-meta");
      const firstBlock=metadataValueLine(COPY[language].firstPublished,p.first_published_on,true);
      const updateBlock=metadataValueLine(COPY[language].lastChanged,lastVersionDate(p),true);
      const versionBlock=metadataValueLine(COPY[language].latestVersionNumber,versionName(p));
      const citationBlock=node("div","area-metadata-line");
      citationBlock.append(node("span","area-meta-label",COPY[language].versionIdentifier),doiLink(p.version_doi,p.version_doi));
      const current=doiLink(p.concept_doi,COPY[language].openLatest);
      current.className="area-latest-link";
      meta.append(firstBlock,updateBlock,versionBlock,citationBlock,current);
      // Public scientific claims remain anchored to the version whose text was checked.
      if(DOI.test(p.highlights_source_doi) && p.highlights_source_doi!==p.version_doi) {
        const provenance=node("div","area-metadata-line");
        provenance.append(node("span","area-meta-label",COPY[language].resultsFromVersion),doiLink(p.highlights_source_doi));
        meta.appendChild(provenance);
      }
      item.append(main,meta);
      rows.appendChild(item);
    }
    group.append(heading,rows);
    container.appendChild(group);
  }
  // The no-match state is rendered separately by renderIndex.
}
function renderIndex() {
  applyLanguage();
  const query=($("search")?.value||"").trim().toLocaleLowerCase();
  const matching=papers.filter(p=>{
    const subject=RESEARCH_AREAS.find(a=>a.id===p.area);
    const searchable=[p.code,p.title,p.summary.en,p.summary.ru,...(p.topics||[]),
      ...(p.highlights||[]).flatMap(x=>[x.en,x.ru]),
      subject?.name.en,subject?.name.ru].filter(Boolean).join(" ").toLocaleLowerCase();
    return searchable.includes(query);
  });
  try { renderAreas(matching); }
  catch (error) {
    const areaContainer=$("area-groups");
    if(areaContainer)areaContainer.replaceChildren(node("p","muted",COPY[language].areasUnavailable));
    console.error("Subject directory rendering failed",error);
  }
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
  const results=$("paper-results");
  results.replaceChildren(...(p.highlights||[]).map(x=>node("li",null,x[language]||x.en)));
  const source=$("paper-results-source");
  source.replaceChildren();
  if(DOI.test(p.highlights_source_doi)){
    source.append(node("span",null,COPY[language].resultsFromVersion+": "),doiLink(p.highlights_source_doi));
  }
  const tags=$("paper-topics");tags.replaceChildren(...(p.topics||[]).map(x=>node("span","tag",x)));
  $("paper-latest").replaceChildren(doiLink(p.concept_doi,COPY[language].openLatest));
  $("paper-version").replaceChildren(doiLink(p.version_doi,p.version_doi));
  $("paper-first-published").textContent=p.first_published_on||COPY[language].missingDate;
  $("paper-last-updated").textContent=lastVersionDate(p)||COPY[language].missingDate;
  $("paper-version-number").textContent=versionName(p);
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
        if((latest.schema===1 || latest.schema===2) && latest.records && typeof latest.records==="object") {
          let resolved=0;
          for(const p of papers) {
            const item=latest.records[p.code];
            if(!item || item.concept_doi!==p.concept_doi || !DOI.test(item.version_doi))continue;
            const changed=item.version_doi!==p.version_doi;
            p.version_doi=item.version_doi;
            const releaseDate=item.last_version_on||item.published_on;
            if(typeof releaseDate==="string" && ISO_DATE.test(releaseDate)) {
              p.last_version_on=releaseDate;
              p.published_on=releaseDate;
            } else if(changed) {
              delete p.last_version_on;
              delete p.published_on;
            }
            if(typeof item.first_published_on==="string" && ISO_DATE.test(item.first_published_on))
              p.first_published_on=item.first_published_on;
            if(typeof item.version_label==="string" && /^[A-Za-z0-9][A-Za-z0-9._+\- ]{0,47}$/.test(item.version_label))
              p.version_label=item.version_label;
            else if(changed) delete p.version_label;
            if(Number.isInteger(item.version_index) && item.version_index>0)
              p.version_index=item.version_index;
            else if(changed) delete p.version_index;
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
    const target=$("area-groups")||$("paper-title");
    if(target)target.textContent=COPY[language].error;
  }
}
document.addEventListener("DOMContentLoaded",init);
