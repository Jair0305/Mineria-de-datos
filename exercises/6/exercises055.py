''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 55. Escribe una función que reciba una lista de números enteros y que devuelva si la lista está ordenada o no.
'''

def list_order(list):
    return list == sorted(list) or list == sorted(list, reverse=True)

print(list_order([1,2,3,4,5,6,7,8,9,10]))