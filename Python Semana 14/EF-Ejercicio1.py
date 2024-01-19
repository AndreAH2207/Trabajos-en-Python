def cantidad_impares(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            count += 1
        n //= 10

    return count

def calcular_serie(n, x):
    if n < 0 or n > 20:
        print("Error: La cantidad de términos de la serie debe estar entre 0 y 20.")
        return 0

    if x <= 0 or x > 2:
        print("Error: El valor de x debe ser positivo y menor o igual a 2.")
        return 0

    suma = 0

    for k in range(n + 1):
        term = ((-1) ** k) * ((x - 1) ** (k + 1)) / (k + 1)
        suma += term

    return suma


def menu():
    while True:
        print("\nMenú de opciones")
        print("1. Hallar cantidad de dígitos impares")
        print("2. Calcular serie")
        print("3. Fin")

        opcion = input("Ingrese la opción deseada (1, 2, o 3): ")

        if opcion == '1':
            num = int(input("Ingrese un número positivo: "))
            resultado = cantidad_impares(num)
            print(f"La cantidad de dígitos impares en {num} es: {resultado}")

        elif opcion == '2':
            n_terms = int(input("Ingrese la cantidad de términos de la serie (entre 0 y 20): "))
            x_value = float(input("Ingrese el valor de x (positivo y menor o igual a 2): "))
            resultado = calcular_serie(n_terms, x_value)
            print(f"El resultado de la serie es: {resultado}")

        elif opcion == '3':
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Por favor, elija 1, 2, o 3.")

menu()