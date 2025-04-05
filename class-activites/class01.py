l_1 = [1,2,3,4]
l_2 = []

for ele in l_1:
    l_2.append(ele**2)

l_3 = [ele**2 for ele in l_1]

n = 20
l_4 = []

for i in range(1, n+1):
    if i%2 == 0:
        l_4.append(i)

l_5 = [i for i in range(1, n+1) if i%2 == 0]

l_6 = []

for i in range(1, n+1):
    if i%2 == 0:
        l_6.append("par")
    else:
        l_6.append("impar")

l_7 = ['par' if i%2 == 0 else 'impar' for i in range(n, n+1)]

# generar una lista con numeros que sean par
# y divisibles por 7

l_8 = [ i for i in range(1, n+1) if i%2 == 0 else i%7 == 0]

# La compresion es una forma elegante de crear
# una lista.
# En algunos casso es mas rapido que en lugar
# de iterar sobre ciclos.
# Toda compresion de listas se puede llevar a
# ciclos.
# Pero no todo los ciclos se pueden llevar a
# compresion de listas.

