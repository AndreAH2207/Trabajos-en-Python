import random

# Genera una lista de números aleatorios en el rango de 1 a 100
random_numbers = [random.randint(1, 100) for _ in range(200)]

# Ordena la lista de forma descendente
random_numbers.sort(reverse=True)

# Crea una lista sin repeticiones
unique_numbers = list(set(random_numbers))

# Imprime los resultados
print("Lista de números aleatorios en orden descendente:")
print(random_numbers)
print("\nLista de números únicos:")
print(unique_numbers)