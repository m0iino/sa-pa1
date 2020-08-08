from zeep  import Client #importamos Client del zeep
client = Client(wsdl="https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl") #url de acceso al web service
c = 0 #contador de clientes a ingresar
for i in range(c): #bucle para crear cliente 
        if c < 10: #van hacer 10 clientes
                print("esto trae",client.service.create("201114527_"+str(c))) #llamamos al servicio y colocamos los parametros
        c +=1 #incremantamos el contador en 1

for c in client.service.readList(0,10,201114527):    #bucle para obtener cliente
        print(c.name) # imprimimos el nombre del cliente



    





