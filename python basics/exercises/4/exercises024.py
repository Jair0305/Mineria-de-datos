''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: 24. Dada una tupla de tuplas, donde cada tupla interna contiene strings, escribe un programa que solicité un string al usuario y determine si se encuentra dentro de alguna tupla interna y el número de tupla que es.
'''

tp = (("hola","como","estas"),("bien","y","tu"),("muy","bien","gracias"),("adios","nos","vemos"))

entry = input("Ingrese un string: ")

for i in range(len(tp)):
    if entry in tp[i]:
        print(f"El string {entry} se encuentra en la tupla {i}")
        break