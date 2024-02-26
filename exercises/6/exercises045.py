''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 45. Lo mismo que el anterior, pero el string también puede contener letras en mayúsculas (sin considerar la Ñ).
'''
import random as rn

caracters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             '1','2','3','4','5','6','7','8','9','0']

n = int(input('Elige un numeor menor a 20: '))

for i in range(n):
    print(rn.choice(caracters),end='')