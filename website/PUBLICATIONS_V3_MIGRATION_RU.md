# CF Dependence — publications v3: один канонический каталог

**Статус:** миграция инфраструктуры (не научный релиз и не Zenodo Publish).

## Источник

Единственный вручную редактируемый источник публикационных данных:
website/data/publications.json. Схема: website/data/publications.schema.json.

Записи индексированы по P-ID, состоят из блоков:
- identity: опубликованное название, область, topics, keywords.
  Особое отличие регистра названия P01 от Zenodo сохранено необязательным
  catalogue_title без изменения научной метадаты.
- science: RU/EN summary, полный approved abstract_html, ровно три
  проверенных RU/EN результата с evidence, числовой ID того публичного
  релиза, в котором эти результаты сверены.
- publication: status=published, Concept DOI, полная известная последовательность
  releases с Version DOI, record ID и датой релиза; проверенные PDF filename,
  размер и MD5 текущей версии, лицензия, changelog и путь открытых исходников.

### Согласованное правило о датах

**publication.first_published_on** и **publication.last_version_on** —
**хранимые утверждённые поля**, а НЕ вычисляемые из history.
При каждом изменении их вносят непосредственно. Для защиты от дрейфа
валидатор сравнивает их с датами известных релизов и останавливает сборку
при противоречии. Он не перезаписывает согласованные даты.

Version index и его доказательное основание также хранятся явно.
В истории P01/P02/P03 две действительно известные публикации;
для остальных 15 пока по одной. Не добавлять Zenodo drafts в releases.

## Сборка из одного источника

Выполнить из корня репозитория:

    python website/tools/materialize_publications.py
    python website/tests/test_unified_publications.py

Генератор сохраняет обратно-совместимые выходные представления только
локально/в CI, без отслеживания Git:
- website/data/papers.json — фронтенд, новости и read-only Zenodo resolver;
- website/data/scholarly/part-NN.json — статические научные HTML/MathML.

Это **производные**, не редактируемые научные источники. Схема допускает
любое число записей; shards нарезаются автоматически по 6 статей,
а действующий генератор открывает все part-NN динамически.

GitHub Actions запускает materialize до validation и отдельно до Pages
deploy; уже существующие JS-контракты, тесты, SEO и научные страницы
работают с такими же представлениями, что до перехода.

Для проверки без записи:

    python website/tools/materialize_publications.py --check-only

## Приёмка миграции

Перед PR выполнена полная обратная проекция всех прежних полей двух
источников по каждому P-ID: расхождений 0. В канонике сохранены 18
публикаций, 54 научных results, 18 full abstract, 18 комплектов PDF metadata
и две подтверждённые версии для каждой из P01–P03. Новые P21/P22/P27
и незавершённая новая версия P12 не добавлены.

Материалы не изменяют научных утверждений, дат, published DOI,
контрольных сумм PDF и AI disclosure.

## Новая статья / новая версия

Сначала SCIENCE_APPROVED и ZENODO_PUBLIC_VERIFIED (публичный GET).
Затем один коммит с добавлением P-ID либо нового published release в
website/data/publications.json. Два **хранимых** поля дат должны быть
явно согласованы и проверены. Полные descriptions, keywords и
математические highlights — только по одобренной публичной рукописи.
Одноимённые JSON views редактировать не надо: они генерируются.

News остаётся отдельной моделью событий в website/data/news.json.
В PR после настоящей публикации добавляют publication_release новость.
Изменение сайта само по себе не является научным выпуском.

Никакого Zenodo API POST/PUT, загрузки файла, резервирования DOI или
автоматического Publish в этом PR нет.

## Проверки и откат

- python website/tests/test_unified_publications.py
- python website/tests/test_public.py
- python website/tests/test_scholarly.py
- python website/tests/test_dynamic_release.py
- node website/tests/test_render.js
- GitHub Pages validate и deploy; PDF cache продолжает принимать только
  проверенные имя, MD5, размер и заголовок PDF.

Откат — revert инфраструктурного merge и восстановление исходных
tracked JSON из Git history.
