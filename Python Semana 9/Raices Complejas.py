from math import sqrt

A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

def Discriminante(a,b,c):
    resultado = b ** 2 - 4 * a * c
    return resultado

d = Discriminante(A,B,C)

def Raiz_1(a, b):
    resultado  = (-b + sqrt(d) / (2 * a))
    return resultado

def Raiz_2(a, b):
    resultado  = (-b + sqrt(d) / (2 * a))
    return resultado

if d < 0:
    print("Son raices completas")
else:
    print("Raiz 1: ", Raiz_1(A, B))
    print("Raiz 2: ", Raiz_2(A, B))