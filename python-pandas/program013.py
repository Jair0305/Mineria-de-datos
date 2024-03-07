''''
Created on Mon Jan 29 08:00:00 2024

@Autor: jair
@Semester: 2024 EJ
@curso: Mineria de datos
@fecha: 2024/02/01
@description: General usage of Pandas
'''

#Pandas is package with useful functiond/modules to work with structures data (such csv files)
import pandas as pd

w_d = 'C:/Users/chama/Desktop/mineria-de-datos/mineria-de-datos/python-pandas/data/'

f_n = 'info_students.csv'

f_i = w_d + f_n
df = pd.read_csv(f_i)
#Specific fucniton for reading csv files #.read_csv()reads the whole csv file and creates a DataFrame object
#that stored in df, A dataFrame is a particular object from Pandas to store an mange structured data --> table

print(df.columns)#Shows the columns of the Dataframe

print(df['age'])#Accessing data using its coumn name
age = df['age']#Accessing data using its column name
#Stores them in a variabke: a Series object in Pandas

