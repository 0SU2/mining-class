'''
Tomando como base el ejercicio 9 

Escribir una funcion que calcule la varianza y la desviacion estandar 
e imprimir el coeficiente de variabilidad (C.V)
'''
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

def resumen(df,var,o_d):
   values = df[var].to_list() 
   values.sort()
   #trim_val = trimm_data(values,10)
   
   #Dispersion natural 
   plt.figure()
   plt.scatter(range(len(values)), values)
   plt.title(f'Dispersion natural de {var}')
   plt.savefig(o_d+ f'{var}Dnatural.jpg',dpi=600)
   # -Dispersion ordenada
   l_o = sorted(values)
   plt.figure()
   plt.scatter(range(len(values)), values) # -Aplica ordenamiento a la lista sin modificarla, hace una copia 
   plt.title(f'Dispersion ordenada de {var}')
   plt.savefig(o_d+ f'{var}Dordenada.jpg',dpi=600)

   Q1 = cuartil(values,1)
   Q3 = cuartil(values,3)
   print(f'Minimo: {min(values)}')
   print(f'Cuartil 1: {Q1}')
   print(f'Cuartil 2: {cuartil(values,2)}')
   print(f'Cuartil 3: {Q3}')
   print(f'Maximo: {max(values)}')
   media = sum(values) / len(values)
   print(f'Media: {media:.2f}')
   varianza, std = var_std(values,media)
   cv = std / media
   print(f'Varianza: {varianza:.2f}')
   print(f'Des. Estandar: {std:.2f}')
   print(f'CV: {cv:.2f}')
   outliers(values,Q1,Q3)
   plt.figure()
   plt.boxplot(values)
   plt.title(f'BoxPlot-TRIM de {var}')
   plt.savefig(o_d+ f'{var}valuesBxP.jpg',dpi=600)
   
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
   print('*'*10)
   print(f'para la variable {v}: ')
   resumen(df,v,w_d)
   print('*'*10)
#-------------------------------------------------

# La media y la mediana tiene como proposito encontrar un valor tipico o esperado que describa al conjunto de datos 
# En otras palabras, alrededor de que valor espero encontrar otros valores si los selecciono al azar 

# La mediana el centro geometrico de los datos
# Necesito saber la posicion para encontrar el valor 
# No le afectan tanto los valores atipicos 

# La media es el centro aritmetico, necesito sumar y dividir para encontrar el valor 
# La media es mas facil de calcular, pero eso no quiere decir que siempre sea la mas adecuada 


# No hay un porcentaje que sea mejor a otros para recortar los datos 
# Este porcentajes depenedera de la distribucion original 

# Algunas otras metricas si se modificaron pero en general 

# La media y mediana son metricas de tendencia central. El objetivo es tener 
# un solo numero que resuma de manera general los datos 
# -------------------------------------------------
#                Estudiantes10
# Para que la media y la mediana sirvan como medidas de tendencia general, sus valores tienen que ser similares 
# la desviacion estandar baja, y por lotanto el coeficiente de variabilidad tiene que ser bajo
# Si se cumple lo anterior, ambas representan 
# el valor atipico (esperado) dentro de la muestra o poblacion 
#
# Reportar media, mediana, desviacion estandar 

# La desviacion estandar me permite saber la dispersion 
# de los datos con respecto a la media 
# Si CV >= 0.3... std es muy grande  y no es buena 
# Si CV <= 0.15 y cv < 0.3... STD es grande
# si CV < 0.15... std es baja 

