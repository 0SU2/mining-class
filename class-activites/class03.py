# Diccionarios, la funcion type, y los operadores
# Coleccion ordenada de pares kye, value.
# En python estan optimizados para recuperar informacion
# Las llaves no se pueden repetir, son unicas. Deben ser objectos
# no mutables.
# Los valores pueden ser cualquier tipo de objeto.
# La forma de acceder en un direccionario es a traves de las llaves.

d = {} # Diccionario vacio.
d = {1: 'uno', 2: 'dos', 3: (1,2,3), (1,1): 1, 'c': [5,6,7]}
print(d[(1,1)])

d.get('c')
print(d[1])
d.get(0)
print(d.get(0, 'hola')) # si no encuentra un valor, le especificamos a python que nos regrese un valor.
d[(1,1)] = 'hello'
d['seis'] = -6.0
# d[[1,2,3]] = 'llave mutable'
d.update({1: 'one'})
print(d)
print(len(d))
del d[1]
print(d)
d_2 = {1:1.0, 2:2.0, 3:3.0}
d_2.clear() # Deja un diccionario vacio.

# Iterar sobre un diccionario
keys = d.keys()
for key in keys:
    print(key)

values = d.values()
for value in values:
    print(value)

items = d.items()
for item in items:
    print(item)

for k, v in d.items():
    print(k,v)

d_3 = {1:{1:0, 2:1}, 'a': {'b': 'hola', 'c': 'mundo'}}

# Funcion type
print(type(d_3))

# Operadores de pertenencia
# Comprueba si un elemtno esta dentro de la coleccion
l = [1,2,3,4]
print(4 in l) # True
print('c' in l) # False
print(7 not in l) # True
print(1 not in l) # False

# Sobre diccionaris key in direccionario
print(10 in d) # False
print(1 not in d) # True
