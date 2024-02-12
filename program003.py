''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.29
@description: Basic while
'''

#Sintaxis del while
# while [condicion]:

#Sumar los valores entre 1 y 9
n = 10
i = 0 #Contador
suma = 0 #Acumulador

while i < 10:
    i+=1#Sumar 1 al contador
    suma += i#Acumular el valor de i en la variable suma
print(f'la suma es {suma}')
#Stirng con formato, me permite darle formato al sitring en la salida a terminal para indicar que es un string con formato
#f antes del string

#El ciclo while ejecuta el bloque de control mientas la condicien sea verdadera

###Use of break
n = 10
i = 0
suma = 0
while i < n:
    i += 1
    if i == 5:
        break#Termina el ciclo while
    suma += i
print(f'la suma es {suma}')

###Use of continue

n = 10
i = 0
suma = 0
while i < n:
    i += 1
    if i == 5 or i == 3:
        continue#Termina la iteracion actual y continua con la siguiente
    suma += i
print(f'la suma es {suma}')

### Us of else

n = 10
i = 0
suma = 0
while i < n:
    i += 1
    if i == 4:
        break#Termina la iteracion actual y continua con la siguiente
    suma += i
else:
    print(f'la suma es {suma}')
#El bloque else en el while se ejecuta solo cuando el ciclo se temrina completamente, es decir, cuando no se ejecuta un break