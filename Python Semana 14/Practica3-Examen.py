import random

class CEncuesta:
    def __init__(self, edad=0, sexo="", tipo="", nivel=""):
        self.edad = edad
        self.sexo = sexo
        self.tipo = tipo
        self.nivel = nivel

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    def set_sexo(self,sexo):
        self.sexo = sexo
    
    def get_sexo(self):
        return self.sexo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_nivel(self,nivel):
        self.nivel = nivel

    def get_nivel(self):
        return self.nivel

    def consultar_encuesta(self):
        print("")
        print(f"Edad  : {self.edad}")
        print(f"Sexo  : {self.sexo}")
        print(f"Tipo  : {self.tipo}")
        print(f"Nivel : {self.nivel}")
        print("")

lista = []

def main():
    print("")
    N = int(input("Ingresar la cantidad de encuestas realizadas: "))
    print("")

    if N < 0  or N > 80:
        print("Ingrese un numero entre 0 y 80")
        print("")
        return main()
    
    for i in range(N):
        print("")
        print(f"Estudiante {i+1}")
        edad = random.randint(17,65)
        sexo = random.choice(["Femenino","Masculino"])
        tipo = random.choice(["Blackboard", "Canvas", "Moodle"])
        nivel= random.choice(["Bueno", "Regular", "Malo"])

        encuesta =  CEncuesta(edad, sexo, tipo, nivel)
        lista.append(encuesta)
        encuesta.consultar_encuesta()

    no_mayores = sum(1 for encuesta in lista if encuesta.get_edad() < 60)
    print(f"La cantidad de estudiantes que no son adultos mayores es de {no_mayores}")

    edad_canvas = [encuesta.get_edad() for encuesta in lista if encuesta.get_tipo() == "Canvas"]
    promedio = sum(edad_canvas) / max(len(edad_canvas), 1)
    print(f"El promedio de edades de los estudiantes que utilizan la plataforma Canvas es de {promedio}" )


    frecuencia_nivel = {nivel: 0 for nivel in ["Bueno", "Regular", "Malo"]}
    
    for encuesta in lista:
        frecuencia_nivel[encuesta.nivel]+=1
    menor_frecuencia_nivel = min(frecuencia_nivel, key=frecuencia_nivel.get)
    print(f"Nivel de satisfacción con menor frecuencia: {menor_frecuencia_nivel}")

    edad_mujeres = [encuesta.get_edad() for encuesta in lista if encuesta.get_tipo() != "Moodle" and encuesta.get_sexo() == "Femenino"]
    edad_mujer_mas_joven_no_usa_moodle = min(edad_mujeres) 

    print(f"La edad de la mujer mas joven que no usa Moodle es de {edad_mujer_mas_joven_no_usa_moodle}")
    print("")
    
main()




    
