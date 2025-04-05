# Manejo de archivos
w_d = '/home/ren01/programming/pyton/'
i_f = w_d + 'test.csv'

# DIferentes modos:
l = [1,2,3,4,'a']
with open(i_f, 'w', encoding='utf-8') as file:
    for _ in range(5):
        file.write(','.join(str(ele) for ele in l) + '\n')

txt = []
with open(i_f, 'r', encoding='utf-8') as file:
    text = file.read()

text = []
with open(i_f, 'r', encoding='utf-8') as file:
    for line in file:
        text.append(line)

# Eliminar whitespaces o \n\t\r
with open(i_f, 'r', encoding='utf-8') as file:
    for line in file:
        text.append(line.strip())

# Leer un csv
with open(i_f, 'r', encoding='utf-8') as file:
    for line in file:
        text.append(line.strip().slip(','))
