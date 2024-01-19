import math

def Sumatoria():
    N = int(input("Ingresa el valor de N (entre 1 y 20) : "))
    while N < 1 or N > 20:
        N = int(input("Ingresa el valor de N (entre 1 y 20) : "))

    a = float(input("Ingresa el valor de a (entre 0.5 y 2): "))
    while a < 0.5 or a > 2:
        a = float(input("Ingresa el valor de a (entre 0.5 y 2): "))


    suma = 0
    for i in range(1, N + 1):
        x = 2**(i - 1)
        suma += math.pow(-1, i + 1)*((2 * i) - 1)* math.pow(a, x)/(2*i)
    print("La sumatoria es: ", suma)

Sumatoria()