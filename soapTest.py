import json
from zeep  import Client
client = Client(wsdl="https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl")
c = 7
#for i in range(c):
#        if c <= 10:
#                print("esto trae",client.service.create("201114527_"+str(c)))
#        c +=1

for c in client.service.readList(0,10,201114527):    
        print(c.name)



