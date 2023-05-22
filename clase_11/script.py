#1 Describir las partes de la url
#2 ¿Qué respuesta obtenés al hacer un get a esa URL
#3 ¿Cuál es el content type de esa respuesta?
#4 ¿Cuál es el status code de la respuesta?
#5 ¿Cuántas habilidades (habilities) tiene este pokemon? 

import requests

#1
# https:// ==> Es el PROTOCOLO que usamos para acceder
# pokeapi.co/ ==> Es el DOMINIO, es el nombre con el cuál voy a mapear una ip en particular. Lo que está detrás del dominio es la ip.
# api/v2/pokemon/ditto ==> Son los RECURSOS

#2
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto") #Es una api REST, para que una api sea REST las urls tiene que de alguna forma mapear recursos. Los recursos son los que almaceno en la base de datos y los puedo consultar. 
print(respuesta)

datos = respuesta.json()
print(datos)

#3
for i in datos:
    print(i["Content-Type"])

#4
print(respuesta.status_code)

#5




