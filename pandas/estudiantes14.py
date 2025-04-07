"""
@@-----PANDAS-----@@
Rehacer el codigo para calcular las estadisticas y graficar los plots 
para las diferentes variables numericas pero separando las estadisticas
y las graficas por la variable sexo [h/m]. Omitir el calculo de los outliers y bins
"""
import matplotlib.pyplot as plt
import pandas as pd

w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)
l_v = ['peso', 'altura','edad','semestre']

def plot_pandas(df, v, var):
  # v es la variable numerica 
  # var es la variable para agrupar 
  plt.figure()
  df.boxplot(column=v, by=var) 
  plt.figure()
  df[v].hist(bins=6, by=df[var]) 
  plt.suptitle(f'{v} Agrupada por {var}')
  plt.show()
  return 

def resumen_pandas(df, l_v, var, p):
  # df son los datos originales 
  # l_v es la lista de variables numericas semestre,peso,edad,altura
  # var es la variable para agrupar h,m
  # p es el porcentaje de datos a recortar 

  labels = set(df[var].to_list())
  print(labels)
  for v in l_v:
    df_sorted = df.sort_values(by=v) # ordenamiento de variables 
    n = len(df)
    k = int((n*p)/100)
    df_sorted = df_sorted[k:n-k]
    
    for label in labels:
      print(v,label) 
      l_filter = (df_sorted[var] == label)
      print(f'Estadisticas de {v} para {label}:')
      print(df_sorted[l_filter].describe())
    plot_pandas(df_sorted,v,var)
  return 

resumen_pandas(df,l_v,'sexo',10)


# 
# # Filtrando por el sexo 
# filtro_h = (df['sexo'] == 'h')
# filtro_m = (df['sexo'] == 'm')
'''
for v in l_v:
  # Bloxplot
  df.boxplot(column=v,by ='sexo')
  df[v].hist(bins=6, by = df['sexo'])
  plt.show()

 Estadisticas
print(df.groupby('sexo').describe())
'''

#l_s = ['h','m']
#
#for s in l_s:
#  print(f'Estadisticas para {s}: ')
#  s_filtro = (df['sexo'] == s)
#  print(df[s_filtro].describe())
#
