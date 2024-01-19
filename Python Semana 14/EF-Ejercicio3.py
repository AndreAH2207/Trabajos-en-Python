import random

class CEncuesta:
    def __init__(self, edad=0, sexo="", plataforma="", satisfaccion=""):
        self.edad = edad
        self.sexo = sexo
        self.plataforma = plataforma
        self.satisfaccion = satisfaccion

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_sexo(self):
        return self.sexo

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_plataforma(self):
        return self.plataforma

    def set_plataforma(self, plataforma):                                                                                   
        self.plataforma = plataforma

    def get_satisfaccion(self):
        return self.satisfaccion

    def set_satisfaccion(self, satisfaccion):
        self.satisfaccion = satisfaccion

    def consultarEncuesta(self):
        print(f"Edad                 : {self.edad}")
        print(f"Sexo                 : {self.sexo}")
        print(f"Plataforma LMS       : {self.plataforma}")
        print(f"Nivel de satisfacción: {self.satisfaccion}")


N = int(input("Ingrese la cantidad de encuestas realizadas (no mayor a 80): "))

if N < 1 or N > 80:
    print("La cantidad de encuestas debe estar entre 1 y 80.")
else:

    encuestas = []

    for _ in range(N):
        edad = random.randint(17, 65)
        sexo = random.choice(["M", "F"])
        plataforma = random.choice(["Blackboard", "Canvas", "Moodle"])
        satisfaccion = random.choice(["Bueno", "Regular", "Malo"])
        encuesta = CEncuesta(edad, sexo, plataforma, satisfaccion)
        encuestas.append(encuesta)

    no_adultos_mayores = sum(1 for encuesta in encuestas if encuesta.edad < 60)

    promedio_edad_canvas = 0
    contador_canvas = 0
    for encuesta in encuestas:
        if encuesta.plataforma == "Canvas":
            promedio_edad_canvas += encuesta.edad
            contador_canvas += 1
    if contador_canvas > 0:
        promedio_edad_canvas /= contador_canvas

    frecuencia_satisfaccion = {}
    for encuesta in encuestas:
        satisfaccion = encuesta.satisfaccion
        if satisfaccion in frecuencia_satisfaccion:
            frecuencia_satisfaccion[satisfaccion] += 1
        else:
            frecuencia_satisfaccion[satisfaccion] = 1

    niveles_menor_frecuencia = [s for s, f in frecuencia_satisfaccion.items() if f == min(frecuencia_satisfaccion.values())]

    edad_mujer_mas_joven = None
    for encuesta in encuestas:
        if encuesta.sexo == "F" and encuesta.plataforma != "Moodle":
            if edad_mujer_mas_joven is None or encuesta.edad < edad_mujer_mas_joven:
                edad_mujer_mas_joven = encuesta.edad

    # Mostrar resultados
    for encuesta in encuestas:
        encuesta.consultarEncuesta()
        print(" ")

    print(" ")
    print(f"Estudiantes no adultos mayores                      : {no_adultos_mayores}")
    print(f"Promedio de edad de estudiantes que utilizan Canvas : {promedio_edad_canvas}")
    print(f"Nivel(es) de satisfacción con menor frecuencia      : {', '.join(niveles_menor_frecuencia)}")
    if edad_mujer_mas_joven is not None:
        print(f"Edad de la mujer más joven que no utiliza Moodle: {edad_mujer_mas_joven}")
    else:
        print("No hay mujeres jóvenes que no utilicen Moodle en la encuesta.")