"""
Leer las publicaciones y para cada genero calcular el numero
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

sexo = list(df['sexo'].unique())

# Multinomial
l_d_m = []
# Bernoulli
l_d_b = []
l_np = []
for s in sexo:
  # preprocesar los posts de s
  f_s = df['sexo'] == s
  posts = df[f_s]['publicacion'].tolist()
  posts = [preproc_text(post, s_w) for post in posts]
  # cuántas personas hay en s
  l_np.append(len(posts))
  # multinomial
  d_f_m = freq_word(posts)
  l_d_m.append(d_f_m)

  # bernoulli
  posts_s = [set(post) for post in posts] # set() devuelve un valor unico para que no se repita en la lista

  # podemos aplicar la frecuencia de cada palabra
  d_f_b = freq_word(posts_s)
  l_d_b.append(d_f_b)

# Calcular la frecuencia de cada
# palabra dado el género de acuerdo
# a las dos definiciones de Bayes

# Multinomial
# Vocabulario
V =  set(l_d_m[0].keys()).union(set(l_d_m[1])) # Aqui solamente se usa el primer diccionario
# Saber las probabilidades de cada genero en Multinomial
l_p_m = []
for d in l_d_m:
  # Un diccionario de palabras (palabra:prob.)
  d_p_w = {}
  for w in V:
    # Calcular las probabilidades de cada palabra
    num = d.get(w,0) # El numero de veces que aparece en el diccionario
    den = sum(d.values())
    # Probabilidad condicional
    p_c = num / den
    d_p_w[w] = p_c
  # Se va a obtener dos diccionarios
  l_p_m.append(d_p_w)

# Bernoulli
l_p_b = []
for d,n in zip(l_d_b, l_np):
  d_p_w = {} # (palabra : prob)
  for w in V:
    num = d.get(w, 0)
    den = n
    p_c = num / den
    d_p_w[w] = p_c
  l_p_b.append(d_p_w)
  # Agregar uno se le conoce como Laplace Smoothing
  # En este caso no aplicacmos aun Laplace porque los valores en estos
  # momentos todos salieron 0.0

# Con Multinomial
# Cuales son las 10 palabras
# mas probables para cada genero?
for d,s in zip(l_p_m, sexo):
  probs = [(p,w) for w,p in d.items()]
  probs.sort(reverse=True)
  print(f'\tPara el sexo {s}')
  print(f'\tLas mas probables son {probs[:10]}')

# Con Bernoulli
# Cuales son las 10 palabras
# mas probables para cada genero?
for d,s in zip(l_p_b, sexo):
  probs = [(p,w) for w,p in d.items()]
  probs.sort(reverse=True)
  print(f'\tPara el sexo {s}')
  print(f'\tLas mas probables son {probs[:10]}')


# Multinomial es mejor para textos largos, pero no tan así
# Cada uno tiene un proposito y se puede usar para casos diferentes.
# Agrupar nuestros textos en topicos que no sabiamos que existian.
# Representación
print("Done")