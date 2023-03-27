import os

with open("archivo_1.txt", "w") as mi_arch:
    mi_arch.write("Soy el archivo 1")
with open("archivo_2.txt", "w") as mi_arch_2:
    mi_arch_2.write("Soy el archivo 2")

os.rename("archivo_1.txt","temp.txt")
os.rename("archivo_2.txt","archivo_1.txt")
os.rename("temp.txt","archivo_2.txt")
