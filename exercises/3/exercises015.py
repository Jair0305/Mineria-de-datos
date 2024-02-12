''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 15. Escribe un programa que cuente cuantas veces aparece el string 'bob' en un string dado (defínelo tú).
'''

str = 'hola bob mundo bob como estas, este es un bob string de prueba para este bob programa bob'

print(str.find("bob"))
parts = str.split()
contadorBob = 0
for i in range(len(parts)):
    if(parts[i] == 'bob'):
        contadorBob += 1

contadorBob