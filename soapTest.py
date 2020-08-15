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
#contador de clientes a ingresar
#bucle para crear cliente 
for i in range(0,10): 
        #van hacer 10 clientes
        #llamamos al servicio y colocamos los parametros
                print("esto trae",client.service.create("201114527_"+str(i))) 

        
#bucle para obtener cliente
for c in client.service.readList(0,10,201114527):    
        # imprimimos el nombre del cliente
        print(c.name) 


