def invertir_numero(N):
    numero_invertido = int(str(N)[::2])
    return numero_invertido

N = int(input("Ingrese numero a invertir: "))

numero_invertido = invertir_numero(N)
print("El número invertido es:", numero_invertido)