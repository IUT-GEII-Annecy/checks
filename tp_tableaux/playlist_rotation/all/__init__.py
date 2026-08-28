import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "04_playlist_rotation"
MAIN = "playlist_rotation.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """playlist_rotation.c existe"""
    with exercise_cwd():
        check50.exists("playlist_rotation.c")


@check50.check(exists)
def compiles():
    """playlist_rotation.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("playlist_rotation.c", lcs50=True)


@check50.check(compiles)
def exemple_enonce():
    """Exemple de l'énoncé : rotation à partir de 'La bandite'"""
    with exercise_cwd():
        actual = check50.run("./playlist_rotation").stdin("5")
        for m in ["J adore", "La symphonie des nuages", "La bandite", "Toxicity", "Basique"]:
            actual = actual.stdin(m)
        actual = actual.stdin("La bandite")
        actual.stdout(
            "La bandite ; Toxicity ; Basique ; J adore ; La symphonie des nuages",
            regex=False,
        )


@check50.check(compiles)
def favori_premier():
    """Le morceau favori est déjà le premier : ordre inchangé"""
    with exercise_cwd():
        actual = check50.run("./playlist_rotation").stdin("3")
        for m in ["Alpha", "Beta", "Gamma"]:
            actual = actual.stdin(m)
        actual = actual.stdin("Alpha")
        actual.stdout("Alpha ; Beta ; Gamma", regex=False)
