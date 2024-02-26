''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/15
@description: 34. Dados dos diccionarios con llaves string y valores string y números, escribe un programa que genere un tercer diccionario como la mezcla de los otros dos. Si hay llaves repetidas, que sume los valores que sean numéricos, sino, que sobreescriba el valor.
'''



dic1 = {'uno':1, 'dos':2, 'tres':3, 'cuatro':4, 'cinco':5}
dic2 = {'uno':6, 'dos':7, 'ocho':8, 'nueve':'nueve', 'cinco':'diez'}
dic3 = {}

for key, value1 in dic1.items():
    dic3.update({key:value1})
for key, value in dic2.items():
    dic3.update({key:value})
    if(key in dic1):
        if(type(dic1[key]) == int and type(value) == int):
            dic3[key] = dic1[key] + value
        else:
            dic3[key] = dic2[key]