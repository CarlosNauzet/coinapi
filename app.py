""" # aqui esta mi primero intneot con las 2 apis (+ adrián)
import requests

apikey = 'F8DD52B3-53AC-4AE0-818B-E2C62A964EE3'
apikey2 = '667629F8-5988-4636-A162-80F446EA8C23'
api_url = 'http://rest-sandbox.coinapi.io'
endpoint = '/v1/exchangerate/BTC/USD'

headers = {'X-CoinAPI-Key' : apikey}

url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey=F8DD52B3-53AC-4AE0-818B-E2C62A964EE3"


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

"""
"""
# aquí tenog que meter "moneda desde" a "moneda a" (desarrolado cona Adri)
def getprecio(Monedadesde, moneda_A, api):
    url = f"https://rest.coinapi.io/v1/exchangerate/{Monedadesde}/{moneda_A}?apikey={api}"
    print(url)
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

getprecio("EUR", "ETH", apikey) 
getprecio("BNB", "DOGE", apikey)
    
"""

# código de TOny
import requests

apikey = '54CC9DB5-A9E5-4DEF-AFCA-BFAEE77C7995'
api_url = 'http://rest-sandbox.coinapi.io'
endpoint = '/v1/exchangerate/BTC/EUR'

headers = {
    'X-CoinAPI-Key': apikey
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

    


