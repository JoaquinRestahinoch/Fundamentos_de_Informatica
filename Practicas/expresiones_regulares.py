import re
#Ejercicio 1

def caracter_permitido (string):
    return bool(re.search(r"[a-zA-Z0-9]", string))
print(caracter_permitido("hola123456789"))
#Ejercicio 2
#Escribí un programa que verifique si un string tiene todos sus 
# caracteres permitidos. 
# Estos caracteres son a-z, A-Z y 0-9.
def caracter_permitido2(string):
    return not bool(re.search(r"[^a-zA-Z0-9]", string))
print(caracter_permitido2("hola123@456789"))
print(caracter_permitido2("hola123456789"))

#Ejercicio 3
#1
print("1")
def encontrar_patron (string):
    patron = r"he*"
    if re.search(patron, string) is not None:
        return("Se encontró el patrón")
    else:
        return "No se encontró el patrón"
print(encontrar_patron("as"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))

#2
print("2")
def encontrar_patron2 (string):
    patron = r"he+"
    if re.search(patron, string) is not None:
        return("Se encontró el patrón")
    else:
        return "No se encontró el patrón"
print(encontrar_patron2("heee"))
print(encontrar_patron2("h"))
print(encontrar_patron2("as"))

#3
print("3")
def encontrar_patron3 (string):
    patron = r"he?"
    if re.search(patron, string) is not None:
        return("Se encontró el patrón")
    else:
        return "No se encontró el patrón"
print(encontrar_patron3("h"))
print(encontrar_patron3("he"))
print(encontrar_patron3(" eeeea"))

#4
print("4")
def encontrar_patron4 (string):
    patron = r"he{2,3}"
    if re.search(patron, string) is not None:
        return("Se encontró el patrón")
    else:
        return "No se encontró el patrón"
print(encontrar_patron4("heh"))
print(encontrar_patron4("hey"))
print(encontrar_patron4("heeeeeee"))


#Ejercicio 4
def guion_bajo(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Patron si"
    else:
        return "Patron no"

print(guion_bajo("enriquepablo"))
print(guion_bajo("enrique_pablo"))

#Ejercicio 5
def numero_especifico(string):
    patron = "^\d"
    if re.search(patron, string) is not None:
        return "Patron s"
    else:
        return "Patron n"

print(numero_especifico("1string"))
print(numero_especifico("string"))


#Ejercicio 6
def frase_dada(lista,frase):
    for i in lista:
        patron = i
        if re.search(patron,frase):
            print("Está")
        else: 
            print("No está")
lista = ["hola", "buen", "dia", "chau"]
print(frase_dada(lista, "hola buen dia pablo"))
#Ejercicio 7
def string(palabra):
    patron = r"\w+\s+"
    return re.search(patron, palabra)


print(string("hola32@4coomoe@"))
print(string("hol4coomoe@"))
print(string("hola324 coomoe@"))


#Ejercicio 8
def numeros (string):
    patron = r"\d"
    return re.findall(patron, string)

print(numeros("Hola 10, TENGO 50 años y soy un 2"))

#Ejercicio 9
def guiones (string):
    patron = r"-(.*?)-"
    return re.findall(patron, string)
print(guiones("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))
#Ejercicio 10
def especiales (string):
    patron = r"[@|&](.*?)[@|&]"
    return re.findall(patron, string)
print(especiales("Hoy estuvimos @trabajando@ con re &regular& expression en python -con VSCode-"))
#Ejercicio 11
def pe(lista):
    lista_p1 = []
    lista_p2 = []
    for i in lista:
        patron = r"^P"
        if re.search(patron, i) is not None:
            lista_p1.append(i)
    lista_p2.append(lista_p1[0])
    lista_p2.append(lista_p1[1])
    print(lista_p2)

listaq = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
print(pe(listaq))
#Ejercicio 12
def reemplazar1(string):
    return re.sub(r"[ _:-]", "|", string)
print(reemplazar1("hola_ _chau:je"))
#Ejercicio 13
def reemplazar2(string):
    return re.sub(r"[\W]", "_", string, count=2)
print(reemplazar2("h&ol@a@_ _chau:je"))
print(reemplazar2("@@@hola123_"))
#Ejercicio 14
def reemplazar3(string):
    return string.replace(" ", ";").replace("\t", ";")
print(reemplazar3("h    & ol@  a@_ _chau:je"))
print(reemplazar3("@    @ @hola123_"))

#Ejercicio 15
def mail_correcto(string):
    return bool(re.search("^\w[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?", string))
print(mail_correcto("restahinoch@gmail.com"))

"""
r: significa que cualquier carácter especial contenido en la cadena se interpreta literalmente. (raw string)
 ^: indica el inicio de línea
 [a-zA-Z0-9._%+-]+: representa el nombre del usuario de la dirección de correo electrónico,  el cual debe estar conformado por uno o más caracteres alfanuméricos, puntos, guiones bajos, porcentajes, más y guiones.
 @: se utiliza para separar el nombre del usuario de la dirección de correo electrónico del dominio.
 [a-zA-Z0-9.-]+: especifica el dominio del correo electrónico, puede estar conformado por uno o más caracteres alfanuméricos, puntos y guiones.
 \.: indica que debe haber un punto.
 [a-zA-Z]{2,}: especifica la extensión de la dirección de correo electrónico, la cual debe estar conformada por dos o más caracteres alfabéticos.
""" 