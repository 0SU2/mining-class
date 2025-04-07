'''
@@@@@----PANDASSSS----@@@@@@
  Usando como base el ejercicio previo 

  estimar las proporciones de hombres y mascotas que tienen mascotas y consola
  Estimar la proporcion 
'''
import pandas as pd
import matplotlib.pyplot as plt
w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

def contigencia_tab(values_1,values_2):
  # Formar la tabla de contingencia
  c_t = {} 
  for x, y in zip(values_1,values_2):
    if x not in c_t: # Si aun no esta definida en el diccionario
      c_t[x] = {}
    c_t[x][y] = c_t[x].get(y,0) + 1
  return c_t

def porcentaje(values_1,values_2,v1,v2,total):

  c_t = contigencia_tab(mascota,consola)
  s_s = c_t[v1[0]][v2[0]]
  s_n = c_t[v1[0]][v2[1]]

  n_s = c_t[v1[1]][v2[0]]
  n_n = c_t[v1[1]][v2[1]]

  t_s = s_s + s_n
  t_n = n_s + n_n
  t_p = t_s + t_n

  if total:
    p_s_s = (s_s / t_p)*100
    p_s_n = (s_n/t_p)*100
    p_n_s = (n_s/t_p)*100
    p_n_n = (n_n / t_p)*100
  else:
    p_s_s = (s_s / t_s)*100
    p_s_n = (s_n/t_s)*100
    p_n_s = (n_s/t_n)*100
    p_n_n = (n_n / t_n)*100

  return [p_s_s,p_s_n,p_n_s,p_n_n]

l_v =['sexo','consola','mascota']
sexo = df['sexo'].to_list()
mascota = df['mascota'].to_list()
consola = df['consola'].to_list()

mascota = ['s' if x != 'n' else x for x in mascota]
c_t = contigencia_tab(sexo,mascota)
# Porcentaje de mujeres con mascota 
h_s = c_t['h']['s']
h_n = c_t['h']['n']

m_s = c_t['m']['s']
m_n = c_t['m']['n']

t_h = h_s + h_n
t_m = m_s + m_n
t_p = t_h + t_m 

p_h_s = (h_s/t_h)*100
p_h_n = (h_n/t_h)*100
p_m_s = (m_s/t_h)*100
p_m_n = (m_n/t_h)*100
p_p_m = ((h_s+m_s)/t_p)*100

print(f'Porcentaje de Hombres que tienen mascota:  {p_h_s:.2f}%')
print(f'Porcentaje de Mujeres que tienen mascota:  {p_m_s:.2f}%')
print(f'Porcentaje de Personas que tienen mascota:  {p_p_m:.2f}%')

# Porcentaje que tienen consola y mascota 
c_t = contigencia_tab(mascota,consola)
s_s = c_t['s']['s']
s_n = c_t['s']['n']

n_s = c_t['n']['s']
n_n = c_t['n']['n']

t_s = s_s + s_n
t_n = n_s + n_n
t_p = t_s + t_n

p_s_s = (s_s / t_p)*100
p_n_n = (n_n / t_p)*100

print(f'Porcentaje de Hombres que tienen consola:  {p_s_s:.2f}%')
print(f'Porcentaje de Mujeres que tienen consola:  {p_n_n:.2f}%')

l = porcentaje(mascota,consola,['s','n'],['s','n'], total = True)
