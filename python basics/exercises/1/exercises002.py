''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/01.29
@description: 2. Escribe un programa para leer las edades de un grupo de n alumnos y obtener la edad promedio.
'''


n = int(input("Ingrese el numero de alumnos: "))
suma = 0
for i in range(n):
    edad = int(input(f"Ingrese la edad del alumno{i+1}: "))
    suma += edad
promedio = suma / n
print("El promedio de edad de los alumnos es: ", promedio)