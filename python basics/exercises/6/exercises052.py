''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 52. Escribe una función que reciba una lista llena con strings, y devuelva una lista de tuplas, cada tupla con 2 elementos, el primero la posición de cada string de la lista original y el segundo el string.
'''

def list_to_tuple(list):
    return [(i, list[i]) for i in range(len(list))]

print(list_to_tuple(['hola', 'mundo', 'cruel', 'y', 'despiadado']))
