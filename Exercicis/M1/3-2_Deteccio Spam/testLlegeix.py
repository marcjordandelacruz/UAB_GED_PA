import os


# IMPORTA la teva funció:
# si està al mateix fitxer, no cal importar
# si està en un altre fitxer, per exemple funcs.py:
# from funcs import llegeix_vocabulari

from spam import llegeix_vocabulari
    
def prova_llegeix_vocabulari():
    nom = "vocab_test.txt"

    # 1) Preparem un fitxer controlat
    with open(nom, "w", encoding="utf-8") as f:
        f.write("hola\n")
        f.write("adeu\n")
        f.write("spam\n")

    # 2) Executem
    v = llegeix_vocabulari(nom)

    # 3) Mostrem
    print("Resultat:", v)

    # 4) Validem automàticament
    assert v == ["hola", "adeu", "spam"], "ERROR: La llista no coincideix amb l'esperat"

    # 5) Neteja
    os.remove(nom)
    print("✅ Prova 1 OK")

def prova_fitxer_inexistent():
    try:
        llegeix_vocabulari("aquest_fitxer_no_existeix.txt")
        assert False, "ERROR: Hauria d'haver fallat amb FileNotFoundError"
    except FileNotFoundError:
        print("✅ Prova 2 (fitxer inexistent) OK")

if __name__ == "__main__":
    prova_llegeix_vocabulari()
    prova_fitxer_inexistent()