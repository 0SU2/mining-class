"""
 Mon Mar 3 of 2025
Mas sobre pandas
"""
import pandas as pd
w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

# Slicing
# [inicio:final-1] por indices
print(df[:10])
print(df[::5])

### Funciones ###
# .describe()
# Regresa informacoin estadistica sobre
# los datos, es equivalente a la funcion
# resumen(). Solo trabaja sobre variables
# numericas.
print(df.describe)
# Si no quiero sobre todas las variables
print(df['edad'].describe())
print(df[['edad', 'altura']].describe())
print(df[:10].describe())
print(df[:10][['edad', 'altura']].describe())
print(df[50:100:5][['edad', 'altura']].describe())

# .boxplot
# Genera un diagrama de cajas para cada
# variable numerica en el dataFrame
df.boxplot()
df[['edad','semestre']].boxplot()
df[10:50][['edad', 'semestre']].boxplot()

# .mean()
# Regres ala media, siempre y cuando, sean
# variables numericas
df['edad'].mean() # Tenemos que especificarle la variable
df[['edad','altura']].mean()
df[:10][['edad','altura']].mean()

# .median()
# Regresa la mediana
df['edad'].median() # Tenemos que especificarle la variable
df[['edad','altura']].median()
df[:10][['edad','altura']].median()

# .quantile(q)
# Regresa el cuartil o percentil correspondiente
# a q.
df['edad'].quantile(0.75) # Tenemos que especificarle la variable
df[['edad','altura']].quantile(0.25)
df[:10][['edad','altura']].quantile(0.25)

# .sort_values()
# Regresa un nuevo dataFrame con las observaciones
# ordenadas de acuerdo a una variable, en ordenada
# ascendente.
df_s = df[10:30].sort_values(by='edad')
df_s = df[10:30].sort_values(by='edad', ascending=False)

### Filtros ###
# Filtrar las observaciones de acuerdo a una
# o mas condiciones que comparan los valores
# de una o mas columnas (variables) con valores
# especificos...
# Regresa un tipo de datos Series (de Pandas),
# que contiene valores booleans (True/False).
filtro_edad = (df['edad'] > 21)
print(df[filtro_edad].sort_values(by='edad', ascending=False))

filtro_c = (df['edad'] > 21) & (df['sexo'] == 'm')

# Filtrar de acuerdo a substrings
filtro_gato = (df['mascota'].str.contains('gato'))
df[filtro_gato].describe()
df[filtro_gato].boxplot()

# Agrupacion de datos. Una vez aplicado el
# filtro, podemos dividir nuestros datos
# de acuerdo a otra variable
df[filtro_gato].boxplot(by='edad', by='consola')

# Otros graficos
df[filtro_gato].plot(x='edad', y='semestre', kind='scatter')

# Histograma
df.hist()
df.hist(bins=6)
df['edad'].hist(bins=6)
