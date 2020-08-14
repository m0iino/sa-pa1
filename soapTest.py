#importamos Client del zeep
from zeep  import Client 
#url de acceso al web service
client = Client(wsdl="https://api.softwareavanzado.world/index.php?option=token&api=oauth2&grant_type=client_credentials&client_id=sa&client_secret=fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745") 
print(client)

    






