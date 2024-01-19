def sumaPromedios(ef, ep, tf):
 suma = (0.55 * ef) + (0.30 * ep) + (0.15 * tf)
 return suma

alumnos = int(input("Ingrese el numero de alumnos: "))
for i in range(1, alumnos + 1):
 ef = int(input(f"Ingrese el EF del Alumno {i}:"))
 ep = int(input(f"Ingrese el EP del Alumno {i}:"))
 tf = int(input(f"Ingrese el TF del Alumno {i}:"))
 promedio_final = sumaPromedios(ef, ep, tf)
 print("Su promedio final es: ", promedio_final)