import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "07_web_moving_avg"
MAIN = "web_moving_avg.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """web_moving_avg.c existe"""
    with exercise_cwd():
        check50.exists("web_moving_avg.c")


@check50.check(exists)
def compiles():
    """web_moving_avg.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("web_moving_avg.c", lcs50=True)


@check50.check(compiles)
def exemple_enonce():
    """Exemple de l'énoncé : 2 10 5 7 1 -> 2 5 7 4 1"""
    with exercise_cwd():
        actual = check50.run("./web_moving_avg").stdin("5")
        for v in [2, 10, 5, 7, 1]:
            actual = actual.stdin(str(v))
        actual.stdout("2 5 7 4 1", regex=False)


@check50.check(compiles)
def extremites_inchangees():
    """out[0] et out[n-1] restent égaux à v[0] et v[n-1]"""
    with exercise_cwd():
        actual = check50.run("./web_moving_avg").stdin("3")
        for v in [9, 0, 3]:
            actual = actual.stdin(str(v))
        actual.stdout("9 4 3", regex=False)
