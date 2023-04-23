#Ejercicio 1
#Ejercicio 2
#Ejercicio 3
#Ejercicio 4
#Ejercicio 5
#Ejercicio 6
#Ejercicio 7
#Ejercicio 8
#Ejercicio 9
#Ejercicio 10
#Ejercicio 11
#Ejercicio 12
#Ejercicio 13
#Ejercicio 14
#Ejercicio 15
import re
def mail_correcto(string):
    return bool(re.search("^\w[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?", string))
print(mail_correcto("restahinoch@gmail.com"))
print(mail_correcto("1restahinoch@gmail.com"))
print(mail_correcto("1resta$%&hinoch@gmail.com"))
print(mail_correcto("123123123123@gmail.com"))
print(mail_correcto("1@restahinochg/&%$#mail.com"))