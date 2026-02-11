import math


def suma_acumulada(llista):
    l = []
    for i in range(len(llista)):
        l.append(sum(llista[:i+1]))
    return l




def factorial_llista(llista):
    l = []
    for i in range(len(llista)):
        l.append(math.factorial(llista[i]))
    return l




def primers(llista):
    l = []
    for i in range(len(llista)):
        if llista[i] % 2 == 1 or llista[i] / 2 == 1:
            l.append(llista[i])
    return l


def elimina_duplicats(llista):
    l = []
    for i in range(len(llista)):
        if llista[i] not in l:
            l.append(llista[i])
    return l


def binari_decimal(binari):
    return binari