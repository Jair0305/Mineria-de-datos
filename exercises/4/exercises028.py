''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: 28. Dadas tres listas llenas con números enteros, escribe un programa que encuentre todos los elementos que comparten las tres listas.
'''

arr1 = [1,2,3,4,5,6,7,8,9,10]
arr2 = [1,2,3,5,6,7,8,9,10]
arr3 = [1,2,3,5,6,7,8,9,10]

for i in range(len(arr1)):
    if arr1[i] in arr2 and arr1[i] in arr3:
        print(f'el objeto {arr1[i]} esta en los tres arr')
    else:
        print(f'el objeto {arr1[i]} no esta en los tres arr')
        break