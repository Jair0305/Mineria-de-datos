''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 46. Escribe una función que reciba un número entero positivo n, y devuelva el factorial de ese número.
'''

n = int(input("Escribe un número entero: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f'El factorial de {n} es: ' + str(factorial(n)))