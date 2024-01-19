def invertir_numero():
    numero_invertido = int(str(N)[::-1])
    return numero_invertido
    
N = int(input("Ingrese numero a invertir: "))
numero_invertido = invertir_numero(N)
print("El numero invertido es: ", numero_invertido)