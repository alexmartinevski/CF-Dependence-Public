# Verified PDF cache R2.1 — 16.10.2026

The optional public Zenodo mirror is now resumable across Pages builds:
a previously complete public artifact and GitHub Actions cache may supply
PDF bytes, but every file is revalidated against the currently approved
Zenodo version's MD5, exact byte length, PDF header and filename.
No stale or corrupt file is served. New verified downloads replenish
the cache. See website/PDF_MIRROR_CACHE_R2_1.md for retention limits,
read-only artifact trust boundaries, tests and final deployment QA.

---
# Обновление R2 — без ручных счётчиков и дублирования новостей (16.10.2026)

Этот раздел ЗАМЕНЯЕТ устаревшие указания R1 ниже о необходимости править число 18,
PDF-суффикс, фиксированные три scholarly shards и вручную редактировать карточки новостей.
Все правила научной приемки и подтверждения публикации Zenodo остаются обязательными.

## Единственный набор данных для новой опубликованной работы

1. website/data/papers.json: добавить Pxx только ПОСЛЕ публичного Zenodo GET;
   Version и Concept DOI, фактические даты, двуязычные summaries, ровно три
   математически подтверждённых highlights с evidence, область исследования.
2. website/data/scholarly/part-NN.json: добавить запись Pxx в существующий или
   новый shard. Указать только ПУБЛИЧНЫЕ Zenodo Title, Description HTML,
   Keywords, record ID, оба DOI, PDF имя, MD5, размер, лицензию и дату.
   website/tools/build_scholarly_pages.py теперь сам находит все part-*.json.
3. website/data/news.json: добавлять одну новость publication_release с реальной
   датой и источником https://doi.org/<fixed-version-DOI>, который уже включён
   в опубликованный papers.json. При необходимости новые новости о результатах
   должны ссылаться на сами научные страницы, не на технические PR.

## Генерация: НЕ надо изменять руками

- Текст количества научных работ, pages /publications/Pxx/, /publications/,
  /author/, итоговый sitemap формируются из настоящего количества N записей.
- website/tools/build_news_fallbacks.py во время deploy сам создаёт четыре
  последние карточки главной (2×2) и полную хронологию news.html на EN/RU
  из того же news.json. Даже без JavaScript карточки останутся читаемыми.
- Статический сайт website/index.html, website/news.html и website/sitemap.xml
  служит исходным шаблоном/срезом; итоговый GitHub Pages artifact важнее.
- PDF теперь допускает разные безопасные release suffix, например
  P21_CF_V8_R1.pdf. Для локального PDF-зеркала действует лимит 64 MiB,
  строгие MD5 + размер + начало %PDF-. Если копия не прошла проверку,
  остаётся прямая ссылка на PDF опубликованного Zenodo record.

## Проверка перед merge

CI: python website/tests/test_public.py; python website/tests/test_scholarly.py;
python website/tests/test_dynamic_release.py; node --check website/assets/site.js;
node website/tests/test_render.js. Новый offline тест моделирует P21 как 19-ю
статью во временном каталоге, четвёртый shard, PDF другого релиза и новую новость.
Он НЕ пишет в GitHub main и НЕ обращается к Zenodo. Тесты продолжают строго
проверять исторические 18 публикаций, даты и основные математические утверждения.

После merge: подтвердить BOTH CI SUCCESS и GitHub Pages deploy SUCCESS;
сверить реальный URL, DOI, Author ORCID, PDF, статический HTML/MathML и sitemap.
Без фактической PUBLIC Zenodo записи статус новой статьи — BLOCKED.

CODEOWNERS только объявляет владельца; настоящая branch protection/ruleset
нуждается в отдельной настройке и не считается включенной автоматически.

---
# CF Dependence — как добавить НОВУЮ опубликованную статью на научный сайт

**Операционный регламент R1 · 16.10.2026.** Действующая статическая инфраструктура: сайт https://math.a-martinevski.com/, открытый репозиторий https://github.com/alexmartinevski/CF-Dependence-Public. Выпуск в Zenodo — в закрытом репозитории по OPS/API/NEW_ARTICLE_PUBLICATION_RUNBOOK_RU.md. **Нельзя выводить unpublished drafts на публичный сайт.** Все данные сверять по последней реально ПУБЛИЧНОЙ версии Zenodo.

## 0. Входной gate из Zenodo (обязателен)

До любого коммита в публичный catalogue получить и проверить:
- Согласованный P-ID, математическое название и уникальность по registry. P05/P10 могут оставаться вне публикации; P21/P22 нельзя автоматически считать следующими опубликованными.
- Публичный Zenodo URL вида https://zenodo.org/records/<реальный-id> и GET https://zenodo.org/api/records/<id>, доступный **без авторизации**; не просто статус private draft inprogress.
- **Version DOI** конкретного выпуска (для точного цитирования) и отдельный **Concept DOI** серии версий. Не перепутать их и не использовать DOI из старого релиза в качестве DOI нового.
- Полные публичные Title, Description HTML (после авторского approval), Keywords, creator Alexandr Martinevski / ORCID 0009-0000-4230-4414, publication_date/version, license.
- Публичный PDF: точное имя, размер, MD5/checksum, Version DOI и отсутствие сомнений в научном тексте. Для частных источников хеш SHA256 отдельно; не публиковать private TeX/script без явно принятого решения.
- Три **проверенные** математические формулировки результата с указателями на теоремы (evidence labels) и фиксированным DOI публикации. Русские и английские формулировки обязательны; не преувеличивать новизну/приоритет.

**Обязательный gate ZENODO_PUBLIC_VERIFIED:** до него нельзя добавлять статью с status=published. Резервирование DOI, draft и право владельца открыть edit НЕ являются публичной публикацией.

## 1. Карта файлов: что править на сайте и зачем

| Файл в публичном main | Изменение для нового P-ID |
|---|---|
| **website/data/papers.json** | Внутри массива papers новая запись: code, title, двуязычные summary, topics, area, status=published, version_doi, concept_doi, record_url/pdf_filename ИЛИ source_path, published_on/first_published_on/last_version_on, version_index и проверенное объяснение, 3 highlights EN/RU с evidence, highlights_source_doi, changes. Обновить last_curated_on. |
| **website/data/scholarly/part-01.json, part-02.json, part-03.json** | Добавить объект с ключом Pxx в **один** part: title, полный утверждённый description_html, keywords, publication_date, version_doi, concept_doi, pdf_filename, pdf_md5, pdf_size, license, record_id. Получать из публичного Zenodo API, а не из частного ожидаемого draft. Суммарное покрытие кодов ровно равно papers.json. |
| **website/tools/build_scholarly_pages.py** | Поднять проверку len(papers)==18 / len(scholarly)==18; расширить regex PDF (сейчас имя строго Pxx_CF_V6_S8.pdf), если новая серия имеет другое суффиксное имя; проверить MAX_PDF=5_000_000 bytes, время загрузки и режим PDF-зеркала. При необходимости нового part-04 расширить цикл чтения (сейчас range(1,4)). Заменить зафиксированные в тексте EN/RU строки о 18 препринтах. |
| **website/tests/test_public.py** | Изменить счётчик published==18; не нарушить исторические проверки дат P01–P20 (2026-10-14 и ранние редакции), а новую статью проверять отдельно по фактической дате. Исправить старые regex PDF и количество новостей, если оно увеличится; НЕ ослаблять тесты проверки источников. |
| **website/tests/test_scholarly.py** | Изменить ожидания 18/18 в raw HTML, index, author, количество DOI/ORCID, sitemap. Учесть PDF filename нового релиза и все 3/4 scholarly chunks. Проверить MathML, полный abstract без JS и citation_pdf_url только после хеш-проверки. |
| **website/tests/test_render.js** | Поменять утверждение о 18 статьях на новое фактическое N; сохранить 3 highlights per paper, 5 разделов (или отдельно согласовать шестой), ссылки и проверку локализации. |
| **website/assets/site.js** | Обновить EN/RU строку «(18)» у scholar index; если новая область, дополнить RESEARCH_AREAS (текущие значения: extremal, transport, algebra, harmonic, statistics) с переводом. При новом формате news source дополнить только явно разрешённый путь в updateSource(). Не разрешать произвольные внешние/GitHub PR ссылки как научные новости. |
| **website/index.html** | Главная: 4 последние новости в сетке 2×2 имеют **статический fallback** на случай недоступности news.json/JS. Обновить содержание первых четырёх карточек, даты, ссылки, ключи data-i18n только при появлении событий, соответствующих свежей публикации. Сохранить корректный переход к каталогу. |
| **website/news.html** | Полная история: сохранить все прежние события и добавить новую статическую fallback-карточку, дату, тип, источники и EN/RU ключи. Не превращать страницы новостей в журнал технических PR. |
| **website/data/news.json** | Добавить подтверждённое событие kind=publication_release с датой реальной публикации, двумя title/summary и source на точный Version DOI (уже поддерживается resolver) или специально allowlisted public page. Сохранять историю, сортировку по фактическим датам. |
| **website/sitemap.xml** | Обновить статическую версию карты сайта до отправки PR: +1 canonical /publications/Pxx/. При deploy build_scholarly_pages.py самостоятельно генерирует итоговую карту с /publications/, /author/ и всеми public entries. |
| **website/README.md и website/NEW_PAPER_SITE_RUNBOOK_RU.md** | Зафиксировать новое число, процедуру нового выпуска, текущие ограничения. Сведения о научных доказательствах и стороннем AI disclosure не менять автоматически. |

**НЕ обязательны** для каждой новой работы: website/achievements.html и четыре главных карточки научных достижений. Это тщательно отобранные результаты, а не автоматическое зеркало всех новых статей. Добавлять туда результат только при отдельном редакционном решении и с полноценной проверкой доказательств и ссылок.

## 2. Точный формат записи в website/data/papers.json

Сверить с P20 и другими опубликованными записями; ключи у каждой записи:
- code: Pxx (сейчас регулярное выражение P[0-9][0-9]); title: строго опубликованное английское имя.
- summary: {"en":"...","ru":"..."} — краткая точная аннотация **на уровне аспиранта**.
- topics: массив терминов; area: один из extremal, transport, algebra, harmonic, statistics, если не согласована новая область.
- status: только "published"; version_doi: "10.5281/zenodo.<real-Version-ID>", concept_doi: отдельный DOI серии.
- Для Zenodo-only статьи: record_url: "https://zenodo.org/records/<id>", pdf_filename: реальное Zenodo PDF имя. Для статей с **разрешёнными** локальными открытыми исходниками: source_path: "papers/<safe-slug>", причём нужны оба paper.pdf и paper.tex в публичном Git, не private release path. Старые три P01–P03 используют source_path, остальные — record_url.
- highlights: **ровно 3** проверенных утверждения, каждое {"en":"...","ru":"...","evidence":"thm:..."}. highlights_source_doi: DOI ТЕХ файлов/теорем, по которым они действительно сверены; обычно новый Version DOI, но не подменять историческую опору.
- published_on / first_published_on / last_version_on: фактическая дата выпуска Zenodo, не дата обновления GitHub/Description. version_index и version_index_evidence: только установленные номер/обоснование. changes: массив проверенных изменений версии, не выдумывать.
- last_curated_on на верхнем уровне: дата реальной редакционной сверки.

В соседнем scholarly/part-*.json (schema=1) объект Pxx содержит полный approved Description HTML, keywords, publication_date, version_doi, concept_doi, pdf_filename, pdf_md5 (ровно 32 hex), pdf_size (int bytes), license, record_id (int). **Не копировать MD5 из локального непроверенного PDF**. Ожидаемые creator/ORCID в страницах берутся из констант AUTHOR и ORCID в build_scholarly_pages.py, поэтому совпадение creator в Zenodo обязательно проверять до выкладки.

## 3. Счётчики 18 и имена PDF — обязательная доработка при +1 статье

По состоянию на 16.10.2026 код/тесты предполагают именно 18 статей и имена "Pxx_CF_V6_S8.pdf". Добавление только JSON без синхронной корректировки кода и тестов сломает CI/деплой.

Проверить точные места:
- website/tools/build_scholarly_pages.py: PDF regex; range(1,4) по scholarly/part-*.json; len(papers)!=18 / len(scholarly)!=18; строки индекса «18 research preprints / 18 научных препринтов». Код ограничивает зеркалируемый PDF MAX_PDF=5_000_000 и валидирует MD5 и %PDF-.
- website/tests/test_scholarly.py: asserts 18, число li в index/author, соответствие article URLs и сквозные DOI; P01-CF_V6_S8 относится к контрольному примерному фикстуру.
- website/tests/test_public.py: 18, особые исторические даты для уже выпущенных P01–P20, PDF regex, количество новостей и конкретные NEWS-kind/даты.
- website/tests/test_render.js: 18 rendered papers, 5 областей и 3 selected results per article.
- website/assets/site.js: двуязычная подпись scholarlyIndexLink с «(18)».
- website/index.html / website/news.html: статические fallback-card counts, локализация и реальная latest-four chronology.
- website/sitemap.xml: статический источник контрольного списка.

**Рекомендация реализации:** текущий новый PR должен не удалять тесты, а привести их к новому факту публикации; когда станет удобно, можно отдельно рефакторить N в одну константу, PDF suffix сделать декларативным и новостные fallback генерировать из JSON. До такого рефакторинга описанные места обязательны.

## 4. Редакционный цикл на сайте

1. Только после ZENODO_PUBLIC_VERIFIED создавать **feature branch** в публичном репозитории, не изменять shared main напрямую без проверки.
2. Менять papers.json и scholarly parts атомарно как логический релиз, обеспечить уникальность P-ID/version DOI/concept DOI и точность всех математических highlights. Поддерживать существующие 18 описаний неизменными, если нет отдельной причины.
3. Обновить news.json, news.html, домашние четыре карточки (2×2), двуязычные переводы и allowlist ссылок. Читатель должен попадать на статью или DOI, не на Github PR.
4. Синхронизировать код builder/tests для N+1, sitemap статический, при необходимости RESEARCH_AREAS и pdf_filename template. Проверить, что научный термин, формула, символы MathML и PDF не исказились.
5. Прогнать CI на PR: python website/tests/test_public.py, python website/tests/test_scholarly.py, node --check website/assets/site.js, node --check website/assets/scholar.js и node website/tests/test_render.js. Генератор школьных страниц вызывается тестом **без сети**. Исправить ошибки, не обходить.
6. Merge после CI: .github/workflows/public-site.yml автоматически выполняет deploy, копирует index/paper/achievements/news, CSS/JS/data, читает публичный Zenodo API для optional zenodo_latest.json, запускает fingerprint_assets.py и build_scholarly_pages.py. В билде MathML конвертируется на стороне Python (latex2mathml==3.81.1); PDF зеркалируется **только** при размере+MD5. Генерируются /publications/Pxx/index.html, /author/index.html, /publications/index.html, sitemap.
7. Ждать BOTH validate SUCCESS и deploy SUCCESS; затем проверить артефакт Github Pages: N+1 HTML и сопоставленные PDF, title/citation_author/citation_author_orcid/citation_doi/citation_pdf_url **только если PDF присутствует и прошёл checksum**, BibTeX, полную аннотацию без JS, sameAs ORCID, canonical URL, SEO sitemap.
8. Проверить живой https://math.a-martinevski.com/publications/Pxx/ и href PDF. Старый paper.html?code=Pxx — только совместимость/noindex, основной путь — статическая статья. Публичный PDF mirror не заменяет Zenodo как источник публикационной истины.
9. Зафиксировать PUBLIC_SITE_VERIFIED, ссылки на PR/commit, run/artifact, место статьи в 5 областях и итоговое число N. ORCID & Scholar индексация требует внешнего прохода краулера; не утверждать, что уже заиндексировано.

## 5. Новая версия старой статьи / чистая правка metadata

Новая версия старой статьи НЕ добавляет новую P-строку. После ручного Zenodo Publish заменить в её строке version_doi, version_index/evidence, last_version_on, ссылки на PDF и highlights_source_doi (когда научный текст/результаты изменены); обновить scholarly metadata, MD5/bytes/filename и соответствующую цитату. Concept DOI должен остаться прежним. Если научные results реально изменились — повторный proof-review.

Только Description/Keywords edit опубликованной Zenodo записи НЕ меняет version DOI и дату первого выпуска. Синхронизировать scholarly cache с новой уже **публично применённой** аннотацией/keywords, но не приписывать редактуре метаданных новую научную версию. Нет причин трогать тексты математических теорем/сайтские highlights без редакционного решения.

## 6. Публикационная и поисковая проверка

- Для каждого Pxx: публичный Zenodo record и публичная статическая статья согласованы по Version/Concept DOI, Title, автору ORCID, Keywords, PDF checksums. Если PDF миррор не прошёл — fallback ведёт на Zenodo, а citation_pdf_url отсутствует: это правильно.
- URL Pxx обязателен в sitemap и библиографическом каталоге, доступен без JavaScript; 18 уже опубликованных работ не должны исчезнуть.
- robots.txt разрешает индексацию; главное меню и авторский профиль связаны с публикациями. Статистику индексации Google Search Console/Scholar проверять отдельно, гарантировать включение в Scholar нельзя.
- Сайт не хранит Zenodo токены и не вызывает Publish. Исходный AI disclosure автора, научные статьи/PDF и DOI в Zenodo здесь не редактируются автоматически.
- При любом несоответствии — **BLOCKED_SITE_CATALOGUE** вместо ложного заявления о завершённом релизе.

## 7. Отчёт и передача

Выпуск считается закрытым только при наличии: Zenodo_PUBLIC_VERIFIED → public PR CI PASS → GitHub Pages deploy SUCCESS → публичный /publications/Pxx/ и PDF-source integrity PASS → обновлённая история и sitemap. Передавать новому чату P-ID, действующие main SHAs обоих репозиториев, Version/Concept DOI и Zenodo ID, verified dates, SHA256/MD5 PDF, отчет proof-review, PR и run IDs, список STOP/долгов. Не выводить unpublished статьи из private Git на публичный сайт.

**Исходники:** .github/workflows/public-site.yml; website/data/papers.json; website/data/scholarly/part-*.json; website/data/news.json; website/tools/build_scholarly_pages.py, resolve_zenodo.py, fingerprint_assets.py; website/tests/{test_public.py,test_scholarly.py,test_render.js}; website/assets/site.js; website/index.html; website/news.html; website/sitemap.xml. Операции Zenodo: закрытый OPS/API/NEW_ARTICLE_PUBLICATION_RUNBOOK_RU.md.
