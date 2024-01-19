import math

n=4
a=1.2
suma=0
signo=1

for i in range(1, n + 1):
    x= 1
    suma += signo* math.pow(-1,i+1)*(2*i-1)*math.pow(a,x)/(2*i)
    signo = -signo
print(Suma)

