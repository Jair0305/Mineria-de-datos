''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: 25. Dadas dos tuplas del mismo tamaño llenas con números flotantes, escribe un programa que genere una nueva tupla que contenga la suma por elementos de las dos tuplas.
'''

tp1 = (1.0, 2.0, 3.0, 4.0)
tp2 = (15.6, 28.50, 39.57, 0.97)

sumas = []

for i in range(len(tp1)):
    sumas.append(tp1[i] + tp2[i])

tp3 = tuple(sumas)

print(tp3)