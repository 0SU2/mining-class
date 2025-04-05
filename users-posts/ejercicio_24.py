"""
1. Convertilas en lista.
2. Transformar cada linea de publicacion en minusculas
3. separar cada linea de publicaciones
en tokens:
  a) Utilizando espacios
"""
import pandas as pd
import os
# Retriving results from csv file
w_d = os.getcwd() + os.sep + "fb_publicaciones.csv"
df = pd.read_csv(w_d)
posts = df['publicacion'].tolist()
posts_l = [pub.lower().split(' ') for pub in posts]

# post_tk = [pub.split(' ') for pub in posts_l]
# for pub in posts_l:
#   temp = pub.split(' ')
#   post_tk.append(temp)

# Modulo regex
import re
posts_tk_v3 = [re.findall('\w+', post.lower()) for post in posts]
print(posts_tk_v3)
# for post in posts:
#   post = post.lower()
#   tokens = re.findall('\w+', post)
#   posts_tk_v3.append(tokens)