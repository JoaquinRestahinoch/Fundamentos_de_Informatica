#Ejercicio 1

lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except TypeError: #Hay que aclarar el tipo de error
    print("No puedo agregar arroz ya que no puedo concatenar un string con una lista") #Este string tiene que ser explicativo y claro de cual es el error

#Ejercicio 2

def numero (lista,numero):
    lista_nueva = []
    try:
        for i in lista:
            num_dividido = i /numero
            lista_nueva.append(num_dividido)
        return lista_nueva
    except ZeroDivisionError:
        return "No se puede dividir por 0"
    except TypeError:
        return "No se puede dividir por un string"
lista2 = [1,2,3,4,5]
print(numero(lista2,2))

#Ejercicio 3
def ejercicio(lista,num):
    try:
        if num > 0:
            lista_3.append(num)
        return lista
    except:
        return "Solo se pueden agregar número positivos, no se pueden agregar ni strings ni numeros negativos"

lista_3 = [10,11,12,13,14]
print(ejercicio(lista_3, "hola"))