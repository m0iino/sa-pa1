import json
from zeep  import Client
client = Client(wsdl="https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl")
c_type = client.get_type("id:271")
cont = 0

for c in client.service.readList():
    
    if cont < 10:

        print(c)
        
        cont +=1

data_set = {"name": "201114527"}
json_dump = json.dumps(data_set)
print(json_dump)


