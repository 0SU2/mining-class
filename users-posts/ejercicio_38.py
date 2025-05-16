"""
Leer las publicaciones y
generar la matriz documento-término
correspondiente. Un documento es
una publicación.
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

def jaccard(a,b):
  num = a.intersection(b)
  den = a.union(b)
  return len(num)/len(den)

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

def filtrado(posts, labels):
  n_posts = []
  n_labels = []

  for post, label in zip(posts, labels):
    if len(post) > 0:
      n_posts.append(post)
      n_labels.append(label)

  return n_posts, n_labels

def my_tokenizer(text):
  return text.split()

nltk.download('stopwords')
w_d = os.getcwd() + os.sep + 'users-posts' +os.sep + "fb_publicaciones.csv"
df = pd.read_csv(w_d)
usuarios = list(set(df['usuario'].tolist()))

# Eliminacion de stopwords
# 1. Cargar la lista precompilada
s_w = stopwords.words('spanish')
s_w = set(s_w) # 0(1)

sexo = list(df['sexo'].unique())
posts = df['publicacion'].tolist()
labels = df['sexo'].tolist()

posts = [preproc_text(post, s_w)
         for post in posts]
# Filtrar
posts, labels = filtrado(posts, labels)
# Cuando se va a filtrar información, debemos tener la misma canntidad en las
# listas.

# Vocabulario
V =  [t for post in posts for t in post]
V = set(V)

# # Método costoso
# dt_m_cost = []
# for post in posts:
#   # nos vamos por cada publicacion
#   vector = []
#   for w in V:
#     # Por cada palabra en cada publicación
#     vector.append(post.count(w))
#   dt_m_cost.append(vector)

# Método 2. Manejando la dispersión
# mediante diccionarios
V_s = sorted(list(V))
idx_voc = {w:i for i,w in enumerate(V_s)}
dt_m_d = []
for post in posts:
  vector = {}
  for w in post:
    # Solo iterar por la palabras que contiene mi publicacion
    idx = idx_voc[w]
    # Obtienes la frecuencia de la palabra en la lista
    vector[idx] = vector.get(idx,0) + 1
  # Agregamos la frecuencia a nuestra matriz
  dt_m_d.append(vector)

# Módulo Scikit-learn (sklearn)
# Método CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
pubs = [' '.join(post) for post in posts]

# 1. Crear el objeto
vectorizer = CountVectorizer(tokenizer=my_tokenizer)
# vectorizer = CountVectorizer()
# 2. Aprender el vocabulario
# . fit(pubs) solo aprende el vocabulario
# .fit_transform(pubs) aprende el vocabulario
# y transforma pubs en una matriz
# documento-termino
dt_matrix = vectorizer.fit_transform(pubs)
# dt_matrix = vectorizer.fit_transform(df['publicacion'].tolist())


# Recuperar vocabulario
voc = list(vectorizer.get_feature_names_out())
print(dt_matrix)