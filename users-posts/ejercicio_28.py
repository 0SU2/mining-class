"""
Convertir caracteres acentuados
(vocales) por no acentuados

word = 'dias'
word_2 = noaccent(word)
word_2 -> 'dias'
"""
from nltk.corpus import stopwords
import pandas as pd
import re
import os
import nltk
def noaccent(word):
  d = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
  for k, v in d.items():
    word = word.replace(k, v)
  return word

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
# Sustitur acentos
posts = [[noaccent(token) for token in post] for post in posts]