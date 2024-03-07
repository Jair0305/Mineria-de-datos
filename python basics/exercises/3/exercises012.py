''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 12. Dado un string (defínelo tú), escribe un programa que genere otro string compuesto por las dos primeras y las dos últimas letras del string original. Si la longitud del string original es menor que 2, que devuelva la leyenda "Empty string".
'''

string1 = 'H'

def substring(str1):
    if len(str1) < 2:
        str2 = 'Empty string'
    else:
        str2 = str1[:2] + str1[-2:]
    return str2

string2 = substring(string1)