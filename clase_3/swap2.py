import os
import sys

def renombrar():
    name1 = sys.argv[1]
    name2 = sys.argv[2]
    with open(name1, "w") as mi_arch:
        mi_arch.write("Soy el archivo 1")
    with open(name2, "w") as mi_arch_2:
        mi_arch_2.write("Soy el archivo 2")

    os.rename(name1,"temp.txt")
    os.rename(name2 ,name1)
    os.rename("temp.txt",name2)

if __name__ == "__main__":
    print(renombrar())