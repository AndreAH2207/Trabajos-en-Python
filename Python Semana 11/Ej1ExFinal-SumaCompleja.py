def digitos_impares(numero):
    contador = 0
    while numero > 0:
        digito = numero % 10
        if digito % 2 != 0:
           contador += 1 
        numero = numero // 10      
 
    return contador

def digitos_impares2(cadena):
    contador = 0
    for digito in cadena:
        if int(digito) % 2 != 0:
            contador += 1
    
    return contador    



def calcularSuma(n, x):
  suma = 0
  for k in range(0, n+1):
     suma+= ((-1)**k) * ((x-1)**(k+1) )/(k+1)
  return suma
#main
print(calcularSuma(1,2)) #se probó en pizarra, prueben calcularSuma(2,2)...etc  

# ------------------------------------------------

def hallar_impares():
    print("\n[1] Hallar impares")    
    numero = int(input("Ingrese numero : "))
    cantidad_impares = digitos_impares(numero)
    print("Digitos impares = ", cantidad_impares)
    print()

def calcular_serie():
    print("\n[2] Calcular serie")
    n = int(input("Ingrese valor para N :"))
    x = int(input("Ingrese valor para X :"))
    resultado = calcular_suma(n, x)
    print("Resultado = ", resultado)    
    print()

def mostrar_menu():
    print("\nMenu de opciones")
    print("[1] Hallar cantidad de digitos impares")
    print("[2] Calcular serie")
    print("[3] Fin")

#  main
while True:
    mostrar_menu()
    opcion = input("Ingrese opcion : ")

    if opcion == "1":
        hallar_impares()
    elif opcion == "2":
        calcular_serie()
    elif opcion == "3":
        break
    else:
        print("Opcion incorrecta")




# numero = int(input("Ingrese numero : "))
# cantidad_impares = digitos_impares1(numero)
# print("Digitos impares = ", cantidad_impares)

# cadena = input("Ingrese numero : ")
# cantidad_impares = digitos_impares2(cadena) 
# print("Digitos impares = ", cantidad_impares)