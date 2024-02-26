''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 56. Escribe una función que reciba dos lista del mismo tamaño con números flotantes y que calcule el producto punto entre las listas.
'''

def dot_product(list1, list2):
    return sum(list1[i] * list2[i] for i in range(len(list1)))

print(dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0])) # 32.0