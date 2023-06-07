#1 Describir las partes de la url
#2 ¿Qué respuesta obtenés al hacer un get a esa URL
#3 ¿Cuál es el content type de esa respuesta?
#4 ¿Cuál es el status code de la respuesta?
#5 ¿Cuántas habilidades (habilities) tiene este pokemon? 

import requests

#1
# https:// ==> Es el PROTOCOLO que usamos para acceder
# pokeapi.co/api/v2/ ==> Es el DOMINIO, es el nombre con el cuál voy a mapear una ip en particular. Lo que está detrás del dominio es la ip. ?
# pokemon/ditto ==> Son los RECURSOS ?
#La diferencia entre un path (es local) y una URL (es en la red, es como un path via internet).

#2
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto") #Es una api REST, para que una api sea REST las urls tiene que de alguna forma mapear recursos. Los recursos son los que almaceno en la base de datos y los puedo consultar. 

contenido_respuesta = respuesta.json()
print(contenido_respuesta.keys()) #De esta forma accedemos a lo que hay dentro del diccionario. 
#Me da por respuesta todos los contenidos asociados al recurso ditto con los detalles de toda su información de la base de datos.


#3
headers = respuesta.headers
print(headers["Content-Type"]) #Trae un json, el protocolo http solo permite que se envien costas en formato de texto. (IMPORTANTE)

#4
print(respuesta.status_code) #Si me devuelve 200, es que está todo OK.

#5
print("Tiene",  str(len(contenido_respuesta["abilities"])), "habilidades")




