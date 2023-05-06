#!/usr/bin/env/ python3
import os, glob, sys

def primeras_lineas(path_a_txt, path_resultado, salida):

    #movemos a marzo
    #extraemos los .txt
    #leemos las primeras lineas
    #hacemos carpeta de salida (resultado)
    #hacer archivo (salidad.txt)
    #poner lineas en archivo nuevo
    os.chdir(path_a_txt)
    textos = glob.glob("*.txt")
    primer_linea = []
    for txt in textos:
        with open(txt, "r") as texto:
            primer_linea.append(texto.readline())
    
    os.chdir("../../")
    os.mkdir(path_resultado)
    os.chdir(path_resultado)
    with open (salida, "a") as final_txt:
        for linea in primer_linea:
            final_txt.write(linea)
primeras_lineas("datos/meses/marzo", "resultado", "salida.txt")