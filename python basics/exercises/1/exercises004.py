''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.29
@description: 4. Escribe un programa que solicite n calificaciones flotantes al usuario y encuentre las calificaciones menor y mayor
'''

n = int(input('Ingresa el numero de calificaciones: '))
calif = []
max = min = 0
for i in range(n):
    calif.append(float(input(f'ingresa la calificacion {i +1}: ')))

def max_min(calif):
    max= calif[0]
    min= calif[0]

    for i in range(1, len(calif)):
        if(calif[i]> max):
            max = calif[i]
        if(calif[i] < min):
            min = calif[i]
    return max, min

max, min = max_min(calif)
print(f'La calificacion menor es: {min} y la calfiicacion mayor es: {max}')

