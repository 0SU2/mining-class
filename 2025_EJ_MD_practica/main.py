import pandas as pd
import matplotlib.pyplot as plt
import os

def cuartil(paises_selc:list,q:int):
  """!
  @brief Busca el valor del cuartil que se le especifica

  @param paises_selc: Lista a buscar el valor del cuartil
  @param q: Numero de cuartil

  @return: Cuartil
  """
  # Definir la posicion
  p_q = (q*(len(paises_selc) -1 )) / 4
  # Elemento a tomar
  idx = int(p_q)
  # Interpolacion
  dec = p_q%1
  # Valor del cuartil
  v_q = paises_selc[idx] + dec * (paises_selc[idx+1] - paises_selc[idx])
  return int(v_q)

def salario_anual(paises_list: list, salarios_list):
  print(paises_list)
  print(salarios_list)
  return

def most_countries(paises_cv:list):
  # Función para encontrar los 10 países con más respuestas

  # Con un objeto vamos a ir guardando las frecuencias como vaya leyendo el
  # archivo csv que le entreamos
  d_f = {}
  for index in paises_cv:
    d_f[index] = d_f.get(index, 0) + 1

  l_p = []
  total = sum(d_f.values())
  for k, v in d_f.items():
    l_p.append((v/total * 100, k, v))

  l_p.sort(reverse=True)
  l_l = []
  l_f = []
  index = 0
  for list in l_p:
    index+=1
    if list[1] == 'Mexico':
      # Debe encontrar a Mexico y terminar el ciclo
      l_l.append(list[1])
      l_f.append(list[-1])
      break
    elif index <= 10:
      # Caso de no encontrar mexico pero esta
      # recolectando los datos de los 10 paises con
      # mas respuestas
      l_l.append(list[1])
      l_f.append(list[-1])

  # Crear grafico de barras
  plt.figure(figsize=(10,7))
  plt.bar(l_l, l_f, width=0.5)
  plt.title('Paises con más respuestas y México')
  plt.tick_params('x', labelsize=8, rotation=70)
  plt.savefig('./barras_paises.pdf', dpi=600)

  # Seleccionar los 3 mejores paises y Mexico
  list_bestO3 = [data for data in l_p[:3]]
  # Conseguir a mexico
  list_bestO3.append(next((k,v,d) for k,v,d in l_p if v == 'Mexico'))

  return list_bestO3


# Retriving results from csv file
survey_results = os.getcwd() + os.sep + "survey_results.csv"
sr_f = pd.read_csv(survey_results)

countries = sr_f['Country'].to_list()
# Consiguiendo los paises con más respuestas
list_countries = most_countries(countries)

# Calculando el salario de los paises
salarios = sr_f[['Country', 'ConvertedCompYearly']]
salario_anual(list_countries, salarios)