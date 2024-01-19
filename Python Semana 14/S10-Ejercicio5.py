def peso_alumno(numero):
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0

    for i in range(numero):
        peso = int(input(f"Peso alumno {i + 1}: "))

        if peso < 40:
            p1 = p1 + 1
        elif peso >= 40 and peso <= 50:
            p2 = p2 + 1
        elif peso > 50 and peso < 60:
            p3 = p3 + 1
        elif peso >= 60:
            p4 = p4 + 1
    
    print("")
    print("Alumnos de menos de 40 kg: ", p1)
    print("")
    print("Alumnos entre 40 y 50 kg: ", p2)
    print("")
    print("Alumnos de más de 50 y menos de 60 kg: ", p3)
    print("")
    print("Alumnos de 60 kg o mas: ", p4)
    print("")


def main():
    n = int(input("Ingrese el numero de alumnos: "))

    while n < 1 or n > 50:
        n = int(input("Ingrese el número de alumnos: "))
    
    peso_alumno(n)

main()

        
        
