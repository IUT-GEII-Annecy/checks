import check50
import check50.c

from pathlib import Path
from contextlib import chdir, nullcontext  # <-- standard lib

EXER_DIR = "2_geometrie"
MAIN = "rectangle.c"

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

@check50.check()
def rectangle_exists():
    """Rectangle : rectangle.c existe"""
    with exercise_cwd():
        check50.exists("rectangle.c")


@check50.check(rectangle_exists)
def rectangle_compiles():
    """Rectangle : rectangle.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("rectangle.c", lcs50=True)


@check50.check(rectangle_compiles)
def aire6x5():
    """Rectangle : Un rectangle de 6 par 5 a une aire de 30.00"""
    check_debug(largeur="6", longueur="5", aire="30.00")


@check50.check(rectangle_compiles)
def aire2x8():
    """Rectangle : Un rectangle de 2 par 8 a une aire de 16.00"""
    check_debug(largeur="2", longueur="8", aire="16.00")

@check50.check(rectangle_compiles)
def aire1150():
    """Rectangle : Un rectangle de 11.5 par 100 a une aire de 1150.00"""
    check_debug(largeur="11.5", longueur="100", aire="1150.00")


# Helpers
def check_debug(largeur: str, longueur: str, aire: str):
    with exercise_cwd():
        actual = check50.run("./rectangle").stdin(largeur).stdin(longueur).stdout(f"L'aire du rectangle est de {aire}")


@check50.check(rectangle_compiles)
def largeurNegative():
    """Rectangle : Largeur négative"""
    check_negative(largeur="-0.5", longueur="100")

@check50.check(largeurNegative)
def longueurNegative():
    """Rectangle : Longueur négative"""
    check_negative(largeur="0.5", longueur="-100")  

@check50.check(longueurNegative)
def valeursNegatives():
    """Rectangle : Les deux valeurs négative"""
    check_negative(largeur="-0.5", longueur="-100") 

@check50.check(valeursNegatives)
def aireNulle():
    """Rectangle : Aire Nulle"""
    check_debug(largeur="0", longueur="100", aire="0.00")
    check_debug(largeur="100", longueur="0", aire="0.00")
# Helpers

def check_negative(largeur: str, longueur: str):
    with exercise_cwd():
        actual = check50.run("./rectangle").stdin(largeur).stdin(longueur).stdout(f"ERREUR : Valeur negative interdite.")