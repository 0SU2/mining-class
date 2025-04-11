'''
Usando como base el ejercicio anterior con la funcion para generar la tabla de contingencia 
entre cada par de variables 
hacer una funcion que calcule el coeficiente Phi de Pearson entre cada par de variables 
en el caso de la variable mascota, convertir a binario [s/n]
todas las tablas deben ser 2x2
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

def phi_coef(c_t,lab_1,lab_2):
  n11 = c_t[lab_1[0]][lab_2[0]]
  n10 = c_t[lab_1[0]][lab_2[1]]
  n01 = c_t[lab_1[1]][lab_2[0]]
  n00 = c_t[lab_1[1]][lab_2[1]]

  n1x = n11 + n10
  n0x = n01 + n00

  nx1 = n11 + n01
  nx0 = n10 + n00
  
  num = n11 * n00 - n10 * n01
  den = (n1x* n0x * nx1 * nx0)**0.5
  phi = num / den

  return phi 


print(f'Sexo --> {sexo}')
print(f'mascota --> {mascota}')

c_t = contigencia_tab(sexo,mascota)

print(f' C_T --> {c_t}')
phi = phi_coef(c_t,['h','m'],['s','n'])
print(f'Tabla de contingencia entre (sexo) y (mascota) es: {c_t}')
print(f'Coeficiente de Pearson entre (sexo) y (mascota) es: {phi}')

c_t = contigencia_tab(sexo,consola)
phi = phi_coef(c_t,['h','m'],['s','n'])
print(f'Tabla de contingencia entre (sexo) y (consola) es: {c_t}')
print(f'Coeficiente de Pearson entre (sexo) y (consola) es: {phi}')

c_t = contigencia_tab(mascota,consola)
phi = phi_coef(c_t,['s','n'],['s','n'])
print(f'Tabla de contingencia entre (mascota) y (consola) es: {c_t}')
print(f'Coeficiente de Pearson entre (mascota) y (consola) es: {phi}')

