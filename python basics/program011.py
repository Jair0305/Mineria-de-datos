'''
Created on Mon Feb 15 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/19
@description: Basic use of user-defined functions
'''

#Functipn definition

#def <function_name>(<parameters>):

def greet(name):
    print('Hello',name)
    return #Indica el fin de la funcion, retorna algo al lugar donde se llamo, en este caso no devolvemos nada, si no lo ponemos, python podria marcar error


greet("hector")
s = 'Juan'
greet(s)#Paso una variable --> se usa su valor

#Toda variable tiene
#Un nombre
#Un valor
#Un tipo de dato

#Taking more than one parameter

def greet_absolute(num, name):
    print(f'Hello {name} Good morning')
    num = abs(num)
    return num#Return value

n = greet_absolute(-5, 'Hector')
print(n)

def greet_absolute_case(num, name):
    print(f'Hello {name} Good morning')
    if num >= 0:
        return num, name.upper()#Return value
    else:
        return abs(num), name.lower()
    #This function`returns two values (separated by ,
    #The value are returned as a tuple

res = greet_absolute_case(-5, 'Hector')
print(res)
#res toma el resultado de la llamada a la funcion
#res is a tuple

n,m = greet_absolute_case(-5, 'Hector')
#Desempaca la tupla devuelta por la funcion
print(n,m)

def greet_default(name, msg = 'Good morning'):
    print(f'Hello {name} {msg}')
    return
greet_default('Hector', 'yooooooo')
greet_default('Hector')

def suma(lista):
    res = sum(lista)
    return res

res = suma([7,8,9,10])
print(res)

try:
    res = suma([7,8,9,suma([10,2,3,4])])
    print(res)
except:
    print('Error en la suma')

