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


@check50.check()
def cercle_exists():
    """Cercle : cercle.c existe"""
    with exercise_cwd():
        check50.exists("cercle.c")


@check50.check(cercle_exists)
def cercle_compiles():
    """Cercle : cercle.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("cercle.c", lcs50=True)


@check50.check(cercle_compiles)
def rayon6():
    """Cercle : Cercle de rayon 6"""
    check_debug(rayon="6", circonference="37.70", aire="113.10")


@check50.check(cercle_compiles)
def rayon100():
    """Cercle : Cercle de rayon 100"""
    check_debug(rayon="100", circonference="628.32", aire="31415.93")

@check50.check(cercle_compiles)
def cercle0():
    """Cercle : Cercle de rayon nul"""
    check_debug(rayon="0", circonference="0.00", aire="0.00")

@check50.check(cercle0)
def rayonNegatif():
    """Cercle : Rayon négatif"""
    check_negatif("-0.5")


# Helpers
def check_debug(rayon: str, circonference: str, aire: str):
    with exercise_cwd():
        actual = check50.run("./cercle").stdin(rayon).stdout(f"Aire : {aire}\n").stdout(f"Perimetre : {circonference}")
    
def check_negatif(rayon: str):
    with exercise_cwd():
        check50.run("./cercle").stdin(rayon).stdout("ERREUR : Valeurs negatives interdites.")

