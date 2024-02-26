''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 39. Escribe un programa que solicite un string al usuario y que imprima un caracter del string al azar.
'''

import random as rn


str = input("Ingrese una palabra: ")
print(rn.choice(str))