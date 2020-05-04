# coding: utf-8
'''
Created on 6 feb. 2018
@author: monoarkhe
'''

from random import randrange

c    = [] # Caracteristicas
rmin = [] # Rango mínimo
rmax = [] # Ranto máximo
l    = [] # Lista de elementos

n = input("Nombre del fichero (sin extensión): ")
f = open(n + ".txt", "w")

# Almacenamiento de características y rangos por parte del usuario
for x in range(5):
    c.append(input("Característica " + str(x) + ": "))
    rmin.append(int(input("Rango mínimo " + c[x] + ": ")))
    rmax.append(int(input("Rango máximo " + c[x] + ": ")))

    # Bucle para rellenar las diferentes listas siguiendo el rango establecido por el usuario
    for i in range(1000):
        l.append([])
        l[x].append(randrange(rmin[x],rmax[x])) # Anidación las listas de elementos según la característica

# Declaración de variable de tipo cadena salida para la extracción de los datos
salida = c[0] + ":" + str(l[0]).replace("[", "").replace("]", "").replace(" ", "") + "\n" + c[1] + ":" + str(l[1]).replace("[", "").replace("]", "").replace(" ", "") + "\n" + c[2] + ":" + str(l[2]).replace("[", "").replace("]", "").replace(" ", "") + "\n" + c[3] + ":" + str(l[3]).replace("[", "").replace("]", "").replace(" ", "") + "\n" + c[4] + ":" + str(l[4]).replace("[", "").replace("]", "").replace(" ", "")

print(salida)   # Impresión por pantalla la salida
f.write(salida) # Escritura la salida en el fichero establecido
f.close()