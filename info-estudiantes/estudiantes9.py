'''
@ 

   1.Hacer una funcion que reciba como parametro una lista de valores ordeanada y un cuartil,
   devuelva el valor para ese cuartil en los datos 

   2. hacer una funcion que reciba como parametro un dataframe y el nombre de la variable a analizar 
   y que imprima el resumen de llos 5 numeros y grafique el diagrama de caja 

   3. Hacer una funcion que tome una lista de valores ordenada, el 01 y 03, la funcion debe calcular 
   e imprimir el IQR, LIF, UIF, el whisker inferior, el whisker superior y los valores atipicos 

   4. Calcular el promedio {media aritmetica} 

   5. Hacer una funcion para recortar los datos originales a un p% {definir p en el codigo de forma inicial}
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

def resumen(df,var,o_d):
   values = df[var].to_list() 
   values.sort()
   trim_val = trimm_data(values,10)

   
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
   outliers(trim_val,Q1,Q3)
   plt.figure()
   plt.boxplot(trim_val)
   plt.title(f'BoxPlot-TRIM de {var}')
   plt.savefig(o_d+ f'{var}trim_valBxP.jpg',dpi=600)
   
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
