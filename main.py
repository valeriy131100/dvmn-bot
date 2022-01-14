import os

import requests
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

        except (ReadTimeout, ConnectionError):
            continue


if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('DVMN_TOKEN')

    for event in longpoll_dvmn(dvmn_token):
        print(event)
