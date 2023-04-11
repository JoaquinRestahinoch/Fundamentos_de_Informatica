import re
"""texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto)) #En cualquier parte del texto la primera aparicion que haya
print(texto[22:26])
#Probamos match
print(re.match(patron, texto))#Solo se fija al principio del texto
print(re.findall(patron, texto))#Me trae todas las apariciones del patron en una lista
print(re.search(patron, texto).group())#Me junta todos los caracteres que surgieron del resultados de mi busqueda"""


texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"
print(re.search(patron,texto))

print(re.search(patron, texto).group())

print(re.search(patron, texto).group(0)) #Todo el intervalo

print(re.search(patron, texto).group(1)) #El intervalo menos lo que yo le aclare

print(re.sub(patron, "###", texto))
