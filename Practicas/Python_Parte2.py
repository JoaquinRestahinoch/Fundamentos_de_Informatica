#Ejercicio 1
def procedimiento (lista):
    for i in lista :
        if i == "control":
            posicion = lista.index(i)
            lista.insert(posicion,"revisado")
            lista.remove (i)
    print(lista)

lista = ["dghhg", "control", "dfghfgh"]
procedimiento (lista)

#Ejercicio 2

def remover (lista):
        lista.pop (0)
        print(lista)

lista2 = ["hola", "chau", "dfghfgh"]
remover (lista2)

#Ejercicio 3

def posicion (elemento):
    lista = ["Hola", "Chau", "Buenas","Dias"]
    for i in lista: 
        return lista.index(elemento)
print(posicion("Chau"))

#Ejercicio 4

#Metodo 1
from random import randrange
def metodo (lista,lista2):
     posicion = randrange(len(lista))
     print(posicion)
     elemento = lista[posicion]
     lista2.append(elemento)
     lista.remove(elemento)
     print(lista)
     print(lista2)
lista4 = ["Hola", "Chau", "Buenas","Dias"] 
lista5 = [1,2,3,4,5]
print(metodo(lista4,lista5))

# Metodo 2
def metodo (lista,lista2,elemento):
     lista2.append(elemento)
     lista.remove(elemento)
     print(lista)
     print(lista2)
lista4 = ["Hola", "Chau", "Buenas","Dias"] 
lista5 = [1,2,3,4,5]
print(metodo(lista4,lista5, "Chau"))

#Ejercicio 5

def booleanos(lista):
    lista2 = []
    for i in lista:
        if i % 2 == 0 :
            lista2.append("True")
        else:
             lista2.append("False")
    return lista2
lista6 = [1,2,3,4,5,6]
print(booleanos(lista6)) 

#Ejercicio 6

def dic(cadena):
    
    diccionario = {}
    for i in cadena:
        if i in diccionario:
         diccionario[i] +=1
        else:
         diccionario[i] = 1
    return diccionario
print(dic("Holaaah"))

#Ejercicio 7

def dic(cadena):
    diccionario = {}
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in cadena:
        if i in diccionario:
         diccionario[i] +=1
        else:
         diccionario[i] = 1
    for i in alfabeto:
        if i not in cadena:
            diccionario[i] = 0
    return diccionario
print(dic("Holaaah"))

#Ejercicio 8

def palindromo (palabra):
     lista = []
     lista.append(palabra)
     inversa = palabra[::-1]
     +lista.append(inversa)
     if lista [0] == lista[1]:
          return True
     else:
          return False
print(palindromo("argra"))

#Ejercicio 9

def productoria(numeros):
    producto = 1
    for i in numeros:
         producto *= i
    return producto
numeros1 = [2,3,1,2]
print(productoria(numeros1))


#Ejercicio 10

def club():
     dic = {1: {"nombre_y_apellido": "Florencia Ocampo", "fecha_de_ingreso": "14092001", "cuota_al_dia": True},
            2: {"nombre_y_apellido": "David Estévez", "fecha_de_ingreso": "14092001", "cuota_al_dia": True},
            3: {"nombre_y_apellido": "Sofía Cáceres", "fecha_de_ingreso": "14092001", "cuota_al_dia": True}}
     return dic
dic = club()
print(club)

def cargar_socio(dic): #Función creada para cargar 10 socios en total (los 3 iniciales + los 7 a eleección del usuario) 
    contador = 3
    while contador < 10:
        socios_ya_cargados = [1,2,3]
        numero = int(input("Ingrese el número de socio: "))
        while numero <= len(socios_ya_cargados):
            numero = int(input("Ingrese el número de socio: "))
        socios_ya_cargados.append(len(socios_ya_cargados) + 1)
        nombre_y_apellido = input("Ingrese el nombre del socio: ")
        apellido = input("Ingrese el apellido del socio: ")
        fecha_de_ingreso = input("Ingrese la fecha de ingreso en formato ddmmaaaa: ")
        cuota_al_dia = (input("La cuota está al día? (True/False): "))
        if cuota_al_dia == "True":
            cuota_al_dia = True
        else:
            cuota_al_dia = False
        dic[numero] = {"nombre_y_apellido": nombre_y_apellido, "fecha_ingreso": fecha_de_ingreso, "cuota_al_dia": cuota_al_dia}
        contador+=1
    print(dic)
print(cargar_socio(dic))

def cantidad_socios(dic):
    socios = 0
    for i in dic.values():
        if "nombre_y_apellido" in i:
            socios+=1
    return socios
print(cantidad_socios(dic))
          
def socio_al_dia(dic):
    socio = int(input("Ingrese el número de socio: "))
    return dic[socio]["cuota_al_dia"]
print(socio_al_dia(dic))

def fecha(dic):
    for i in dic:
        if dic[i]["fecha_de_ingreso"] == "21102017":
            dic[i]["fecha_de_ingreso"] = "22102017"
print(fecha(dic))

def eliminar_socio(dic):
    nombre = input("Ingrese el nombre completo de la persona a dar de baja: ")
    for i in dic:
        if dic[i]["nombre_y_apellido"] == nombre:
            del dic[i]
            break
    print(dic)
print(eliminar_socio(dic))
print(dic)
