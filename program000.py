""""
Commentary multilinea
Created on Thu Jan 25 08:14:26 2024

@autor: jair
@description: This is my first program in python.
Initialize some variables and print some results
"""

#Python es un lenguaje interpretado. Ejecuta na instruccion a la vez. Si hay un error en una linea, se detiene la ejecucion
#No hace un proceso de compilacion previo

#Lo que escribimos aqui es un script, un conjunto de instrucciones d elenguaje

print('hello World')

a = 5 #Inicializacion de una variable

#Python usa tipos dinamicos, no es necesario declarar el tipo de variable
#Python lo infiere a partir del valor asignado. El tipo de variable puede cambiar durante la ejecucion

a = 5.6 #Ahora a es un float

#Toda variable que inicialice, se queda en la memoria del kernel. Puedo acceder a ella desde el script o desde la terminal

b = 7
c = -8

#Python permite la asignacion multiple
d = e = f = g = 19.2

h = 7.5 * a

#Eliminar variables de la memoria
#Limpiar la temrinal

#Salida de la terminal
print(d) #Envia ua salida a la temrinal, inserta un salto d elinea al final

print(a*b)
print(e,h,f) #Envia varios elementos a la terminal separados por un espacio

###Basic arithmetic operators
# --> Takes to two numerical operands and return a numerical value(int, float, imarginary, ...
# int: not decimals (.)
# float: decimals (.)
a = b + c #Sum
a = b - c #Substraction
a = b * c #Multiplication
a = b / c #Division
a = b // c #Integer division
a = b ** c #Exponentiation
a = b % c #Modulus

### In-Site arithmetic operators
a += b #a = a + b
a -= b #a = a - b
a *= b #a = a * b
a /= b #a = a / b
a //= b #a = a // b
a **= b #a = a ** b
a %= b #a = a % b

###Comparation operators
# --> returns a boolean value (True, False)
a == b #Equal
a != b #Not equal
a > b #Greater than
a < b #Less than
a >= b #Greater than or equal to
a <= b #Less than or equal to

#Boolean values
i = True # Orange color (Spyder) = Language reserved word
j = False

#### Logical operators
# --> Take two boolean values and returns a boolean value: True or False
i and j #Logical AND
i or j #Logical OR
not i #Logical NOT
not j

# Los operadores logicos me sirven para unir varias operaciones de comparacion o el resultado deoperaicones logicas

(a == b) and (e > h)
# F        and      F        =           F
(a<b) and (e==h)
# V        and      F        =           F

### Basic string

s = 'Hello World' #Apostrofes
t = "Hello World" #Comillas dobles
#Lo que esta dentro de '' o "" es un string

# El size en el explorador de variables me indica el numero de caracteres que tiene el string
len(s) #Cantidad de caracteres del string --> int

print(s)
print(t)

#### Input
#Solicita una entrada al usuario en la terminal
#Recibe como parametro un string que se mostrara en kla temrinal
#Input simepre captura la entrada como un string, si quiero capturar un numero debo convertirlo
n = input('Enter a number: ')
print(n)

n = int(input('Enter a number: '))
#Casting
#Convierte un tipo de dato en otro

n = float(input('Enter a number: '))