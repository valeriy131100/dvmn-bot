# dvmn-bot

Telegram-бот отправляющий уведомления о проверке работ на [dvmn](https://dvmn.org).

## Установка
Вам понадобится установленный Python 3.6+ и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/dvmn-bot
```

Создайте в этой папке виртуальное окружение:
```bash
$ cd dvmn-bot
$ python3 -m venv venv
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Использование
Заполните файл .env.example и переименуйте его в .env или иным образом задайте переменные среды:
* DVMN_TOKEN - токен к [Devman API](https://dvmn.org/api/docs/).
* TELEGRAM_TOKEN - токен бота Telegram. Можно получить у [@BotFather](https://t.me/BotFather).
* TELEGRAM_CHAT_ID - ваш идентификатор Telegram. Можно узнать у бота [@userinfobot](https://t.me/userinfobot).

Перед запуском напишите вашему боту любое сообщение, чтобы в будущем он мог писать вам.

Находясь в директории dvmn-bot исполните:
```bash
$ venv/bin/python main.py
```

Бот запустится и будет отправлять вам в личные сообщения новые проверки на dvmn.