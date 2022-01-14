import os

import requests
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    dvmn_token = os.getenv('DVMN_TOKEN')

    headers = {
        'Authorization': f'Token {dvmn_token}'
    }

    url = 'https://dvmn.org/api/user_reviews/'

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    print(response.json())
