
def ingresar(n):
 EF=int(input(f"Ingrese la nota del EF del alumno {n} "))
 EP=int(input(f"Ingrese la nota del EP del alumno {n} "))
 TF=int(input(f"Ingrese la nota del TF del alumno {n} "))
 return EF,EP,TF

def calcularPromedio(EF,EP,TF):
 promedio = float(EF*55/100+EP*30/100+TF*15/100)
 return promedio

n=int(input("Ingrese la cantidad de alumnos: "))
for i in range(1,n+1):
 (a,b,c)= ingresar(i)
 print(calcularPromedio(a,b,c))