# Para las variables de intervalo
# - Peso
# - altura
# - Edad
# - Semestre
# Obtener una gráfica de dispersión natural, y una dispersión
# ordenada.
# Crear una función que reciba el dataFrame y el nombre de la
# varaible que se quiere analizar
import matplotlib.pyplot as plt
import pandas as pd

def resumen(df, var, o_d):
    values = df[var].to_list()

    # Dispersion
    plt.figure()
    plt.scatter(range(len(values)), values)
    plt.title(f'Dispersion natural de {var}')
    plt.savefig(o_d+f'{var}_nscatter.pdf')
    
    # Dispersion ordenada
    plt.figure()
    plt.scatter(range(len(values)), sorted(values))
    plt.title(f'Dispersion ordenada de {var}')
    plt.savefig(o_d+f'{var}_oscatter.pdf') 
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
