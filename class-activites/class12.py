# Para las variables nominales: Sexo, mascota, consola y para la variable
# - Imprimir los porcentajes en orden descendete
#- Hacer una gráfica de pastel
# - Hace una gráfica de barras
# Para la variable peso, calcular la frecuencia
# y porcentajes en los rangoes [0-50], [50-60],
# [60-70], [70-80], [80+]
import pandas as pd
import matplotlib.pyplot  as plt
w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'

def resumen(df, var):
    # 1. Calcular frecuencias y variables
    freq = df[var].to_list()

    d_f = {}
    for key in freq:
        if type(key) == str:
            tokens = key.split('/')
        else: # Para tipos no string
            tokens = [key]

        if var!= 'peso':
            for token in tokens:
                d_f[token] = d_f.get(token,0) + 1

        else:
            if key >= 0 and key <= 49:
                d_f['[0-49]'] = d_f.get('[0-49]', 0) + 1
            elif key >= 50 and key <= 59:
                d_f['[50-59]'] = d_f.get('[50-59]', 0) + 1
            elif key >= 60 and key <= 69:
                d_f['[60-69]'] = d_f.get('[60-69]', 0) + 1
            elif key >= 70 and key <= 79:
                d_f['[70-79]'] = d_f.get('[70-79]', 0) + 1
            elif key >= 80:
                d_f['[80+]'] = d_f.get('[80+]', 0) + 1
        
    l_p = []
    total = sum(d_f.values())
    for k,v in d_f.items():
        l_p.append((v/total * 100, v, k))
        # (porcentaje, freq, categorias)
    l_p.sort(reverse=True)
    
    # 2. Imprimir los valores
    l_l = []
    l_f = []
    for t in l_p:
        print(f'{t[2]}: {t[1]} -> {t[0]:.2f}')
        # Frecuencias
        l_f.append(t[1])
        l_l.append(t[-1])

    # 3. Las graficas de pastel y de barras
    # 1. Lienzo en blanco
    plt.figure()
    # 2. Tipo de grafico
    plt.pie(l_f, labels=l_l)
    plt.title(var)
    plt.savefig(w_d+var+'_'+'pastel.pdf', dpi=600)
    # 3. Poner un titulo y nombre a ejes
    plt.figure()
    plt.bar(l_l, l_f) # Primero lo que va sobre 
    plt.title(var)
    plt.xlabel('Categoria')
    plt.ylabel('Frecuencia')
    plt.savefig(w_d+var+'_'+'barras.pdf', dpi=600)    
    return

df = pd.read_csv(i_f)
l_v = ['peso']
for v in l_v:
    print('*'*10)
    print(f'Para la variable {v}')
    resumen(df,v)
    print('*'*10)
    print('\n')
