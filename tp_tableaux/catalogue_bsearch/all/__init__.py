import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "09_catalogue_bsearch"
MAIN = "catalogue_bsearch.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """catalogue_bsearch.c existe"""
    with exercise_cwd():
        check50.exists("catalogue_bsearch.c")


@check50.check(exists)
def compiles():
    """catalogue_bsearch.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("catalogue_bsearch.c", lcs50=True)


@check50.check(compiles)
def id_trouve():
    """id=10 20 30 40 50, x=40 -> 3"""
    with exercise_cwd():
        actual = check50.run("./catalogue_bsearch").stdin("5")
        for v in [10, 20, 30, 40, 50]:
            actual = actual.stdin(str(v))
        actual = actual.stdin("40")
        actual.stdout("3", regex=False)


@check50.check(compiles)
def id_absent():
    """id=2 4 6 8, x=5 -> -1"""
    with exercise_cwd():
        actual = check50.run("./catalogue_bsearch").stdin("4")
        for v in [2, 4, 6, 8]:
            actual = actual.stdin(str(v))
        actual = actual.stdin("5")
        actual.stdout("-1", regex=False)
