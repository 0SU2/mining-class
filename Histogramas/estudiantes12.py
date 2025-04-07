"""

Tomando como base el ejercicio previo, 
Hacer una funcion que tome una lista de datos ordenados 
y la separe en n bins { el numero de bins por el usuario }. 
Encontrar y regresar los limites superiores e inferiores de los n bins. 

Esta funcion se manda llamar dentro de la funcion resumen 
"""


import matplotlib.pyplot as plt
import pandas as pd

def cuartil(l_v,q):
   p_q = (q*len(l_v)-1) / 4 # Posicion en la lista 

   # Parte entera que nos dice cual elemento tomar 
   idx = int(p_q)   # casteo
   # valor que permite hacer una interpolacion lineal 
   dec = p_q%1
   # valor del cuartil q
   v_q = l_v[idx] + (dec * (l_v[idx+1] - l_v[idx]))

   return v_q

def outliers (l_o,q1,q3):
   IQR = q3 - q1 
   LIF = q1 - 1.5 * IQR
   UIF = q3 + 1.5 * IQR 
   print(f'IQR: {IQR:.2f}')
   print(f'LIF: {LIF:.2f}')
   print(f'UIF: {UIF:.2f}')

   #whisker inferior y superior    
   for v in l_o:
      if v >= LIF:
         lw = v 
         break 
   
   for v in l_o[::-1]:
      if v <= UIF:
         uw = v 
         break 
   print(f'Whisker inferior: {lw:.2f}')
   print(f'Whisker superior: {uw:.2f}')


   outs = []
   for v in l_o:
      if v < lw  or v > uw:
         outs.append(v)
   
   print(f'Outliers: {outs}')
   return      

def trimm_data(datos,p=10):
   # Sobre los datos ordenados, calcular k
   n = len(datos)
   k = int((p*n)/100)

   return datos[k:n-k]

def var_std(datos,media):
   n = len(datos)
   
   for x_i in range(len(datos)):
      var = (datos[x_i] - media)**2
      var += (var/n)   
   # var = [(x_i - media)**2 for x_i in datos]
   # var = sum(var/ len(datos))
   std = var**0.5
   return var,std

def get_bins(values,n):
   lim_bins = []
   # 1.Encontrar el rango 
   min = values[0]
   max = values[-1]
   rango = abs(min-max)
   # 2.Dividir el rango
   size = rango/n
   l_i = min
   l_s = min + size
   
   # 4. Definir el limite superior e inferior de cada bin y agregarlo a una lista de listas 

   # Primera forma 
   lim_bins = [[l_i+(size*i),l_s+(size*i)] for i in range(n)]
   # Segunda forma 
   #i = 0
   #l_temp = []
   #while i < n: 
   #   l_temp = [l_i,l_i+size] 
   #   lim_bins.append(l_temp)
   #   l_i += size 
   #   i += 1
   
   return lim_bins
         


def resumen(df,var,o_d,p):
   values = df[var].to_list() 
   values.sort()
   bins =  int(input("Numero de bins a calcular: "))
   n = get_bins(values, bins)
   print(f"bins calculados: {n}")
   trim_val = trimm_data(values,p)
   
   #Dispersion natural 
   plt.figure()
   plt.scatter(range(len(trim_val)), trim_val)
   plt.title(f'Dispersion natural de {var}')
   plt.savefig(o_d+ f'{var}Dnatural.jpg',dpi=600)
   # -Dispersion ordenada
   l_o = sorted(values)
   plt.figure()
   plt.scatter(range(len(trim_val)), trim_val) # -Aplica ordenamiento a la lista sin modificarla, hace una copia 
   plt.title(f'Dispersion ordenada de {var}')
   plt.savefig(o_d+ f'{var}Dordenada.jpg',dpi=600)

   Q1 = cuartil(trim_val,1)
   Q3 = cuartil(trim_val,3)
   print(f'Minimo: {min(trim_val)}')
   print(f'Cuartil 1: {Q1}')
   print(f'Cuartil 2: {cuartil(trim_val,2)}')
   print(f'Cuartil 3: {Q3}')
   print(f'Maximo: {max(trim_val)}')
   media = sum(trim_val) / len(trim_val)
   print(f'Media: {media:.2f}')
   varianza, std = var_std(trim_val,media)
   cv = std / media
   print(f'Varianza: {varianza:.2f}')
   print(f'Des. Estandar: {std:.2f}')
   print(f'CV: {cv:.2f}')
   outliers(trim_val,Q1,Q3)
   
   plt.figure()
   if p != 0:
      plt.boxplot([values, trim_val],labels=['Completos', 'Recortados'])
      #plt.xticks([1,2], labels=["Completos", "Recortados"])
      #plt.savefig(o_d+ f'{var}trim_valBxP.jpg',dpi=600)
      plt.title(f'BoxPlot de {var}')
      plt.savefig(o_d+ f'{var}BoxRecortados-Completos.jpg',dpi=600)
   else: 
      #plt.figure()
      plt.boxplot(trim_val)
      plt.title(f'BoxPlot de {var}')
      plt.savefig(o_d+ f'{var}BoxRecortados-Completos.jpg',dpi=600)
   
   return   

'''
Pq = q(n-1)/4 
Qn = int(q)+ (dec(q))

'''
#-------------------------------------------------
w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'

df = pd.read_csv(i_f)
l_v = ['peso', 'altura','edad','semestre']
#l_v = ['edad']
for v in l_v: 
   print('*'*50)
   print(f'para la variable {v}:')
   print("Datos completos")
   resumen(df,v,w_d,0) 
   print('-'*20)
   print("Datos Recortados")
   resumen(df,v,w_d,10)
#-------------------------------------------------