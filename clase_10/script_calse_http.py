import requests #Laos verbos http son las consultas que disparan acciones particular en el servidor
respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs") #get = Es el verbo http asociado a las consultas
datos = respuesta.json() #Estructura de dato, es como una estructura de diccionario o (lista)

#1)Obtener cantidad de organizaciones
print(len(datos))

#2)Obtener lista de nombres de las orgs en las que estoy involucrado - TAREA
print(respuesta)
print(respuesta.headers) #Nos printea un objeto
print(respuesta.status_code  )



#El verbo post está asociado a persistir datos (de cero), generar una nueva entrada de la base de datos.
#EL verbo delete se encarga de borrar datos.
#El verbo patch está asociado a reescribir datos.
#En los headers voy a encontrar toda la información asociada a los requests


"""
Tipico Ejercicio de Parcial

Quiero obtener los nombres de las organizaciones
"""
