import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "01_moyenne"
MAIN = "moyenne.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """moyenne.c existe"""
    with exercise_cwd():
        check50.exists("moyenne.c")


@check50.check(exists)
def compiles():
    """moyenne.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("moyenne.c", lcs50=True)


@check50.check(compiles)
def moyenne_suite_1_a_10():
    """Moyenne de 1..10 = 5.50"""
    check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "5.50")


@check50.check(compiles)
def moyenne_notes_identiques():
    """Moyenne de 10 notes à 12 = 12.00"""
    check([12] * 10, "12.00")


@check50.check(compiles)
def moyenne_avec_decimales():
    """Moyenne avec notes décimales"""
    check([10.5, 12.5, 8, 15, 9, 11, 13.5, 7.5, 14, 10], "11.10")


# Helpers
def check(notes, moyenne_attendue: str):
    with exercise_cwd():
        actual = check50.run("./moyenne")
        for n in notes:
            actual = actual.stdin(str(n))
        actual.stdout(f"{moyenne_attendue}", regex=False)
