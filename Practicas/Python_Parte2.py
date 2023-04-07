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

def metodo (lista4,lista5,elemento):
     return

lista4 = ["Hola", "Chau", "Buenas","Dias"] 
lista5 = [1,2,3,4,5]