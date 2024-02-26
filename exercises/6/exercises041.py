''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 41. Escribe un programa que genere una lista llena con números enteros aleatorios entre 100 y 1000, que sean divisibles entre 2 y 7.
'''

import random as rn


list = []
for i in range(1,1000):
    rndm = rn.randint(100,1000)
    if rndm%2 == 0 and rndm%7 == 0:
        list.append(rndm)
print(list)