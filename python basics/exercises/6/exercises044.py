''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 44. Escribe un programa que solicite al usuario un número entero n (< 20) y que genere un string con n caracteres alfanuméricos: dígitos del 0 al 9 y letras minúsculas a-z (sin considerar la ñ).
'''

import random as rn

caracters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

n = int(input('Elige un numeor menor a 20: '))

for i in range(n):
    print(rn.choice(caracters),end='')
