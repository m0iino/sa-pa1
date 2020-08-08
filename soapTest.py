#importamos Client del zeep
from zeep  import Client 
#url de acceso al web service
client = Client(wsdl="https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl") 
#contador de clientes a ingresar
c = 0 
#bucle para crear cliente 
for i in range(c): 
        #van hacer 10 clientes
        if c < 10: 
                #llamamos al servicio y colocamos los parametros
                print("esto trae",client.service.create("201114527_"+str(c))) 
        #incremantamos el contador en 1
        c +=1 
#bucle para obtener cliente
for c in client.service.readList(0,10,201114527):    
        # imprimimos el nombre del cliente
        print(c.name) 

    





