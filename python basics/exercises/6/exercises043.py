''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 43. Escribe un programa juegue a los dados con el usuario, genere un número entero aleatorio entre 2 y 12 (la suma de los dos dados), y que pregunte al usuario si quiere jugar, si confirma (s), que se generen dos número aleatorios enteros entre 1 y 6, y que los imprima junto con la suma. Si la suma es mayor que el número inicial, enviar un mensaje de felicitaciones; si no, enviar un mensaje de consolación.
'''

import random as rn



def game():
    n = rn.randint(2,12)
    d1 = rn.randint(1,6)
    d2 = rn.randint(1,6)
    sum = d1+d2
    print(f'the computer has chosen {n}')
    print(f'You rolled was {d1} and {d2} that sum is {sum}')

    if(sum > n):
        print('Congratulations, {sum} is greater than {n} you win!')
    elif(sum == n):
        print('draw, try again')
    else:
        print('Sorry, you lose')

decision = input('Do you want to play? (y/n): ').lower().strip()
if decision == 'y':
    game()
else:
    print('Goodbye')