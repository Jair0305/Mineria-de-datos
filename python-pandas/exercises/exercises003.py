''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description: Leer el archvio csv con pandas y para cada variable nominal, sex, pet, console y para la variable nominal y para la variable
numerica weight calcular las frecuencias de rangos de valores [0-50],[60-100],[100-150],[150-200] y su porcentaje

'''


import pandas as pd
import matplotlib.pyplot as plt
w_d = 'D:/Users/chama/Desktop/Mineria-de-datos/python-pandas/data/'

f_n = 'info_students.csv'

f_i = w_d + f_n
df = pd.read_csv(f_i)

freq = {}
var = df['weight']

for v in var:
    if v <= 50:
        freq['0-50'] = freq.get('0-50',0) + 1
    elif v <= 100:
        freq['51-100'] = freq.get('51-100',0) + 1
    elif v <= 150:
        freq['101-150'] = freq.get('101-150',0) + 1
    else:
        freq['151-200'] = freq.get('151-200',0) + 1

total = len(var)
l_p = [(freq[k]/total*100,freq[k],k) for k in freq.keys()]
l_p.sort(reverse = True)
for p,f,v in l_p:
    print(f'{v}:{f}:{p}%')

lab = []
val = []
for p,f,v in l_p:
    lab.append(v)
    val.append(f)
    plt.pie(val, labels = lab, autopct = '%1.1f%%')
    plt.title(f'{var.name} de los estudiantes')
    plt.figure()
    plt.bar(lab,val)
