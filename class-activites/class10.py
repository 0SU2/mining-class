# Para la variable sexo, calcular las frecuencias y porcentajes de cada valor.
# Imprimir los resultados en orden descendente.
# Crear un grafico de pastel y uno de barras.
import pandas as pd
import matplotlib.pyplot  as plt
w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'

df = pd.read_csv(i_f)
freq = df['sexo'].to_list()

d_f = {}
for key in freq:
    d_f[key] = df.get(key,0) + 1

# lista.sort(reverse=True)
l_p = []
total = sum(d_f.values())
for k,v in d_f.items():
    l_p.append((v/total * 100, v, k))
    # (porcentaje, freq, categorias)

l_p.sort(reverse=True)
l_l = []
l_f = []
for t in l_p:
    print(f'{t[2]}: {t[1]} -> {t[0]}')
    # Frecuencias
    l_f.append(t[1])
    l_l.append(t[-1])

# La secuencia para crear graficos
# 1. Lienzo en blanco
plt.figure()
# 2. Tipo de grafico
plt.pie(l_f, labels=l_l)
# 3. Poner un titulo y nombre a ejes
plt.title('Sexo')
plt.show()
# 4. Exportar la figura
# plt.savefig(w_d+'pastel.pdf', dpi=600)
# plt.bar(l_l, l_f) # Primero lo que va sobre x,
                    # despues lo de y.
# plt.title('Sexo')
# plt.xlabel('Categoria')
# plt.ylabel('Frecuencia')
# plt.savefig(w_d+'barras.pdf', dpi=600)

#####
# En análisis de datos hay dos partes principales:
# 1. Los cálculos, que permiten encontrar asociaciones
# dispersión de los datos, estadísticas, encontrar
# patrones...
# 2. La interpretación, el resumen, el reporte
# una aplicación externa. Esto últimose encía a la
# persona encargada de la toma de decisiones.

# En la interpretación podemos inlcuir
# hipótesis o especulaciones para tratar
# de explicar los datos...

# ¿Por qué tenemos frecuencias similares?
# 1. Las ingenerías tiene más hombre, pero
# las demás carreras tienen más mujeres.
# 2. El diseño de la recopilación pedía
# un equilibrio entre hombres y mujeres.
# 3. Una mala captura de datos.

# La hipótesis más sostenible es la segunda
# Para la tercera requerimos mayor información de la
# recopilación.
# Para la primera requerimos de un muestreo más
# grande.
