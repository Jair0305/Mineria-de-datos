''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 36. Dada una lista llena con strings, escribe un programa para crear un diccionario en donde la llave es un string y el valor es el número de veces que ese string aparece en la lista.
'''

arr = ["hola", "mundo", "este", "es", "un", "texto", "de", "prueba", "para", "este", "programa", "hola", "mundo", "este", "programa", "programa"]
dic = {}
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            print(arr[i])
            count += 1

    dic[arr[i]] = count