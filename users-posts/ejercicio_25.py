"""
Utilizando el resultado del ejercicio previo:
La lista de tokens por publicacion

1. Filtrar los tokens para dejar aquellos
que estén compuestos solo de letras
"""
import pandas as pd
import re
import os
w_d = os.getcwd() + os.sep + "fb_publicaciones.csv"
df = pd.read_csv(w_d)
posts = df['publicacion'].tolist()

posts_tk_v3 = [re.findall('\w+', post.lower()) for post in posts]

posts_2 = [[token for token in post if token.isalpha()] for post in posts]
# posts_2 = []
# for post in posts_tk_v3:
#   temp = []
#   for token in post:
#     if token.isalpha():
#       temp.append(token)
#   # cuando termine de guardar todos los tokens de letras solamente,
#   # guardar todo
#   posts_2.append(temp)
