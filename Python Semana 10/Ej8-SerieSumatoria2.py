def sumatoria(num):
    suma = 0
    for i in range(num):
        if i%2 == 0:
            suma += 1/(2**i)
        else:
            suma -= 1/(2**i)
    
    return suma

n = int(input("Ingresa a N: "))
suma = sumatoria(n)
print("La suma es: ", suma)