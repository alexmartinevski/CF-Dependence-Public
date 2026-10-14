# Настройка math.a-martinevski.com

Этот документ описывает домен публичного сайта CF Dependence.
Исходный репозиторий: `alexmartinevski/CF-Dependence-Public`.
Публикация сайта — из `website/` посредством GitHub Actions.

## После согласования и merge PR

1. Открыть [Settings → Pages](https://github.com/alexmartinevski/CF-Dependence-Public/settings/pages).
2. Установить Source: **GitHub Actions**.
3. В поле **Custom domain** указать `math.a-martinevski.com`, нажать Save.
4. В DNS-зоне `a-martinevski.com` создать запись:

   | Type | Host/name | Target |
   |---|---|---|
   | CNAME | math | alexmartinevski.github.io |

   Не добавлять `/CF-Dependence-Public` в значение CNAME. Если запись `math` уже существует,
   сначала проверить её назначение, не перезаписывать чужую службу вслепую.

5. Проверить DNS: `dig math.a-martinevski.com CNAME +short` либо
   `Resolve-DnsName math.a-martinevski.com -Type CNAME` на Windows.
6. Дождаться проверки DNS/сертификата; затем включить **Enforce HTTPS**.
7. Убедиться, что открывается `https://math.a-martinevski.com/`,
   `/sitemap.xml` и страницы P01–P03.

До завершения шагов адрес — целевой, а не подтверждённый работающий сайт.
Нельзя утверждать, что DNS и Pages уже настроены, лишь на основании исходников.

## Безопасность

Лучше подтвердить владение доменом в GitHub до DNS-перенаправления. Не использовать wildcard
`*.a-martinevski.com` для этого сайта. Приватный научный репозиторий не публиковать.
CNAME-файл **не нужен**, если источник Pages — GitHub Actions: настройка Custom domain
выполняется в административном интерфейсе GitHub.

Документация:
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages
