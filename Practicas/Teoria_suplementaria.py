#!/user/bin/python
import os, glob

def carpeta():
    os.chdir("../Informes")
    txt = glob.glob("*.txt")
    cantidad_estado = []
    cantidad_lineas = []
    print(txt)
    for archivo in txt:
        with open (archivo, "r") as file:
            archivo_completo = file.read()
            cantidad_estado.append (archivo_completo.count("estado"))
            print(cantidad_estado)
            cantidad_lineas.append (archivo_completo.count("\n"))
            print(cantidad_lineas)
    os.mkdir("Apellidos")
    with open ("Apellidos/Lista.txt", "w") as salida:
        for archivo in txt:
            with open(archivo, "r") as file:
                primer_linea = file.readline()
                salida.write(primer_linea)

if __name__ == "__main__":
    print(carpeta())