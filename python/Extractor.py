# coding: utf-8
'''
Created on 19 feb. 2018
Objetivo: media, moda, máximo, mínimo y varianza

@author: monoarkhe
'''

'''
FUNCIONES
'''
# Cálculo de la media
def media(l):
    suma = 0
    total = len(l)

    for i in range(total):
        suma += int(l[i])
    resultado = suma / total

    return resultado

# Cálculo de la moda
def moda(l):
    M = 0
    cont = 0
    ll=sorted(l)
    moda = "error" # Si no se repite ningún número ni una sola vez, no habrá moda

    for i in range(0,len(l)-1):
        if (ll[i] == ll[i+1]):
            cont = cont + 1
            if cont >= M:
                M = cont
                moda = ll[i]
        else:
            cont=0

    return moda

# Cálculo del mínimo y del máximo
def minimo(l):
    ll=sorted(l)
    nl = []

    for i in range(len(l)) :
        nl.append(int(ll[i]))

    minimo = min(nl)

    return minimo

def maximo(l):
    ll=sorted(l)
    nl = []

    for i in range(len(l)) :
        nl.append(int(ll[i]))

    maximo = max(nl)

    return maximo

# Cálculo de la varianza
def varianza(l):
    m = media(l)
    t = 0

    for i in range(len(l)):
        t = t + pow((int(l[i]) - m), 2)

    varianza = t / len(l)

    return varianza

'''
CÓDIGO
'''
# Declaración y apertura del fichero sobre el que trabajar
n = input("Nombre del fichero (sin extensión): ")
f = open(n + ".txt", "r")
entrada = f.read()

# Declaración de variables
n = [] # Lista de nombres de caracteristicas
matrix = [] # Matriz de elementos numéricos
l = entrada.split("\n")

for i in range(len(l)):
    n.append(l[i].split(":")[0]) # Almacena los nombres de variables
    matrix.append([])
    matrix[i] = l[i].split(":")[1].split(",")  # Almacena elementos en matrix

    print(n[i].upper() + "\n")
    print("Media: " + str(media(matrix[i])))
    print("Moda: " + str(moda(matrix[i])))
    print("Mínimo: " + str(minimo(matrix[i])))
    print("Máximo: " + str(maximo(matrix[i])))
    print("Varianza: " + str(varianza(matrix[i])))
    print("------------------------------------------------------")

f.close