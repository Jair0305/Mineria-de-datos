''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 33. Dadas dos listas llenas con strings y números (del mismo tamaño), escribe un programa que genere un diccionario donde las llaves son los objetos de la primera lista y los valores los objetos de la segunda.
'''

list1 = [1, 2, 3, 4, 5,6,7,8,9,10]
list2 = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']
d = {}

for i in range(len(list1)):
    d[list1[i]] = list2[i]
