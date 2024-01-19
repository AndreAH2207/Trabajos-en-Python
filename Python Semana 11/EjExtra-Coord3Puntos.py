# Se tienen 3 coordenadas de 3 puntos,
# se pide la menor distancia entre ellos:
# Ej: (2,3) , (4,5) , (2,6)

import math
def distancia(c1, c2):
  return math.sqrt((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2)

def menorDistancia(lista):
  resultados = []
  for i in range(len(lista)):
    for coordenada2 in lista[i +1:]:
      #print(lista[i], "--", coordenada2)
      d = distancia(lista[i], coordenada2)
      #print(d)
      resultados.append(d)
  return min(resultados)
#main
lista = [(2, 3) , (4,5) , (2,6) ]
print("Menor distancia:",menorDistancia(lista))