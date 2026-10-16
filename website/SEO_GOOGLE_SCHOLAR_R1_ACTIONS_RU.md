# CF Dependence — SEO & Google Scholar Audit R1, исправления и дальнейшая проверка
Дата фиксации: 2026-10-16.

## Исправления исходников

- \`website/index.html\`: убрать исторический текст «(18)» из статической ссылки
  на научный каталог; точное число показывается штатным JS-счётчиком из актуального
  опубликованного \`papers.json\`. Фолбэк-ссылка теперь не устаревает.
- \`website/sitemap.xml\`: идентичен генерируемому sitemap для текущих 21
  опубликованных статей и пяти основных URL (всего 26).
- \`website/tests/test_public.py\`: обязательное точное сравнение адресов
  исходного sitemap с каноническим каталогом и проверка отсутствия
  жёсткого числа статей в HTML-ссылке.
- \`website/tests/test_scholarly.py\`: проверка побайтового соответствия
  исходного snapshot sitemap окончательному sitemap, который строится в Pages.
  При новом выпуске необходимо обновить исходный sitemap вместе с
  \`publications.json\`; случайный дрейф блокируется CI.
- \`website/tools/verify_live_crawl.py\`: read-only HTTP/TLS/DNS проверка
  действующего домена, robots.txt, sitemap, 21 HTML-научной страницы, метатегов
  Scholar, canonical и 21 PDF (байты и MD5). Запросов к Google/Zenodo для
  записи не выполняет.
- \`.github/workflows/seo-live-audit.yml\`: отдельный read-only запуск проверки
  **после успешного Pages-деплоя** (и вручную через workflow_dispatch).
  Результат \`report.json\` сохраняется в артефакте, явные проблемы с
  DNS/HTTPS/HTML/PDF не замалчиваются и не меняют статус уже выполненной
  публикации на Zenodo.
- Нет изменений в тексте научных статей, DOI, PDF, исторических датах или
  содержании утверждений.

## Границы внешней проверки

Проверка с GitHub runner диагностирует **реальную публичную доступность**
HTTPS из одного внешнего датацентра. Это **не статус включения в индекс
Google и Google Scholar**. Если DNS или внешний сетевой маршрут не работает,
в отчёте появляется \`BLOCKED_DNS\` / \`BLOCKED_HTTP\`; нельзя приравнивать
это к отсутствию сайта для всех пользователей.

Публичный поисковый запрос вида \`site:math.a-martinevski.com\`
даёт лишь ориентировочный сигнал; отсутствие результата не подтверждает
отсутствие страницы в индексе.

## Обязательные действия в Google Search Console

1. Открыть https://search.google.com/search-console/ и выбрать/добавить
   свойство \`https://math.a-martinevski.com/\` (URL-prefix) либо весь
   \`a-martinevski.com\` (Domain, обычно требует DNS TXT).
   Если свойство уже существует, не создавать дубликат без причины.
2. Подтвердить владение средствами Google. ChatGPT/GitHub workflow
   не имеют доступа к закрытому аккаунту Search Console и не могут
   подтвердить владение без собственника.
3. Открыть Sitemaps, передать \`https://math.a-martinevski.com/sitemap.xml\`.
   Проверить статус обработки и количество найденных URL. Sitemap содержит
   26 канонических URL (21 научная страница плюс пять основных).
4. Через **URL Inspection** проверить главную и примеры P12, P21, P22, P27,
   затем все остальные работы. Сохранить \`Page indexing\`,
   \`Page fetch\`, \`Indexing allowed\`, \`Google-selected canonical\`
   и \`Last crawl\`; при необходимости \`Test live URL\` и \`Request indexing\`.
   При массовом обновлении отдавать предпочтение sitemap, а не множеству
   отдельных индексирующих запросов.
5. Проверить Google Scholar по полному названию + \`Alexandr Martinevski\`
   и по exact Version DOI. Если появляются Zenodo и наша страница, искать
   одну объединённую научную запись вместо отдельного цитирования двух дублей.
   Видимость в Scholar и автоматическое объединение версий не гарантируются.
6. Уточнить, отображаются ли статьи в авторском профиле Scholar, при
   необходимости выполнить ручную коррекцию **без создания ложных цитирований**.

## Что считать DONE

- CI = PASS и GitHub Pages deployment = SUCCESS после этих изменений.
- Новый Pages artifact: 26/26 sitemap URL и 21/21 корректных PDF/HTML.
- GitHub live SEO audit = PASS с DNS/HTTPS/robots/HTML/PDF проверкой
  (либо явно указан сетевой BLOCKED, требующий ручной проверки).
- В Search Console: все 21 научная URL имеют проверенный статус; если
  \`not indexed\`, причина и следующая дата проверки зафиксированы.
- Google Scholar: по 21 работам \`found/not found/unknown\` с датой
  фактического поиска, без предположения, что CI = индексация.

## Источники процедуры

- https://support.google.com/webmasters/answer/9012289
- https://search.google.com/search-console/
- https://scholar.google.com/intl/en/scholar/inclusion.html
