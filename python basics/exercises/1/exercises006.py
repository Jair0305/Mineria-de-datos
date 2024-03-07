''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.29
@description: 6. Escribe un programa que imprima los números pares entre 1 y un número entero dado por el usuario.
'''

n = int(input(f'Escribe el numero a evaluar: '))

for i in range(1,n+1):
    if i %2 == 0:
        print(i)