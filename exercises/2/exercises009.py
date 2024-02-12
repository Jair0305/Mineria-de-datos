''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description 9. Dado un número entero positivo n por el usuario, escribe un programa que genere una lista que contenga n listas internas y que cada lista interna contenga n ceros.
'''

n = int(input('Introduce un numero: '))
lists = []
list = []

for i in range(n):
    lists.append(0)
for i in range(n):
    list.append(lists)
