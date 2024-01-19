import random

class EncuestaEmpleado:
    def __init__(self, edad=0, tos=False, fiebre=False, cansancio=False):
        self.edad = edad
        self.tos = tos
        self.fiebre = fiebre
        self.cansancio = cansancio

    def generar_datos_aleatorios(self):
        self.edad = random.randint(18, 75)
        self.tos = random.choice([True, False])
        self.fiebre = random.choice([True, False])
        self.cansancio = random.choice([True, False])

    def mostrar_datos(self):
        print(f"Edad: {self.edad}")
        print(f"Tos: {1 if self.tos else 0}")
        print(f"Fiebre: {1 if self.fiebre else 0}")
        print(f"Cansancio: {1 if self.cansancio else 0}")

def genera_y_muestra_lista(N):
    lista_empleados = []
    for _ in range(N):
        empleado = EncuestaEmpleado()
        empleado.generar_datos_aleatorios()
        lista_empleados.append(empleado)

        print(f"Empleado {_ + 1}")
        empleado.mostrar_datos()
        print()

    return lista_empleados

def hallar_mayor_y_menor(lista_empleados):
    edades = [empleado.edad for empleado in lista_empleados]
    mayor_edad = max(edades)
    menor_edad = min(edades)
    return mayor_edad, menor_edad

def porcentaje_con_y_sin_lista(lista_empleados):
    menores_25_con_covid = sum(1 for empleado in lista_empleados if empleado.edad < 25 and empleado.tos and empleado.fiebre and empleado.cansancio)
    mayores_50_sin_covid = sum(1 for empleado in lista_empleados if empleado.edad > 50 and (not empleado.tos or not empleado.fiebre or not empleado.cansancio))
    
    total_menores_25 = sum(1 for empleado in lista_empleados if empleado.edad < 25)
    total_mayores_50 = sum(1 for empleado in lista_empleados if empleado.edad > 50)
    
    porcentaje_con_covid = (menores_25_con_covid / total_menores_25) * 100 if total_menores_25 > 0 else 0
    porcentaje_sin_covid = (mayores_50_sin_covid / total_mayores_50) * 100 if total_mayores_50 > 0 else 0
    
    return porcentaje_con_covid, porcentaje_sin_covid

def promedio_edad_por_lista(lista_empleados):
    edades_tos = [empleado.edad for empleado in lista_empleados if empleado.tos]
    edades_fiebre = [empleado.edad for empleado in lista_empleados if empleado.fiebre]
    edades_cansancio = [empleado.edad for empleado in lista_empleados if empleado.cansancio]

    promedio_edad_tos = sum(edades_tos) / len(edades_tos) if len(edades_tos) > 0 else 0
    promedio_edad_fiebre = sum(edades_fiebre) / len(edades_fiebre) if len(edades_fiebre) > 0 else 0
    promedio_edad_cansancio = sum(edades_cansancio) / len(edades_cansancio) if len(edades_cansancio) > 0 else 0

    return promedio_edad_tos, promedio_edad_fiebre, promedio_edad_cansancio

def main():
    N = int(input("Ingrese el numero de empleados: "))
    
    lista_empleados = genera_y_muestra_lista(N)
    
    mayor_edad, menor_edad = hallar_mayor_y_menor(lista_empleados)
    print(f"\nMayor Edad: {mayor_edad}, Menor Edad: {menor_edad}")
    
    porcentaje_con_covid, porcentaje_sin_covid = porcentaje_con_y_sin_lista(lista_empleados)
    print(f"\nPorcentaje de empleados menores de 25 con COVID-19: {porcentaje_con_covid}%")
    print(f"Porcentaje de empleados mayores de 50 sin COVID-19: {porcentaje_sin_covid}%")
    
    promedio_edad_tos, promedio_edad_fiebre, promedio_edad_cansancio = promedio_edad_por_lista(lista_empleados)
    print(f"\nPromedio de Edad para empleados con Tos: {promedio_edad_tos}")
    print(f"Promedio de Edad para empleados con Fiebre: {promedio_edad_fiebre}")
    print(f"Promedio de Edad para empleados con Cansancio: {promedio_edad_cansancio}")

if __name__ == "__main__":
    main()