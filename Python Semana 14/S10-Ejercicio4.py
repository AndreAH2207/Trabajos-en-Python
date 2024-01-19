def Promedio():
    n = int(input("Ingrese el numero de alumnos: "))
    print("")

    for i in range(n):
        EF = int(input(f"Ingrese el EF del Alumno {i+1}: "))
        EP = int(input(f"Ingrese el EP del Alumno {i+1}: "))
        TF = int(input(f"Ingrese el TF del Alumno {i+1}: "))
        print("")

        prom_EF = 0.55 * EF
        prom_EP = 0.30 * EP
        prom_TF = 0.15 * TF
        promedio_total = prom_EF + prom_EP + prom_TF

        print("Su promedio final es: ", promedio_total)
        print("")

Promedio()


    
    