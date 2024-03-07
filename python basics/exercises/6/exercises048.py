''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 48. Escribe una función que reciba un número entero n, y que devuelva una una lista de listas que represente una matriz de nxn llena de ceros.
'''

def listofLists(n):
    for i in range(n):
        print([0 for i in range(n)])


n = int(input("Escribe un número entero: "))
listofLists(n)