"""
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
         pass
    return diccionario
print(dic("Holaaa"))

#Ejercicio 7

#Ejercicio 8

def palindromo (palabra):
     lista = []
     lista.append(palabra)
     inversa = palabra[::-1]
     lista.append(inversa)
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
"""
#Ejercicio 10

def club():
     dic = {1: {"nombre_y_apellido": "Florencia Ocampo", "fecha_de_ingreso": "14092001", "cuota_al_dia": True},
            2: {"nombre_y_apellido": "David Estévez", "fecha_de_ingreso": "14092001", "cuota_al_dia": True},
            3: {"nombre_y_apellido": "Sofía Cáceres", "fecha_de_ingreso": "14092001", "cuota_al_dia": True}}
     return dic
dic = club()
print(club)

def cantidad_socios(dic):
    socios = 0
    for i in dic.values():
        if "nombre_y_apellido" in i:
            socios+=1
    return socios
print(cantidad_socios)
          

