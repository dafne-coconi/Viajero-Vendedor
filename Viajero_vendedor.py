import numpy as np
import random 

global mat_Dist
global initial_City

mat_Dist = np.array([[0,8,4,15],[8,0,7,9],[4,7,0,10],[15,9,10,0]])
initial_City = int(input('Ciudad inicial(0,1,2,3): '))
num_Iteraciones = int(input('Ingresa número de interaciones: '))

def camino_Inicio():
  global mat_Dist
  global initial_City
  copy_mat_Dist = mat_Dist.copy() # matriz a seguir
  ruta_Inicial = [initial_City]
  sig_Ciudad = initial_City
  a = 0
  while len(ruta_Inicial) < len(mat_Dist[0,:]):
    copy_mat_Dist[sig_Ciudad,:] = 0
    r = np.where(copy_mat_Dist[:,sig_Ciudad]>0) #busca ciudades disponibles
    sig_Ciudad = random.choice(r[0])
    ruta_Inicial.append(sig_Ciudad)
  ruta_Inicial.append(initial_City)
  print(ruta_Inicial)
  return ruta_Inicial

def intercambia(num_Iteraciones,ruta_Inicial):
  nueva_Ruta = ruta_Inicial.copy()
  mejor_Ruta = ruta_Inicial.copy()
  print(ruta_Inicial)
  for i in range(num_Iteraciones):
    anterior_Ruta = nueva_Ruta.copy() 
    elemento1 = random.randint(1,len(nueva_Ruta)-2)
    r = list(range(1,elemento1)) + list(range(elemento1+1,len(nueva_Ruta)-1))
    elemento2 = random.choice(r)
    nueva_Ruta[elemento1], nueva_Ruta[elemento2] = nueva_Ruta[elemento2], nueva_Ruta[elemento1] 
    if evalua_Ruta(anterior_Ruta,nueva_Ruta):
      mejor_Ruta = nueva_Ruta.copy()
    print(mejor_Ruta)
    
def evalua_Ruta(anterior_Ruta,nueva_Ruta):
  global mat_Dist
  suma_Ranterior = 0
  suma_Rnueva = 0
  for i in range(len(anterior_Ruta)-1):
    suma_Ranterior += mat_Dist[anterior_Ruta[i],anterior_Ruta[i+1]]
    suma_Rnueva += mat_Dist[nueva_Ruta[i],nueva_Ruta[i+1]]
  print(suma_Rnueva)
  return suma_Rnueva < suma_Ranterior

ruta_Inicial = camino_Inicio()
intercambia(num_Iteraciones,ruta_Inicial)