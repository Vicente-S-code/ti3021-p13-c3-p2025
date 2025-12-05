import requests

# Donde esta la api
base_url = "https://cl.dolarapi.com"
# [Protocolo]--- [Dominio]---[Recurso]

# Ruta endpoint que nos dice el precio del dolar segun CLP
endpoint_dolar = "/v1/cotizaciones/usd"

# Juntamos la url y su endpoint para realizar una peticion de tipo GET  
respuesta = requests.get(f"{base_url}{endpoint_dolar}")
#                                 ↑----https://cl.dolarapi.com/v1/cotizaciones/usd

try:
    # Serializamos la informacion de JSON para trabajarla de forma estructurada
    data = respuesta.json()
    # Mostramos la data rescatada de la respuesta
    print(data)
except:
    print(respuesta)