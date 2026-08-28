import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "06_stock_clamp"
MAIN = "stock_clamp.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """stock_clamp.c existe"""
    with exercise_cwd():
        check50.exists("stock_clamp.c")


@check50.check(exists)
def compiles():
    """stock_clamp.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("stock_clamp.c", lcs50=True)


@check50.check(compiles)
def clamp_min_et_max():
    """Valeurs bornées entre minQ=1 et maxQ=8"""
    with exercise_cwd():
        actual = check50.run("./stock_clamp").stdin("5")
        for v in [0, 3, 10, 7, 2]:
            actual = actual.stdin(str(v))
        actual = actual.stdin("1").stdin("8")
        actual.stdout("1 3 8 7 2", regex=False)


@check50.check(compiles)
def valeurs_deja_dans_les_bornes():
    """Aucune valeur à corriger : tableau inchangé"""
    with exercise_cwd():
        actual = check50.run("./stock_clamp").stdin("3")
        for v in [2, 4, 6]:
            actual = actual.stdin(str(v))
        actual = actual.stdin("0").stdin("10")
        actual.stdout("2 4 6", regex=False)
