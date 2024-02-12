''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/08
@description 17. Dada una lista llena con enteros y strings mezclados (crea una lista por tu cuenta), escribe un programa que separe en dos listas los strings de los enteros.
'''

arr = [1,2,5,'hola','como','45',43,12,64,34,'estas','hola',30,'mundo']
arrNum = []
arrStr = []
for i in arr:
    if str(i).isnumeric():
        arrNum.append(i)
    else:
        arrStr.append(i)

arrNum
arrStr