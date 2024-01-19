def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

def sumar(n):
    s = 0
    signo = 1
    for i in range(1, n+1):
        s+=signo *(i/factorial(i))
        signo = -signo
    return s

n = int(input("Ingrese numero positivo: "))
print("Suma:", sumar(n))