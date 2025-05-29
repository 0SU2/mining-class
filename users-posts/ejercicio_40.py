'''
Crear la matriz documento-termino, con |--TIEF--|
'''


import pandas as pd
import re
import matplotlib.pylab as plt
from nltk.corpus import stopwords

def preproc_text(post,s_w):
  # Filtrando solo por letras minusculas y que sean caracteres alfanumericos
  # Obtener tokens
  post = re.findall('\w+',post.lower())
  # Filtrando que solo contenga string y no numeros con el metodo isalpha()
  post = [token for token in post if token.isalpha()]
  # Conservar solo aquellas con longitud mayor a 3 y menor a 20
  post = [token for token in post if len(token) >= 3 and len(token) <= 20 ]
  # DEJAR los tokens que no son stopwords
  # filtra que no sea una palabra vacia y sin expresion
  post = [token for token in post if token not in s_w ]
  #print(posts + '\n')
  # Quitar los acentos de las vocales que contengan
  post = [noaccent(token) for token in post]
  return post

def noaccent(word):

  # Forma 1
  vocal = {'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
  for k, v in vocal.items():
    word = word.replace(k,v)
  # Forma 2
  # replace('á','a')
  #
  #
  return word

def frecuencias(posts):
  d = {}

  for post in posts:
    for token in post:
      d[token] = d.get(token,0)+ 1

  return d

def freq_ord(d):
  lista = [(v,k) for k,v in d.items()]
  # como son tuplas, siempre ordena a partir de primer elemento en la tupla
  lista.sort(reverse=True)
  #sorted(paises.items(), key=lambda x: x[1], reverse=True)

  return lista

def jaccard(A,B):
  num = A.intersection(B)
  den = A.union(B)
  return len(num) / len(den)

def filtrado(posts,labels):
  n_posts = []
  n_labels = []

  for post,label in zip(posts,labels):
    if len(post) > 0:
      n_posts.append(post)
      n_labels.append(label)

  return n_posts, n_labels

def my_tokenizer(text):

  return text.split()

import os
i_f = os.getcwd() + os.sep + 'users-posts' +os.sep + "fb_publicaciones.csv"
df = pd.read_csv(i_f)
# 1.Leer publicaciones y convertir a lista
posts = df['publicacion'].tolist() # Lista de la columna publicacion

#-----------Eliminacion de StopWords----------
# 1.Cargar la lista pre-compilada vacia
s_w = stopwords.words('spanish')
s_w = set(s_w) # complejidad de 0 a 1

sexo = list(df['sexo'].unique())
users = df['usuario'].unique()

docs = []
for user in users:
  f_u = df['usuario'] == user
  posts = df[f_u]['publicacion'].tolist()
  posts = [preproc_text(post,s_w) for post in posts]
  posts = [' '.join(post) for post in posts]
  docs.append(' '.join(posts)) # se pierde el significado

#####---- vectorizacion de textos ----####
from sklearn.feature_extraction.text import TfidfVectorizer
# concatenando cada publicacion, separa por espacios
pubs = [' '.join(post) for post in posts]
# 1. Crear el objeto
# usamos una funcion my_tokenizer porque la funcion de defecto concidera palabras que no tienen
# significado
vectorizer = TfidfVectorizer(tokenizer=my_tokenizer)
# 2. Aprender vocabulario
# fit permite aprender el vocabulario
# fit_transform aprende el vocabulario y transforma las publicaciones
# en una matriz documento-termino
dt_matrix = vectorizer.fit_transform(docs)
#print(dt_matrix)
# obtener el vocabulario
voc = list(vectorizer.get_feature_names_out())
#print(voc)

## PIZARRON ##
'''
52 x 7732
Indice Jackar J(A,B) = [AnB] / [AuB] (creo)

D1 -> V1 1x7732    tamaño del vector 1x7732
V1 = [2,4]
V2 = [7,2]
V3 = [4,0] como tiene cero no se guarda porque es una matriz dispersa

# Calculo de la distancia con "pairwise distances"
d1(V1,V2) = sqrt((2-7)^2+(4-2)^2) = sqrt(29)
d(V1,V2) = sqrt((2-4)^2+(4-0)^2) = sqrt(20)
'''
## Medir distancia entre usuarios
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
# Calculando la matriz de distancias con pairwise_distances
# cambiando la metrica se pueden obtener resultados mas exactos
# cosine, euclidean
d_users = pairwise_distances(dt_matrix,metric='manhattan')

# Recuperando los vectores de distancia para cada usario
for i, user in enumerate(users[:4]):
    # Conocer el punto mas cercano a i:
    # Recuperando el primer vector de distancia del usuario 1
    row_i = d_users[i].copy()
    ## Obtiene el argumento minimo
    row_i[i] = np.inf # Truco para evitar que tome el cero como argumento minimo
    closest_user = np.argmin(row_i) # obteniendo el argumento minimo
    #print(f'Para {user}, el mas cercano es')
    #print(f'{users[closest_user]}')

    # Obteniendo los K=3 mas cercanos
    idx_closest_users = np.argsort(row_i) # ordena
    # Obtiene los 3 mas cercanos
    closest_3 = [users[j] for j in idx_closest_users[:3]]
    print(f'Los 3 mas cercanos para { user}\n{closest_3}')

# Transformacion
