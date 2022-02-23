import html
import logging
import os
import time
from textwrap import dedent

import requests
import telegram
from dotenv import load_dotenv
from requests.exceptions import ConnectionError, ReadTimeout

logger = logging.getLogger('dvmn_bot_logger')


class TelegramBotLogHandler(logging.Handler):
    def __init__(self, bot: telegram.Bot, chat_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = html.escape(self.format(record))

        if record.levelno > logging.WARNING:
            start_text = 'Бот упал с ошибкой'
        else:
            start_text = 'Бот сообщает, что'

        self.bot.send_message(
            chat_id=self.chat_id,
            text=dedent(f'''
            {start_text}:
            <pre>{log_entry}</pre>
            '''),
            parse_mode='HTML'
        )


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_bot = telegram.Bot(token=telegram_token)

    dvmn_token = os.getenv('DVMN_TOKEN')
    dvmn_longpoll = 'https://dvmn.org/api/long_polling/'
    dvmn_headers = {
        'Authorization': f'Token {dvmn_token}'
    }

    success_message = '''
    Преподавателю всё понравилось, можно приступать к следующему уроку.
    '''

    failure_message = 'К сожалению, в работе нашлись ошибки.'

    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramBotLogHandler(telegram_bot, telegram_chat_id))
    logger.info('Бот запущен')

    timestamp = None

    while True:
        try:
            response = requests.get(
                dvmn_longpoll,
                params={'timestamp': timestamp},
                headers=dvmn_headers,
                timeout=91
            )
            response.raise_for_status()

            event = response.json()
            if event['status'] == 'timeout':
                timestamp = event['timestamp_to_request']
            else:
                timestamp = event['last_attempt_timestamp']

                for review in event['new_attempts']:
                    lesson_title = review['lesson_title']
                    lesson_url = review['lesson_url']
                    is_negative = review['is_negative']

                    message = f'''
                    Преподаватель проверил работу
                    <a href="{lesson_url}">{lesson_title}</a>.
                        
                    {failure_message if is_negative else success_message}
                    '''

                    telegram_bot.send_message(
                        chat_id=telegram_chat_id,
                        text=dedent(message),
                        parse_mode='HTML'
                    )
        except ReadTimeout:
            continue
        except ConnectionError:
            time.sleep(60)
        except Exception as error:
            logger.error(error, exc_info=True)
