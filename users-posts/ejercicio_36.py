"""
Calcular el indicie Jaccard entre par de usuarios.
J(user1,user2) = 0 No hay similitud
J(user1,user2) = 1 Son identicos
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

nltk.download('stopwords')
w_d = os.getcwd() + os.sep + 'users-posts' +os.sep + "fb_publicaciones.csv"
df = pd.read_csv(w_d)
usuarios = list(set(df['usuario'].tolist()))

# Eliminacion de stopwords
# 1. Cargar la lista precompilada
s_w = stopwords.words('spanish')
s_w = set(s_w) # 0(1)

d_voc = {}
for user in usuarios:
  f_s = df['usuario'] == user
  posts = df[f_s]['publicacion'].tolist()
  # Limpiar el texto
  posts = [preproc_text(post, s_w) for post in posts]
  dic_posts = freq_word(posts)

  # Vocabulario para s {hombre , mujer}.
  # Conjunto de palabras única.
  voc = set(dic_posts.keys())
  d_voc[user] = voc

for user1 in usuarios:
  voc_a = d_voc[user1]
  l_jac = []
  # Calcular i_j de user1 contra todos los demas
  for user2 in usuarios:
    if user1 != user2:
      voc_b = d_voc[user2]
      i_j = jaccard(voc_a, voc_b)
      print(f'Indice JACCAR entre {user1} y {user2}: {i_j:.2f}')
      l_jac.append((i_j,user2))
  # Lista para saber el que más se le parece
  l_jac.sort(reverse=True)
  print(f'Para {user1}, los que más se parecen son:')
  for i in range(2):
    # Desempaquetar
    jac, user = l_jac[i]
    print(f'{user} con {jac:.4f}')

q = input('Dame una frase: ')
# se procesa a la frase
q = preproc_text(q, s_w)

voc_a = set(q)
l_jac = []

for user1 in usuarios:
  voc_b = d_voc[user1]
  i_j = jaccard(voc_a, voc_b)
  l_jac.append((i_j,user1))
# Lista para saber el que más se le parece
l_jac.sort(reverse=True)
jac, user = l_jac[0]
print(f'El mas similar es {user} con {jac:.4f}')

# Este es el principio basico en
# information retrieval.
# A partir de una consulta, encuentra
# los documentos mas similares (relevantes)
# a las palabra/terminos de la consulta.