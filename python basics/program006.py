''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: list comprehension
'''

#Create a new list with items from an interable and apply an operation to each otems of the iterble(multiply by 2)

l_1 = [4,5,6,7,8,9]
l_2 = []

for i in l_1:
    r = i * 2
    l_2.append(r)

#With list comprehension

l_2 = [i*2 for i in l_1]
#Sintaxis:
# new_list = [item_to_insert for control_variable in iterable]

##When i need to create a new lsit i can use list comprehension
##List comprehension always creates a new list

#Create a list with even numbers in certain range

L_even = []

for i in range(1,20):
    if i%2 == 0:
        L_even.append(i)

#Using conditionals in a list comprehension

l_even = [i for i in range(1,20) if i%2 == 0]
#Appends in the list only those numbers from the iterable that are even

# Create a list with numbers that even and divisile by 5

l_numbers = [i for i in range(1,100) if i%2 == 0 and i%5 == 0]

#With list comprehension we can create a list with the result of applying a function to each item of an iterable

l_numbers = [i for i in range(1,51) if i%5 == 0 and i%2 == 0]

#Create a list strings 'Even' or 'Odd' depending on the number

l_numbers = ['Even' if i%2 == 0 else 'Odd' for i in range(1,20)]

# Important:
#1. List comprehension is an elegante way to define and create lists on axisting iterables
#2. List comprehension is generally more compact and FASTER than normal functions and loops for creating lists
#Specially useful with very loare lists
#3. However, we should wwiting very long list comprehension in one line, to ensure that the code is
#user firnedly and readable
#4. Every list comprehensions can be rewritte in a for loop, but not every for lopps can e writting as a list comprehension
