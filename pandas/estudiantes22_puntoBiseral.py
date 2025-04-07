'''

Hacer una funcion que calcule la correlacion Punto-Biseral entre una variable categorica y una variable
numerica

Utilizar la funcion para calcular la correlacion entre el genero y las variables numericas: 
  edad
  peso
  altura 
  semestre 
'''
import pandas as pd
import matplotlib.pyplot as plt
w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

l_v =['edad','altura','semestre','peso']
sexo = df['sexo'].to_list()

# -Funcion desviacion estandar 
def std(l_v):  
  mean = sum(l_v)/len(l_v)
  var = sum([(x-mean)**2 for x in l_v]) / (len(l_v)-1)
  return var**0.5

def pb_corr(var_1,var_2, lab):
  # lab = [grupo_1, grupo0]
  # Comprobar si las frecuencias en var_1 (variable binaria )
  # estan balanceadas. 
  ### 
  n_0 = n_1 = s_0 = s_1 = 0

  # variable numerica y 
  for i , j in zip(var_1,var_2):
    if i == lab[0]:
      # grupo 1 
      # sumar los valores 
      s_1 += j
      n_1 += 1
    else: 
      # grupo 0
      s_0 += j
      n_0 += 1

  # Media de grupo 1 y 0 
  m_0 = s_0 / n_0
  m_1 = s_1 / n_1

  # Numero total de elementos 
  n = n_1 + n_0

  # Desviacion estandar 
  s_y = std(var_2)
  r_pb = ((m_1-m_0) / s_y) * ((n_1*n_0)/(n*n))**0.5
  return r_pb 

for var in l_v:
  var_2 = df[var].tolist()
  r_pb = pb_corr(sexo,var_2,['h','m'])
  print(f'Correlacion Punto-Biseral entre [sexo , {var}]: {r_pb:.3f}')


# El grupo 1 pertenece a los valores 'h'
# sexo - edad : 0.08 
# correlacion casi nula 
# sexo - peso : 0.69
# correlacion media 
# sexo - semestre 
# correlacion casi nula 
# sexo - altura 
# corr media, los hombres tienden a ser mas altos 