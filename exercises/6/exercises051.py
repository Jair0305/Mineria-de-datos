''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 51. Escribe una función que reciba un string, que lo separe por espacios y devuelva un diccionario en donde la llave es cada substring y el valor es el número de veces que ese substring aparece en el string principal.
'''

def string(str):
    dic = {}
    for i in range(len(str)):
        repeat = repetition(str[i], str)
        dic[str[i]] = repeat
    return dic

def repetition(char, str):
    count = 0
    for i in range(len(str)):
        if str[i] == char:
            count += 1

    return count
    print(f'El caracter {char} se repite {count} veces en la cadena')

string('yoyoyoyoyo qpq')
