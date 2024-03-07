''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 54. Escribe una función que reciba dos listas de strings del mismo tamaño, y que devuelva un diccionario en donde las llaves son los string de la primera lista y los valores son los string de la segunda lista.
'''

def list_to_dict(list1, list2):
    return {list1[i]: list2[i] for i in range(len(list1))}

print(list_to_dict(['hola', 'mundo', 'cruel', 'y', 'despiadado'], ['hello', 'world', 'cruel', 'and', 'merciless']))

