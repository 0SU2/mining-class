'''
Para 1 variable 
  Prueba X^2 de ajuste de longitud 
  Compara una distribucion 

Para 2 variables 
  Prueba x^2 de independencia 

Prueba de ""hipotesis"" Ho nula quiere decir que siempre habra independencia 
Prueba de ""alternativa"" H1 nula quiere decir que las variables son dependientes 

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Tomar como base la funcion para generar la tabla de contingencia .
Hacer una funcion que calcule la probablidad condicional 

tener una mascota dado que se es hombre/mujer. (Considerar la variable mascota como binaria)

tener una consola dado que se es hombre/mujer 
'''

import pandas as pd
import matplotlib.pyplot as plt
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


def prob_cond(c_t, val_A,val_B):
  p_AB = c_t[val_B][val_A] 
  print(p_AB)
  p_B = sum(c_t[val_B].values())  # Probabiildad de B 
  print(p_B)
  #p_c = p_AB / p_B

  return p_AB / p_B

# Sexo - Mascota 
c_t = contigencia_tab(sexo,consola)
print('Tabla de contingencia',c_t)
print('Sexo ->',sexo)
print('Mascota ->',consola)
print(f'Tabla de contingencia entre sexo y consola')
p_c = prob_cond(c_t,'s','h')
print(f'Probabilidad de que sea hombre y tenga consola: {p_c} ')
p_c =  prob_cond(c_t,'s','m')
print(f'Probabilidad de que sea mujer y tenga consola: {p_c} ')

# Sexo - Consola 
c_t = contigencia_tab(sexo,mascota)
print(f'\nTabla de contingencia entre sexo y mascota')
p_c = prob_cond(c_t,'s','h')
print(f'Probabilidad de que sea hombre y tenga mascota: {p_c} ')
p_c =  prob_cond(c_t,'s','m')
print(f'Probabilidad de que sea mujer y tenga mascota: {p_c} ')

# como resumen 
# Sexo-mascota 
# la probabilidad de tener una mascota es mayor cuando se es hombre o mujer 
# siendo mujer 
# si se seleecciona la observacion de un hombre al azar , ¿Cual es la probablidad de que tenga mascota 
# 
# Si se selecciona 
#

