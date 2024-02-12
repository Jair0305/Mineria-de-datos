''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.29
@description: 5. Escribe un programa que solicite n números enteros al usuario y diga cuántos son pares, cuántos impares, cuántos negativos, cuantos positivos y cuántos ceros
'''

count_pares=0
count_impares=0
count_positivos=0
count_negativos=0

n = int(input('Ingresa el numero de numeros: '))
numeros = []
for i in range(n):
    numeros.append(int(input(f'ingresa el numero {i +1}')))
    if(numeros[i] % 2 == 0):
        count_pares += 1
    else:
        count_impares += 1
    if(numeros[i] > 0):
        count_positivos +=1
    else:
        count_negativos+=1

print(f'de los {n} numeros dados, El numero de nueros pares es de: {count_pares}, el numero de numeros impares es de: {count_impares}, el numero de numeros positivos es de: {count_positivos} y el numero de numeros negativos es de {count_negativos}')
