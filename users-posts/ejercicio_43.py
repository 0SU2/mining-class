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

# Eliminacion de stopwords
# 1. Cargar la lista precompilada
s_w = stopwords.words('spanish')
s_w = set(s_w) # 0(1)

# Etiquetas/labels
sexo = df['sexo'].tolist()

# Publicaciones/documentos
posts = df['publicacion'].tolist()
posts = [preproc_text(post,s_w)
         for post in posts]
# Tokenizador
docs = [' '.join(post) for post in posts]

# Transformacion matriz documento-termino
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB
import numpy as np
# Metricas
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors  import NearestCentroid
# 1. Crear el objeto
vectorizer = TfidfVectorizer(tokenizer=my_tokenizer, norm='l2')

dt_matrix = vectorizer.fit_transform(docs)
# dt_matrix = vectorizer.fit_transform(df['publicacion'].tolist())
voc = list(vectorizer.get_feature_names_out())

#  Deividr el conjunto de datos
from sklearn.model_selection import train_test_split
docs_tr, docs_tst, lab_tr, lab_tst = train_test_split(dt_matrix, sexo,
                                                      test_size=0.20,
                                                      stratify=sexo,
                                                      random_state=0)

# Entrenar el clasificador
clf = BernoulliNB()
clf.fit(docs_tr, lab_tr)

# Evaluar clasificador
predicted = clf.predict(docs_tst)

# Media desempeño
# Exactitud/Accuracy
acc = accuracy_score(lab_tst, predicted)
clf_perf = classification_report(lab_tst, predicted)
print(f'Voc: {len(vectorizer.get_feature_names_out())}')

# Corrigiendo la fuga de informacion
# Primero dividir los documentos (no transformados)
docs_tr, docs_tst, lab_tr, lab_tst = train_test_split(docs, sexo, test_size=0.20, stratify=sexo, random_state=0)

# Transformacion de los documentos
vectorizer = TfidfVectorizer(tokenizer=my_tokenizer, norm='l2')

# Documentos entrenamiento
dt_m_tr = vectorizer.fit_transform(docs_tr)

# Docs de prueba
dt_m_tst = vectorizer.transform(docs_tst)

# Entrenar el clasificador
clf = BernoulliNB()
clf.fit(dt_m_tr, lab_tr)

# Evaluar clasificador
predicted = clf.predict(dt_m_tst)

# Media desempeño
# Exactitud/Accuracy
acc = accuracy_score(lab_tst, predicted)
clf_perf = classification_report(lab_tst, predicted)
print(f'Voc: {len(vectorizer.get_feature_names_out())}')

# Centroides
clf_1 = NearestCentroid()
clf_1.fit(dt_m_tr, lab_tr)

predicted = clf_1.predict(dt_m_tst)

acc = accuracy_score(lab_tst, predicted)
clf_perf = classification_report(lab_tst, predicted)