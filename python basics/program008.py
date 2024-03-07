'''
Created on Mon Feb 15 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: list comprehension
'''


# A dictionary is an ordered collection of pairs key:value. They
# order matters
#They are optimized to retrieve information

# [key] ---> value

#Key must be of an inmutable type (not a list, set or dictionary)
#Keys are unique, there are not two identical keys

#Value could be of any type

# A dictionary is a similar to a JSON format
# A dictionary is similar to a list (or an array), but intead of and index to acces an item, we use a key

d = {}#Empty dictionary
d = {'uno':'valor1', 'dos':'valor2', 3:'valor3', (1,2):4.56}#dictionary with 4 items

print(d['uno'])#valor1
print(d[3])#valor3
print(d[(1,2)])#4.56
print(d[2])#Error, there is not a key 2

d_2 = {0:'uno', 1:'dos', 2:'tres', 3:'cuatro', 4:'cinco'}
l = ['uno', 'dos', 'tres', 'cuatro', 'cinco']

print(d_2[0], l[0])#with dict value between [] is a key, with list value between [] is an index

print(d[3]) # Notation []
print(d.get(3))# Notation get --> siminal to []

print(d[2])#Error
print(d.get(2))#None

print(d.get(2, 'hola'))#Return value associated with key,
# if key does not exist, return 'hola'

print(d.get(3, 'hola'))
## Changing values indise the dictionary

d['uno'] = 1378#Changes the value associated with key 'uno'
d[(1,2)] = 'hola'

##Addong pairs to a dictionary
d['five'] = 5000 #Inserts ath the end a new pair 'five':5000
d[78] = 'mundo'

d[[4,5]] = 'Python'#Error, key must be of an inmutable type

d.update({6:'seis', 7:'siete', 'eight':'hello'})#Inserts at the end the pairs 6:'seis' and 7:'siete'

#Length of a dictionary
print(len(d), len(d_2)) # Number of pairs

del d[78]#Deletes the pair with key 78
d.clear()#Deletes all the pairs

keys = d.keys()#Returns an iterable function iterable with the keys

values = d.values()#Returns an iterable function iterable with the values

#Iteation over dictionaries
for key in keys:
    print(key)

for value in values:
    print(value)

items = d.items()#Returns an iterable funciton with all the pairs in d, each pair is returned as a tuple

for item in items:
    print(item)#item as a tuple


#Dictionaries are ordered, thus, pairs are inserted at the end of dict in order. insertion is kep

#During an interation, the kays, values or pairs are returned insertion order

for k in d:
    print(k)

for i in d.items():#iterates over the pairs of d
    print(i[0], i[1])#i is a tuple

for k, v in d.items():#Unpacking the tuple  in k and v
    print(k,v)

d_n = {1:'Geeks', 2:'For', 3:{'A':'Welcome', 'B':'To', 'C':'Geeks'}}
d_l = {1:['one', 'two', 'three'], 2:['four', 'five', 'six'], 3:['seven', 'eight', 'nine']}

for k, v in d_n.items():
    print(k, v)

for k, v in d_l.items():
    for i in v:
        print(f'\t{i}')


#Type of objects

print(type(d))#<class 'dict'>
print(type(i))
print(type(item))
print(type(l))
print(type(value))

if type(d) == int:
    print('d is an int')
else:
    print('d is not an int')


## Operadores de pertenencia
#in, not in
#Comprueban si un valor está en un objeto iterable

'tres' in l #Comprueba si 'tres esta en l, retorna un valor booleano

3 in item

9 in item

'tres' not in l

3 not in item

9 not in item

