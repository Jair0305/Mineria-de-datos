''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 42. Escribe un programa que solicite un entero n (n>100) al usuario, que genere una lista con la secuencia de 1 hasta n, y que seleccione 5 números de esa lista al azar.
'''
import random as rn
n = int(input('Enter  number between 1 and 100: '))
list = []
all = []
for i in range(1,n+1):
    all.append(i)

for i in range(5):
    rndm = rn.choice(all)
    list.append(rndm)

list