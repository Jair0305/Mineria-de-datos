''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: 26. Dada una tupla de tuplas, en donde cada tupla interna está formada por 2 números enteros, escribe un programa que genere una lista que contenga aquellos pares de tuplas que sean simétricas (a,b) (b,a).
'''

arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [1,2,3,5,6,7,8,9,10]

for i in range(len(arr1)):
    if arr1[i] in arr2:
        continue
    else:
        print(f'el objeto {arr1[i]} no esta en el arr2')
        break