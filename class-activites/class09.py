## Variables dominables
## Leer archivo csv y para la variable sexo, calcular las frecuencias de cada valor (hm) y su porcentaje
import pandas as pd

w_d = '/home/ren01/Downloads/'
i_f = w_d + 'info_estudiantes.csv'

df = pd.read_csv(i_f)
freq = df['sexo'].to_list()
count_h = freq.count('h')
count_m = freq.count('m')

print(f'Hombres: {count_h/len(freq)*100}')
print(f'Mujeres: {count_m/len(freq)*100}')

# Segunda forma 
# para mas de dos valores?
d_f = {}
for key in freq:
    d_f[key] = df.get(key,0) + 1
    # El metodo get busca el valor asociado
    # a key, si la llave no existe regresa 0
    # - Si la llave no existe regresa 0
    # - Si la llave existe regresa el valor asociado.
print('Con diccionarios...')
for k, v in d_f.items():
    print(f'{k}: {v}, {v/sum(d_f.values())*100}')
