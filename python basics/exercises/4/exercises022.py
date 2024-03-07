''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: 22. Dada una tupla de tuplas, donde cada tupla interna contiene números flotantes, escribe un programa para generar una nueva tupla que contenga los promedios de cada tupla interna.
'''
arr = [(1.0, 2.0, 3.0),(15.6,28.50,39.57,0.97), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
suma = 0
promedio = 0
tp = ()
arr = [list(tup) for tup in arr]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        suma += arr[i][j]
    tp = tp + (suma / len(arr[i]),)
    suma = 0
