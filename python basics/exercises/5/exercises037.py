''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 37. Tomando el diccionario generado en el ejercicio anterior, escribe un programa que devuelva los 5 strings que más se repiten en la lista original.
'''

arr = ["hola", "mundo", "este", "de", "de", "de", "de", "es", "hello", "world", "hola", "mundo", "es", "un", "texto", "de", "prueba", "para", "este", "programa", "hola", "mundo", "este", "programa", "programa"]
dic = {}
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    dic[arr[i]] = count

sorted_tuples = sorted(dic.items(), key=lambda item: item[1], reverse=True)
top_5_tuples = sorted_tuples[:5]
top_5_dic = dict(top_5_tuples)