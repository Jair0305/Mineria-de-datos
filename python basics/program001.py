""""
Created on Tue Nov  3 14:00:00 2020

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.25
@description: Basic conditionals
"""

#{}
#Python no utiliza {} para definir bloques de codigo, utiliza la identacion (tabulacion)
# para indicar un conjunto de instrucciones pertenece a un bloque de control
# if, elif, else, for, while, def, class, try, except, finally, with, ...

num = 10
# condition
if num > 0:
    print('Positive number')
    print("End")

    #Que las instrucciones esten tabuladas a la derecha, indica que pertenecen al bloque de control definido arriba (if)
else:
    print('Negative number')
    print("Second instruction")
    #Estas instrucciones pertenecen al subloque else
print('Finish') #Esta instruccion no pertenece al bloque de control if, por lo tanto se ejecuta siempre porque no esta tabulada


#### Nested ifs

n = float(input('Enter a number: '))
if n >= 0:
    if n == 0:
        print('Zero')
    else:
        print('Positive number')
else:
    print('Negative number')

#### Use of elif

# n = float(input('Enter a number: '))
# if n > 0: #Primera condicion a evaluar
#     print('Positive number')
# else:
#     if n == 0:
#         print('Zero')
#     else:
#         print('negative numbre')

#Con elif

if(n> 0):
    print('positive number')
elif (n == 0):
    print('zero')
elif(n%5 == 0):
    print('algo')
else:
    print('Negative number')