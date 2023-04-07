#Ejercicio 1

def anterior (numero):
    return numero - 1
print(anterior(4))

def siguiente(numero):
    return numero + 1
print(siguiente(4))

#Ejercicio 2

def doble (num):
    return num *2
print(doble(3))

#Ejercicio 3

def dobant(numero):
    return ((numero-1) * 2)
def dobsig(numero):
    return ((numero+1) * 2)
print(dobant(2))
print(dobsig(4))

#Ejercicio 4

def retirar_dinero (saldo,monto):
    return max(saldo-monto,0)
print(retirar_dinero(1000,50))

#Ejercicio 5

def dia_de_la_semana_favorito (dia):
    return dia == "Sábado"
    
print(dia_de_la_semana_favorito("Sábado"))

#Ejercicio 6

def longitud(onda):
    return onda >= 223.0 and onda <= 586.8
print(longitud(250))

#Ejercicio 7

def longitud2(onda):
    return (onda >= 223.0 and onda <= 586.8) and onda != 314.5
print(longitud2(314.5))

#Ejercicio 8

def tiene_descuento (edad):

    return edad <= 12 or edad >= 60
print(tiene_descuento(50))

#Ejercicio 9
def xor(a, b):
    
    return (a and not b) or (not a and b)

print(xor(True, False))


#Ejercicio 10

def saludo (nombre, apellido):
    return "Hola como estás" + " " + str(nombre) + " " + str(apellido)
print(saludo("Juan", "Garcia"))

#Ejercicio 11

def primeraletra(string):
    if string[0] == "H":
        return(len(string))
print(primeraletra("HAS"))

#Ejercicio 12

def buen(string):
    return str.startswith(string, "Buenos" or "Buenas")
print(buen("Buenos Dias"))

#Ejercicio 13

def es_multiplo (num1, num2):
    if num2 % num1 == 0:
        return True
    else:
        return False
print(es_multiplo(5,10))

#Ejercicio 14

def numero (num):
    if num == 0:
        return "El número" + " " + "es 0"
    elif num % 2 == 0 :
        return "El número" + " " + "es par"
    else:
        return "El número" + " " + "es impar"
print(numero(3))

#Ejercicio 15

def qa (frase):
    qas = 0
    for i in frase:
        if i == "a" or i == "A":
            qas +=1
    return "La frase:" + " " + str(frase) + ", " + "tiene un total de" + " " + str(qas) + " " + "a/A"
print(qa("Hola soy Agustin"))

#Ejercicio 16

def dinero (monto):
    gasto = 60000
    return "Se pueden subsistir un total de " + str(int(monto/gasto)) + " " + "meses."
print(dinero(180001))



