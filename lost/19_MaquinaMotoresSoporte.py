'''
Aplicar el clasificador de centroides (rocchio) sobre las publicaciones recolectadas



'''
import os
import pandas as pd 
import re
import matplotlib.pylab as plt
from nltk.corpus import stopwords
from sklearn.neighbors import NearestCentroid

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
w_d = os.getcwd() + os.sep + 'lost' + os.sep
i_f = w_d + 'fb_publicaciones.csv'
df = pd.read_csv(i_f)
# 1.Leer publicaciones y convertir a lista
posts = df['publicacion'].tolist() # Lista de la columna publicacion 
#-----------Eliminacion de StopWords----------
# 1.Cargar la lista pre-compilada vacia 
s_w = stopwords.words('spanish')
s_w = set(s_w) # complejidad de 0 a 1
# etiquetas
sexo = df['sexo'].tolist() # Etiqueta a predecir 
# Para entrenar un clasificador se requiere 
# tener una matriz publicaciones x features 
# tener un vector de clases/categorias en este caso sexo 

# Publicaciones
posts = df['publicacion'].tolist()
# Preprocesando el texto
posts = [preproc_text(post,s_w) for post in posts ]

# concatenando cada publicacion, separa por espacios 
docs = [''.join(post) for post in posts]
#####---- vectorizacion de textos ----####
from sklearn.feature_extraction.text import TfidfVectorizer
# 1. Crear el objeto
# usamos una funcion my_tokenizer porque la funcion de defecto concidera palabras que no tienen
# significado 
vectorizer = TfidfVectorizer(tokenizer=my_tokenizer,norm='l2', token_pattern=None)
# 2. Aprender vocabulario 
# fit permite aprender el vocabulario 
# fit_transform aprende el vocabulario y transforma las publicaciones 
# en una matriz documento-termino 
dt_matrix = vectorizer.fit_transform(docs)
# obtener el vocabulario 
voc = list(vectorizer.get_feature_names_out())

## Dividir el conjunto de datos (publicaciones)
from sklearn.model_selection import train_test_split
# stratify permite que las pruebas y entrenamiento no esten desvalandeadas 

docs_train, docs_test, lab_train,lab_test = train_test_split(dt_matrix,sexo,test_size=0.20,stratify=sexo,random_state=0)

# Clasificador  
from sklearn.naive_bayes import BernoulliNB, MultinomialNB, ComplementNB
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
# Entrenar clasificador con fuga de informacion 
# Entrenar sin fuga de informacion 
print(f'Corrigiendo la fuga de informacion')
# Primero dividir los documentos no transformados 

docs_train, docs_test, lab_train,lab_test = train_test_split(docs,sexo,test_size=0.20, stratify=sexo,random_state=0)
# transformoacion de los documentos
vectorizer = TfidfVectorizer(tokenizer=my_tokenizer,norm='l2', token_pattern=None)
# documentos de entrenamiento 
dt_matrix_tr = vectorizer.fit_transform(docs_train)
# documentos de prueba 
dt_matrix_test = vectorizer.transform(docs_test)

# CENTROIDEEEEEEES
clf_1 = NearestCentroid()
#Entrenar clasificador 
clf_1.fit(dt_matrix_tr,lab_train)
# Evaluar clasificador 
# Medir desempeño 
predicted = clf_1.predict(dt_matrix_test)
# Medir desempeño 
# Exactitud/Accuracy
acc = accuracy_score(lab_test,predicted)
clf_perf = classification_report(lab_test,predicted)
print(F'Accuracy {acc}')
print(clf_perf)
# Entrenar sin fuga de informacion 
print(f'Corrigiendo la fuga de informacion')
# Primero dividir los documentos no transformados 

docs_train, docs_test, lab_train,lab_test = train_test_split(docs,sexo,test_size=0.20, stratify=sexo,random_state=42)
# transformoacion de los documentos
vectorizer = TfidfVectorizer(tokenizer=my_tokenizer,norm='l2', token_pattern=None)
# documentos de entrenamiento 
dt_matrix_tr = vectorizer.fit_transform(docs_train)
# documentos de prueba 
dt_matrix_test = vectorizer.transform(docs_test)
