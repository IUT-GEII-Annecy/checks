import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "03_cinema_occupation"
MAIN = "cinema_occupation.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """cinema_occupation.c existe"""
    with exercise_cwd():
        check50.exists("cinema_occupation.c")


@check50.check(exists)
def compiles():
    """cinema_occupation.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("cinema_occupation.c", lcs50=True)


@check50.check(compiles)
def places_libres_et_taux():
    """Indices libres dans l'ordre + taux d'occupation arrondi"""
    with exercise_cwd():
        actual = check50.run("./cinema_occupation")
        actual = actual.stdin("5")
        for v in [1, 0, 1, 1, 0]:
            actual = actual.stdin(str(v))
        actual.stdout("1", regex=False).stdout("4", regex=False).stdout("60", regex=False)


@check50.check(compiles)
def complet():
    """Rangée complète : affiche Complet"""
    with exercise_cwd():
        actual = check50.run("./cinema_occupation")
        actual = actual.stdin("3")
        for v in [1, 1, 1]:
            actual = actual.stdin(str(v))
        actual.stdout("Complet").stdout("100", regex=False)
