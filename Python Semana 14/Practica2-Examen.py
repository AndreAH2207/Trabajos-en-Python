import random

def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input("Ingrese el numero de elementos de una lista de numeros: "))
    print("")

    if n<0 or n>50:
        print("Ingrese un numero mayor a 0 y menor a 50")
        print("")
        return main()

    lista = [random.randint(50, 1000) for _ in range(n)]
    print(f"Lista generada: {lista}")
    print("")


    primos = [numero for numero in lista if es_primo(numero)]
    print("Cantidad de numeros primos: ", primos)
    print("")


    no_primos = [numero for numero in lista if not es_primo(numero)]
    print("Cantidad de numeros no primos: ", no_primos)
    print("")


    maximo = max(lista)
    repeticiones_maximo = lista.count(maximo)
    print(f"El maximo valor de la lista es {maximo} y se repite {repeticiones_maximo} veces")
    print("")

    lista.sort(reverse = True)
    print("Lista ordenada descendentemente: ", lista)
    print("")


main()
