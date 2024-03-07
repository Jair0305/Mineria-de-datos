''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description 11. Dada una lista de strings (creada por ti directamente en el código) y un número n dado por el usuario, escribe un programa que divida la lista original en listas con n elementos. Solo la última lista puede contener menos de n elementos. Que el programa genere una nueva lista llena con estas sublistas.
'''


listString = ['Ala', 'Burro', 'Carro', 'Dado', 'Ella', 'Francisco', 'Gato', 'Hugo', 'yoooo','yoooo','yoooo','yoooo','yoooo','yoooo','yoooo','yoooo','yoooo','yoooo','yoooo','yoooo']
finalList = []
subLists = []
n = int(input('Introduce un numero: '))
for i in range(0, len(listString), n):
    subLists.append(listString[i:i+n])

i = 0
while i < len(subLists):
    finalList.append(subLists[i])
    i+=1


print(finalList)