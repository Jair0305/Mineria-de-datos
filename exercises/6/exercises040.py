''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 40. Lo mismo que el anterior, pero el caracter impreso debe ser una vocal del string.
'''
import random as rn
vocales = ['a','e','i','o','u']

str = input("ingrese una palabra: ")
rndm = rn.choice(str)
while rndm not in vocales:
    rndm = rn.choice(str)

print(rndm)