"""
Hacer una funcion que calcule la correlacion Punto-Biseral
entre una variable categoricaa y una variable numerica.
Utilizar la funcion para caluclar la correlacion entre el genero
y las variables numericas
- Edad
- Peso
- Estatura
- Semestre
"""
import pandas as pd

def std(var):
    return

def pb_corr(var_1,var_2,l):
    # lab = [grupo_1, grupo_0]
    
    # Comprobar si las frecuencias
    # en var_1 (variable binaria)
    # estan balanceadas.
    # Esto simplifica el calculo de r_pb
    ###

    n_0, n_1, s_0 = s_1 = 0
    for i, j in zip(var_1,var_2):
        if i==lab[0]:
            # grupo 1
            s_1 += j
            n_1 += 1
        else:
            # grupo 0
            s_0 += j
            n_0 += 1
    m_0 = s_0 / n_0
    m_1 = s+1 / n_1

    n =n_1 + n_0

    s_y = std(var_2)

    return

w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

sexo = df['sexo'].to_list()
l_v = ['edad', 'peso', 'semestre', 'altura']

for var  in l_v:
    var_2 = dv[var].tolist()
    r_pb = pb_corr(sexo,var_2, ['h','m']) # Suponiendo que sabemos los sexos
    print(f'Correlacion Punto-Biseral)
