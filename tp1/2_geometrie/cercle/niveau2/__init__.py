import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext  # <-- standard lib



EXER_DIR = "2_geometrie/"
MAIN = "cercle.c"


def exercise_cwd():
    """
    Si hello.c est à la racine → pas de cd.
    Si hello.c est dans 0_hello/ → cd 0_hello.
    Sinon → erreur explicite.
    """
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)   # <-- au lieu de check50.cd(...)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")
        
check50.import_checks("../cercle/niveau1")
from niveau1 import *

@check50.check(cercle0)
def rayonNegatif():
    """Cercle : Rayon négatif"""
    check_negatif("-0.5")

def check_negatif(rayon: str):
    with exercise_cwd():
        check50.run("./cercle").stdin(rayon).stdout("ERREUR : Valeurs negatives interdites.")
