def interseccio(llista1, llista2):
    l = []
    for i in range(len(llista1)):
        if llista1[i] in llista2:
            l.append(llista1[i])
    return l


def unio(llista1, llista2):
    l = []
    for i in range(len(llista1)):
        l.append(llista1[i])
    for i in range(len(llista2)):
        if llista2[i] not in l:
            l.append(llista2[i])
    return l

def multiplicacio_llistes(llista1, llista2):
    n = min(len(llista1), len(llista2))
    resultat = []
    for i in range(n):
        resultat.append(llista1[i] * llista2[i])
    return resultat
            


def multiplicacio_elements(llista1, llista2):
    return [[x * y for y in llista2] for x in llista1]



def distancia_hamming(binari1, binari2):
    if len(binari1) != len(binari2):
        raise ValueError("Les dues llistes han de tenir la mateixa longitud.")
    d = 0
    for b1, b2 in zip(binari1, binari2):
        if b1 != b2:
            d += 1
    return d
