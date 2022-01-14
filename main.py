import os

import requests
from dotenv import load_dotenv
from requests.exceptions import ConnectionError, ReadTimeout

if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('DVMN_TOKEN')

    headers = {
        'Authorization': f'Token {dvmn_token}'
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
            print(api_answer)
            if api_answer['status'] == 'timeout':
                timestamp = api_answer['timestamp_to_request']
            else:
                timestamp = api_answer['last_attempt_timestamp']

        except (ReadTimeout, ConnectionError) as e:
            continue
