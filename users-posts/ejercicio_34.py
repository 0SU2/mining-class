
"""

"""
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import nltk

def create_plot_freq(lista:list, label:str):
  l_l = []
  l_f = []
  for f,w in lista:
    l_l.append(w)
    l_f.append(f)

  plt.figure()
  plt.bar(l_l, l_f)
  plt.title(f'{label}')
  plt.xticks(rotation=90)
  plt.savefig(f'./pdf-tests/{label}_plot.pdf')
  return

def freq_ord(d:dict):
  lista = [(v,k) for k,v in d.items()]
  lista.sort(reverse=True)
  return lista

def freq_word(posts):
  d_f = {}
  for post in posts:
    for token in post:
      d_f[token] = d_f.get(token,0) + 1
  return d_f

def noaccent(word):
  d = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
  for k, v in d.items():
    word = word.replace(k, v)

  return word

def preproc_text(post, s_w):
  # Obtener tokens (palabras)
  post = re.findall('\w+', post.lower())
  # SOlo secuencias de letras
  post = [token for token in post if token.isalpha()]
  # Conservar aquello con longitud entre 3 y 20 caracteres
  post = [token for token in post if len(token) >=3 and len(token) <= 20]
  # Descartar palabras vacias
  post = [token for token in post if token not in s_w]
  # Sustitur acentos
  post = [noaccent(token) for token in post]
  return post

nltk.download('stopwords')
w_d = os.getcwd() + os.sep + 'users-posts' +os.sep + "fb_publicaciones.csv"
df = pd.read_csv(w_d)
sexo = set(df['sexo'].tolist())

# Eliminacion de stopwords
# 1. Cargar la lista precompilada
s_w = stopwords.words('spanish')
s_w = set(s_w) # 0(1)

d_voc = {}
for s in sexo:
  filtro_s = df['sexo'] == s
  posts = df[filtro_s]['publicacion'].tolist()
  # Limpiar el texto
  posts = [preproc_text(post, s_w) for post in posts]
  dic_posts = freq_word(posts)
  list_freq = freq_ord(dic_posts)
  create_plot_freq(list_freq[:20], s)

  # Vocabulario para s {hombre , mujer}.
  # Conjunto de palabras única.
  voc = set(dic_posts.keys())
  d_voc[s] = voc

# Interseccion de las palabras que usan hombres y mujeres
inter = d_voc['hombre'].intersection(d_voc['mujer'])
h_diff = d_voc['hombre'].difference(d_voc['mujer'])
m_diff = d_voc['mujer'].difference(d_voc['hombre'])
print(f'Palabras que solo usan los hombre: {h_diff}')
print(f'Palabras que solo usan los hombre: {len(h_diff)}')
print(f'Palabras que solo usan las mujeres: {m_diff}')
print(f'Palabras que solo usan las mujeres: {len(m_diff)}')