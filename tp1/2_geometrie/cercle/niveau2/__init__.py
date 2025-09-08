import check50
import check50.c

check50.import_checks("../cercle/niveau1")
from niveau1 import *

@check50.check(cercle0)
def rayonNegatif():
    """Cercle : Rayon négatif"""
    check_negatif("-0.5")

def check_negatif(rayon: str):
    with exercise_cwd():
        check50.run("./cercle").stdin(rayon).stdout("ERREUR : Valeurs negatives interdites.")