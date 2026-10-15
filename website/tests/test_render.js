#!/usr/bin/env node
"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const ROOT = path.resolve(__dirname, "..");
const papers = JSON.parse(fs.readFileSync(path.join(ROOT,"data","papers.json"),"utf8")).papers;
const entries = JSON.parse(fs.readFileSync(path.join(ROOT,"data","news.json"),"utf8")).entries;
class FakeElement {
  constructor(tag) {
    this.tagName = tag;
    this.children = [];
    this.className = "";
    this.href = "";
    this.dateTime = "";
    this._text = "";
    this.dataset = {};
    this.value = "";
    this.classList = {toggle: () => {}};
  }
  set textContent(value) {
    this._text = String(value);
    this.children = [];
  }
  get textContent() {
    return this._text + this.children.map(c => c.textContent || "").join("");
  }
  append(...items) { this.children.push(...items); }
  appendChild(element) { this.children.push(element); return element; }
  replaceChildren(...items) { this.children = items; this._text = ""; }
}
const elements = {
  "area-groups": new FakeElement("div"),
  "area-snapshot": new FakeElement("p"),
  "search": new FakeElement("input"),
  "paper-count": new FakeElement("span"),
  "no-matches": new FakeElement("p"),
  "news-items": new FakeElement("div"),
  "paper-code": new FakeElement("span"),
  "paper-title": new FakeElement("h1"),
  "paper-summary": new FakeElement("p"),
  "paper-description": new FakeElement("p"),
  "paper-results": new FakeElement("ol"),
  "paper-results-source": new FakeElement("p"),
  "paper-topics": new FakeElement("div"),
  "paper-latest": new FakeElement("dd"),
  "paper-version": new FakeElement("dd"),
  "paper-first-published": new FakeElement("dd"),
  "paper-last-updated": new FakeElement("dd"),
  "paper-version-number": new FakeElement("dd"),
  "paper-downloads": new FakeElement("div"),
  "paper-history": new FakeElement("div")
};
const document = {
  documentElement: {lang: "en"},
  getElementById: id => elements[id] || null,
  createElement: tag => new FakeElement(tag),
  querySelectorAll: () => [],
  addEventListener: () => {}
};
const context = vm.createContext({
  document, location:{search:"?lang=ru",href:"https://math.a-martinevski.com/?lang=ru"}, history:{replaceState:()=>{}}, URLSearchParams, URL, __papers:papers, __news:entries,
  console,
});
const code = fs.readFileSync(path.join(ROOT,"assets","site.js"),"utf8");
vm.runInContext(code, context, {filename:"site.js"});
vm.runInContext('language="ru"; papers=__papers; catalogueDate="2026-10-14"; renderAreas();', context);
let sections=elements["area-groups"].children;
assert.equal(sections.length,5,"There must be five subject areas");
const articles=sections.flatMap(group=>group.children[1].children);
assert.equal(articles.length,18,"Every released paper must appear once");
for(const entry of articles){
  const code=entry.children[0].children[0].children[0].textContent;
  const paper=papers.find(x=>x.code===code);
  assert.ok(paper,"Unknown paper code "+code);
  const meta=entry.children[1];
  const action=meta.children.find(x=>x.className==="area-latest-link");
  assert.ok(action,"Every publication must offer a latest-version action");
  assert.ok(meta.textContent.includes("Первая публикация"),"First publication label missing");
  assert.ok(meta.textContent.includes("Последнее обновление"),"Latest update label missing");
  assert.ok(meta.textContent.includes("Последняя версия"),"Version label missing");
  if(paper.first_published_on)
    assert.ok(meta.textContent.includes(paper.first_published_on),"First date missing");
  if(paper.last_version_on)
    assert.ok(meta.textContent.includes(paper.last_version_on),"Latest-version date missing");
  assert.equal(action.href,"https://doi.org/"+paper.concept_doi,
    "Current Zenodo link must be the concept DOI for "+code);
  assert.ok(entry.textContent.includes(paper.summary.ru),"Russian abstract missing for "+code);
  for(const highlight of paper.highlights) {
    assert.ok(entry.textContent.includes(highlight.ru),"Russian mathematical result missing for "+code);
  }
  assert.equal(entry.children[0].children[3].children.length,3,
    "Each paper should have exactly three visible key results");

}
assert.ok(elements["area-snapshot"].textContent.includes("Каталог"),
  "Localized metadata note not rendered");
vm.runInContext('language="en"; renderAreas();', context);
assert.ok(elements["area-snapshot"].textContent.includes("Catalogue"),
  "English switch did not rerender area index");
assert.equal(elements["area-groups"].children.length,5);
vm.runInContext('renderAreas([papers.find(p=>p.code==="P04")]);',context);
assert.equal(elements["area-groups"].children.length,1,"A filtered map should show one research area");
assert.equal(elements["area-groups"].children[0].children[1].children.length,1,"Filter must show one paper");

elements["search"].value = "105/34";
vm.runInContext('language="ru"; renderIndex();',context);
assert.equal(elements["paper-count"].textContent,"1","Search must match a mathematical result");
assert.equal(elements["area-groups"].children.length,1,"Search should retain the matching scientific field");
assert.ok(elements["area-groups"].textContent.includes("P04"),"Results search must show P04");
elements["search"].value = "NONEXISTENT-SEARCH-TERM-zz";
vm.runInContext('renderIndex();',context);
assert.equal(elements["paper-count"].textContent,"0","No-match counter must be zero");
assert.equal(elements["area-groups"].children.length,0,"No-match search must clear subject groups");
vm.runInContext('location.search="?lang=ru&code=P04"; language="ru"; renderDetail();',context);
assert.equal(elements["paper-first-published"].textContent,"2026-10-14","Detail first date");
assert.equal(elements["paper-last-updated"].textContent,"2026-10-14","Detail latest date");
assert.equal(elements["paper-version-number"].textContent,"Выпуск Zenodo №1","Curated initial release ordinal");
vm.runInContext('delete papers.find(p=>p.code==="P04").version_index; renderDetail();',context);
assert.ok(elements["paper-version-number"].textContent.includes("не подтверждён"),"Unknown semantic version must not be fabricated");
vm.runInContext('papers.find(p=>p.code==="P04").version_index=1; renderDetail();',context);
assert.equal(elements["paper-version-number"].textContent,"Выпуск Zenodo №1");
vm.runInContext('papers.find(p=>p.code==="P04").version_label="0.6"; renderDetail();',context);
assert.equal(elements["paper-version-number"].textContent,"0.6");
const translationCheck=vm.runInContext('[COPY.ru.achievementGhzExactProblem, COPY.ru.achievementGhzThreeWhy, COPY.ru.achievementMixingAnswer, COPY.ru.achievementSourcesHeading, COPY.ru.sourceRoleOur, COPY.en.sourceRolePrior]',context);
assert.equal(translationCheck.length,6);
assert.ok(translationCheck.every(x=>typeof x==="string" && x.length>10),"Explanations and sources must have meaningful localized text");
vm.runInContext('language="ru"; news=__news; newsLoaded=true; renderIndex();',context);
const renderedNews=elements["news-items"].children;
assert.equal(renderedNews.length,6,"News must include 2 site changes and 4 publication updates");
assert.ok(renderedNews[0].textContent.includes("математические"),"Recent Russian website update must render first");
assert.ok(renderedNews[0].children.some(x=>x.href?.endsWith("/pull/12")),
  "GitHub PR #12 must be linked");
assert.ok(renderedNews[1].children.some(x=>x.href?.endsWith("/pull/11")),
  "GitHub PR #11 must be linked");
assert.ok(renderedNews[2].children.some(x=>x.href?.startsWith("https://doi.org/")),
  "Publication release must retain its DOI link");
vm.runInContext('language="en"; renderUpdates(document.getElementById("news-items"),true);',context);
assert.ok(elements["news-items"].children[0].textContent.includes("mathematical"),
  "English translation must apply to updates");
const previous=elements["news-items"].children[0];
vm.runInContext('newsLoaded=false; renderIndex();',context);
assert.equal(elements["news-items"].children[0],previous,
  "Existing update cards must remain in place when news.json fails");
assert.equal(vm.runInContext('updateSource("https://evil.example/test")',context),null);
assert.equal(vm.runInContext('updateSource("https://github.com/unknown/repo/pull/12")',context),null);
console.log("PASS: aligned homepage news, RU/EN, PR + DOI, fallback and full article catalogue.");
