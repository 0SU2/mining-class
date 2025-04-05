"""
Tomando como base el ejercicio previo:
- Rehacer el codigo para calcular las estadisticas
y graficar los plots para las diferentes
variables numericas pero separando las estadisitcas
y las graficas por la variable sexo (h/m). Omitir el
calculo de los outliers y bins.
"""
import pandas as pd
import matplotlib.pyplot as plt

def plot_pandas(df, v, var):
    # v es la variable numerica
    # var es la variable para agrupar

    # boxplot
    plt.figure()
    df.boxplot(column=v, by=var)

    # histrograma
    plt.figure()
    df[v].hist(bins=6, by=df[var])
    plt.suptitle(f'{v} agrupada por {var}')

    return

def resumen_pandas(df, l_v, var, p):
    # var es la variable para agrupar
    # l_v es la lista de variables numericas
    # p s el porcentaje de datos a recortar

    label = set(df[var].tolist())
    for v in l_v:
        df_sorted = df.sort_values(by=v)
        n = len(df)
        k = int((n*p)/100)
        df_sorted = df_sorted[k:n-1]
        for label in lables:
            l_filter = (df_sorted[var] == label)
            print(f'\tEstadisticas de {v} para {label}')
            print(df_sorted[l_filter][v].describe())
        plot_pandas(df_soted,v,var)

    return

w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

l_v = ['peso', 'altura', 'edad', 'semestre']

# Variable de control
hombre = (df['sexo'] == 'h')
mujeres = (df['sexo'] == 'm')

df.boxplot(column='peso', by='sexo')
df.boxplot(column='altura', by='sexo')
df.boxplot(column='edad', by='sexo')
df.boxplot(column='semestre', by='sexo')

# df['peso'].hist(bins=6, by=df['sexo'])
# df['altura'].hist(bins=6, by=df['sexo'])
# df['edad'].hist(bins=6, by=df['sexo'])
# df['semestre'].hist(bins=6, by=df['sexo'])

# for v in l_v:
#     df.boxplot(column=v, by=['sexo'])
#     df[v].hist(bins=6, by=df['sexo'])

# df.groupby('sexo').describe()
# l_s = ['h','m']

# for s in l_s:
#     print(f'\nEstadisitcas para {s}')
#     s_filtro = (df['sexo'] == s)
#     print(df[s_filtro].describe())

resumen_pandas(df, l_v, '
