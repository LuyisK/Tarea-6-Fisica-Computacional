
"""
Created on Wed Jun 23 04:16:16 2021

Física Cpmputacional - Tarea 6

Valentina Campos Aguilar
Luis Guerrero Camacho

ALGORITMO GENÉTICO MODIFICADO
"""
#Se importan las bibliotecas necesarias para la ejecución del método
import numpy as np
import matplotlib.pyplot as plt

#Se definen las coordenadas de las ciudades a visitar por el vendedor ambulante
lista_ciudades = [[0.2554, 18.2366],
[0.4339, 15.2476],
[0.7377, 8.3137],
[1.1354, 16.5638],
[1.5820, 17.3030],
[2.0913, 9.2924],
[2.2631, 5.3392],
[2.6373, 2.6425],
[3.0040, 19.5712],
[3.6684, 14.8018],
[3.8630, 13.7008],
[4.2065, 9.8224],
[4.8353, 2.0944],
[4.9785, 3.1596],
[5.3754, 17.6381],
[5.9425, 6.0360],
[6.1451, 3.8132],
[6.7782, 11.0125],
[6.9223, 7.7819],
[7.5691, 0.9378],
[7.8190, 13.1697],
[8.3332, 5.9161],
[8.5872, 7.8303],
[9.1224, 14.5889], 
[9.4076, 9.7166],
[9.7208, 8.1154],
[10.1662, 19.1705],
[10.7387, 2.0090],
[10.9354, 5.1813],
[11.3707, 7.2406],
[11.7418, 13.6874],
[12.0526, 4.7186],
[12.6385, 12.1000],
[13.0950, 13.6956],
[13.3533, 17.3524],
[13.8794, 3.9479],
[14.2674, 15.8651],
[14.5520, 17.2489],
[14.9737, 13.2245],[15.2841, 1.4455],
[15.5761, 12.1270],
[16.1313, 14.2029],
[16.4388, 16.0084], 
[16.7821, 9.4334],
[17.3928, 12.9692],
[17.5139, 6.4828],
[17.9487, 7.5563],
[18.3958, 3.5112],
[18.9696, 19.3565], 
[19.0928, 16.5453]]

#Se definen las variables globales de la simulación
tpoblación = 100 #tamaño de la población
nciudades = len(lista_ciudades) #número de ciudades
ngeneraciones = 300 #número de generaciones
prob_mut = 0.6 #probabilidad de mutación

#Se inicializan las listas que almacenaran los valores de ajuste y población de cada generación
lista_ajustes_total = []
lista_poblaciones_tot = []

'''Se crea una función que permita encontrar la distancia entre dos ciudades con parámetros:
- posición x de una ciudad
- posición y de una ciudad
- lista de coordenadas de ciudades
Esta retornará la posición mínima que debe asumir el vendedor. '''

def Distancia_Mínima(posxi, posyi, coordenadas):
    #Se define un valor alto como parámetro de distancia mínima que el vendedor recorrerá 
    parámetro_dist = 100000
    #Se define la posición mínima en 50 ya que debe visitar 50 ciudades en total
    pos_min = 50
    #Se recorre la lista de coordenadas de ciudades
    for i in coordenadas:
      #Se definen las posiciones actuales del vendedor como la entrada i de la lista de coordenadas
        x_nueva = i[0]
        y_nueva = i[1]
      #Se calcula la diferencia entre las posiciones actuales del vendedor y las posiciones de la ciudad anterior establecidas por el parámetro en las coordenadas x y y
        deltax = x_nueva-posxi
        deltay = y_nueva-posyi
      #La distancia que recorre el vendedor se calcula como la raíz de la suma de las diferencias de posición para cada coordenada al cuadrado
        distanciaEm = np.sqrt(deltax**2+deltay**2)
      #Cuando la distancia entre las ciudades es mayor al parámetro de distancia este se actuaiza y se indica como posición mínima la entrada i de la lista de coordenadas
        if distanciaEm < parámetro_dist:
            parámetro_dist = distanciaEm
            pos_min = coordenadas.index(i)
            
    return pos_min
''' Se crea la función de inicialización para el algoritmo genético modificado donde los parámetros serán:
- el tamaño de la población
- el número de ciudades 
La misma retornará la población codificada. '''

def Inicialización_Modificada(tpoblación, nciudades):
    #Se inicializa la lista de la población
    población = []
    #Se empieza a recorrer el tamaño de la población
    for i in range(tpoblación):
        #Se escoge una ciudad inicial de manera aleatoria
        ciud_inicial = np.random.randint(0, nciudades)
        #Se inicializa una lista de ciudades y de coordenadas 
        ciudades = []
        lista_coordenadas = []
        #A la lista de coordenadas se le anexa las coordenadas de la ciudad inicial
        lista_coordenadas.append(lista_ciudades[ciud_inicial])
        #Se copia la lista de ciudades en otra lista y esta será la lista de coordenadas de ciudades que al vendedor le falta por recorrer
        coordenadas = lista_ciudades.copy()
        #De la lista se excluye la coordenada de la ciudad inicial
        coordenadas.pop(ciud_inicial)      
        #Se crea un ciclo que se generará mientras hayan más de 0 coordenadas por recorrer para el vendedor
        while len(coordenadas) > 0:
          #Se calculan las posiciones actuales del vendedor como las últimas entradas de la lista de coordenadas
            posxi = lista_coordenadas[-1][0]
            posyi = lista_coordenadas[-1][1]
          #Se define la ciudad siguiente con la función de distancia mínima, que dirá la ciudad más próxima para el vendedor
            ciud_siguiente = Distancia_Mínima(posxi, posyi, coordenadas)
          #Se anexan las coordenadas de la siguiente ciudad a visitar a la lista de coordenadas
            lista_coordenadas.append(coordenadas[ciud_siguiente])
          #Se excluyen de la lista de ciudades por visitar las coordenadas de la ciudad siguiente
            coordenadas.pop(ciud_siguiente)
        #Se recorre la lista de ciudades por visitar   
        for j in lista_coordenadas:
            #Se va actualizando la lista de ciudades recorridas 
            ciudad_j = lista_ciudades.index(j)
            ciudades.append(ciudad_j)
        población.append(ciudades)
    #Se recorre el largo de la población a partir de 1 para no mutar el primer individuo de la població
    for k in range (1,len(población)):
        #Se designa el cromosoma como la entrada k de la población
        cromosoma = población[k]
        #Se busca un número aleatorio entre 3 y 11 de mutaciones a realizar en el cromosoma
        mutaciones = np.random.randint(3,11)
        #Se crea un ciclo que realice las mutaciones definidas
        for p in range (0, mutaciones):
            #El cromosoma se muta utilizando el Operador de Mutación
            cromosoma_mutado = Operador_Mutación(cromosoma, prob_mut, nciudades)
        #Se actualiza el cromosoma como el cromosoma mutado
        población[k] = cromosoma_mutado
    return población 
'''Se crea la función para decodificar los cromosomas, con el cromosoma a analizar como parámetro, además se calcula para este cromosma el valor de ajuste.
Se retorna el cromosoma decodificado y el valor de ajuste del mismo'''

def Decodificación(cromosoma):
   #Se inicializan los valores de la distancia euclidiana y el ajuste en 0
  distanciaE = 0
  fajuste = 0
  #Se inicializan listas para almacenar las coordenadas x y y del cromosoma decfodificado
  lista_x = []
  lista_x = []
  lista_y = []
  ngenes = len(cromosoma)
  #Se crea un ciclo que recorre el largo del cromosoma y se van guardando las coordenadas en x y en y para cada gen del cromosma en las listas respectivas
  for i in range(ngenes):
    gen_escogido = int(cromosoma[i])
    pos_x = lista_ciudades[gen_escogido][0]
    pos_y = lista_ciudades[gen_escogido][1]
    lista_x.append(pos_x)
    lista_y.append(pos_y)
  #Se crea un ciclo que vaya recorriendo el número de ciudades para calcular la diferencia de distancia en ambas coordenadas entre la ciudad pasada y la actual
  for j in range(0, nciudades-1):
    deltax = lista_x[j]-lista_x[j+1]
    deltay = lista_y[j]-lista_y[j+1]
    #La distancia recorrida por el vendedor entre ambas ciudades se calcula como la raíz de la suma de las diferencias de distancia al cuadrado de cada coordenada
    distanciaE += np.sqrt(deltax**2+deltay**2)
  #Como la trayectoria debe ser cerrada se debe incluir la distancia que recorre el vendedor desde la última ciudad que visita de vuelta a la primera que 
  #visitó, por esto se calcula la distancia entre la posición final e inicial
  delta_fx = lista_x[nciudades-1]-lista_x[0]
  delta_fy = lista_y[nciudades-1]-lista_y[0]
  distanciaf = np.sqrt(delta_fx**2+delta_fy**2)
  #La distancia euclidiana total que recorre el vendedor se calculará como la suma de las distancias que recorre en cada cambio de ciudad más la distancia para
  #volver al punto de origen. Esta será la distancia euclidiana de un cromosoma
  distanciaE += distanciaf
  #Se calcula el valor de ajuste como el inverso de la distancia euclidiana
  fajuste = 1/distanciaE
  return distanciaE, fajuste

'''Se crea la función que permite generar mutaciones en los cromosomas, donde los parámetros serán:
- el cromosoma
- la probabilidad de mutación definida inicialmente
- el número de ciudades
Se retornará el cromosoma ya mutado.'''

def Operador_Mutación(cromosoma, prob_mut, nciudades):
  #Se inicializa el cromosoma como una copia del cromosoma a mutar
  cromosoma_mutado = np.copy(cromosoma)
  #Se genera un número aleatorio para comparar con la probabilidad de mutación y decidir si esta se hace o no
  val_random = np.random.random()
  #Se escogen dos genes del cromosoma de manera aleatoria a intercambiar
  gen1 = np.random.randint(0, nciudades)
  gen2 = np.random.randint(0, nciudades)
  if val_random < prob_mut:
  #Cuando la probabilidad de mutación supera el valor aleatorio generado las posiciones de los genes en el cromosoma original se intercambiaran en el gen mutado
    cromosoma_mutado[gen1] = cromosoma[gen2]
    cromosoma_mutado[gen2] = cromosoma[gen1]

  return cromosoma_mutado

'''Se crea la función que permite obtener los valores de ajuste de toda la población, con la población como parámetro.
La misma retornará la lista de valores de ajuste para cada población una vez que la lista se implemente en todas las generaciones. '''
def Ajuste_Población(población):
  #Se inicializa la lista de valores de ajuste para una población
  lista_ajustes = []
   #Se recorre el largo de la población y se define al cromosoma como la entrada i de la población
  n = len(población)
  for i in range(n):
    cromosoma = población[i]
    #Se definen el valor de ajuste y la distancia euclidiana para el cromosoma en estudio llamando a la función de decodificación
    distancia_euclidiana, fajuste_crom = Decodificación(cromosoma)
    #Se van anexando los valores de ajuste para cada cromosoma en la población
    lista_ajustes.append(fajuste_crom)
  #Se van anexando las listas de valores de ajustes de cada población para cuando la función se implementa para todas las generaciones.
  lista_ajustes_total.append(lista_ajustes)
  return lista_ajustes_total

'''Se crea la función que permite obtener el mejor camino del vendedor, donde los parámetros son:
- la lista de ajustes de todas las poblaciones
- la lista de todas las poblaciones 
Esta retornará la lista con el mejor camino. '''

def Mejor_Camino(lista_ajustes_total, lista_poblaciones_tot):
  #Se inicializa el valor del ajuste máximo en 0
  fmax = 0
  #Se recorre para cada generación el tamaño de las poblaciones hasta encontrar el valor de ajuste máximo en toda la lista de valores de ajuste de todas las poblaciones
  for i in range(ngeneraciones):
    for j in range(tpoblación):
      ajuste = lista_ajustes_total[i][j]
      if ajuste > fmax:
         #Se ajusta el valor de ajuste máximo así como la generación y punto de la población con la que se obtiene este valor
        fmax = ajuste
        imax = i
        jmax = j 
      else:
        pass
  #Se define el mejor camino como la entrada de la lista de todas las poblaciones en la generación y punto de la población que generan el ajuste máximo
  mejor_camino = lista_poblaciones_tot[imax][jmax]
  return mejor_camino

'''Se crea la función que permite analizar la evolución del algoritmo genético a partir de la variación en los valores de ajuste.
Esta tiene como parámetro la lista de ajustes de todas de las poblaciones y retorna un gráfico de comparación entre los valores de ajuste promedio de 
cada población y los valores máximos de estas.'''

def Evolución_Ajuste(lista_ajustes_total):
   #Se convierte en array la lista de ajustes de todas las poblaciones
    valores_ajuste = np.asarray(lista_ajustes_total)
  #Se calcula la media de las listas de ajustes de cada población en el array
    ajuste_promedio = np.mean(valores_ajuste, 1)
  #Se obtienen los valores máximos de ajuste de cada población
    valores_ajuste_max = np.max(valores_ajuste,1)
   #Se grafican los valores máximos y promedio de ajuste en función de las generaciones 
    fig,ax=plt.subplots(dpi=120)
    ax.plot(ajuste_promedio, label='ajuste promedio', c = 'm')
    ax.plot(valores_ajuste_max, label = 'ajuste máximo')
    ax.set_title('Comparación entre valores de ajuste promedio y valores máximos de ajuste')
    ax.set_xlabel('generaciones')
    ax.set_ylabel('valores de ajuste')
    ax.legend(loc='best')
    plt.show()
    
#Se define la población inicial llamando a la función de inicialización con el tamaño de población y número de ciudades establecidos
población_inicial = Inicialización_Modificada(tpoblación, nciudades)
#Se calculan los valores de ajuste llamando a la función correspondiente para la población inicial.
Ajuste_Población(población_inicial)
#Se anexa la población inicial a la lista de poblaciones
lista_poblaciones_tot.append(población_inicial)

#Se recorren las generaciones para realizar las mutaciones sobre todas las poblaciones
for i in range(ngeneraciones-1):
  población = lista_poblaciones_tot[i]
  #Se inicializa la lista de la población mutada
  población_mutada = []
  #Se va recorriendo el largo de la población para mutar cada uno de los cromosomas en esta
  for j in range(len(población)):
    cromosoma = población[j]
    #Se llama al operador de mutación para que se ejecute la mutación
    cromosoma_mutado = Operador_Mutación(cromosoma, prob_mut, nciudades)
    #Se van actualizando los cromosomas de la población
    población[j] = cromosoma_mutado
    población_mutada.append(cromosoma_mutado)
  #Se van anexando las poblaciones mutadas a la lista de todas las poblaciones y se van calculando para estas los valores de ajuste
  lista_poblaciones_tot.append(población_mutada)
  Ajuste_Población(población)

#Se define el mejor camino con la función correspondiente teniendo ya la lista de ajustes de todas las poblaciones una vez que estas fueron todas mutadas
mejor_camino = Mejor_Camino(lista_ajustes_total, lista_poblaciones_tot)
#Se calcula la longitud del mejor camino con la función de decodificación y este resultado se imprime
longitud_mejorc = Decodificación(mejor_camino)[0]
print('La longitud del mejor camino es:', longitud_mejorc)
#print(mejor_camino)

#Se inicializan las listas de las coordenadas del mejor camino, generales, en x y en y
coordenadas_mejorcamino = []
coordenadas_mcx = []
coordenadas_mcy = []
#Se va recorriendo el mejor camino y anexando las coordenadas de cada ciudad a la lista correspondiente
for i in mejor_camino:
  coordenadas_mejorcamino.append(lista_ciudades[int(i)])
#Se va recorriendo el largo del mejor camino para guardar las coordenadas de cada ciudad en x y y respectivamente
for j in range(len(mejor_camino)):
  coordenadas_mcx.append(coordenadas_mejorcamino[j][0])
  coordenadas_mcy.append(coordenadas_mejorcamino[j][1])

#Se agregan a las tres listas de coordenadas la posición inicial de cada una de estas para que la trayectoria del vendedor sea cerrada
coordenadas_mejorcamino.append(coordenadas_mejorcamino[0])
coordenadas_mcx.append(coordenadas_mejorcamino[0][0])
coordenadas_mcy.append(coordenadas_mejorcamino[0][1])

#Se convierte en arreglos las listas de coordenadas x y y que sigue el vendedor en su mejor camino 
coordenadas_mejorcamino_array = np.asarray(coordenadas_mejorcamino)
coordenadas_mcx1 = np.asarray(coordenadas_mcx)
coordenadas_mcy1 = np.asarray(coordenadas_mcy)

#Se grafica el mejor camino encontrado para el vendedor
fig,ax=plt.subplots(dpi=120)
ax.plot(coordenadas_mcx1,coordenadas_mcy1, "c-")
ax.plot(coordenadas_mcx1,coordenadas_mcy1, "go")
ax.set_title('Mejor camino para el vendedor ambulante')
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.legend(["Ruta","Ciudad"])
plt.show()

#Se registra el arreglo de las coordenadas del mejor camino en un archivo de texto. Es importante notar que este constará de 51 entradas, porque se incluye
#la primera ciudad para que la trayectoria sea cerrada. 
np.savetxt('caminoMásCorto_AGM.txt', coordenadas_mejorcamino_array)

#Se llama a la función de evolución para mostrar el gráfico comparativo de los valores de ajuste
Evolución_Ajuste(lista_ajustes_total)