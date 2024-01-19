lista=[]
while True:
  numero = int(input("Ingrese número: "))
  if numero == 0:
    break
  lista.append(numero)
  lista.sort()
  print("Lista: ",lista)
print("Lista final: ",lista)