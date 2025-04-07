'''
@PANNNDASSS

'''

import pandas as pd
import matplotlib.pyplot as plt
w_d = 'C:\\Users\\mk4c1\\OneDrive\\Documentos\\1.-DICIS.-OctavoSemestre\\MineriaDatos\\ManejoArchivos-Estudiantes\\'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

print(df)

# Slicing 
# [inicio:final-1]
print(df[:10])
print(df[::5])

## -- Funciones --##
# .describe()
# Regresa informacion estadistica sobre los datos, es equivalente a la funcion resumen()
# Solo trabaja sobre valores numericos 
print(df.describe()) 
print(df['edad'].describe()) # Para un valor en especifico
print(df[:10].describe())
print(df[:10][['edad']].describe()) # Para un valor en especifico

# .boxplot()
# Genera un diagrama de cajas para cada variable 
# numerica en el dataframe 


#df.boxplot()
#df[['edad']].boxplot()
#df[['edad','semestre']].boxplot()
#df[10:50][['edad','semestre']].boxplot()

# .mean()
# Regresa la media, siempre y cuando sean variables numericas#
print(df['edad'].mean())

# .median()
# Regresa la mediana 

print(df['edad'].median())

# quantiles(q)
# Regresa el cuartil o percentil correspondiendte  a q

print(df['edad'].quantile(0.25))

# .sort_values(by=var)
# Regresa un nuevo dataframe con las observaciones ordenadas
# de acuerdo a una variable, en orden ascendente 

# ascendente 
df_s = df[10:30].sort_values(by='edad')
print(df_s)
#descendente 
df_s = df[10:30].sort_values(by='edad',ascending=False)
print(df_s)

### Filtros ###
# Filtrar las observaciones de acuerdo a una o mas condiciones que comparan los valores 
# de una o mas columnas (variables) con valores especificos 
# Regresa un tipo de dato Series (de pandas )
# que contiene valores booleanos (True/False)
filtro_edad = (df['edad'] > 21)
print(df[filtro_edad])

# filtro compuesto 
filtro_c = (df['edad'] > 21) & (df['sexo'] == 'm')
print(df[filtro_c])

# Filtrar de acuerdo a substrings 
filtro_gato = (df['mascota'].str.contains('gato')) # Filtra los que tengan gato y gato/perro
print(df[filtro_gato])

print(df[filtro_gato].describe())

df[filtro_gato].boxplot()
plt.show()

# Agrupacion de datos 

# Una vez aplicado el filtro se puede dividir nuestros datos 
# de acuerdo a otra variable 

df[filtro_gato].boxplot(column='edad', by='sexo')
plt.show()
df[filtro_gato].boxplot(column='edad', by='consola')
plt.show()
# Otros graficos 
df[filtro_gato].plot(x='edad',y='semestre')

# histograma
df.hist()
plt.show()
df.hist(bins=5)
plt.show()
df['edad'].hist(bins=3)
plt.show()
df[filtro_gato]['edad'].hist(bins=6)
plt.show()
