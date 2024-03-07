''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 20. El ejercicio anterior, pero seleccionando solo aquellos strings que contengan 'jpg' o 'png' después del punto (solo esos tres caracteres).
'''

arr = ["Hola", ".Mundo", "Python", "Programación.jpg", "String.png", "Lista", "Ejemplo", "Desarrollo.", "Datos", "Cadena."]

l_arr = [i for i in arr if '.jpg' in i or '.png' in i]

