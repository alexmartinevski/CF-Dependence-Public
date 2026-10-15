#!/usr/bin/env node
"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const ROOT = path.resolve(__dirname, "..");
const papers = JSON.parse(fs.readFileSync(path.join(ROOT,"data","papers.json"),"utf8")).papers;
class FakeElement {
  constructor(tag) {
    this.tagName = tag;
    this.children = [];
    this.className = "";
    this.href = "";
    this.dateTime = "";
    this._text = "";
    this.dataset = {};
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
  "area-snapshot": new FakeElement("p")
};
const document = {
  getElementById: id => elements[id] || null,
  createElement: tag => new FakeElement(tag),
  addEventListener: () => {}
};
const context = vm.createContext({
  document, location:{search:"?lang=ru"}, __papers:papers,
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
  const action=entry.children[1].children[2];
  assert.equal(action.href,"https://doi.org/"+paper.concept_doi,
    "Current Zenodo link must be the concept DOI for "+code);
  assert.ok(entry.textContent.includes(paper.summary.ru),"Russian abstract missing for "+code);
}
assert.ok(elements["area-snapshot"].textContent.includes("Каталог"),
  "Localized metadata note not rendered");
vm.runInContext('language="en"; renderAreas();', context);
assert.ok(elements["area-snapshot"].textContent.includes("Catalogue"),
  "English switch did not rerender area index");
assert.equal(elements["area-groups"].children.length,5);
console.log("PASS: 18 papers in 5 topic groups; Russian/English; latest Zenodo concept links.");
