def start_with(letra, archivo):
    contador = 0
    with open (archivo, "r") as file:
        for line in file:
            if (line[0] != letra.lower() or line [0] != letra.upper ()):
                count +=1
    print("El númer de líneas que no empiezan con" , letra, "es", count)

start_with("H", "documento")

#Ejercicio 3

def read_n_back_lines (n, archivo):
    texto = open (archivo, "r").readlines()
    for i in range ((len(texto) -n), len(texto)):
        print(texto)

print(read_n_back_lines(4,"documento"))