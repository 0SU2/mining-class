# Funciones integradas
# No requieren de importar algun modulo externo

a = -1.0
abs(a)

l = [2,4,1,4,5,6]
print(min(l))
print(max(l))

l_c = ['b', 'c', 'e', 'a']
print(max(l_c))
print(min(l_c))

# Suma
# Solo se puede aplicar sobre colecciones numericas
# sum(l_c) # ERROR
sum(l)

# Sorted. Util cuando no queremos modificar el objeto
# original
l_o = sorted(l, reverse=True)
print(l_o)

# Enumerate. Enumerar elementos de una coleccion
# Regresa uan tupla(i, val)
for t in enumerate(l_c):
    print(t)

for n,v in enumerate(l_c):
    print(n,v)

l_min = ( len (l_c) if len(l_c) < len(l) else len(l_l) )

for i in range(l_min):
    print(l[i], l_c[i])

# Zip. Se detendrade acuerdo a lista con el menor
# numero de objetos
l_3 = [0.1,0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
for t in zip(l, l_c, l_3):
    print(t)

for v1,v2,v3 in zip(l, l_c, l_3):
    print(v1,v2,v3)    
