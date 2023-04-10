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