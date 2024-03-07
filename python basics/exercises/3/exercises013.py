''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 13. Dado un string (defínelo tú), escribe un programa que remueva el enésimo caracter de ese string (definir n tú mismo). Comprobar que el string tiene más de n caracteres.
'''

str1 = 'Hello World'
n = 2
str2 = ''
if (len(str1) > n):
    for i in range(len(str1)):
        if (i == n):
            continue
        str2 += str1[i]

print(str2)