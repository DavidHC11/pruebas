# modulo1.py

# /Users/davidhdz/Documents/Github/pruebas/Modulos
#!/usr/bin/env python3

""" modulo1.py - es un ejemplo de un modulo de python"""

from regex import D


if __name__ == "__main__":
    print("Estas editando en el principal")
else:
    print("Estas editando en: ", __name__)

#mi primera variable en un modulo 

a = 100
b = 101

def sumalist(lista):
    suma = 0
    for x in lista:
        suma += x

    return suma

def prodlist(lista):
    contador = 1
    for x in lista:
        contador *= x
    return contador