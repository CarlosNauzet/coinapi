import requests

apikey = '54CC9DB5-A9E5-4DEF-AFCA-BFAEE77C7995'
api_url = 'http://rest-sandbox.coinapi.io'
# api_url = 'http://rest.coinapi.io'
endpoint = '/v1/exchangerate'

headers = {
    'X-CoinAPI-Key': apikey
}


# Pedir moneda origen: BTC
# Pedir moneda destino: EUR
# Preguntat el cambio a la API
# Recoger el dato
# Mostrar un mensaje "Un XXX vale lo mismo que NNN YYY"
#                    "UN BTC vale lo mismo que 23000 EUR"
# Preguntar: ¿Quieres consultar de nuevo? (S/N)

# controlador
seguir = 's'

while seguir.lower() == 's':
# end controlador    
    # vista   
    moneda_origen = input('¿Qué moneda quieres cambiar? ')
    moneda_destino = input('¿Qué moneda deseas obtener? ')
    # end vista

    # modelo
    url = f'{api_url}{endpoint}/{moneda_origen}/{moneda_destino}'
    response = requests.get(url, headers=headers)
    exchange = response.json()
    rate = exchange.get("rate")
    # end modelo

    # vista
    print(f'Un {moneda_origen} vale lo mismo que {rate:,.2f} {moneda_destino}')
    # vista

    # controlador
    seguir = ''
    while seguir.lower() not in ('s', 'n'):
        seguir = input('¿Quieres consultar de nuevo (S/N) ')
    # end cotrolador