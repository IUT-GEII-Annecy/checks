import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "10_image_seuillage_2D"
MAIN = "image_seuillage_2D.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """image_seuillage_2D.c existe"""
    with exercise_cwd():
        check50.exists("image_seuillage_2D.c")


@check50.check(exists)
def compiles():
    """image_seuillage_2D.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("image_seuillage_2D.c", lcs50=True)


@check50.check(compiles)
def exemple_enonce():
    """Exemple de l'énoncé : h=2, w=3, T=100"""
    with exercise_cwd():
        actual = check50.run("./image_seuillage_2D").stdin("2").stdin("3")
        for v in [0, 120, 255, 80, 100, 90]:
            actual = actual.stdin(str(v))
        actual = actual.stdin("100")
        actual.stdout("0 1 1", regex=False).stdout("0 1 0", regex=False)
