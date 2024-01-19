# Solicita al usuario ingresar un número entero positivo
N = int(input("Ingrese N: "))

# Inicializa los primeros dos términos de la serie
a, b = 1, 1

# Imprime los primeros N términos de la serie de Fibonacci
print("Serie de Fibonacci:")
for _ in range(N):
    print(a, end=", ")
    a, b = b, a + b
