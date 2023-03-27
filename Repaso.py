#Ejercicio 1

def anterior (numero):
    return numero - 1
print(anterior(4))

def siguiente(numero):
    return numero + 1
print(siguiente(4))

#Ejercicio 2
"""
def doble (num):
    return str(doble(anterior(num)) + " "+ str(doble(siguiente)))
print(doble(3))
"""
#Ejercicio 3

def dobant(numero):
    return ((numero-1) * 2)
def dobsig(numero):
    return ((numero+1) * 2)
print(dobant(2))
print(dobsig(4))

#Ejercicio 4

def retirar_dinero (saldo,monto):
    max(saldo-monto,0)
print(retirar_dinero(100,50))

#Ejercicio 5

def dia_de_la_semana_favorito (dia):
    return dia == "Sábado"
    
print(dia_de_la_semana_favorito("Sábado"))

#Ejercicio 11

def primeraletra(string):
    if string[0] == "H":
        return(len(string))
print(primeraletra("SAS"))

#Ejercicio 12

def buen(string):
    return str.startswith(string, "Buenos" or "Buenas")
print(buen("Buenos Dias"))