import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import os

def create_plot(l_l:str=None, l_f:str=None, label_title:str=None, label_file:str=None, type_of_plot:str=None, values:list=None):
  if type_of_plot == 'bar':
    plt.figure(figsize=(10,7))
    plt.bar(l_l, l_f, width=0.5)
    plt.title(f'{label_title}')
    plt.tick_params('x', labelsize=8, rotation=70)
    plt.savefig(f'./{label_file}.pdf', dpi=600)
    return
  if type_of_plot == 'boxplot':
    plt.figure()
    plt.boxplot(values)
    plt.title(f'Boxplot de {label_title}')
    plt.savefig(f'salario_anual_{label_file}_boxplot.pdf')
    return

def var_std(lista, media):
  var = [(x_i - media)**2 for x_i in lista]
  var = sum(var) / (len(lista)-1)

  std = var**0.5
  return var,std

def outliers(l, q1, q3):
  iqr = q3 - q1
  lif = q1 - 1.5 * iqr
  uif = q3 + 1.5 * iqr

  print(f'\tIQR :{iqr:.2f}')
  print(f'\tLIF :{lif:.2f}')
  print(f'\tUIF :{uif:.2f}')

  # Whisker inferior y superior
  for v in l:
      if  v >= lif:
          lw = v
          break

  for v in l[::-1]:
      if v <= uif:
          uw = v
          break
  
  print(f'\tWhisker inferior: {lw}')
  print(f'\tWhisker superior: {uw}')

  # Outliers
  outs = [v for v in l if v < lw or v > uw]
  print(f'\tOutliers: {outs}')
  
  return

def cuartil(l_v, q):
  # Posicion en la lista
  p_q = (q*(len(l_v) - 1)) / 4

  # Parte entera que nos dice cual
  # elemento tomar
  idx = int(p_q)

  # Valor que nos permite hacer una
  # interpolacion lineal
  dec = p_q%1

  # Valor del cuartil q
  v_q = l_v[idx] + dec * (l_v[idx+1] - l_v[idx])

  return v_q

def trimm_data(datos,p=10):
  # Sobre los datos ordenados, calcular k
  n = len(datos)
  k = int((p*n)/100)

  return datos[k:n-k]

def get_bins(values,n):
  lim_bins = []
  # 1.Encontrar el rango 
  min = values[0]
  max = values[-1]
  rango = abs(min-max)
  # 2.Dividir el rango
  size = rango/n
  l_i = min
  l_s = min + size
  
  # 3. Definir el limite superior e inferior de cada bin y agregarlo a una lista de listas 
  lim_bins = [[l_i+(size*i),l_s+(size*i)] for i in range(n)]
  bins = [[]]
  i = 0
  for v in values: 
    if (v >= l_s) and (i < n-1):
        bins.append([])
        i += 1
        l_s += size
    if (v < l_s) or (i == n-1):
        bins[i].append(v)
  
  return lim_bins

def busqueda_frecuencias(l_p:list):
  l_l = []
  l_f = []
  index = 0
  for list in l_p:
    index += 1
    if list[1] == 'Mexico':
      # Debe encontrar a Mexico y terminar el ciclo
      l_l.append(list[1])
      l_f.append(list[-1])
      break
    elif index <= 10:
      # Caso de no encontrar a mexico pero esta recolectando
      # los datos de los 10 paises con mas respuestas
      l_l.append(list[1])
      l_f.append(list[-1])

  return l_l, l_f

def cat_wages(values:DataFrame):
  categorizacion_salario = {"Bajo": [], "Medio": [], "Alto": []}
  for value in values:
    if value <= 10000:
      categorizacion_salario['Bajo'].append(value)
    elif value > 10000 and value <= 50000:
      categorizacion_salario['Medio'].append(value)
    elif value > 50000:
      categorizacion_salario['Alto'].append(value)
  return categorizacion_salario

def resumen_salarios(country_label:str, list_Comp:DataFrame):
  # Obteniendo los datos del pais
  data = list_Comp[list_Comp['Country'].str.contains(country_label)]
  values = data['ConvertedCompYearly'].to_list()
  values.sort(reverse=True)
  # values.sort()
  # Calcular k, los cuartiles, la media y desviacion estandar
  trim_val = trimm_data(values)
  n = get_bins(values, 10)
  Q1 = cuartil(values, 1)
  med = cuartil(values, 2)
  Q3 = cuartil(values, 3)
  m_a = sum(values)/len(values)
  # Usar los datos recortados a un %10 para la desviacion
  _, std = var_std(values,med)

  print(f'\tSalario minimo en {country_label}: ' + str(min(values)))
  print(f'\tCuartil 1: {Q1}')
  print(f'\tCuartil 2(Mediana): {med}')
  print(f'\tCuartil 3: {Q3}')
  print(f'\tSalario maximo en {country_label}: ' + str(max(values)))
  print(f'\tMedia: {m_a:.2f}')
  print(f'\tDevisacion estandar: {std:.2f}')

  # Boxplot
  create_plot(label_title=country_label, label_file=country_label, type_of_plot='boxplot', values=values)

  # Categorizando los salarios en 3 tipos, alto, medio y bajo
  cat_sal = cat_wages(values)
  freq_b = len(cat_sal['Bajo'])
  freq_m = len(cat_sal['Medio'])
  freq_a = len(cat_sal['Alto'])
  cat_freq_dic = {"Alto": freq_a, "Medio": freq_m,"Bajo": freq_b }
  catg = list(cat_freq_dic.keys())
  freq = list(cat_freq_dic.values())
  print(freq)
  # create_plot(l_l=['Alto', 'Medio', 'Bajo'], l_f=[freq_a, freq_m, freq_b],label_title=f'Frecuencias de salarios {country_label}', label_file=f'frecuencia_salario_{country_label}' ,type_of_plot='bar')
  plt.figure(figsize=(10,7))
  barra = plt.bar(catg, freq, color='blue')
  plt.bar_label(barra, color='blue', label_type='edge')
  plt.title(f'test')
  plt.tick_params('x', labelsize=8, rotation=70)

  return 

def resume_country(sr_f:DataFrame):
  paises_lists = sr_f['Country'].to_list()
  # Con un objecto vamos a ir guardando las frecuecias como vaya leyendo el archivo
  d_f = {}
  for index in paises_lists:
    d_f[index] = d_f.get(index,0) + 1

  l_p = []
  total = sum(d_f.values())
  for k, v in d_f.items():
    l_p.append((v/total * 100, k, v))
  
  l_p.sort(reverse=True)
  l_l, l_f = busqueda_frecuencias(l_p)
  # Crear grafico de barras
  create_plot(l_l, l_f, label_title='Paises con mayor respuestas',label_file='barras_paises' ,type_of_plot='bar')

  # # Seleccionar los 3 mejores y a México, pero tambien calcular q1,q2,q3, etc.
  # print('------------')
  # for best03 in l_l[:3]:
  #   resumen_salarios(best03, sr_f)
  #   print('------------')
  # Seleccionar a Mexico
  resumen_salarios(l_l[:1][0],sr_f)
  print('------------')

  return

# Obtener los datos del csv
survey_results = os.getcwd() + os.sep + "survey_results.csv"
sr_f = pd.read_csv(survey_results)

resume_country(sr_f)