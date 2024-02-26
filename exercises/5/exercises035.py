''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 35. Dado un string (definido por ti), escribe un programa que genere un diccionario en donde la llave es la posición de cada caracter del string y el valor el caracter.
'''

str1 = 'hola mundo, este es un texto de prueba para este programa'
dic = {}
for i in range(len(str1)):
    dic[i] = str1[i]