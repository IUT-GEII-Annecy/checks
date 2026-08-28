import check50
import check50.c
from pathlib import Path
from contextlib import chdir, nullcontext

EXER_DIR = "05_playlist_dedupe"
MAIN = "playlist_dedupe.c"

def exercise_cwd():
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def exists():
    """playlist_dedupe.c existe"""
    with exercise_cwd():
        check50.exists("playlist_dedupe.c")


@check50.check(exists)
def compiles():
    """playlist_dedupe.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("playlist_dedupe.c", lcs50=True)


@check50.check(compiles)
def exemple_enonce():
    """Exemple de l'énoncé : 4 9 4 2 9 1 2 -> 4 9 2 1"""
    with exercise_cwd():
        actual = check50.run("./playlist_dedupe").stdin("7")
        for v in [4, 9, 4, 2, 9, 1, 2]:
            actual = actual.stdin(str(v))
        actual.stdout("taille=4", regex=False).stdout("4 9 2 1", regex=False)


@check50.check(compiles)
def sans_doublons():
    """Aucun doublon : taille et ordre inchangés"""
    with exercise_cwd():
        actual = check50.run("./playlist_dedupe").stdin("3")
        for v in [1, 2, 3]:
            actual = actual.stdin(str(v))
        actual.stdout("taille=3", regex=False).stdout("1 2 3", regex=False)
