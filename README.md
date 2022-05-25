# dvmn-bot

Telegram-бот отправляющий уведомления о проверке работ на [dvmn](https://dvmn.org).

## Установка и запуск

### Запуск локально с помощью виртуального окружения
Вам понадобится установленный Python 3.6+ и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/dvmn-bot
```

В папке со скачанным репозиторием создайте виртуальное окружение:
```bash
$ cd dvmn-bot
$ python3 -m venv venv
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Заполните файл .env.example и переименуйте его в .env или иным образом задайте переменные среды:
* DVMN_TOKEN - токен к [Devman API](https://dvmn.org/api/docs/).
* TELEGRAM_TOKEN - токен бота Telegram. Можно получить у [@BotFather](https://t.me/BotFather).
* TELEGRAM_CHAT_ID - ваш идентификатор Telegram. Можно узнать у бота [@userinfobot](https://t.me/userinfobot).

Перед запуском напишите вашему боту любое сообщение, чтобы в будущем он мог писать вам.

Находясь в директории dvmn-bot исполните:
```bash
$ venv/bin/python main.py
```

### Запуск локально с помощью Docker
Вам понадобится установленный git, [Docker](https://docs.docker.com/get-docker/) и [Docker Compose](https://docs.docker.com/compose/install/).

#### Сборка

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/dvmn-bot
```

В папке со скачанным репозиторием исполните:
```bash
$ docker-compose build
```

#### Запуск

Заполните файл .env.example и переименуйте его в .env:
* DVMN_TOKEN - токен к [Devman API](https://dvmn.org/api/docs/).
* TELEGRAM_TOKEN - токен бота Telegram. Можно получить у [@BotFather](https://t.me/BotFather).
* TELEGRAM_CHAT_ID - ваш идентификатор Telegram. Можно узнать у бота [@userinfobot](https://t.me/userinfobot).

Для запуска созданного контейнера исполните:
```bash
$ docker-compose up -d
```

### Деплой на [Heroku](https://heroku.com/)
Вам понадобится установленный git и [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli).

1. Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/dvmn-bot
```

2. Зарегистрируйтесь и создайте приложение Heroku.
3. Перейдите в раздел `Settings - Config Vars` и задайте те же переменные среды, что и для запуска локально.
4. В папке с загруженным репозиторием исполните:
```bash
$ heroku stack:set container -a {имя вашего приложения heroku}
$ heroku git:remote -a {имя вашего приложения heroku}
$ git push heroku master
```
5. Перейдите в раздел `Resources` и запустите dyno для `bot`.
