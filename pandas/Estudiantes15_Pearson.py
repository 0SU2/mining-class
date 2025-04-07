'''
@@@@
  Hacer una funcion que calcule el coeficiente de pearson para dos variables.
  Pasar como parametro las listas de los valores de cada variable 
'''
import pandas as pd
import matplotlib.pyplot as plt

w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)
edad = df['edad'].to_list()
semestre = df['semestre'].to_list()
#temp = [14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2]
#sell = [215,325,185,332,406,522,412,614,544,421,445,408]
def coef_pearson(val_1,val_2):
  r = 0
  if len(val_1) != len(val_2):
    print('La lista debe tener la misma logitud')
    return 
  
  x_mean =  sum(val_1) / len(val_1)
  y_mean = sum(val_2) / len(val_2)

  num = 0
  den1 = 0
  den2 = 0
  for x,y in zip(val_1,val_2):
    num += (x-x_mean)*(y-y_mean)
    den1 += (x-x_mean)**2
    den2 += (y-y_mean)**2 

  r = num/((den1**0.5)*(den2**0.5))

  return r

print(coef_pearson(edad,semestre))

''' 
df = pd.read_csv(i_f)


media = sum(temp)/ len(temp)
print(media)
for t in temp: 
  s_t = (t - media)
  r_t = math.sqrt(t-media)
  rxy += s_t / r_t
  print(rxy)

'''
