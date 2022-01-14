import os

import requests
from requests.exceptions import ReadTimeout, ConnectionError
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('DVMN_TOKEN')

    headers = {
        'Authorization': f'Token {dvmn_token}'
    }

    url = 'https://dvmn.org/api/long_polling/'

    while True:
        try:
            response = requests.get(url, headers=headers, timeout=90)
            print(response.json())
        except (ReadTimeout, ConnectionError):
            continue
