import cmath
"""
a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions

sol1 = (-b-cmath.sqrt(d)/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#El error está en la linea 11, hay un paréntesis que nunca se cierra. Aparece en rojo.
#La diferencia entre el Try and Except con el if es que el codigo se corta con el if, mientras que con el try and except el código sigue.
"""
def eneavo(numero):
    return 1/numero

print(eneavo(9))

def eneavo(numero):
    try:
        return 1/numero
    except ZeroDivisionError:
        return "No se puede dividir por 0"

print(eneavo(0))
