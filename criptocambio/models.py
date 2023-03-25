import requests

from . import APIKEY


api_url = 'http://rest-sandbox.coinapi.io'
endpoint = '/v1/exchangerate'
headers = {
    'X-CoinAPI-Key': APIKEY
}


class APIError(Exception):
    pass

class CriptoModel:
    """
    - constructor
    - moneda origen
    - moneda destino
    - cambio
    - método(operación) consultar cambio
    """

    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.cambio = 0.0

    def consultar_cambio(self):
        url = f'{api_url}{endpoint}/{self.origen}/{self.destino}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            exchange = response.json()
            self.cambio = exchange.get("rate")
        else:
            raise APIError(
                f'Error {response.status_code} {response.reason} al consultar la API'
                )
        
