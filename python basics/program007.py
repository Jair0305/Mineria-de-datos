"""
Created on Mon Feb 12 08:12:59 2024

# -*- coding: utf-8 -*-

@author: Naydelin Alondra Zavala Zúñiga
@semestre: 2024 EJ
@curso: Mineria de datos
@fecha: 2024-02-12

@description: Tuples and sets
"""

### Tuples
# Una tupla en python es una colección ordenada de objetos
# (el orden de insercion importa, se pueden acceder por su indice/posición)
# que no es mutable.
# Son como listas pero inmutables.


# Tuple definition, use () instead of [] from lists
# We can put any type of objects inside the tuple
e = () #Empty tuple
t = ('tuples', 'are', 'like', 'lists', 'but', 'inmutable', 1, 4.1, [1,2])
print(t[0]) # Indexing, accesing and item by its position/index
print(t[-1]) # Indexing, accesing the last item from t
print(t[:3]) # Slicing, returns items from indexx 0 to 3-1
# --> Returns a tuple

# Tuples are inmutables
t[0] = 'this is not possible'

### Concatenatiom
# Since tuples are inmutables, we cannot add items to the
# but we can concatenate tuples to a new tuple

t2 = t + ('more', 'items', 6, 7, 8)
# Concatenates tuple t with the second tuple
# It creates a new tuple

#Adding one item to a tuple
t3 = t2 + (9, )# with only one otem, thee ',' is necesary
# to indicate to python that it is a tuple
# with only one item,
# without, ',' python considers the item
# as a number between ()

# De manera similar como las tuplas son mutables no hay metodos para eliminar
# elementos dentro de la tupla.
# En vez de eso podemos utilizar el slicing, para cortar porciones de la tupla
# formar una nueva tupla sin los elementos  deseados.
t4 = t[:4] + t[5:]

# NOTA: Hay que determinar porque se quiere agregar o eliminar elementos de una
# tupla
# Si la inserción y borrados es constante, mejor usa una lista.

# La concatenación y el slicing creando una nueva tupla, es más costoso.

### Useful functions
#
print(t2.index(1)) # Returns the index of the first ocurrence of 1
t5 = t2 * 3 # Repetition of tuples

print(t5.count(1)) # Returns the number of times that 1 appears in t5

### Casting
a = [(1,2), (3,4), (5,6)] # List of tuples
b = ([1,2], [3,4], [5,6]) # Tuple if lists


c = tuple(a) # Liste to tuple
d = list(b) # Tuple to list

### Length
print(len(a), len(b), len(c))

### Tuples unpacking
t = ('a', 'b')
x,y = t # Tuple unpacking. Each object in the left takes an
# item from the tuple. We need to put as many
# objects in the lefts as items in the tuple.


### Iteration over tuples
for i in a: # Tuples are iterables objects
    print(i) # i iterates  over each item from a

# Tuples are faster than lists to access and index items.
# The are useful when a collection items is not going to
# change during the program execution.

# If yu to create a tuple from scratch (starting from)
# an emty collection). It's better to first createa list
# (prefereably using list comprehension) and afterwards
# cast it to a tuple.


#########################
### Sets
#########################
# Sets are unordered collections of objects that are mutables

a = set() # Empty set
a = {1,2,3,4,5.5,'a','b','c'} # Set definition using {}
b = {5,1,2,3,4,4,5,5,3,2} # A set is a collection
# of unique items,
# repeated items are el iminated
print(b[0]) # The collection is unordered
# Insertion order does not matter, there are
# no indexes for the items.
# so, we cannot acces the items by index

c = {3,4,5,6,7,8}
print(b.union(c)) # Returns a new set that is the union of b y c
print(b.intersection(c)) # Returns a new set that is the intersection of b y c
print(b.difference(c)) # Returns a new set  with items b that are not in c
print(c.difference(b)) # Returns a new set with items c that are not in b


# Sets are mutable
b.add('hola') # Add one item to b
b.update(['one', 'two', 'three']) #Update b with items from a list
b.update(['four', 'five']) # Update b with items from tuple
b.update(['six', 'seven', 9]) # Update b with items from a set

# Since sets are unordered, new items are not inserted (necesarily)
# at the  end

b.remove(3) # Removes an specific item from b
# Items in a set are unique.

print(len(a), len(b), len(c)) # Length of set

## Iterations over sets

for i in b: # Sets iterable objects
    # i iterables over each item of b
    # but the is not garatee about the order
    # in wich the items will be accessed
    print(i)

# if we need to access the items inside a collections in
# a specific order, er need to use an ordered collection:
# lists and tuples

## Casting
e = [1,2,3,'hola',3,4,5] # list
f = (1,2,3, 'hola',3,4,5) # tuple

g = set(e)#Tuple to set
h = set(f) #Tuple to set

l = list(b) # Set to list
t = tuple(b) # Set to tuple

# Sets are(much) faster than lists and tuples for searches and accesing.
# They are useful when a collecton containg
# only unique items.

# Accesing in a list 0(n)
# Accesing in a set 0(1)