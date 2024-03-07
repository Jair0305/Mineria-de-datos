''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description: Basic lists
'''

# Las listas son colecciones ordenadas (orderes) de objetos (Variables).
# --> El orden de insercion si importa. el orden de la listase mantiene a lo largo de la ejecucion, los objetos
#estan indexado: cada objetoi en la coleccion tiene un indice asociado, el primer elemento tiene indice 0, el segundo 1, y asi sucesivamente
# -- > Podemos acceder a los objetos por su indice

#Las listas son como arreglos, pero mas flexibles

#Los objetos en las listas pueden ser de diferentes tipos

#Las listas son mutables, es decir, podemos cambiar su contenido que estan ubicados en un indice especifico

a = [1,2,3,4,5,6,7,8,9,10] #Lista de objetos int
b = [1, 2.2, 'hola', True, [4,5,6]] #Lista de objetos de diferentes tipos

c = [] #Lista vacia

###Acceder a los elementos de una lista por indicie

#Positive index (from 0 to the length of the list - 1) From left to right
#List are indexed with base 0 (index 0 is the first element)

print(b[4]) #1
print(b[2]) #hola

#### Accessing several items at the same time
#Slicing, cut the list in pieces
#Slicing return a list that is sub list of the original list
print(a[2:6])#Slicing: return a list with the elements from index 2 to 5
print(a[:3]) #Slicing: return a list with the elements from index 0 to 2
print(a[3:]) #Slicing: return a list with the elements from index 3 to the end
print(a[:]) #Slicing: return a list with all the elements
print(a[2:8:2]) #Slicing: return a list with the elements from index 2 to 7, with a step of 2

#Negative index (from -1 to -length of the list) from right to left
print(a[-1]) #10
print(a[-3]) #8
print(a[-3:]) #Slicing: return a list with the elements from index -3 to the end
print(a[:-3]) #Slicing: return a list with the elements from index 0 to -4
print(a[::-1]) #Slicing: return a list with the elements in reverse order
print(a[-5::-1]) #Slicing: return a list with the elements from index -5 to the beginning in reverse order

print(b[-1]) #Access the last item of b
print(b[-1][-1]) #Accesses the last item of the last item of the list b

print(b[-1][::-1])

###MUtate the list

b[1] = 'Hundred' #Change the value of the second element of the list b
print(b)
b[-1] = 4.5 #Change the value of the last element of the list b
print(b)

###Add elements to the list
#Items are appened at the end of the list
b.append('Two hunddred')#Add an item at the end of b
print(b)
c.append('Hello')
c.append(123)

#append allows to add only one item to a list

c.append(['a','b', 12.5])
print(c)

#adding the items idependently
c.extend(['a','b', 12.5])
print(c)
#Extend c with another list
#each item of the list is added to the end of the list

###Useful fucntions/methods

b.insert(3,2000) #Insert 2000 at index 3
#The items at the right of the index are shifted to the right

print(len(a), len(b), len(c)) #Return the length of the list

d = [len(a), len(b), len(c)] #Create a list with the length of the lists a, b, and c

last = b.pop() #Remove the last item of the list b and return it
print(last)
print(b)

fifth = b.pop(4) #Remove the item at index 4 of the list b and return it
print(fifth)
third = b.pop(2) #Remove the item at index 2 of the list b and return it

d = int(str(len(a)) + str(len(b)) + str(len(c))) #Sum of the length of the lists a, b, and c

c.append('python')
c.remove('python') #Remove the first occurrence of 'python' in the list c

c.append('world')
c.index('world') #Return the index of the first occurrence of 'world' in the list c

len(c[2]) #Return the length of the third item of the list c

d = a + c #Concatenates lists a and c and creates a new List

##Repetition
e = c * 3 #Creates a new list with three copies of the list c

###Membership operators --> Returns a boolean value
print('world' in c) #True
print('world' not in c) #False

print('java' in c) #False
print('java' not in c) #True

###Other useful methods
print(e.count('world')) #Return the number of occurrences of 'world' in the list e

f = c*3 and c.copy() #Create a new list with the same elements of

f = [12,20,15,8,1,3,250]
f.sort() #Sort the list in ascending order
print(f)

g = [12,4,5,[c*2]]

f.sort(reverse=True) #Sort the list in descending order
print(f)

## To apply the sort fucntions, all the items inside the list must be comparable

g = ['hola', 'adios', 'mundo', 'python', 'Ala', 'ala']
g.sort() #Sort the list in ascending order

g.append('45')
g.sort()
g.append(45)
g.sort() #Error, the items are not comparable

g.clear() #Remove all the items of the list g

#### List iteration

for i in c: #Lists are iterable objects. i conrol variable iterates over the items of the list
    print(i)
for i in c[10:]:
    print(i)
for i in c[::-1]:
    print(i)

#Iteratig by index
n = len(c)
for i in range(n):
    print(c[i])

###Lists of lists
lista = [[1,2,3], [4,5,6], [7,8,9]]
print(lista[1][1]) #5

for i in lista: #Iterating over the lists of the list
    for j in i: #Iterating over the items of the lists
        print(j)