def es_numero_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    indice = 5
    while indice * indice <= numero:
        if numero % indice == 0 or numero % (indice + 2) == 0:
           return False
        indice += 6
    return True

def es_numero_primo2(numero):
    if numero <= 1:
        return False

    for indice in range(2, int(numero / 2) + 1):
        if numero % indice == 0:
            return False
    return True

# main    
numero = int(input("Ingrese numero : "))

if es_numero_primo(numero):
    print(f"{numero} es numero primo")
else:
    print(f"{numero} no es numero primo")

