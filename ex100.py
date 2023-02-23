from random import randint
from time import sleep


def sorteio():
    numeros = []
    for i in range(5):
        numeros.append(randint(1, 10))
        print(f"Sorteando 5 valores da lista: {numeros}. Pronto.")
        sleep(0.3)
    return numeros


def soma_par():
    soma_pares = 0
    numeros = sorteio()
    for numero in numeros:
        if numero % 2 == 0:
            soma_pares += numero
    print(f"Soma dos valores pares de {numeros}: {soma_pares}")


soma_par()
