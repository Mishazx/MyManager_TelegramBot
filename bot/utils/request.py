import requests
from config import DOMAIN_SERVICE_URL, API_SECRET_KEY


def RequestAPI(url, method='GET', data = None):
    headers = {
        'Content-Type': 'application/json', 
        'Authorization ': f'{API_SECRET_KEY}',  # Добавьте другие заголовки, если необходимо
    }
    if method.upper() == 'POST':
        response = requests.post(f"{DOMAIN_SERVICE_URL}{url}", headers=headers, json=data)
    elif method.upper() == 'GET':
        response = requests.get(f"{DOMAIN_SERVICE_URL}{url}", headers=headers, params=data)
    else:
        raise ValueError("Method not supported")
    
    return response
    # response = requests.post(f"{DOMAIN_SERVICE_URL}{url}", headers=headers, data=data)
    # return response