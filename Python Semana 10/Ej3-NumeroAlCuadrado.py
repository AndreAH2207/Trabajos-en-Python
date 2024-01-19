# n al cuadrado
def cuadrado(n):
  impar = 1
  suma = 0
  #n veces se ejecutar el for
  for i in range(0, n):
    suma = suma + impar
    impar = impar + 2
  return suma

print(cuadrado(4))