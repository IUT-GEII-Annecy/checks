import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "02_filtre_notes"
MAIN = "filtre_notes.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """filtre_notes.c existe"""
    with exercise_cwd():
        check50.exists("filtre_notes.c")


@check50.check(exists)
def compiles():
    """filtre_notes.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("filtre_notes.c", lcs50=True)


@check50.check(compiles)
def notes_filtrees_ordre():
    """Notes au-dessus du seuil affichées dans l'ordre d'origine"""
    with exercise_cwd():
        actual = check50.run("./filtre_notes")
        for n in [10, 8, 15, 6, 12]:
            actual = actual.stdin(str(n))
        actual = actual.stdin("9")
        actual.stdout("10.00", regex=False).stdout("15.00", regex=False).stdout("12.00", regex=False)


@check50.check(compiles)
def aucune_note():
    """Aucune note au-dessus du seuil"""
    with exercise_cwd():
        actual = check50.run("./filtre_notes")
        for n in [5, 5, 5]:
            actual = actual.stdin(str(n))
        actual = actual.stdin("100")
        actual.stdout("Aucune")


@check50.check(compiles)
def compte_correct():
    """Nombre de notes affichées correct"""
    with exercise_cwd():
        actual = check50.run("./filtre_notes")
        for n in [10, 8, 15, 6, 12]:
            actual = actual.stdin(str(n))
        actual = actual.stdin("9")
        actual.stdout("3", regex=False)
