import json
import requests
import uuid
from app import app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return 'Error: the translation service is not configured.'
    
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&from={}&to={}'.format(source_language, dest_language)
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    
    body = [
        {"Text": text}
    ]

    response = requests.post(constructed_url, headers=headers, json=body)
    if response.status_code != 200:
        return 'Error {}: the translation service failed.'.format(response.status_code)

    return response.json()
