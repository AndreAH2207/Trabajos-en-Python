def Sumatoria(numero):
    Suma = 0
    for i in range(numero):
        Suma += 1/2**i
    return Suma
    

def main():
    n = int(input("Ingrese N: "))
    while n < 0:
        n = int(input("Ingrese N: "))
   
    resultado = Sumatoria(n)
    print("La suma es:", resultado)

main()
    
    
