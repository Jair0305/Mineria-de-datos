''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description 7. Dada una lista de números flotantes (creada por ti directamente en el código), escribe un programa que devuelva los valores mínimo y máximo en la lista.
'''

list = [5.4,8.9, 7.23, 49.23, 70.5, 34.5, 1.23]

min = max = list[0]

for i in list:
    if i < min:
        min = i
    if i > max:
        max = i

print(f'El valor maximo es: {max}')
print(f'El valor minimo es: {min}')