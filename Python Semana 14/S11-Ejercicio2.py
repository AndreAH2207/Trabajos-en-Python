
lista = []

def main():
    n = int(input("Ingrese numero: "))
    lista.append(n)
    lista.sort()

    if n == 0:
        print("Lista final: ", lista)
    else:
        print ("Lista = ", lista)
        return main()

main()

