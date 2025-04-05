"""
Para las variables de intervalo/razón
[edad, estatura, peso, semestre]

1. Hacer una función que reciba como parámetros
una lista de valores ordenada y un cuartil,
y devuelva el valor para ese cuartil en los
datos.

2. Hacer una función que recia como parámetros
un dataFrame y el numbre de la variable a
analizar, y que imprima el resumen de los
cinco números (fie number summary), y
grafique el diagrama de caja (boxplot) correspondiente.

3. Hacer una función que tome una lista de valores
ordenada, el Q1 y el Q3. La función debe calcular e
imprimir el IQR, LIF, UIF, el whisker inferior, el whisker
superior y los valores atípicos.

4. Calcular el promedio dentro de la funcion
resumen

5. Hacer una función para recortar los datos originales a un %p (definir
p en el código, de forma inicial 10%)
"""
import matplotlib.pyplot as plt
import pandas as pd

def trimm_data(datos, p):
    # Sobre los datos ordenados
    # Calcular k
    n = len(datos)
    k = int((p*n)/100)

    return datos[k:n-k]

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

def resumen(df, var, o_d):
    values = df[var].to_list()
    values.sort()
    
    trim_val = trimm_data(values, 10)
    
    # Dispersion
    #plt.figure()
    #plt.scatter(range(len(trim_val)), values)
    #plt.title(f'Dispersion natural de {var}')
    #plt.savefig(o_d+f'{var}_trimmed_nscatter.pdf')
    
    # Dispersion ordenada
    plt.figure()
    plt.scatter(range(len(trim_val)), trim_val)
    plt.title(f'Dispersion ordenada de {var}')
    plt.savefig(o_d+f'{var}_trimmed_oscatter.pdf')

    Q1 = cuartil(trim_val, 1)
    med = cuartil(trim_val, 2)
    Q3 = cuartil(trim_val, 3)

    print(f'\tValor minimo en {var}: ' + str(min(trim_val)))
    print(f'\tCuartil 1: {Q1}')
    print(f'\tCuartil 2: {med:.2f}')
    print(f'\tCuartil 3: {Q3}')
    print(f'\tValor maximo en {var}: ' + str(max(trim_val)))
    outliers(trim_val, Q1, Q3)
    m_a = sum(trim_val)/len(trim_val)
    print(f'\tMedia: {m_a:.2f}')

    # Boxplot
    plt.figure()
    plt.boxplot(trim_val)
    plt.title(f'Boxplot de {var}')
    plt.savefig(o_d+f'{var}_trimmed_boxplot.pdf')
    return

w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'
df = pd.read_csv(i_f)

#l_v = ['edad']
l_v = ['peso', 'altura', 'edad', 'semestre']

for v in l_v:
    print('*'*10)
    print('Datos Recortados')
    print(f'Para la variable {v}')
    resumen(df,v, w_d)
    print('*'*10)
    print('\n')

# Una vez recortados los datos...
# La media se modifiva, y se vuelve más
# adecuada para representar los datos...
# La media se convierte en una mejor
# media de centralidad (y la centralidad
# de los datos...)

# No hay un porcentaje que sea mejor a
# otros para recortar los datos. Este
# porcentaje dependerá de la distribución
# original.

# Algunas otras métricas se modificaron
# pero su cambio es leve.

# La media y la mediana son metricas de
# tendica central. El objetivo es tener un
# solonumero que resuma de manera
# general los datos.
