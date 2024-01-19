
'''
Realizar una aplicación en Python que permita:
Generar una lista (máximo 200 elementos) de números positivos generados
aleatoriamente.
Los números deben estar en el rango de 1 a 100.
Luego ordene la lista de forma descendente.
Finalmente, genere una lista de los números, pero sin repeticiones
'''

import random

def GenerateList(n):
    lista = []
    for i in range(0,n):
        lista.append(random.randint(1,100))
    return lista

def generateListsWithoutRepetitions(lista):
    listWithoutRepetition = []
    for number in lista:
        if number not in listWithoutRepetition:
            listWithoutRepetition.append(number)
    return listWithoutRepetition

def showList(lista):
    print("**Lista**")
    for number in lista:
        print(number)

#main

numbers = GenerateList(200)
showList(numbers)
numbers.sort(reverse=True)
withoutRepetition = generateListsWithoutRepetitions(numbers)
showList(withoutRepetition)




