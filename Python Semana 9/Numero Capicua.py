try:
  n = int(input("ingrese numero: "))
  if 1000 > n > 99:
    a = n // 100
    b = n % 10
    if a == b:
      print("el numero", n, "es capicua")
    else:
      print("el numero", n, "no capicua")
  else:
   print("ingrese un numero de 3 digitos")
except:
  print("numero no valido")

numero = int(input("Ingrese el numero: "))
unidad = numero // 100
decena = (numero%100)//10
centena = numero % 10
if numero>999:
  print("El numero es invalido!!!")
elif unidad == centena:
  print("CAPICUA")
else:
  print("NO ES CAPICUA")