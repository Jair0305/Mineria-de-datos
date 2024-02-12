''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.29
@description: Basic for loop
'''


#Sintaxis del for

#variable de control
#variable --> contador
#Tipos de variable por su uso:
#contador: contar cosas
#acumulador: almacenas cosas acumuladas algo que guarda el resultado de un conjunto de operaciones
#bandera: variable que indica el estado de algo

#En C
# variale de control
#variale --> contador
# for(int i = 0; i < 10; i++){

# }

#Sitnaxis de for es mas sencilla en python
#for [varibale de control] in [iterable]:
# for i in range(10):

#Imprimir la secuenia de enteros entre 0 y 100

for i in range(101):
    print(i)

#En python para controlar el ciclo for se utiliza un iterable que puede ser un objeto
#o puede ser una funcion

#Iterable: objeto (variable) o una funcion

#En el ejemplo de arriba en cada iteracion (ciclo, repeticion)
#dle bloque for, i (variable de control_ toma un valor que es generado por el iterable (fucnion range)

#la funcion range es una funcion iterable que genera un valor en cada ciclo de manera secuencial

#range(10) --> 0,1,2,3,4,5,6,7,8,9

#La funcion range no genera toda la secuencia de valroes al mismo tiempo
#Para poder utilizar la funcion iterable, necesito algo que itere sobre ella

#La funcion range genra los valroes dentro de un rango definido
# (val_ini, val_end-1, step
# Si el valor inicial se omite, inicia en 0
#Si el paso(step) se omite, elvlor por default es 1
#Se genera los valores entre val_ini y val_end-1 en pasos de step

#Imprimir valores entre 1 y  10

for i in range (1,11):
    print(i)

#Imprimir valores entre 1 y 10 con incrementos de 2

for i in range(1,11,2):
    print(i)

###Use of break

for i in range(10): #itera valores entre 0 y 9
    print(i)
print('End!')

for i in range(10):
    if i == 3:
        break
    print(i)
print("End!")

### Use of continue

for i in range(10):
    if i == 3 or i ==5:
        continue
    print(i)
print('End!')

### Use of else in for

for i in range(10):
    if i ==3:
        break
    print(i)
else:
    print('No numbers lef!')
#El bloque else e el for se ejecuta solo cuand ciclo temrina coompletamente, es decir, cuando no se ejecuta un break

for i in range(10):
    if i ==3:
        continue
    print(i)
else:
    print('No numbers lef!')

### Use of nested for
for i in range(1,11):
    for j in range(1,11):
        k = i * j
        print(i, '*', j, '=', k)

