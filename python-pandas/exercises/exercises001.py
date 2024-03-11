import pandas as pd

w_d = 'D:/Users/chama/Desktop/Mineria-de-datos/python-pandas/data/'

f_n = 'info_students.csv'

f_i = w_d + f_n
df = pd.read_csv(f_i)

df['sex'] = df['sex'].str.lower()
sexs = df['sex'].tolist()
# counth = 0
# countm = 0
# for i in range(len(sex)):
#     if sex[i] == 'h':
#         counth += 1
#     if sex[i] == 'm':
#         countm += 1
#
# porcenth = (counth/len(sex)) * 100
#
# porcentm = (countm/len(sex)) * 100
#
# if porcenth > porcentm:
#     print(f'{porcenth}% de los estudiantes son hombres\n{porcentm}% de los estudiantes son mujeres')
# else:
#     print(f'{porcentm}% de los estudiantes son mujeres\n{porcenth}% de los estudiantes son hombres')

#Generalizandod = {}
d = {}
for sex in sexs:
    # if sex not in d:
    #     d[sex] = 1
    # else:
    #     d[sex]+=1
    d[sex] = d.get(sex,0) + 1

print(d)
total = len(sexs)
l_p = [(d[k]/total*100,d[k],k) for k in d.keys()]
# for i in d.keys():
#     porc = d[i]/total * 100
#     l_p.append((porc,d[i], i))

l_p.sort(reverse = True)

for p,f,v in l_p:
    print(f'{v}:{f}:{p}%',end = ' ')

import matplotlib.pyplot as plt #Modulo apra crear graficas sencillas

lab = []
val = []
for p,f,v in l_p:
    lab.append(v)
    val.append(f)

plt.pie(val, labels = lab, autopct = '%1.1f%%')
plt.title('Sexo de los estudiantes')

plt.figure()#Crea un nuevo papel para dibujar otra grafica, evita que 2 graficas se encimen

plt.bar(lab,val)
plt.title('Sexo de los estudiantes')

#Hay 2 partes cuando se trabaja con el analisis de datosÑ
#1. Los calculos tal cual para encontrar patrones, asociaciones, reglas, estadisticas, etc.
#2.Una interpretacion, resumen y rpeorte de los resultados se envia esto a las personas encargadas de tomar decisiones o a
#una aplicacion externa

#En la parte de la interpretacion, podemos incluir especulaciones e hipotesis, para tratar de explicar los datos.
#Sin embargo, hay que tener cuidado cuando se hagan estas expeculaciones e hipotesis.
#Primero se deberia intentar probar que las hipotesis sean correctas dentro del marco estadistico

#Ahora esto no siemrpe es factible

#Resumen de mis daots:
#-Hay 47% de mujeres y 53% de hombres
#   -Son cantidades similares, hay 6% mas de hombresque de mujeres
#-por que?
#Hipotesis/especulaciones:
#   -Las ingenierias tienenmas hombres que mujeres, pero otras carreras tienen mas mujeres que hombres, nivelan la poblacion
#   -El diseno de la recopilacion de datos, pedia explicitamente un equilibrio entre hombre y mujeres.
#   -Se capturaron mal los datos, hubieorn perosnas que no capturaron informaiconde las mujeres
#La uncia hipoteis sostenible es la segunda
#