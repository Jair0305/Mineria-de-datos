''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 50. Escribe una función que reciba un número entero positivo y que devuelva si ese número es primo o no (True/False).

'''

n = int(input('Ingrese un numero: '))

def esPrimo(n):
    if n <2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(esPrimo(n))