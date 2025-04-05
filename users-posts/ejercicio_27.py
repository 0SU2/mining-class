"""
Utilizando el resultado del ejercicio previo.
Filtrar las publicaciones descartando las palabras
vacías (stopwords)
"""
from nltk.corpus import stopwords
import pandas as pd
import re
import os
import nltk
nltk.download('stopwords')
w_d = os.getcwd() + os.sep + "fb_publicaciones.csv"
df = pd.read_csv(w_d)
posts = df['publicacion'].tolist()

posts = [re.findall('\w+', post.lower()) for post in posts]

# Conservar aquellos compuestos solo por letras
posts = [[token for token in post if token.isalpha()] for post in posts]

# Conservar aquello con longitud entre 3 y 20 caracteres
posts = [[token for token in post if len(token) >=3 and len(token) <= 20] for post in posts]

# Eliminacion de stopwords
# 1. Cargar la lista precompilada
s_w = stopwords.words('spanish')
s_w = set(s_w) # 0(1)

posts = [[token for token in post if token not in s_w] for post in posts]
# se eliminan palabras repetidas
# set(post) es un conjunto y un conjunto no tiene elementos repetidosd
# post_v2 = [list(set(post).difference(s_w)) for post in posts]