#importamos request
import requests
import json
# url para obtener el acces_token
endpoint = "https://api.softwareavanzado.world/index.php?option=token&api=oauth2"
#colocamos en el header los valores del body con la llave client_secret
headers = {"client_id":"sa",
            "client_secret":"fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745",
            "grant_type": "client_credentials",
            }
#guardamos en un response el request post
response = requests.post(endpoint, data=headers)
#imprimirmos el status del response
print("status cod:", response.status_code)
print(response.json()["access_token"])
# guardamos el access_token en el bearer
bearer = response.json()["access_token"]
#url para hacer un crear
endpoint = "https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal"
# iteramos 10 porque vamos a crear 10 contactos
for i in (0,10):
    #nombre del contacto
    data = {"name":"201114527_"+str(i)}
    #agregamos en el header el bearer 
    headers = { "Authorization": "Bearer "+str(bearer)
            }
    #hacemos un request tipo post y lo guardamos en un response
    response = requests.post(endpoint, data=data, headers=headers )
    #imprimimos el status del response
    print("status code:", response.status_code)
    print(response)
# url para listar a los contactos
endpoint = "https://api.softwareavanzado.world/administrator/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal&filter[search]=201114527B"
#agregamos el bearer al header
headers = { "Authorization": "Bearer "+str(bearer)
            }
# hacemos un request get y lo guardamos en un response
response = requests.get(endpoint, headers=headers )
# imprimimos el status del reponse
print("status code:", response.status_code)
# imprimimos el listado
print(response.json())
