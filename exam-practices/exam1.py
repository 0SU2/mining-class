import pandas as pd
import os
w_d = os.getcwd() + os.sep
curretDirs = os.listdir()

for readDirs in curretDirs:
    enterDir = w_d + readDirs
    os.chdir(enterDir)
    listFiles = os.listdir()
    try:
        filePub = listFiles.index('fb_publicaciones.csv')
        filePub = listFiles[filePub]
        break
    except ValueError:
        continue

w_d = enterDir + os.sep + filePub
df = pd.read_csv(w_d)

user_l = df['publicacion'].to_list()
user_s = df['sexo'].to_list()

# tokens
import re
posts = [ post.lower().split(' ') for post in user_l]
tokens_post = [re.findall('\w+', post.lower()) for post in user_l]

# users
all_user_s = {}
for sexo in user_s:
    all_user_s[sexo] = all_user_s.get(sexo, 0) + 1
print(all_user_s)