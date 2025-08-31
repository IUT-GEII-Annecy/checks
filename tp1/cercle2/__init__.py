import check50
import check50.c

check50.import_checks("../cercle")
from cercle import *

@check50.check(cercle0)
def rayonNegatif():
    """Rayon négatif"""
    check_negatif("-0.5")

# Helpers
def check_debug(rayon: str, circonference: str, aire: str):
    actual = check50.run("./cercle").stdin(rayon).stdout(f"Aire : {aire}\n").stdout(f"Perimetre : {circonference}")

def check_negatif(rayon: str):
    check50.run("./cercle").stdin(rayon).stdout("ERREUR : Valeur negative interdite.")