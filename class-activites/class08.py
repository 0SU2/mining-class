# Uso general de Pandas.
import pandas as pd
# DataFrame, es compo manejar una tabla
w_d = '/home/ren01/programming/pyton/'
i_f = w_d + 'test.csv'
df = pd.read_csv(i_f)

print(df.columns)
lista = df['V1']
lista = df['V1'].to_list()
