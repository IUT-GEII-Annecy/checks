import check50
import check50.c

from pathlib import Path
from contextlib import chdir, nullcontext  # <-- standard lib

EXER_DIR = "1_fixme"
MAIN = "fixme.c"

def exercise_cwd():
    """
    Si fixme.c est à la racine → pas de cd.
    Si fixme.c est dans 1_fixme/ → cd 1_fixme.
    Sinon → erreur explicite.
    """
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)   # <-- au lieu de check50.cd(...)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")


@check50.check()
def fixme_exists():
    """fixme.c exists"""
    with exercise_cwd():
        check50.exists(MAIN)


@check50.check(fixme_exists)
def fixme_compiles():
    """fixme.c compiles"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(fixme_compiles)
def harry():
    """Input of \"Harry\" and \"Godrick's Hollow\" produces output \"Hello, Harry, from Godrick's Hollow!\""""
    check_debug(name="Harry", place="Godrick's Hollow")


@check50.check(fixme_compiles)
def dumbledore():
    """Input of \"Dumbledore\" and \"Mould-on-the-Wold\" produces output \"Hello, Dumbledore, from Mould-on-the-Wold!\""""
    check_debug(name="Dumbledore", place="Mould-on-the-Wold")


# Helpers
def check_debug(name: str, place: str):
    with exercise_cwd():
        check50.run("./fixme").stdin(name).stdin(place).stdout(f"Hello, {name}, from {place}!")