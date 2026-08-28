import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "08_tarifs_selection_sort"
MAIN = "tarifs_selection_sort.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """tarifs_selection_sort.c existe"""
    with exercise_cwd():
        check50.exists("tarifs_selection_sort.c")


@check50.check(exists)
def compiles():
    """tarifs_selection_sort.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("tarifs_selection_sort.c", lcs50=True)


@check50.check(compiles)
def tri_correct():
    """Tri croissant correct (exemple de l'énoncé)"""
    with exercise_cwd():
        actual = check50.run("./tarifs_selection_sort").stdin("6")
        for v in [500, 200, 400, 600, 100, 300]:
            actual = actual.stdin(str(v))
        actual.stdout("sorted= 100 200 300 400 500 600", regex=False)


@check50.check(compiles)
def nombre_echanges():
    """Nombre d'échanges d'un tri par sélection standard sur cet exemple

    NB: l'énoncé TP1-tableaux.tex indique swaps=4 pour cet exemple, mais un
    tri par sélection standard (déplacement du minimum à chaque passe,
    échange seulement si l'indice change) donne 3 échanges pour cette
    entrée - vérifié par simulation. À corriger dans l'énoncé (cf. rapport).
    """
    with exercise_cwd():
        actual = check50.run("./tarifs_selection_sort").stdin("6")
        for v in [500, 200, 400, 600, 100, 300]:
            actual = actual.stdin(str(v))
        actual.stdout("swaps= 3", regex=False)
