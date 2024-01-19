def saber_si_es_numero_perfecto(n):
        suma = 0

        for i in range(1, n):
            if n % i == 0:
                suma += i

        if n == suma:
            return True
        else:
            return False

def sumatoria_numeros_perfectos(n, N):
        numeros_perfectos = []
        num = 2
        while len(numeros_perfectos) < n and num <= N:
            if saber_si_es_numero_perfecto(num):
                numeros_perfectos.append(num)
            num += 1

        return sum(numeros_perfectos)

def sumatoria_n_x(n, x):

        sumatoria = 0
        for i in range(0, n):
            p = (2 * i + 1) ** 2
            sumatoria += x ** p
        
        return sumatoria

def calcular_cantidad_y_promedio():
        numeros = []

        while True:
            valor = input("Ingrese un número (0 para culminar): ")
            if valor == "0":
                break  # Salir del bucle si el usuario ingresa "0"

            numeros.append(float(valor))

        cantidad = len(numeros)

        if cantidad == 0:
            print("No se ingresaron números.")
            return 0, 0  # En caso de que no haya números en el conjunto

        promedio = sum(numeros) / cantidad

        print(f"Cantidad de números: {cantidad}")
        print(f"Promedio de los números: {promedio}")
        print("") 

    
def main():
        while True:
            print("   Menu ")
            print("1. Determinar si es numero perfecto")
            print("2. Calcular la sumatoria de los n numeros perfectos que esten enre 1 a N")
            print("3. Calcular la sumatoria x, n")  
            print("4. Cálculo de cantidad y promedio de numeros")
            print("5. Salir")
            print("")
            
            op = int(input(" Seleccione una opcion: "))
            print("")

            if op == 1:
                n = int(input("Ingrese un numero: "))
                if saber_si_es_numero_perfecto(n):
                    print("El numero es perfecto")
                    print("")
                else:
                    print("El numero no es perfecto")
                    print("")

            elif op == 2:
                n = int(input("Ingrese el valor de n: "))
                N = int(input("Ingrese el valor de N: "))
                sumatoria_n_p = sumatoria_numeros_perfectos(n,N)
                print("La sumatoria sera: ", sumatoria_n_p)
                print("")
            
            elif op == 3:
                n = int(input("Ingrese el valor de n: "))
                x = int(input("Ingrese el valor de x: "))
                sumatoria = sumatoria_n_x(n,x)
                print("La sumatoria es : ", sumatoria)
                print("") 

            elif op == 4:
                calcular_cantidad_y_promedio()

            elif op == 5:
                print("Saliendo del programa...")
                print("")
                break


main()

        