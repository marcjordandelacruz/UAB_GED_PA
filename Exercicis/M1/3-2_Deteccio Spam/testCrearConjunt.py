import os
import shutil
from typing import List, Dict, Tuple

# Ajusta l'import al teu mòdul:
# from spam import crea_conjunt_entrenament, crea_bow
from spam import crea_conjunt_entrenament, crea_bow

def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def dict_from_training_set(training_set):
    """
    Converteix la llista de tuples a un diccionari:
    nom_fitxer -> (bow, etiqueta)
    """
    out = {}
    for (fname, bow, is_spam) in training_set:
        out[fname] = (bow, is_spam)
    return out

def test_crea_conjunt_entrenament_basic():
    # 1) Muntem un directori train temporal
    train_dir = "train_test_dir"
    os.makedirs(train_dir, exist_ok=True)

    # 2) Creem fitxers
    write_file(os.path.join(train_dir, "001_spm.txt"), "hola spam spam\n")
    write_file(os.path.join(train_dir, "002_ok.txt"), "hola hola\n")
    write_file(os.path.join(train_dir, "003.txt"), "spam\n")

    vocab = ["hola", "spam"]

    # 3) Executem
    ts = crea_conjunt_entrenament(train_dir, vocab)
    print("training_set:", ts)

    # 4) Validacions bàsiques
    assert isinstance(ts, list), "Ha de retornar una llista"
    assert len(ts) == 3, f"Esperava 3 elements i n'he rebut {len(ts)}"

    m = dict_from_training_set(ts)

    # Ha d'incloure exactament aquests fitxers (ordre pot variar)
    assert set(m.keys()) == {"001_spm.txt", "002_ok.txt", "003.txt"}, f"Noms inesperats: {set(m.keys())}"

    # 5) Validar etiquetes segons el criteri 'spm' al nom
    assert m["001_spm.txt"][1] is True, "001_spm.txt hauria de ser spam (True)"
    assert m["002_ok.txt"][1] is False, "002_ok.txt hauria de ser no spam (False)"
    assert m["003.txt"][1] is False, "003.txt hauria de ser no spam (False) segons el teu criteri actual"

    # 6) Validar BoW (assumint que crea_bow compta ocurrències i inclou totes les paraules del vocab a 0)
    bow_1 = m["001_spm.txt"][0]
    bow_2 = m["002_ok.txt"][0]
    bow_3 = m["003.txt"][0]

    assert bow_1.get("hola") == 1 and bow_1.get("spam") == 2, f"BoW incorrecte per 001_spm.txt: {bow_1}"
    assert bow_2.get("hola") == 2 and bow_2.get("spam") == 0, f"BoW incorrecte per 002_ok.txt: {bow_2}"
    assert bow_3.get("hola") == 0 and bow_3.get("spam") == 1, f"BoW incorrecte per 003.txt: {bow_3}"

    # 7) Neteja
    shutil.rmtree(train_dir)
    print("✅ test_crea_conjunt_entrenament_basic OK")

if __name__ == "__main__":
    test_crea_conjunt_entrenament_basic()