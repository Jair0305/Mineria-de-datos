''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 21. Dada una lista de tuplas, donde cada tupla interna contiene números flotantes, escribe un programa que ordene cada tupla dentro de la lista en orden descendente.
'''

arr = [(1.0, 2.0, 3.0),(15.6,28.50,39.57,0.97), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]

arr = [list(tup) for tup in arr]

for i in range(len(arr)):
    for j in range(len(arr[i]) - 1):
        for k in range(len(arr[i]) - j - 1):
            if arr[i][k] < arr[i][k + 1]:
                arr[i][k], arr[i][k + 1] = arr[i][k + 1], arr[i][k]

arr = [tuple(lst) for lst in arr]