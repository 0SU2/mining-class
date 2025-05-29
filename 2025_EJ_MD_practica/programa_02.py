"""
@author: Oscar Ricardo Rosas Zavala
Minería de Datos
Lunes 14 de Abril del 2025
"""
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import os
from scipy.stats import chi2

def create_plot(catg:list=None, freq:list=None, label_title:str=None, label_file:str=None, type_of_plot:str=None, values:list=None, country:str=None):
    if type_of_plot == 'bar':
        plt.figure(figsize=(10,7))
        barra = plt.barh(catg, freq, color='blue')
        plt.bar_label(barra, color='black', label_type='edge')
        plt.title(f'{label_title}')
        plt.tight_layout()
        try:
            if country != None: 
                os.makedirs(f'graficos_programa_02/{country}')
            else:
                os.mkdir(f'graficos_programa_02')
            plt.savefig(f'./graficos_programa_02/{label_file}.jpg', dpi=300)
            plt.close()
            return
        except:
            if country != None: 
                plt.savefig(f'./graficos_programa_02/{country}/{label_file}.jpg', dpi=300)
            else:
                plt.savefig(f'./graficos_programa_02/{label_file}.jpg', dpi=300)
            plt.close()
            return
    if type_of_plot == 'boxplot':
        plt.figure()
        plt.boxplot(values)
        plt.title(f'{label_title}')
        try:
            if country != None: 
                os.makedirs(f'graficos_programa_02/{country}')
            else:
                os.mkdir(f'graficos_programa_02')
            plt.savefig(f'./graficos_programa_02/{label_file}.jpg', dpi=300)
            plt.close()
            return
        except:
            if country != None: 
                plt.savefig(f'./graficos_programa_02/{country}/{label_file}.jpg', dpi=300)
            else:
                plt.savefig(f'./graficos_programa_02/{label_file}.jpg', dpi=300)
            plt.close()
            return
    if type_of_plot == 'hist':
        plt.figure()
        plt.hist(x=values,data=values, bins=10) 
        plt.grid(visible=True)
        plt.title(f'{label_title}')
        try:
            if country != None: 
                os.makedirs(f'graficos_programa_02/{country}')
            else:
                os.mkdir(f'graficos_programa_02')
            plt.savefig(f'./graficos_programa_02/{label_file}.jpg', dpi=300)
            plt.close()
            return
        except:
            if country != None: 
                plt.savefig(f'./graficos_programa_02/{country}/{label_file}.jpg', dpi=300)
            else:
                plt.savefig(f'./graficos_programa_02/{label_file}.jpg', dpi=300)
            plt.close()
            return

def phi_coef(c_t:dict):
    t_g = 0
    for label in c_t.keys():
        for index in c_t[label]:
            t_g += c_t[label][index]
    c_t_totals = []
    for label in c_t.keys():
        temp = 0
        for index in c_t[label]:
            temp += c_t[label][index]
        c_t_totals.append(temp)
            
    freq_sal = {}
    for x in c_t.values():
        for freq in x:
            value_temp = x[freq]
            freq_sal[freq] = freq_sal.get(freq,0) + value_temp

    # sacando xi
    xi = 0
    for freq_label in freq_sal.keys():
        temp_index_g = 0
        for contg_label in c_t.keys():
            oi = c_t[contg_label][freq_label]
            ei = (c_t_totals[temp_index_g]*freq_sal[freq_label])/t_g
            xi += ((oi - ei) ** 2) / t_g
            temp_index_g += 1

    d_f = (len(c_t_totals) - 1)*(len(freq_sal.keys()) - 1)
    a = 0.05
    # Valor critico
    p = chi2.isf(a, d_f)
    if xi > p:
        print('\tEl tipo de trabajo no influye en el salario anual de los usuarios')
        print(f'\tCoeficiente de pearson: {xi:.2f}')
    elif xi < p:
        print('\tEl tipo de trabajo influye en el salario anual de los usuarios. ')
        print(f'\tCoeficiente de pearson: {xi:.2f}')

    return

def prob_cond(c_t, val_A,val_B):
  p_AB = c_t[val_B][val_A] 
  p_B = sum(c_t[val_B].values())  # Probabiildad de B 
  #p_c = p_AB / p_B

  return p_AB / p_B

def define_category_wage(value:int):
    if value <= 10000:
        return 'Bajo'
    elif value > 10000 and value <= 50000:
        return 'Medio'
    elif value > 50000:
        return 'Alto'
    return

def calcular_probabilidad_condicional(titulo:str, nivel:str, c_t:dict):
    total = sum(c_t[titulo].values())
    if nivel in c_t[titulo]:
        return c_t[titulo][nivel] / total
    else:
        return 0

def tab_cot(values_1:list, values_2:list):
    # Formar la tabla de contingencia
    c_t = {} 
    for x, y in zip(values_1,values_2):
        if x not in c_t: # Si aun no esta definida en el diccionario
            c_t[x] = {}
            # agregar los 3 tipos 
            c_t[x]['Alto'] = 0
            c_t[x]['Medio'] = 0
            c_t[x]['Bajo'] = 0
        c_t[x][y] = c_t[x].get(y,0) + 1
    return c_t

def var_std(lista, media):
  var = [(x_i - media)**2 for x_i in lista]
  var = sum(var) / (len(lista)-1)

  std = var**0.5
  return var,std

def trimm_data(datos,p=10):
  # Sobre los datos ordenados, calcular k
  n = len(datos)
  k = int((p*n)/100)

  return datos[k:n-k]

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

def resumen_wage_dev(label_dev:str,list_comp:DataFrame, country_label:str=None):
    l_country = list_comp['DevType'].to_list()
    l_wage = list_comp['ConvertedCompYearly'].to_list()
    
    cat_wage = [ define_category_wage(value) for value in l_wage]

    c_t = tab_cot(l_country, cat_wage)
    
    for value in c_t.get(label_dev):
        p_c = prob_cond(c_t, f'{value}', f'{label_dev}')
        print(f'\tProbabilidad de que trabaje como {label_dev}, sea de {country_label} y tenga salario {value}: {p_c:.2f}')

    return

def resumen_salarios(label_dev:str, list_Comp:DataFrame, country_label:str=None):
    # Obteniendo los datos del pais
    data = list_Comp[list_Comp['DevType'].str.contains(label_dev)]
    values = data['ConvertedCompYearly'].to_list()
    values.sort(reverse=True)
    # Calcular k, los cuartiles, la media y desviacion estandar
    trim_val = trimm_data(values)
    n = get_bins(values, 10)
    Q1 = cuartil(values, 1)
    med = cuartil(values, 2)
    Q3 = cuartil(values, 3)
    m_a = sum(values)/len(values)
    # Usar los datos recortados a un %10 para la desviacion
    _, std = var_std(values,med)

    print(f'\tSalario minimo como {label_dev} en {country_label}: ' + str(min(values)))
    print(f'\tCuartil 1: {Q1}')
    print(f'\tCuartil 2(Mediana): {med}')
    print(f'\tCuartil 3: {Q3}')
    print(f'\tSalario maximo como {label_dev} en {country_label}: ' + str(max(values)))
    print(f'\tMedia: {m_a:.2f}')
    print(f'\tDesviacion estandar: {std:.2f}')

    # Boxplot
    create_plot(label_title=f'Boxplot de {label_dev} en {country_label}', label_file=f'frecuencias_boxplot_{label_dev}_{country_label}', type_of_plot='boxplot', values=values, country=country_label)
    # Histograma
    create_plot(label_title=f'Histograma de salario como {label_dev} en {country_label}', label_file=f'histograma_salario_{label_dev}_{country_label}', type_of_plot='hist', values=values, country=country_label)

    # # Categorizando los salarios en 3 tipos, alto, medio y bajo
    catg_wage_l = [define_category_wage(wage) for wage in values]
    c_t = tab_cot(catg_wage_l, values)
    freq = []
    catg = list(c_t.keys())
    for l in catg:
        freq.append(len(c_t[l]))
    create_plot(catg, freq, label_title=f'Frecuencias de salario como {label_dev}, en {country_label}', label_file=f'frecuencias_salario_categorica_{label_dev}_{country_label}', type_of_plot='bar', country=country_label)

    return

def freq(list_data:list, country:bool=False):
    # Con un objecto vamos a ir guardando las frecuecias como vaya leyendo el archivo
    d_f = {}
    for index in list_data:
        d_f[index] = d_f.get(index,0) + 1

    l_p = []
    total = sum(d_f.values())
    for k, v in d_f.items():
        l_p.append((v/total * 100, k, v))

    l_p.sort(reverse=True)
    l_l = []
    l_f = []
    index = 0
    if country:
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
    else:
        for list in l_p:
            l_l.append(list[1])
            l_f.append(list[-1])

    return l_l, l_f

def resumen(sr_f:DataFrame):
    paises_lists = sr_f['Country'].to_list()
    country_l, _ = freq(paises_lists, country=True)
    # Seleccionando los paises del punto uno.
    # De acuerdo a cada pa ́ıs, haga un gr ́afico de barras considerando solo los 3 trabajos m ́as populares
    print('------------')
    for country in country_l[:3]:
        data = sr_f[sr_f['Country'].str.contains(f'{country}')]
        country_data = data['DevType'].to_list()
        country_data_wage = data['ConvertedCompYearly'].to_list()
        data_l, data_f = freq(country_data) 
        create_plot(catg=data_l[:3], freq=data_f[:3], label_title=f'Trabajos mas populares de {country}', label_file=f'frecuencias_trabajos_{country}', type_of_plot='bar', country=country)
        for catg in data_l[:3]:
            print('------------')
            resumen_salarios(catg, data, country)

        print('------------')

        cat_wage_t = [ define_category_wage(value) for value in country_data_wage]
        c_t = tab_cot(country_data, cat_wage_t)

        probabilidades = {}
        for label in c_t:
            probabilidad = calcular_probabilidad_condicional(label, 'Alto', c_t)
            probabilidades[label] = probabilidad
        
        print("\n")
        probabilidades_ordenadas = sorted(probabilidades.items(), key=lambda x:x[1], reverse=True)
        label_country_work = probabilidades_ordenadas[0][0]
        label_prob_work = probabilidades_ordenadas[0][1]
        print(f"\tEn {country}, el título con mayor probabilidad de un salario alto es {label_country_work} con el {label_prob_work:.2f}")
        probabilidades = {}
        for label in c_t:
            probabilidad = calcular_probabilidad_condicional(label, 'Bajo', c_t)
            probabilidades[label] = probabilidad
        
        probabilidades_ordenadas = sorted(probabilidades.items(), key=lambda x:x[1], reverse=True)
        label_country_work = probabilidades_ordenadas[0][0]
        label_prob_work = probabilidades_ordenadas[0][1]
        print(f"\tEn {country}, el título con mayor probabilidad de un salario bajo es {label_country_work} con el {label_prob_work:.2f}")

        phi_coef(c_t)

        print('------------')
    
    data = sr_f[sr_f['Country'].str.contains(f'{country_l[-1:][0]}')].sort_values(by='ConvertedCompYearly', ascending=False)
    country_data = data['DevType'].to_list()
    country_data_wage = data['ConvertedCompYearly'].to_list()
    data_l, data_f = freq(country_data) 
    create_plot(catg=data_l[:3], freq=data_f[:3], label_title=f'Trabajos mas populares de {country_l[-1:][0]}', label_file=f'frecuencias_trabajos_{country_l[-1:][0]}', type_of_plot='bar', country=country_l[-1:][0])
    for catg in data_l[:3]:
        print('------------')
        resumen_salarios(catg, data, country_label=country_l[-1:][0])

    cat_wage_t = [ define_category_wage(value) for value in country_data_wage]
    c_t = tab_cot(country_data, cat_wage_t)

    probabilidades = {}
    for label in c_t:
        probabilidad = calcular_probabilidad_condicional(label, 'Alto', c_t)
        probabilidades[label] = probabilidad
    
    print("\n")
    probabilidades_ordenadas = sorted(probabilidades.items(), key=lambda x:x[1], reverse=True)
    label_country_work = probabilidades_ordenadas[0][0]
    label_prob_work = probabilidades_ordenadas[0][1]
    print(f"\tEn {country_l[-1:][0]}, el título con mayor probabilidad de un salario alto es {label_country_work} con el {label_prob_work:.2f}")
    probabilidades = {}
    for label in c_t:
        probabilidad = calcular_probabilidad_condicional(label, 'Bajo', c_t)
        probabilidades[label] = probabilidad
    
    probabilidades_ordenadas = sorted(probabilidades.items(), key=lambda x:x[1], reverse=True)
    label_country_work = probabilidades_ordenadas[0][0]
    label_prob_work = probabilidades_ordenadas[0][1]
    print(f"\tEn {country_l[-1:][0]}, el título con mayor probabilidad de un salario bajo es {label_country_work} con el {label_prob_work:.2f}")
    phi_coef(c_t)

    return

# Obtener los datos del csv
survey_results = os.getcwd() + os.sep + "survey_results.csv"
sr_f = pd.read_csv(survey_results)
resumen(sr_f)