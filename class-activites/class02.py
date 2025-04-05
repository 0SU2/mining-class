# Una tupla es una coleccion ordenada.
# Similar a las listasm pero no es mutable.
# Al ser similares a las listas, se puede acceder
# a sus elemtnos mediante los indices.

t = () # Tupla vacia
t = (1,2,3,1.0,'s',[1,2,3],(1,1))

# Acceso mediante indices
print(t[0])
print(t[1])

print(t[:3]) # slicing regresa una subtupla

# Concatenacion
t2 = t + (6,7,8)
t3 = t2 + (5,) # la coma es necesaria, por que si no detecta la suma de una tupla mas un entero

# Slicing
# Es usado cuando queremos eliminar algunos
# elementos de la tupla.
t4 = t3[:4] + t3[7:]
print(t4)

# Si la insercion o la eliminacion de
# elementos es constate, mejor usen una lista

# Funciones utiles
print(t4.index(1.0))
t5 = t4 * 2
print(t5.count(1))

# Casting
l = [(1,1), (2,2), (3,3)]
t = ([1,2,3], [4,5,6], [7,8,9])

a = tuple(l)
b = list(t)
print(a,b)

print(len(t))

# Desempaquetamiento de tuplas
t = ('a', 'b', 'c', 'd')
v1, v2, v3, v4 = t
print(v1,v2,v3,v4)

# las tuplas son objetos iterables
for ele in a:
    print(ele)

# El acceso a los elementos es mas rapido
# que en las listas debido a que sus elementos
# no se pueden mutar.
# Mala practica es comenzar con una tupla vacia

# Conjuntos
# Son colecciones no ordenadas.
# Son mutables.
# Orden de insercion no importa. NO sabemos si
# al agregar un elemento es colcado al final
# o al inicio.
# Sus elementos son unicos.
# Son objetos iterables.
a = set() # conjunto vacio
a = {1,2,3,'a','c','d'}
print(len(a))

# en este caso python va a ignorar los casos repetidos
b = {1,1,2,3,5,6,1,2,3}

# Operaciones sobre conjunto
c = {5,6,'c','w','z'}
# En python, se regresa un nuevo conjunto
print(b.union(c)) # Union de los dos conjuntos
print(b.intersection()) # Lo que esta en ambos conjuntos
print(b.difference(c)) # Lo que esta en b, pero no en c
print(c.difference(b)) # Lo que esta en c pero no en a

# Otros metodos
a.add('hola')
a.update([1,2,3,4])
a.update((1,2,3,4))
a.update(b)
a.remove('hola')

for ele in a:
    print(ele)

# Casting se aplica cuando se requiere
# acceder a los elemenots en un orden
l = [1,2,3,4]
t = (6,7,8,9)

e = set(l)
f = set(t)

lista = list(a)
# Superar en busqueda y acceso a las listas
# y las tuplas
