''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.29
@description: 1. Escribe un programa para generar el factorial de un número n entero dado por el usuario. n! = 1*2*3*…*n
'''

n = int(input("Escribe un número entero: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f'El factorial de {n} es: ' + str(factorial(n)))