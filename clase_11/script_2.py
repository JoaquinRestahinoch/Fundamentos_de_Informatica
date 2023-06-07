import requests

#Con un get me traigo todos los  /recurso  y si quiero algo más especifico con un get me puedo traer una fila en especifica de una base de datos si es asi /recurso/id. El id se lo conoce como un parámetro. Se lo agrega a la url para que se pueda utilizar y de alguna forma filtrar en la base de datos.

"""
[{'ability': {'name': 'limber', 'url': 'https://pokeapi.co/api/v2/ability/7/'}, 'is_hidden': False, 'slot': 1},
{'ability': {'name': 'imposter', 'url': 'https://pokeapi.co/api/v2/ability/150/'}, 'is_hidden': True, 'slot': 3}]

"""
rta = requests.get("https://pokeapi.co/api/v2/ability/150/")
print(rta.json())

r = requests.get('https://macowins-server.herokuapp.com/prendas?talle=40')

"""
https://   /recurso             (Con un get me traigo todos los items de ese recurso
https://   /recurso/id          (Con un get me traigo un item en particular)
https://   /recurso?key=valor   (Con un get me traigo todos los items que tienen ese valor en esa key)

? El signo de pregunta significa "Busca".
Los query params son todas las claves que le paso a la api a través de la url para filtrar la busqueda de la base de datos
key ==> Es la clave
valor ==> Es el valor
Con el & puedo concatenar filtados https://   /recurso?key=valor&key=valor (Ejemplo en GitHub Teórico)


/recurso/id


#Get ==> Me muestra el item del recurso.
#Post/Patch ==> Modificando ese item.
#Delete ==> Borrar ese item.


Para cada URL api REST voy a tener distintos verbos http para usar.
No tendria sentido tirar un delete de /recurso

Cuando hago un post le tengo que pasar los datos.
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)

Put ==> Modifica todo el item
Patch ==> Modifica una parte del item

POST /ventas/1 crear uno con ID (QMP no lo soporta) ==> (No debería ser así)

Cuando yo quiero crear un nuevo item lo tengo que hacer sobre /recurso/ y no sobre /recurso/id

Los frameworks son como bibliotecas pero que tienen muchas más utilidades y son más sencillas
El back es todo lo que esta manejando los datos
El front es toda la interfaz del usuario

Las API son las rutas (endpoint) donde un usuario pueder acceder a los recursos
"""