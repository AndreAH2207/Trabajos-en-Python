def sumaImpares(n):
  impares = range(1,n+1,2)
  return sum(impares)

n = int(input("n:"))
print("Suma de impares:" , sumaImpares(n))
