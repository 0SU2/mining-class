# Funciones definidas por el usuario
# def nombre_funcion(parametros): return

def saludo(nombre):
    print(f'Hola {nombre}')
    return

saludo('Ricardo')

def saludo_v2(nombre, num):
    if num < 0:
        print(f'Hola {nombre}')
    else:
        print(f'Adios {nombre}')
    return

saludo_v2('Ricardo', 12)
def saludo_v3(nombre, num):
    if num < 0:
        return f'Hola {nombre}'
    else:
        return f'Adios {nombre}'

s = saludo_v3('Ricardo', -1)
print(s)
def saludo_v4(nombre, num):
    if num < 0:
        return f'Hola {nombre}', abs(num)
    else:
        return f'Adios {nombre}', num

t = saludo_v4('Ricardo', -12)

# Try, except
def suma(lista):
    return sum(lista)

l = [1,2,3,4,5,6]
s = suma(l)
print(s)

l = [1,2,3,4,5,'a']
try:
    res = suma(l)
except:
    print(f'Error al realizar la suma')
