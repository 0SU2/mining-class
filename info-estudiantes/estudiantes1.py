'''
@ Leer archivo info_estudiantes.csv
para la variable sexo, calcula:
las frecuencias de cada valor (h,m)
y su porcentaje 
'''

import pandas as pd

w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'

df = pd.read_csv(i_f)
# Obtiene todos los valores de la categoria sexo en una lista 
freq = df['sexo'].to_list()

# Cuenta el numero de veces que se repite h y m 
count_h = freq.count('h')
count_m = freq.count('m')

# Calculo del porcentaje de mujeres y hombres 
print(f'{count_h}: {count_h/len(freq)*100}')
print(f'{count_m}: {count_m/len(freq)*100}')

# Para mas de dos valores 
# Si no se sabe cuantos elementos existen 
d_f = {}
for key in freq:
   
   d_f[key] = d_f.get(key, 0) + 1 
   # el metodo get busca el valor asociado a key 
   # si la llave no existe regresa 0 
   # si la llave existe regresa el valor asociado
print('Con diccionarios...')
for k,v in d_f.items(): # Itera desempaquetando la llave y el valor  
   print(f'{k}:{v}, {v/sum(d_f.values())*100} ')

