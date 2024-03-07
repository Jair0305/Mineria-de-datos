''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: 26. Dada una tupla de tuplas, en donde cada tupla interna está formada por 2 números enteros, escribe un programa que genere una lista que contenga aquellos pares de tuplas que sean simétricas (a,b) (b,a).
'''

tp = ((1, 2), (3, 4), (5, 6), (7, 8),(3,3))
arr = list(tp)
arrresult = []
for i in range(len(arr)):
    if arr[i][0] == arr[i][1]:
        arrresult.append(arr[i])

tp = tuple(arr)
tupleresult = tuple(arrresult)


print(tupleresult)
