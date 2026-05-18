# Onec-offer — коммерческое предложение 1ОС.ЭДО.Легаси

Статический лендинг с коммерческим предложением по приложению **1ОС.ЭДО.Легаси** (интеграция учётной системы с оператором ЭДО Доки, «Астрал»).

## Публикация на GitHub Pages

1. В репозитории на GitHub откройте **Settings** → **Pages**.
2. В блоке **Build and deployment** для поля **Source** выберите **GitHub Actions** (не «Deploy from a branch», если хотите использовать workflow из этого репозитория).
3. Выполните push в ветку `main` (например, слейте pull request). Запустится workflow **Deploy GitHub Pages**.
4. После успешного деплоя сайт будет доступен по адресу вида `https://<ваш-логин>.github.io/<имя-репозитория>/`.

Если workflow **Deploy GitHub Pages** уже падал с ошибкой *Get Pages site failed* / *Not Found*: в настройках **Pages** убедитесь, что источник — **GitHub Actions**, затем на вкладке **Actions** откройте последний запуск и нажмите **Re-run all jobs**, либо запустите workflow вручную (**Actions** → **Deploy GitHub Pages** → **Run workflow**). В текущей версии workflow сам включает Pages при необходимости (`enablement: true`).

Альтернатива без Actions: в **Pages** выберите источник **Deploy from a branch**, ветка **main**, папка **/ (root)** — тогда будет опубликован файл `index.html` из корня без workflow.

## Локальный просмотр

Откройте файл `index.html` в браузере или поднимите локальный сервер, например:

```bash
python3 -m http.server 8080
```

и перейдите на `http://127.0.0.1:8080`.
