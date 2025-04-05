"""
@Descripcion: Hacer una funcion que calcule el coeficiente
              de Pearson para dos variables. Pasar como
              parametros las listas de los
              valores de cada variable.
"""
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

edades = df['edad'].tolist()
semestre = df['semestre'].tolist()

r = coef_pearson(edades, semestre)
print(r)
