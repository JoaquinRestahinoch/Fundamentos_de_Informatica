#!/bin/python3
import os,sys

archivo = sys.argv[1]

def saludador (nombre):
    return "Hola " + nombre

if __name__ == "__main__":
    print(saludador(archivo))