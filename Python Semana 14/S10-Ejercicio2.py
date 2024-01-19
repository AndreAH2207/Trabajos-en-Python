def sumaImpares(n):

#Empieza desde 1
#Termina hasta n+1 
#Va sumando de a 2

  impares = range(1,n+1,2)
  return sum(impares)

n = int(input("n:"))
print("Suma de impares:" , sumaImpares(n))