'''
para la variable sexo, calcula las frecuencias y porcentajes de cada valor 
imprimir los resultados en orden descendiente por porcentaje 
Crear un grafico de pastel y uno de barras 
'''

import matplotlib.pyplot as plt
import pandas as pd

w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'

df = pd.read_csv(i_f)
# Obtiene todos los h y m que hay en el csv 
freq = df['sexo'].to_list()

# Para mas de dos valores 
# Si no se sabe cuantos elementos existen 
d_f = {}

# Crea un diccionario de h y m y almacena el total de cada una 
for key in freq:
   d_f[key] = d_f.get(key, 0) + 1 
   # el metodo get busca el valor asociado a key 
   # si la llave no existe regresa 0 
   # si la llave existe regresa el valor asociado


l_p = []
total = sum(d_f.values())
# Crea una lista de tuplas que contiene el porcentaje, frecuencia y categoria 
for k,v in d_f.items():
   # tupla que es porcentaje, frecuencia, categoria 
   l_p.append((v/total * 100, v , k))

l_p.sort(reverse=True)


l_l = []
l_f = []

# ---Itera lista de tuplas--- 
for t in l_p:
   print(f'{t[2]}: {t[1]} -> {t[0]}')
   # Frecuencias
   l_f.append(t[1])
   l_l.append(t[-1])

print(l_f) 
print(l_l)
# ---Secuencia para crear graficos ---
# 1. lienzo en blanco 
plt.figure()
# 2. Tipo grafico 
plt.pie(l_f, labels=l_l)
# 3. Poner un titulo 
plt.title('Sexo') 
# 4. Exportar la figura 
# plt.show()
plt.savefig('pastel.jpg',dpi=600)

plt.figure()
plt.bar(l_l,l_f) # Primero lo que va en x y despues lo que va en y
plt.title('Sexo')
plt.xlabel('Categoria')
plt.ylabel('Frecuencia')
plt.savefig('barras.jpg', dpi=600)

#############
# En analisis de datos hay dos partes principales 
# Primero se tienen los calculos que permiten encontrar asociaciones, dispersiones de datos, estadisticas
# encontrar patrones


# Lo segundo es hacer la interpretacion, el resumen, el reporte 
# una aplicacion externa esta se envia a la persona encargada de la toma de decisiones 

# la interpretacion puede incluir hipotesis o especulaciones para tratar de explicar los datos 

# ¿Por qué? # (en este caso no se puede realizar una hipotesis porque los datos estan sesgados )
# 1. porque las ingenierias tienen mas hombres, pero las demas carreras tiene mas mujeres 
# 2. El diseño de la recopilacion pedia un equilibrio entre hombres y mujeres 
# 3. Una mal captura de los datos 
#
# La hipotesis mas sostenible es la segunda 
# para la tercera requerimos mayor informacion de la recopilacion 
# para la primera se necesita un muestreo grande 



