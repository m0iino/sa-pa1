#importamos autenticación httbasic
from requests.auth import HTTPBasicAuth
#importamos session
from requests import Session
# importamo zeep
from zeep import Client
# porque vamos a utilizar autenticacion zeep necesita de Transport
from zeep.transports import Transport
# se crea una sesion para usar en el request
session = Session()
#variable de usuario
user = 'sa'
#variable contraseña
password = 'usac'
# utilizamos la autenticación de HTTPBasicAuth
session.auth = HTTPBasicAuth(user, password)
# request autenticado
client = Client(wsdl='https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl',
            transport=Transport(session=session))
print(client)




