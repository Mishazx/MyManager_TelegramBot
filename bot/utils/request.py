import requests
import json
from config import DOMAIN_SERVICE_URL, API_SECRET_KEY
from session import logger


def RequestAPI(url, method='GET', data = None):
    print(API_SECRET_KEY)
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'{API_SECRET_KEY}',
    }
    full_url = f'{DOMAIN_SERVICE_URL}{url}'
    logger.debug(f'full_url: {full_url}')
    logger.debug(f'API_KEY: {API_SECRET_KEY}')
    
    logger.debug(f'Headers: {headers}')
    logger.debug(f'Data: {json.dumps(data)}') 
    try:
        if method.upper() == 'POST':
            response = requests.post(full_url, headers=headers, json=data)
        elif method.upper() == 'GET':
            response = requests.get(full_url, headers=headers, params=data)
        else:
            raise ValueError("Method not supported")
        
        logger.debug(f'Response status code: {response.status_code}')
        logger.debug(f'Response text: {response.text}')
        return response
    except Exception as e:
        print(e)
        raise e