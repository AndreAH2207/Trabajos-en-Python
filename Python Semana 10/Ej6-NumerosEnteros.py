numeros=[]
positivos=0
negativos=0

while(True):
    numero=int(input("Ingrese numero: "))
    if numero == 0:
        break
    numeros.append(numero)
    if numero>0:
        positivos=positivos + 1
    elif numero<0:
        negativos = negativos + 1

print("Positivos: ", positivos)
print("Negativos: ", negativos)
print("Maximo   : ", max(numeros))  
print("Minimos  : ", min(numeros))
print("Promedio : ", sum(numeros)/len(numeros))
