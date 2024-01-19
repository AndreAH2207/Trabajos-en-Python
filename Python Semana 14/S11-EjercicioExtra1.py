''' 
Se tienen 3 coordenadas de 3 puntos, se pide la menor distancia entre ellos.
Ejemplo: [(2, 3) , (4,5) , (2,6) ]
'''

import math

def distancia(c1, c2):
    return math.sqrt((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2)


def calcular_menor(lista):
    resultados = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            n = distancia(lista[i], lista[j])
            resultados.append(n)
    
    return min(resultados)

def main():
    x1 = int(input("Ingrese el valor de x1: "))
    y1 = int(input("Ingrese el valor de y1: "))
    x2 = int(input("Ingrese el valor de x2: "))
    y2 = int(input("Ingrese el valor de y2: "))
    x3 = int(input("Ingrese el valor de x3: "))
    y3 = int(input("Ingrese el valor de y3: "))

    lista = [(x1,y1), (x2,y2), (x3, y3)]
    print("La menor distancia es: ", calcular_menor(lista))

main()