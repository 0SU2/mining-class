import matplotlib.pyplot as plt
import pandas as pd
'''
Para las variables nominales: 
sexo, mascota, consola, y para la variable intervalo razon de 
   -Imprimir los porcentajes en orden descendente
   -Hacer una grafica de pasterl 
   -Hacer una grafica de barras 

   Para la variable peso, calcula frecuencias y porcentaje en los rangos [0-50], 
   [60-70], [70-80], [80+]



'''
def resumen(df,var):
   # 1. Calcular frecuencias y porcentajes 
   d_f = {}
   freq = df[var].to_list()
   for key in freq:   
      if type(key) == str: 
         tokens = key.split('/')
      else:  # para tipos no strings 
         tokens = [key]
      if var != 'peso':
         for tk in tokens: 
            d_f[tk] = d_f.get(tk, 0) + 1 
      else:
         if key >= 0 and key < 50:
            d_f['[0-49]'] = d_f.get('[0-49]', 0) + 1 
         elif key >= 50 and key < 60:
            d_f['[50-59]'] = d_f.get('[50-59]', 0) + 1 
         elif key >= 60 and key < 70:
            d_f['[60-69]'] = d_f.get('[60-69]', 0) + 1 
         elif key >= 70 and key < 80:
            d_f['[70-79]'] = d_f.get('[70-79]', 0) + 1 
         elif key > 80:
            d_f['[80+]'] = d_f.get('[80+]', 0) + 1 
   
   # -Calculo de la frecuencia 
   l_p = []
   total = sum(d_f.values())
   for k,v in d_f.items():
      # tupla que es porcentaje, frecuencia, categoria 
      l_p.append((v/total * 100, v , k))
   # Orden descendente
   l_p.sort(reverse=True)
   l_l = [] # Categorias en var
   l_f = [] # Frecuencia de c
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
l_v = ['sexo', 'mascota','consola','semestre','peso']
for v in l_v: 
   print()
   print(f'para la variable {v}: ')
   resumen(df,v)
#-------------------------------------------------