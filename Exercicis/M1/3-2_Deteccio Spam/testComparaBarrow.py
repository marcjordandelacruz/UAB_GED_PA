from typing import Dict

# importa la funció:
# from spam import compara_bow

from spam import compara_bow

def approx_equal(a: float, b: float, eps: float = 1e-9) -> bool:
    return abs(a - b) <= eps

def test_compara_bow_identics():
    bow1 = {"hola": 2, "adeu": 1}
    bow2 = {"hola": 2, "adeu": 1}
    d = compara_bow(bow1, bow2)
    print("identics:", d)
    assert approx_equal(d, 1.0), f"Esperava 1.0 i ha sortit {d}"
    print("✅ test_compara_bow_identics OK")

def test_compara_bow_disjunts():
    bow1 = {"hola": 2}
    bow2 = {"adeu": 3}
    d = compara_bow(bow1, bow2)
    print("disjunts:", d)
    assert approx_equal(d, 0.0), f"Esperava 0.0 i ha sortit {d}"
    print("✅ test_compara_bow_disjunts OK")

def test_compara_bow_parcial():
    # solapament: min(2,1)=1
    # sum1=2+1=3, sum2=1+5=6, min=3
    # distancia = 1/3 = 0.3333333333...
    bow1 = {"hola": 2, "adeu": 1}
    bow2 = {"hola": 1, "spam": 5}
    d = compara_bow(bow1, bow2)
    print("parcial:", d)
    assert approx_equal(d, 1/3), f"Esperava {1/3} i ha sortit {d}"
    print("✅ test_compara_bow_parcial OK")

def test_compara_bow_escalat():
    # mateixes paraules i proporció; el min a cada clau és bow1, i min(sum)=sum(bow1)
    bow1 = {"a": 1, "b": 1}
    bow2 = {"a": 2, "b": 2}
    d = compara_bow(bow1, bow2)
    print("escalat:", d)
    assert approx_equal(d, 1.0), f"Esperava 1.0 i ha sortit {d}"
    print("✅ test_compara_bow_escalat OK")

def test_compara_bow_suma_zero():
    # Edge: min(sum(...)) = 0 -> ZeroDivisionError amb la teva implementació actual
    bow1 = {}
    bow2 = {"hola": 1}

    try:
        d = compara_bow(bow1, bow2)
        print("suma_zero:", d)
        # Decideix una convenció; habitualment 0.0 (no hi ha info / no hi ha solapament)
        assert d == 0.0, f"Esperava 0.0 (convenció) i ha sortit {d}"
        print("✅ test_compara_bow_suma_zero OK (sense excepció)")
    except ZeroDivisionError:
        print("⚠️ test_compara_bow_suma_zero: ZeroDivisionError (has d'afegir un cas especial)")

if __name__ == "__main__":
    test_compara_bow_identics()
    test_compara_bow_disjunts()
    test_compara_bow_parcial()
    test_compara_bow_escalat()
    test_compara_bow_suma_zero()