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

numero = int(input("Ingrese numero : "))

if es_numero_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")



