''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/015
@description: 32. Escribe un programa que genere un diccionario en donde las llaves son las secuencias desde 1 hasta n (define n) y los valores son las llaves al cuadrado. (Para n = 5, el diccionario sería d = {1:1, 2:4, 3:9, 4:16, 5:25}
'''

dic = {}

for i in range(1,10):
    dic[i] = i**2