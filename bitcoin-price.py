import requests

print("""
This code uses the requests library to get the current Bitcoin price from the CoinDesk API. 
The requests library is very useful for interacting with APIs and making HTTP requests in Python.
""")

# URL de la API
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# Hacer la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a JSON
    data = response.json()
    
    # Extraer el precio del Bitcoin en USD
    bitcoin_price = data['bpi']['USD']['rate']
    
    print(f"El precio actual del Bitcoin es: ${bitcoin_price}")
else:
    print("Error al obtener los datos")

