# Función principal para registrar votos y encontrar al ganador

def main():
    n = int(input("Ingrese la cantidad de votantes: "))
    candidatos = {
        1: "Sergio Massa",
        2: "Javier Milei",
        3: "Patricia Bullrich",
        4: "Juan Schiarett",
        5: "Myriam Bregman"
    
    }
    votos = {candidato: 0 for candidato in candidatos.values()}

    for i in range(n):
        print(f"\nVotante {i + 1}, elija un candidato:")
        for candidato_id, candidato_nombre in candidatos.items():
            print(f"{candidato_id}: {candidato_nombre}")

        voto = int(input("Ingrese el número del candidato elegido: "))

        # Verificar si el voto es válido
        if voto in candidatos:
            votos[candidatos[voto]] += 1
        else:
            print("Voto no válido. Intente de nuevo.")

    # Encontrar al candidato ganador
    porcentaje_ganador = 0
    ganador = None

    for candidato, votos_candidato in votos.items():
        porcentaje = (votos_candidato / n) * 100
        if porcentaje > porcentaje_ganador:
            ganador = candidato
            porcentaje_ganador = porcentaje

    # Imprimir los resultados
    print("\nResultados de la votación:")
    print("")
    for candidato, votos_candidato in votos.items():
        porcentaje = (votos_candidato / n) * 100
        print(f"{candidato}: {votos_candidato} votos ({porcentaje}%)")

    print(f"\nEl ganador es {ganador} con un {porcentaje_ganador}% de los votos.")

#main
main()