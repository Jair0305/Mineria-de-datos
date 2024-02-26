''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 49. Escribe una función que reciba un número entero positivo y que devuelva el producto de sus dígitos individuales.
'''

n = input('Escribe un numero')
res = 1
for i in range(len(n)):
    res *= int(n[i])

print(f'El resultado de la multiplicacion de tus digitos individuales es {res}')