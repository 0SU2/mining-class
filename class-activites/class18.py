"""
Escribir una funcion que calcule la varianza y
la desviacion estandar e imprimir el coeficiente
de variabilidad (c.v.)
"""
import matplotlib.pyplot as plt
import pandas as pd
import math as mt

def var_std(lista, media):
    var = [(x_i - media)**2 for x_i in lista]
    var = sum(var) / (len(lista)-1)

    std = var**0.5
    return var,std

def outliers(l, q1, q3):
    iqr = q3 - q1
    lif = q1 - 1.5 * iqr
    uif = q3 + 1.5 * iqr

    print(f'\tIQR :{iqr:.2f}')
    print(f'\tLIF :{lif:.2f}')
    print(f'\tUIF :{uif:.2f}')

    # Whisker inferior y superior
    for v in l:
        if  v >= lif:
            lw = v
            break

    for v in l[::-1]:
        if v <= uif:
            uw = v
            break
    
    print(f'\tWhisker inferior: {lw}')
    print(f'\tWhisker superior: {uw}')

    # Outliers
    outs = [v for v in l if v < lw or v > uw]
    print(f'\tOutliers: {outs}')
    
    return

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

def resumen(df, var, o_d,p):
    values = df[var].to_list()
    values.sort()
    
    trim_val = trimm_data(values, p)
    
    # Dispersion
    #plt.figure()
    #plt.scatter(range(len(trim_val)), values)
    #plt.title(f'Dispersion natural de {var}')
    #plt.savefig(o_d+f'{var}_trimmed_nscatter.pdf')
    
    # Dispersion ordenada
    #plt.figure()
    #plt.scatter(range(len(values)), values)
    #plt.title(f'Dispersion ordenada de {var}')
    #plt.savefig(o_d+f'{var}_std_oscatter.pdf')

    Q1 = cuartil(trim_val, 1)
    med = cuartil(trim_val, 2)
    Q3 = cuartil(trim_val, 3)

    print(f'\tValor minimo en {var}: ' + str(min(trim_val)))
    print(f'\tCuartil 1: {Q1}')
    print(f'\tCuartil 2: {med:.2f}')
    print(f'\tCuartil 3: {Q3}')
    print(f'\tValor maximo en {var}: ' + str(max(trim_val)))
    
    outliers(values, Q1, Q3)
    avg = sum(trim_val)/len(trim_val)
    print(f'\tPromedio: {avg:.2f}')
    
    var, std = var_std(trim_val,med)
    # Coeficiente
    cv = std / avg
    print(f'\tVarianza: {var:.2f}')
    print(f'\tDevisacion estandar: {std:.2f}')
    print(f'\tC.F: {cv:.2f}')

    # Boxplot
    plt.figure()
    if != 0:
        plt.boxplot([values, trim_val], labels=['Completos', 'Recortados'])
        # plt.xticks([1,2], labels=['Completos', 'Recortados'])
    else:
        plt.boxplot(trim_val, labels=['Completos', 'Recortados'])

    plt.title(f'Boxplot de {var}')
    # plt.savefig(o_d+f'{var}_std_boxplot.pdf')
    return

w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

#l_v = ['edad']
l_v = ['peso', 'altura', 'edad', 'semestre']

for v in l_v:
    print('*'*10)
    print(f'Para la variable {v}')
    print('*'*10)
    print('Datos completos')
    resumen(df,v, w_d, 0)
    print('*'*10)
    print('Datos recortados')
    resumen(df,v, w_d, 10)
    print('\n')    
    
# Para que la meida y la mediana sirvan
# como medidas de tencencia general, sus
# valores tiene que ser similares, la
# desviacion estandarbaja, y por lo tanto el
# coeficiente de variabilidad tiene que ser bajo.

# Si se cumple lo anterior,ambas represetan
#  el valor tipico (esperado) dentro de lamuestra o poblacion

# Reporten media, mediana, desviacion estandar (en ese orden).

# La desivaicon estandar me permite saber
# la dispersion de los datos con respecto
# a la media...

# Si cv >= 0.3... Std es muy grande
# Si cv <= 0.15 y cv < 0.3... Std es grande
# Si cv < 0.15... Std es baja

