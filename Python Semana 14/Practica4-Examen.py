import random
import matplotlib.pyplot as plt

def generar_datos():
    ingresos = [random.randint(5000, 20000) for _ in range(24)]
    gastos = [random.randint(3000, 15000) for _ in range(24)]
    return ingresos, gastos

def crear_grafico(ingresos, gastos):
    meses = [f'Mes {i+1}' for i in range(24)]

    plt.barh(meses, ingresos, color='green', label='Ingresos')
    plt.barh(meses, gastos, color='red', label='Gastos')

    plt.xlabel('Cantidad')
    plt.ylabel('Meses')
    plt.title('Evolución de ingresos y gastos')
    plt.legend()
    plt.show()

def main():
    ingresos, gastos = generar_datos()
    crear_grafico(ingresos, gastos)

if __name__ == "__main__":
    main()