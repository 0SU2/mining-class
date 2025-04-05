# Numeros aleatorios
# Se requiere de un modulo externo
import random as rn

print(rn.random()) # Genera un valor aleatorio entre [0,1.0)
            # No toma en cuenta el 1.0
print(rn.uniform(2.0,3.3))

# Establecer la semilla
rn.seed('as')
rn.seed(1)
rn.seed(1.0)

rn.random()
rn.randint(1,100)

l = ['a', 'b', 'c', 'd']
print(rn.choice(l))
print(rn.choices(l, k=3))
rn.sample(l, k=3))
s = 'murcielago'
rn.choice(s)
rn.choices(s,k=3)
rn.sample(s,k=4)
