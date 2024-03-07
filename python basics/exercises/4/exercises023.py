''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description: 23. Dada una lista llena con strings, escribe un programa que genere otra lista llena de tuplas del tipo (index, string)
'''

arr = ["Hola", "Mundo", "Python", "Programación", "String", "Lista", "Ejemplo", "Desarrollo", "Datos", "Cadena"]

l_arr = [(i, arr[i]) for i in range(len(arr))]
