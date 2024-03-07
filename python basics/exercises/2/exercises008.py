''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description 8. Dada una lista llena con números flotantes (creada por ti directamente en el código), escribe un programa que calcule la suma y el promedio de todos los elementos.
'''

list = [5.4,8.9, 7.23, 49.23, 70.5, 34.5, 1.23]
sum = 0
for i in list:
    sum += i

promedio = sum/len(list)

print(f'El promedio es {promedio}')