def cantidad_impares(n):
    count = 0
    
    if n < 0:
        print("Debes ingresar un valor mayor a 0")
        print("")
        return 0
  
    elif n > 0:
        digit = n % 10
        
        if digit % 2 != 0:
            count += 1
        n//= 10
    return count

def calcular_Suma(n,x):
    if n < 0 or n > 20:
        print("Debe ser un valor mayor que 0 y menor que 20")
        print("")
        return 0
    
    if n < 0 or n > 2:
        print("Debe ser un valor mayor que 0 y menor que 2")
        print("")
        return 0

    suma = 0

    for k in range(n+1):
        suma += (-1 ** k)*((x - 1)** (k + 1)) /k + 1
    return suma


def main():
    while True:
        print("Menu de opciones")
        print("1. Hallar la cantidad de dígitos impares")
        print("2. Calcular serie")
        print("3. Fin")

        opcion = int(input("Ingrese una opcion (1, 2, 3): "))
        print("")

        if opcion == 1:
            numero = int(input("Ingrese el valor de n: "))
            print("")
            resultado = cantidad_impares(numero)
            print(f"Cantidad de digitos impares en {numero} es: {resultado}")
            print("")
        
        elif opcion == 2:
            n_value = int(input("Ingrese el valor de n: "))
            x_value = int(input("Ingrese el valor de x: "))
            resultado = calcular_Suma(n_value,x_value)
            print(f"La suma de los terminos es: {resultado}")
            print("")

        elif opcion == 3:
            print("Saliendo del programa")
            print("")
            break

main()


