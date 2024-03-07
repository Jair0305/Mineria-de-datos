''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 16. Dado un string (defínelo tú), escribe un programa que genere otro string en donde todas las repeticiones del primer caracter son reemplazadas por el caracter $, excepto el primer caracter.
'''

str = 'Hola como estas, este es un programa hecho para hacer un string reemplazando la h por otra letra que no sea h'
str = str.lower()
str2 = ''
char = str[0]
for i in range(len(str)):

    if str[i] == char:
        str2 += '$'
    else:
        str2 += str[i]

print(f'Frase original: {str}\n\n frase final = {str2}')