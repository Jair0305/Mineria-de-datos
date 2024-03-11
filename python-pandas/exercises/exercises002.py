''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description: Leer el archvio csv con pandas y para cada variable nominal, sex, pet, console y para la variable numerica, semestre, calcular las frecuencias de cada valor y su porcentaje
EN el caso de la mascota(pet), separar los valores por la / y considerar cada valor de manera independiente

['cat','dog','cat/other] --> [cat,dog,cat,other]

Imprimir los valroes en orden descendente por porcentaje

Haccer una grafica de pay y una grafica de barrar para las frecuencias

Hacer una funcion que tome el dataframe y el nombre de la variable como aprametros e imprima los datos y genere las graficas


'''
import pandas as pd
import matplotlib.pyplot as plt
w_d = 'D:/Users/chama/Desktop/Mineria-de-datos/python-pandas/data/'

f_n = 'info_students.csv'

f_i = w_d + f_n
df = pd.read_csv(f_i)

def summary_fre(df, var):
    d = {}
    var = df[var]
    isnom = var.dtype == 'object'
    for v in var:
        if isnom:
            if '/' in v:
                pets = v.split('/')
                for p in pets:
                    d[p] = d.get(p,0) + 1
            else:
                d[v] = d.get(v,0) + 1
        else:
            d[v] = d.get(v,0) + 1
    total = len(var)
    l_p = [(d[k]/total*100,d[k],k) for k in d.keys()]
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
    plt.title(f'{var.name} de los estudiantes')
    plt.show()
    return

#Version de carranza

def summary_fre(df, var):
    data = df[var].tolist()
    d = {}

    for i in data:
        if(type(i) == str):
            tokens = i.split('/')
        else:
            tokens = [i]
        for j in tokens:
            d[j] = d.get(j,0) + 1
    total = len(data)
    l_p = [(d[k]/total*100,d[k],k) for k in d.keys()]
    l_p.sort(reverse = True)

    for p,f,v in l_p:
        print(f'{v}:{f}:{p}%')

    lab = []
    val = []
    for p,f,v in l_p:
        lab.append(v)
        val.append(f)
    plt.pie(val, labels = lab, autopct = '%1.1f%%')
    plt.title(f'{var} de los estudiantes')
    plt.figure()
    plt.bar(lab,val)
    plt.title(f'{var} de los estudiantes')
    plt.show()
    return


summary_fre(df,'pet')