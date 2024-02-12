''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 14. Dada una lista llena con strings (crea una lista por tu cuenta), escribe un programa que devuelva cuál es el string más largo de la lista.
'''

arr1 = ['hello','world','how','are','you', 'yooooooo','niqq']

word=''
wordIndex = 0
for i in range(len(arr1)):
    if len(arr1[i]) > len(word):
        word = arr1[i]
        wordIndex = i

print(f'la palabra del array mas larga es {arr1[wordIndex]} y su tamano es de {word}')