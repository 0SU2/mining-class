# Para las variables de intervalo
# - Peso
# - altura
# - Edad
# - Semestre
# Obtener una gráfica de dispersión natural, y una dispersión
# ordenada.
# Imprimir el valor mínimo y el máximo.
# Hacer una función que reciba una lista de valores ordenados y un
# cuartil, y devuelva el valor para ese cuartil en los datos.
# Crear una función que reciba el dataFrame y el nombre de la
# varaible que se quiere analizar.
import matplotlib.pyplot as plt
import pandas as pd

def cuartil(l_v, q):
    # Posicion en la lista
    p_q = (q*(len(l_v) - 1)) / 4

    # Parte entera que nos dice cual
    # elemento tomar
    idx = int(p_q)

    # Valor que nos permite hacer una
    # interpolacion lineal
    dec = p_q%1

    # Valor del cuartil q
    v_q = l_v[idx] + dec * (l_v[idx+1] - l_v[idx])

    return v_q

def resumen(df, var, o_d):
    values = df[var].to_list()
    
    # Dispersion
    plt.figure()
    plt.scatter(range(len(values)), values)
    plt.title(f'Dispersion natural de {var}')
    plt.savefig(o_d+f'{var}_nscatter.pdf')
    
    # Dispersion ordenada
    l_o = sorted(values)
    plt.figure()
    plt.scatter(range(len(values)), l_o)
    plt.title(f'Dispersion ordenada de {var}')
    plt.savefig(o_d+f'{var}_oscatter.pdf')

    print(f'\tValor minimo en {var}: ' + str(min(values)))
    print(f'\tCuartil 1: {cuartil(l_o, 1)}')
    print(f'\tCuartil 2: {cuartil(l_o, 2)}')
    print(f'\tCuartil 3: {cuartil(l_o, 3)}')
    print(f'\tValor maximo en {var}: ' + str(max(values)))

    # Boxplot
    plt.figure()
    plt.boxplot(l_o)
    plt.title(f'Boxplot de {var}')
    plt.savefig(o_d+f'{var}_boxplot.pdf')
    return

w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

l_v = ['peso', 'altura', 'edad', 'semestre']

for v in l_v:
    print('*'*10)
    print(f'Para la variable {v}')
    resumen(df,v, w_d)
    print('*'*10)
    print('\n')
