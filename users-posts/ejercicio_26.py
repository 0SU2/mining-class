"""
Utilizando el resultado del ejercicio previo. Quitar
aquellos tokens que sean muy cortos o muy largos.

Muy cortos: longitud < 3
muy largos : longitud > 20
"""
import pandas as pd
import re
import os
w_d = os.getcwd() + os.sep + "fb_publicaciones.csv"
df = pd.read_csv(w_d)
posts = df['publicacion'].tolist()

posts_tk_v3 = [re.findall('\w+', post.lower()) for post in posts]

# Conservar aquellos compuestos solo por letras
posts_2 = [[token for token in post if token.isalpha()] for post in posts]

# Conservar aquello con longitud entre 3 y 20 caracteres
posts_3 = [[token for token in post if len(token) >=3 and len(token) <= 20] for post in posts]