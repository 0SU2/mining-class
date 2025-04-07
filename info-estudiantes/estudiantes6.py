'''
--- PARA VARIABLE INTERVALO RAZON 
   -PESO
   -ALTURA
   -EDAD
   -SEMESTRE

   Obtener una grafica de dispersion
   natural y una de dispersion ordenada 
   Calcular el minimo y maximo
   Crear una funcion que reciba el dataframe y el nombre de la variable que se quiere analizar 

'''
import matplotlib.pyplot as plt
import pandas as pd

def resumen(df,var):
   values = df[var].to_list()
   #Dispersion natural 
   plt.figure()
   plt.scatter(range(len(values)), values)
   plt.title(f'Dispersion natural de {var}')
   plt.savefig(var+'Dnatural.jpg',dpi=600)
   # -Dispersion ordenada 
   plt.figure()
   plt.scatter(range(len(values)), sorted(values)) # -Aplica ordenamiento a la lista sin modificarla, hace una copia 
   #plt.xlim(min(values),max(values))
   #plt.ylim(min(values),max(values))
   plt.title(f'Dispersion ordenada de {var}')
   plt.savefig(var+'Dordenada.jpg',dpi=600)

   print(f'Minimo: {min(values)}')
   print(f'Minimo: {max(values)}')

   return   

#-------------------------------------------------
w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'

df = pd.read_csv(i_f)
l_v = ['sexo', 'mascota','consola','semestre','peso', 'altura']
for v in l_v: 
   print('*'*10)
   print(f'para la variable {v}: ')
   resumen(df,v)
   print('*'*10)
#-------------------------------------------------
