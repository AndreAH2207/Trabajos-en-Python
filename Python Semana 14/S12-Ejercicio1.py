class Alumno:
    def __init__(self, codigo, nombre, lb1, Ea, Lb2, Tf, Pa, Eb):
        self.codigo = codigo
        self.nombre = nombre
        self.lb1 = lb1
        self.Ea = Ea
        self.Lb2 = Lb2
        self.Tf = Tf
        self.Pa = Pa
        self.Eb = Eb

    def calcular_promedio(self):
        return (self.lb1 * 0.15 + self.Ea * 0.2 + self.Lb2 * 0.15 + self.Tf * 0.25 + self.Pa * 0.05 + self.Eb * 0.20)

    def to_string(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}"

class Administrador:
    def __init__(self, N):
        self.N = N
        self.alumnos = []

    def insertar(self, alumno):
        if len(self.alumnos) < self.N:
            self.alumnos.append(alumno)
        else:
            print("No se pueden agregar más alumnos. La lista está llena.")

    def listar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno.to_string())
            print(f"Promedio: {alumno.calcular_promedio()}")

# Función principal
def main():
    N = int(input("Ingrese el número de alumnos a registrar: "))
    administrador = Administrador(N)

    for i in range(N):
        print(f"Ingrese los datos del alumno {i + 1}:")
        codigo = input("Código del alumno: ")
        nombre = input("Nombre del alumno: ")
        lb1 = float(input("Nota de práctica laboratorio 1: "))
        Ea = float(input("Nota de evaluación parcial: "))
        Lb2 = float(input("Nota de práctica laboratorio 2: "))
        Tf = float(input("Nota del trabajo final: "))
        Pa = float(input("Nota de participación: "))
        Eb = float(input("Nota de evaluación final: "))

        alumno = Alumno(codigo, nombre, lb1, Ea, Lb2, Tf, Pa, Eb)
        administrador.insertar(alumno)

    print("\nListado de alumnos y sus promedios:\n")
    administrador.listar_alumnos()

main()         

'''
class Alumno:
  codigo = ""
  nombre = ""
  lb1 = ""
  la =""
  lb2 =""
  tf= ""
  pa =""
  eb=""

def __init__(self, codigo, nombre, lb1, la, lb2, tf, pa, eb):
    self.codigo = codigo
    self.nombre = nombre
    self.lb1 = lb1
    self.la = la
    self.lb2 = lb2
    self.tf =tf
    self.pa =pa
    self.eb =eb

def calcularPromedio(self):
    return (self.lb1*0.15 + self.la*0.2 + self.lb2*0.15 + self.tf*0.25+
            elf.pa*0.05 + self.eb*0.20)
    def to_string(self): # self siempre va en cada método, se use o no
        return self.codigo + self.nombre


class Administrador:
  alumnos = []
  n = 0

def __init__(self, n):
    self.n = n

def insertar(self, alumno):
    if(len(self.alumnos)<self.n):
        self.alumnos.append(alumno)
    
def getAlumnos(self):
    return self.alumnos

#test

administrador = Administrador(2) #llama al constructor init
alumno1 = Alumno(20212345, "Pepe",10,18,14,18,19,12)
alumno2 = Alumno(20212225, "Carlos",19,13,14,18,10,17)
administrador.insertar(alumno1)
administrador.insertar(alumno2)
administrador.insertar(alumno2)
lista = administrador.getAlumnos()

for a in lista:
  print(a.codigo,"\t\t" ,a.nombre,"\t\t" ,a.calcularPromedio())
                                                  

'''

'''

def calcular_promedio(notas):
    # Definir los pesos de cada nota
    pesos = {
        'Lb1': 0.15,
        'Ea' : 0.20,
        'Lb2': 0.15,
        'Tf' : 0.25,
        'Pa' : 0.05,
        'Eb' : 0.20
    }
    
    # Calcular el promedio ponderado
    promedio = sum(notas[nota] * peso for nota, peso in pesos.items())
    return promedio

# Función principal para registrar alumnos y calcular promedios
def RegistrarAlumnos():
    n = int(input("Ingrese la cantidad de alumnos: "))
    alumnos = []

    for i in range(n):
        print(f"\nIngrese los datos del alumno {i + 1}:")
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        notas = {
            'Lb1': float(input("Nota de práctica laboratorio 1: ")),
            'Ea' : float(input("Nota de evaluación parcial    : ")),
            'Lb2': float(input("Nota de práctica laboratorio 2: ")),
            'Tf' : float(input("Nota de trabajo final         : ")),
            'Pa' : float(input("Nota de participación         : ")),
            'Eb' : float(input("Nota de evaluación final      : "))
        }

        # Calcular el promedio del alumno
        promedio_alumno = calcular_promedio(notas)

        # Agregar al alumno a la lista de alumnos
        alumno = {
            'Código': codigo,
            'Nombre': nombre,
            'Notas': notas,
            'Promedio': promedio_alumno
        }
        alumnos.append(alumno)

    # Imprimir los resultados
    print("\nResultados:")
    for alumno in alumnos:
        print(f"\nCódigo: {alumno['Código']}")
        print(f"Nombre: {alumno['Nombre']}")
        print("Notas:")
        for nota, valor in alumno['Notas'].items():
            print(f"{nota}: {valor}")
        print(f"Promedio: {alumno['Promedio']}")


RegistrarAlumnos()

'''