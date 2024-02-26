''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description 31. Escribe un programa que tome dos diccionarios (definidos por ti) y que genere un tercero como la mezcla de los otros dos. Si hay llaves repetidas, toma los valores del segundo diccionario.
'''

dic1 = {1:2, 3:4, 5:6, 7:8, 9:10}
dic2 = {7:11, 9:12, 13:14, 15:16, 17:18}
dic3 = {}
for key, value in dic1.items():
    dic3.update({key:value})
for key, value in dic2.items():
    dic3.update({key:value})
    if(key in dic1):
        dic3[key] = dic2[key]