import pandas as pd

w_d = 'C:/Users/chama/Desktop/mineria-de-datos/mineria-de-datos/python-pandas/data/'

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
