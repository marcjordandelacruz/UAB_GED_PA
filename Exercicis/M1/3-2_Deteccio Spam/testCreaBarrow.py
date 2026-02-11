import os
from typing import List, Dict

# Si crea_bow està en un altre fitxer, importa-la així:
# from el_teu_fitxer import crea_bow

from spam import crea_bow

def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def test_crea_bow_basic():
    nom = "msg_test.txt"
    write_file(nom, "hola hola adeu\nhola\n")
    vocab = ["hola", "adeu"]

    bow = crea_bow(nom, vocab)
    print("Basic bow:", bow)

    # Esperat: hola=3, adeu=1
    assert bow.get("hola") == 3, f"Esperava hola=3 i m'ha sortit {bow.get('hola')}"
    assert bow.get("adeu") == 1, f"Esperava adeu=1 i m'ha sortit {bow.get('adeu')}"

    os.remove(nom)
    print("✅ test_crea_bow_basic OK")

def test_crea_bow_file_not_found():
    
    try:
        crea_bow("no_existeix_123.txt", ["hola"])
        assert False, "Hauria d'haver llençat FileNotFoundError"
    except FileNotFoundError:
        print("✅ test_crea_bow_file_not_found OK")

def test_crea_bow_edge_substring():
    """
    Aquest test et diu si estàs comptant 'substrings' en lloc de paraules.
    Si el professor vol coincidència de paraula exacta, 'ho' NO hauria de comptar dins 'hola'.
    """
    nom = "msg_test2.txt"
    write_file(nom, "hola\n")
    vocab = ["ho"]

    bow = crea_bow(nom, vocab)
    print("Substring bow:", bow)

    # Si vols paraules exactes, l'esperat seria que NO aparegui "ho"
    # (aquest assert probablement FALLARÀ amb el teu codi actual, i és normal)
    assert "ho" not in bow, "Estàs comptant substrings. Si vols paraules exactes, això és un error."

    os.remove(nom)
    print("✅ test_crea_bow_edge_substring OK")

if __name__ == "__main__":
    test_crea_bow_basic()
    test_crea_bow_file_not_found()

    # Activa aquest només si el vostre enunciat demana paraules exactes:
    # test_crea_bow_edge_substring()