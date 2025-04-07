'''
para las variables nominales 
- sexo, mascota y consola 
- y la variable numerica semestre 
1. calcular las frecuencias y porcentajes 
2. en la variable mascota, separar las combinaciones y cosniderar cada valor de manera independiente
3. Imprimir los valores en orden descendente por porcentajes 
4. crear grafico de pastel y de barras 

Implementar una funcion que tome el dataframe y el nombre de la variable que queremos 
analizar 
'''

import matplotlib.pyplot as plt
import pandas as pd


def resumen(df,var):
   # 1. Calcular frecuencias y porcentajes 
   d_f = { }
   # Almacena todos los valores de la columna iterada
   freq = df[var].to_list()
   for key in freq:   
      if type(key) == str: 
         tokens = key.split('/')
      else:  # para tipos no strings 
         tokens = [key]
      for tk in tokens: 
         d_f[tk] = d_f.get(tk, 0) + 1 

   l_p = []
   total = sum(d_f.values())
   for k,v in d_f.items():
      # tupla que es porcentaje, frecuencia, categoria 
      l_p.append((v/total * 100, v , k))
   
   l_p.sort(reverse=True)
   l_l = []
   l_f = []
   # Itera lista de tuplas 
   for t in l_p:
      print(f'{t[2]}: {t[1]} -> {t[0]}')
      # Frecuencias
      l_f.append(t[1])
      l_l.append(t[-1])
      # 2. Tipo grafico 
   plt.figure()
   plt.pie(l_f, labels=l_l)
   # 3. Poner un titulo 
   plt.title(var) 
   # 4. Exportar la figura 
   # plt.show()
   plt.savefig(var+'_pastel.jpg',dpi=600)

   plt.figure()
   plt.bar(l_l,l_f) # Primero lo que va en x y despues lo que va en y
   plt.title(var)
   plt.xlabel('Categoria')
   plt.ylabel('Frecuencia')
   plt.savefig(var+'_barras.jpg', dpi=600)

   return
   

#-------------------------------------------------
w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'

df = pd.read_csv(i_f)
l_v = ['sexo', 'mascota','consola','semestre']

for v in l_v: 
   print()
   print(f'para la variable {v}: ')
   resumen(df,v)
#-------------------------------------------------




