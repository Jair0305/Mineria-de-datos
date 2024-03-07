'''
Created on Mon Feb 15 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/19
@description: Built-in functions
'''

#Funcitons/methods that do not requiere module/package to work
#We do not impot anything
#Built-in funciton are highlighted with a different color(red)

x = -16
print(x)#output: -16
print(abs(x))#output: 16

a = [1,6070,34,14,183]
b = ['a','b','c','d','e','zapato','h']
c = [1.4,2.5,3.6]

print(max(a))#Returns the largest item in a collection (list, tuple, set, dictionary
#Objects in the collection mut be of the same type

print(max(b))#Los string se compararan por el orden lexicografico, la posicicon dentro de la tabla de codificacion
#Se compara caracter por caracter, si hya dos caracteres iguales en la misma poscion, se compara el siguiente caracter

print(max(c))

print(min(a))#Returns the smallest item in a collection (list, tuple, set, dictionary
print(min(b))
print(min(c))

print(sum(a))#Returns the sum of all items in a collection (list, tuple, set, dictionary)
print(sum(c))
print(sum(b))#Error, los elementos de la coleccion deben ser numericos

t = (10,7,3,1,20,45)

d = sorted(t)#Returns a new sorted list from the items in iterable
print(d)

d = sorted(t,reverse=True)#Returns a new sorted list from the items in iterable
#Lista.sort() --> modifica la lista in place
#sorted(lista) --> retorna una nueva lista ordenada

### Enumerate items from a collection
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i in seasons: #Iterate over seasons
    print(i)#i takes each item from season

for i in range(len(seasons)):
    print(i,seasons[i])

for i, s in enumerate(seasons): # s takes each item from seasons
    print(i,s)# i takes the count each item s in seasons

#enumerate is an iterable fucntion that for each iteration returns a tuple with count and the value of each item
#of the iterable object, it generates one tuple at a time for each iteration
#The tuple is unpacked in i, s

for t in enumerate(seasons):
    print(t)

###Packing items from collecitons
if len(a) < len(b):
    lm = len(a)
else:
    lm = len(b)

for i in range(lm):
    print(i, a[i], b[i])

for i, j in zip(a,b):#i and j iterate over items of lists a and b
    print(i,j)#at the same time
    #i takes items from a
    #j takes items from b
for t in zip(a,b):
    print(t)
#zip is iterable funciton that for each iteration return a tuple with items from the iterablle objects
#I t generates a tuple at a time for each iteration

#Zip stops at the shortest iterable object
#zip allows to create n-tuples for n iterables

for i,j,k in zip(a,b,c):
    print(i,j,k)

for i,j,k,l in zip(a,b,c,d):
    print(i,j,k,l)

for t in zip(a,b,c,d):
    print(t)

#Cuando necesite iterar sobre varias colecicones al mismo tiempo para acceder a sus valores/objetos, puedo usar zip
