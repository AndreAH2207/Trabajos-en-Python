def suma(n):
  s = 0
  for i in range(1,n+1):
    s = s + i
  return s
#main
n=5
print("Suma:", suma(n))