import time
import os
from textwrap import dedent

import requests
import telegram
from dotenv import load_dotenv
from requests.exceptions import ConnectionError, ReadTimeout


def longpoll_dvmn(token):
    headers = {
        'Authorization': f'Token {token}'
    }

    url = 'https://dvmn.org/api/long_polling/'

    timestamp = None
    while True:
        try:
            params = {
                'timestamp': timestamp
            }

            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=91
            )
            response.raise_for_status()

            api_answer = response.json()
            if api_answer['status'] == 'timeout':
                timestamp = api_answer['timestamp_to_request']
            else:
                timestamp = api_answer['last_attempt_timestamp']
                yield api_answer

        except ReadTimeout:
            continue

        except ConnectionError:
            time.sleep(60)


if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('DVMN_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_bot = telegram.Bot(token=telegram_token)

    success_message = '''
    Преподавателю всё понравилось, можно приступать к следующему уроку\\.
    '''

    failure_message = 'К сожалению, в работе нашлись ошибки\\.'

    for event in longpoll_dvmn(dvmn_token):
        for review in event['new_attempts']:
            lesson_title = review['lesson_title']
            lesson_url = review['lesson_url']
            is_negative = review['is_negative']

            message = f'''
            Преподаватель проверил работу
            [{lesson_title}]({lesson_url})\\.
                
            {failure_message if is_negative else success_message}
            '''

            telegram_bot.send_message(
                chat_id=telegram_chat_id,
                text=dedent(message),
                parse_mode='MarkdownV2'
            )
