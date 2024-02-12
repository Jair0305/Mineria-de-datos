''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description 10. Dada una lista de listas con números enteros (creada por ti directamente en el código), escribe un programa que imprima la sublista cuya suma de elementos es la más alta.
'''

lista = [[5,2,6],[8,2,4],[9,1,2],[9,0,4]]
suma = 0
sumamaxima = 0
for i in lista:
    for j in i:
        suma = suma + j
        if suma > sumamaxima:
            sumamaxima = suma
            suma = 0
print(f'La suma maxima es {sumamaxima}')