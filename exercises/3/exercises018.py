''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 18. Dada una lista con strings, escribe un programa usando una comprensión de listas para generar una lista que contenga las longitudes de cada string de la lista original.
'''

arr = ["Hola", "Mundo", "Python", "Programación", "String", "Lista", "Ejemplo", "Desarrollo", "Datos", "Cadena"]
l_arr = [len(i) for i in arr]