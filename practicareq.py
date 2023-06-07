import requests
#DESAFIO 1
pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu") #A) El dominio es pokeapi.co
pokemones = requests.get("https://pokeapi.co/api/v2/pokemon") #A) El dominio es pokeapi.co

#B
headers = pikachu.headers
print(headers["Content-Type"]) #CONTENT TYPE
print(pikachu.status_code) #STATUS CODE
contenido_pikachu = pikachu.json()
keys = pikachu.json().keys()
print(keys)
print(contenido_pikachu["forms"]) #FORMS
#C
contenido_pokemones = pokemones.json()
print((contenido_pokemones["count"]))
#D
"https://pokeapi.co/api/v2/ability" # URL PARA HABILIDADES
"https://pokeapi.co/api/v2/ability/2" #URL PARA LA HABILIDAD 2
#E
sylveon = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")
contenido_sylveon = sylveon.json()
"""
string_sylveon = str(sylveon.json())
print(string_sylveon)"""
with open("ficha_tecnica_pokemon.txt", "wb") as ficha:
    ficha.write(pikachu.content)
    ficha.write(b"\n")
    ficha.write(sylveon.content)

#F

#RESPONDER LA PREGUNTA
print()
#DESAFIO 2

#https://jsonplaceholder.typicode.com/todos

#A - jsonplaceholder.typicode.com

desafio = requests.get("https://jsonplaceholder.typicode.com/todos")
headers_2 = desafio.headers
print(headers_2["Content-Type"]) #CONTENT TYPE
print(desafio.status_code) #STATUS CODE