'''
Tomando como base el ejercicio previo
  Usando pandas, calcular el coeficiente de correlacion de Pearson entre cada par de variables 
  numericas: edad,altura, peso y semestre 

  Hacer el grafico de dispersion correspondiente a cada par de variables 
'''

import pandas as pd
import matplotlib.pyplot as plt

w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

#print(df[['edad','semestre']].corr())
l_v =['edad','altura','semestre','peso']
n = len(l_v)
#print(range(n-1))
#for v in range(n-1):
#  for v1 in range(n):
#    if l_v[v]!= l_v[v1] and l_v[v1] != l_v[v]:
#      print(df[[l_v[v],l_v[v1]]].corr())


for i in range(n-1):
  for j in range(i+1,n):
    v1 = l_v[i]
    v2 = l_v[j]
    r = df[[v1,v2]].corr().iloc[0,1]
    df.plot(x=v1,y=v2,kind='scatter')
    plt.title(f'Grafico de dispersion entre {v1} y {v2}: {r:.4f}')
    print(f'Grafico de dispersion entre {v1} y {v2}: {r:.4f}')
    
plt.show()

# El coeficiente de correlacion es simetrico r(x,y) = r(y,x)
# El coeficiente de correlacion de una variable contra si misma es 1 

# RANGOS EMPIRICOS EN CORRELACIONES:
# -Correlacion muy alta: 0.9 a 1 
# -Correlacion alta: 0.7 a 0.9 
# -Correlacion media: 0.5 a 0.7
# -Correlacion baja: 0.3 a 0.5 
# -Correlacino casi nula: 0.0 a 0.3 
# -Correlacion nula: 0

# Edad y altura. casi nula 
# Edad y semestre. casi nula
# Edad y peso. media 
# Altura y semestre. nula
# Altura y peso. media 
# Semestre y peso. casi nula 