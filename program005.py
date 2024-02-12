''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: Basic lists
'''

# Una cadena - secuencua (coleccion de datos ordenada) de caracteres
#Un caracter es un simbolo que esta dentro la tabla de calificacion
#Vamos a utilizar la tabla utf-8


#Ordenado --> esta indexad
#Inmutable --> no podemos cambiar su contenido

s = 'Hola Mundo'
print(s)
print(s[3]) # Char at index 3 (starint from 0)
print(s[:5]) # Slicing: from the beginning to index 4
print(s[5:]) # Slicing: from index 5 to the end
print(s[:6:2]) # Slicing: from the beginning to index 5, with a step of 2

#Slicing return a new String

s[3] = 'x' #Error, las cadenas son inmutables

s = ('Hello')
t = ('World')
u = s + ' ' + t #Concatenacion

print(u)

w = u *3 #Repetir la cadena 3 veces
print(w)

print(len(s), len(t), len(u), len(w)) #Length of the strings

##Iterates over the string

#A string is an iterable object

for i in u:# i iterates over the characters of the string u
    print(i, end = ' ')#it takes each char from u and print it

for i in u[2:5]:# i iterates over u from index 2 to 4
    print(i, end = ' ')

for i in u[::-1]:# i iterates over u in reverse order
    print(i, end = ' ')

### Some useful string methods
#Strings are inmutbale, so the methods always return another string
#The method does no modify the current string

s1 = '\t\n Hello World from Python World  \n\t'
#\t --> tab
#\n --> new line
#\r --> carriage return

s2 = 'Alphabetic'
s3 = '123456'

print(s1.lower())#Convert the string to lower case

s4 = s1.lower()#In case i need to work with a lowercase version of s1
#I beed to save the result of the method in a new variable

print(s1.upper())#Convert the string to upper case

print(s1.strip())#Remove the leading and trailing white spaces
#Whitespaces = spaces, tabs, new lines, carriage returns

print(s2.isalpha()) #Tests if all the chars in s2 are alphabetic
#chars -> return a boolean value

print(s1.isalpha()) #False, because of the leading and trailing white spaces

print(s3.isdigit()) #Tests if all the chars in s3 are digits

print(s1.isdigit()) #False, because of the leading and trailing white spaces

print(s1.isspace()) #Tests if all the chars in s1 are whitespaces

print(s1.find('World')) #Return the index of the first occurrence of 'World' in s1
#Search for the given string 'World' in s1 and return the first
#index where it begins or -1 if not found
#Searches are done by comparing string
#Lexicographically (following the values in the encoding table  utf-8)

print(s1.find('java'))

print(s1.replace('World', 'Python')) #Replace all the occurrences of 'World' with 'Python' in s1

s4 = s1.lower()
print(s4.replace('world', 'Everyone'))

### Stirng to list
### List to string

s1 = 'Hello world! How are you?'
s1.split() #Returns a list of strubstrings separated by the given delimiter, the delimiter
#is another strong
#Withour argument it splitss on all whtispace chars.
#string --> List

parts = s1.split('!')
parts

### List to string
words2 = ['hola','mundo','que','tal']

phrase = words2[0] + ' ' + words2[1] + ' ' + words2[2] + ' ' + words2[3]
print(phrase)

phrase = ''
for word in words2:
    phrase+= '' + word
    #Delimiter
phrase = ' '.join(words2)#Returns a string formed by the concatenation of all
#the strings in a list, separated by a delimiter ('')
#List --> string

phrase = '*->'.join(words2)

