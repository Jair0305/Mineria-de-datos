# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 08:12:01 2024

@author: Zavala Zuñiga Naydelin Alondra
@semestre: 2024-EJ
@curso: Mineria de datos
@fecha: 2024-02-29
@descripcion:Files and general usage of pandas
"""

'''
Para trabajar con archivos, es recomendable tener
# dos variables, una que controle el directorio
# de entrada de los datos y otra que controla
# el nombre del archivo de entrada.
'''

w_d = 'C:/Users/chama/Desktop/mineria-de-datos/mineria-de-datos/python-pandas/data/'
# archivo (nombre.extension)
f_n = 'info_students.csv'
f_i = w_d + f_n # ruta completa de archivos (string)

# General usage of files
with open(f_i, 'r', encoding='utf-8') as f_r: # File manager
    text = f_r.read()# Reads the whole file to a single string

# f_r is a file manager, that is also in iterable
text = []
with open(f_i, 'r', encoding='utf-8') as f_r:
    for line in f_r: # line iterates over each line of f_r
        text.append(line) # line is a string
        print(line)

# each  line in a text file contains a \n (\r\n) at the end (except
# maybe the last one)
# Sometimes it is usefull to remove such \n --> use .strip() from strings
text = []
with open(f_i, 'r', encoding='utf-8') as f_r:
    for line in f_r: # line iterates over each line of f_r
        text.append(line.strip()) # line is a string
        print(line.strip())
    # -------------------------------------------------------------------
    # splitting by:
    text = []
    with open(f_i, 'r', encoding='utf-8') as f_r:
        for line in f_r: # line iterates over each line of f_r
            text.append(line.strip()) # line is a string
            print(line.strip().split(',')) # Line is a str,