''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 53. Escribe una función que reciba una lista de números enteros y que devuelva el promedio, el mínimo y el máximo de la lista.
'''

def list_numbers(list):
    return (sum(list)/len(list), min(list), max(list))

print(list_numbers([1,2,3,4,5,6,7,8,9,10]))