# Тестовое задание "Структура компании"


## Стек технологий

Python 3.10, Django 4.2.3, Django REST Framework 3.14.0, PostgreSQL 15.3, nginx 1.25, drf-yasg 1.21.5, Docker, Docker-compose


## Локальный запуск

Клонируйте код проекта на свой компьютер:

```bash
  git clone git@github.com:afoninsb/company.git
```
Переименуйте файл .env.dist в .env и отредактируйте его содержимое (при необходимости):

```bash
DEBUG=False

SECRET_KEY="django-insecure-dfdsfsdsfvohd;vn8e6t345dfgshijlgv_oem#$t8wsds&sz"

DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=testdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

Запустите терминал, перейдите в папку '/infra/' и запустите docker-compose:

```bash
  cd <путь_до_папки_проекта>/company/infra
  docker-compose up --build
```

Запустите ещё один терминал, перейдите в папку '/infra/' и запустите скрипт run.sh:
```bash
  cd <путь_до_папки_проекта>/company/infra
  sh run.sh
```
Скрипт выполнит следующие действия:
  - Соберёт статику
  - Выполнит миграции
  - Загрузит в базу данных тестовые данные
  - Создаст суперпользователя


## Адреса

http://127.0.0.1/admin/ -админпанель Django

http://127.0.0.1/api/redoc/ - описание API в формате Redoc

http://127.0.0.1/api/swagger/ - описание API в формате Swagger


## Очистка компьютера

После теста приложения вы можете очистить свой компьютер от созданных приложением артефактов: контейнеров, образов, томов.

Запустите терминал, перейдите в папку '/infra/' и запустите скрипт clean.sh:
```bash
  cd <путь_до_папки_проекта>/company/infra
  sh clean.sh
```


## Контакты

[Вопросы лучше задавать в Telegram @afoninsb](https://t.me/afoninsb)

[Можно написать на почту afoninsb@yandex.ru](mailto:afoninsb@yandex.ru)
