#de Kevin Espinoza
def suma_impares(n):
    impar = 0
    for numero in range(n+1):
        if numero % 2 != 0:
            impar += numero
    return impar

n = int(input("Ingrese N:"))
resultado = suma_impares(n)
print("La suma es ", resultado)