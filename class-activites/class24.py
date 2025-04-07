"""
@ Descripcion: Tomando como base el ejercicio previo.
- Usando Pandas, calcular el coeficiente
de correlacion de Pearson entre cada persona
de variables numericas: edad, altura, peso
y semestre.

- Hace el grafico de dispersion correspondiente
a cada par de variables.
"""
import matplotlib.pyplot as plt
import pandas as pd
def coef_pearson(val_1, val_2):
    r = 0
    if len(val_1) != len(val_2):
        print('Deben ser de la misma longitud')
        return
    x_m = sum(val_1) / len(val_1)
    y_m = sum(val_2) / len(val_2)

    num = 0
    den1 = 0
    den2 = 0
    for x_i, y_i in zip(val_1, val_2):
       num += (x_i-x_m)*(y_i-y_m) 
       den1 += (x_i-x_m)**2 
       den2 += (y_i-y_m)**2 

    r = num / ((den1**0.5) * (den2**0.5))
    return r
w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

print(df[['edad','semestre']].corr())

l_v = ['edad','altura','semestre','peso']
n = len(l_v)
for i in range(n-1):
    for j in range (i+1, n):
        # v1 = l_v[i]
        # v2 = l_v[j]

        # values_1 = df[v1].to_list()
        # values_2 = df[v2].to_list()

        r = df[[v1,v2]].corr().iloc[0,1]
        plt.figure()
        df.plot(x=v1. y=v2, kind='scatter')
        plt.title(f'GGrafico de dispersoin entre {v1} y {v2}:\nr = {r:.4f}')

# El coeficiente de correlacion es
# simetrico r(x,y) = r(y,x)
# El coeficienite de correlacion de una
# variable contra si misma es 1.

# Rangos empiricos en correlaciones:
# Correlacion muy alta: 0.9 a 1
# Correlacion alta: 0.7 a 0.9
# Correlacion media: 0.5 a 0.7
# Corrleacion baja: 0.3 a 0.5
# COrrelacion casi nula: 0.0 a 0.3
# Correlacion nula: 0.0

# Sobre nuestros datos:

# Edad y altura. Casi nula

# Edad y semestre. Media

# Edad y peso. Casi nula

# altura y semestre. Casi nula

# Altura y peso. Media

# Semestre y peso. Casi nula
