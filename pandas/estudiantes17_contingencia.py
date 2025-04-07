'''
@@@@@----PANDASSSS----""""""!!!qq,QQ,aqq@@@@@@
  En el caso de la variable mascota, transformar los datos a binario(s/n)
  todas las tablas de contingencia seran de 2x2 
'''

import pandas as pd
import matplotlib.pyplot as plt

w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

l_v =['sexo','consola','mascota']
n = len(l_v)
def contigencia_tab(values_1,values_2):
  # Formar la tabla de contingencia
  c_t = {} 
  for x, y in zip(values_1,values_2):
    if x not in c_t: # Si aun no esta definida en el diccionario
      c_t[x] = {}
    c_t[x][y] = c_t[x].get(y,0) + 1
      
  return c_t

for i in range(n-1):
  v1 = l_v[i]
  values_1 = df[v1].to_list()
  if v1 == 'mascota': 
    values_1 = ['s' if x != 'n' else x for x in values_1]
  for j in range(i+1,n):
    v2 = l_v[j]
    values_2 = df[v2].to_list()
    if v2 == 'mascota': 
      values_2 = ['s' if x != 'n' else x for x in values_2]
    c_t = contigencia_tab(values_1,values_2)
    print(f'La tabla de contingencia entre {v1} y {v2}:')
    print(f'{c_t} \n')