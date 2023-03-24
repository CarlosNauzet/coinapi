import requests

apikey = 'F8DD52B3-53AC-4AE0-818B-E2C62A964EE3'
api_url = 'http://rest-sandbox.coinapi.io'
endpoint = '/v1/exchangerate/BTC/USD'

headers = {
    'X-CoinAPI-Key' : apikey
    }

url = api_url + endpoint

response = requests.get(url, headers=headers)
status_code = response.status_code

if status_code == 200:
    print('El resultado de la consulta es')
    print(response.text)
else:
    print('La petición a la API ha fallado')
    print(f'El código de error es {status_code}')
    print(f'Motivo del error {response.reason}')
    print(response.text)