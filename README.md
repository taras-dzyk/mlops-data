# Лабораторні роботи MLOps
Це репозиторій версіювання даних та розмітки

## Як працювати
### Розмітка
Розмітку даних виконано в [Label Studio](https://labelstud.io/)

**Передумови:**
- встановлений docker compose

`cd labeling/label-studio`

`docker-compose up --build -d`

Це запустить Label Studio на http://localhost:8080/

Log in:  

    `t.dzyk@setuniversity.edu.ua`

    `JPv$u#DaXP4m4Pr`

Recent Projects -> MLOps-hw-1

Автоматично буде створено дві папки для імпорту і експорту

`%repo_location%/../data-raw`
`%repo_location%/../data-labeled`

### Версіювання
**Передумови:**
- встановлений DVC

`dvc repro`

`ggit add dvc.yaml dvc.lock`

`git commit`

`dvc push`

Я створив dvc pipeline `dvc.yaml` який має стадію `copy-labeled`. Ця стадія копіює розмічені файли в папку `dataset` сворюючи структуру папок що відповідає розміченим класам. 

Ця папка додалася в `.gitignore` на цьому ж рівні, що виключило власне сам датасет, який може бути дуже великим з git трекінгу.

Я налаштував dvc data storage для цієї лабораторної на локальному середовищі. `../data-storage-dvc/`. Це можна побачити в файлі `.dvc/config`

Відповідно при виконанні `dvc push` дані будуть направлені в сховище. В реальному проекті це буде клауд бакет
