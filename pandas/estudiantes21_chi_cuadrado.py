'''
Hacer una funcion para la prueba del chi-cuadrado de Pearson 
'''

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
w_d = '/home/osu2/programming/mining-class/info-estudiantes/'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

l_v =['sexo','consola','mascota']
sexo = df['sexo'].to_list()
mascota = df['mascota'].to_list()
consola = df['consola'].to_list()

mascota = ['s' if x != 'n' else x for x in mascota]

def contigencia_tab(values_1,values_2):
  # Formar la tabla de contingencia
  c_t = {} 
  for x, y in zip(values_1,values_2):
    if x not in c_t: # Si aun no esta definida en el diccionario
      c_t[x] = {}
    c_t[x][y] = c_t[x].get(y,0) + 1
  return c_t


# Sexo - mascota

c_t = contigencia_tab(sexo, mascota)
print(f'CTT->',c_t)
l = [list(v.values()) for v in c_t.values()]
'''
v.values() regresa los valores de s y n 
for k, v in c_t.items() itera sobre el sub-diccionario 
'''

print(f'SEXO-> {sexo}')
print(f'mascota-> {mascota}')
print(f'c_T-> {c_t}')
print(f'Lista l-> {l}')
#l = []
#for v in c_t.values:
#  temp = v.values() # Tipo dic_values
#  temp = list(temp) # dict_values a lista 
#  l.append(temp)
#print(l)
p_x2 = stats.chi2_contingency(l)
alpha = 0.05 # 0.01
print(f' SEXO+MASCOTA -> {p_x2.pvalue}')
if p_x2.pvalue < alpha:
  print('Las variables (sexo,mascota) son dependientes')
else: 
  print('Las variables (sexo,mascota) son independientes')

# primer lista valores de H, seguda valores de m 
# l = [l_h,l_m]
# 1_h = [f_s,f_n]
# 1_m = [f_s,f_n]
#[[12,10],[8,4]]

l = []
# Sexo - consola
c_t = contigencia_tab(sexo, consola)
print(c_t)
l = [list(v.values()) for v in c_t.values()]
'''
v.values() regresa los valores de s y n 
for k, v in c_t.items() itera sobre el sub-diccionario 
'''
p_x2 = stats.chi2_contingency(l)
alpha = 0.05 # 0.01 
print(f' SEXO+CONSOLA -> {p_x2.pvalue}')
if p_x2.pvalue < alpha: #
  print('Las variables (sexo,consola) son dependientes')
else: 
  print('Las variables (sexo,consola) son independientes')



'''
Como resumen 

con un alpha = 0.05 

--sexo y mascota--
grados de libertad = 1
x^2 = 0.14
valor de referencia = 3.841
con un 95% de seguridad se ACEPTA la HIPOTESIS NULA 
no existe una dependencia entre sexo y mascota 
No importa si se es hombre o mujer, se puede tener mascota 

--sexo y consola--
grados de libertad = 1
valor de referencia = 3.841
con un 95% de seguridad se RECHAZA la HIPOTESIS NULA 
no existe una dependencia entre sexo y consola 
Si importa si se es hombre o mujer para tener mayor o menor probabilidad de tener consola  

'''