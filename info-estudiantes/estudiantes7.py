'''
--- PARA VARIABLE INTERVALO RAZON 
   -PESO
   -ALTURA
   -EDAD
   -SEMESTRE

   Obtener una grafica de dispersion
   natural y una de dispersion ordenada 
   Calcular el minimo y maximo

   Crear una funcion que reciba una lista de valores ordenados y un
   cuartil, y devuelva el valor para ese cuartil en los datos 

   Crear una funcion que reciba el dataframe y el nombre de la variable que se quiere analizar 

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


def resumen(df,var,o_d):
   values = df[var].to_list()
   #Dispersion natural 
   plt.figure()
   plt.scatter(range(len(values)), values)
   plt.title(f'Dispersion natural de {var}')
   plt.savefig(o_d+ f'{var}Dnatural.jpg',dpi=600)
   # -Dispersion ordenada
   l_o = sorted(values)
   plt.figure()
   plt.scatter(range(len(values)), l_o) # -Aplica ordenamiento a la lista sin modificarla, hace una copia 
   #plt.xlim(min(values),max(values))
   #plt.ylim(min(values),max(values))
   plt.title(f'Dispersion ordenada de {var}')
   plt.savefig(o_d+ f'{var}Dordenada.jpg',dpi=600)

   print(f'Minimo: {min(values)}')
   print(f'Cuartil 1: {cuartil(l_o,1)}')
   print(f'Cuartil 2: {cuartil(l_o,2)}')
   print(f'Cuartil 3: {cuartil(l_o,3)}')
   print(f'Maximo: {max(values)}')

   plt.figure()
   plt.boxplot(l_o)
   plt.title(f'Boxplot de {var}')
   plt.savefig(o_d+ f'{var}_boxplot.jpg',dpi=600)

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
