import re
import os
import glob
#Ejercicio 1
def letra(letra, archivo):
    contador = 0
    with open (archivo, "r") as file:
        for line in file:
            if (line[0] != letra.lower() and line [0] != letra.upper ()):
                contador +=1
    print("El número de líneas que no empiezan con" , letra, "es", contador)

letra("h", "mda.txt")

#Ejercicio 2
def linea(qlineas, archivo):
    with open (archivo, "r") as file:
        lineas = file.readlines()
        for i in lineas[:qlineas]:
            print(i, end = "")

linea(2, "mda.txt")

#Ejercicio 3

def lineas(ultimas,archivo):
    with open (archivo, "r") as file:
        lineas3 = file.readlines()
        ulineas = lineas3[-ultimas:]
        for linea in ulineas:
            print(linea, end="")
lineas(2,"mda.txt")

#Ejercicio 4

def palabras(archivo):
    with open (archivo, "r") as file:
        lineas4 = file.readlines()
        contador = 0
        for i in lineas4:
            contador+=1
        print()
        print(contador)
palabras("mda.txt")

#Ejercicio 5

def reemplazar(letra, archivo1, archivo2):
    with open (archivo1, "r") as file:
        letras = file.read()
    for i in letra:
            nuevaletra = letras.replace (letra, letra + "\n")
    with open (archivo2, "w") as file:
        file.write(nuevaletra)
        
reemplazar("h","mda.txt","mda2.txt")

#Ejercicio 6


def eliminar(archivo1, archivo2):
    with open(archivo1, "r") as file:
        lineas = file.readlines()
    print(lineas)
    lineas2 = []
    for linea in lineas:
        linea2 = re.sub("\n", "", linea)
        lineas2.append(linea2)
    print(lineas2)
    with open(archivo2, "w") as file2:
        for i in lineas2:
            lineas3 = file2.write(i)
        
eliminar("mda.txt","mda3.txt")


#Ejercicio 7

def larga(archivo1):
    with open(archivo1, "r") as file:
        lista = file.readlines()
        lineas = []
        print(lista)
        for linea in lista:
            linea = re.sub("\n", "", linea)
            lineas.append(linea)
        print(lista)
        print(lineas)
        lista2 = []
        for i in lineas:
            lista2.append(len(i))
        posicion = lista2.index(max(lista2))
        print("La palabra más larga es", lista[posicion])
        print("Tiene un total de" + " " + str(posicion) + " " +  "caracteres" )
larga("mda.txt")

#Ejercicio 8

def arhcivos(archivo1,archivo2, archivo3):
    with open(archivo1, "r") as file:
        arch = file.read()
    with open(archivo2, "r") as file2:
        arch1 = file2.read()
    with open(archivo3, "w") as file3:
        file3.write(arch) 
        file3.write(arch1) 
arhcivos("mda.txt","mda2.txt","mda4.txt")

#Ejercicio 9

def frecuencia(archivo):
    with open (archivo, "r") as file:
        palabras = file.readlines()
        total = len(palabras)
        for i in palabras:
            veces = palabras.count(i)
            frecuencia = veces/total
            print("La palabra" + " " + i + " " + "aparece" + " " + str(veces) +" veces" + " " + ",es decir, un " + str(frecuencia) + " % del total" )
        print(palabras)

print(frecuencia("mda.txt"))

#Ejercicio 10

def leer ():
    os.chdir("Carpeta1")
    txt = glob.glob("*.txt")
    if not os.path.exists("Resultado"):
        os.mkdir("Resultado")
    for i in txt:
        with open (i, "r") as file:
            archivo = file.read()
            os.chdir("Resultado")
            with open ("todo.txt", "a") as file_2:
                file_2.write(archivo)
                os.chdir("..")
    return "todo.txt fue creado correctamente."
print(leer())
