'''
Created on Mon Feb 15 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/19
@description: Random numbers
'''

# For using random numbers, wee need to import the random module
import random as rn #rn is the name that will use in my code

rn.random() #Returns the next random floating point number in the range [0.0, 1.0).

rn.uniform(2.5,7.8)#Returns a random floating point number between the two specified numbers with a uniform distribution.

# Random genera secuencia de numeros aleatorios a partir de una semilla (seed), si no se define la semilla, se toma esta directamente del sistema
#(Hora del sistema)
#Si la semilla se queda fija, la secuencia de numeros generados sera siempre la misma

rn.seed(2.5) #Initilize internal state (seed) of the random number generator

print(rn.random())
print(rn.random())
print(rn.random())
print(rn.random())

rn.randint(100,200)#Returns a random integer n such that a<=n<=b.
                        #a = 100, b = 200

x = ['a','b','c','d','e','f','g','a','b','c']
rn.choice(x)#Returns a random element from the non-empty sequence x.
rn.choices(x,k=3)#Returns 3 items at random from x(iterable with remplacement (could choice two times the same item)
rn.sample(x,3)#Returns 3 items at random from x (iterable) without replacement (could not choice two times the same item)
                    #--> Returns a list
                    #Selects the items by index
rn.shuffle(x)#Shuffle the sequence x in place
s = ('esto es una prueba')
rn.choice(s)#Returns a random element from the non-empty sequence s.
rn.choices(s,k=3)#Returns 3 items at random from s(iterable with remplacement (could choice two times the same item)
rn.sample(s,3)


