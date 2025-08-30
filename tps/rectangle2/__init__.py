import check50
import check50.c


@check50.check()
def exists():
    """rectangle.c existe"""
    check50.exists("rectangle.c")


@check50.check(exists)
def compiles():
    """rectangle.c compile sans erreur"""
    check50.c.compile("rectangle.c", lcs50=True)


@check50.check(compiles)
def aire5x5():
    """Un rectangle de 5 par 5 a une aire de 25.00"""
    check_debug(largeur="5", longueur="5", aire="25.00")


@check50.check(compiles)
def aire2x5():
    """Un rectangle de 2 par 5 a une aire de 10.00"""
    check_debug(largeur="2", longueur="5", aire="10.00")

@check50.check(compiles)
def aire2x5():
    """Un rectangle de 11.5 par 100 a une aire de 1150.00"""
    check_debug(largeur="11.5", longueur="100", aire="1150.00")

@check50.check(compiles)
def largeurNegative():
    """Largeur négative"""
    check_negative(largeur="-0.5", longueur="100")

@check50.check(largeurNegative)
def longueurNegative():
    """Longueur négative"""
    check_negative(largeur="0.5", longueur="-100")  

@check50.check(longueurNegative)
def valeursNegatives():
    """Les deux valeurs négative"""
    check_negative(largeur="-0.5", longueur="-100") 

@check50.check(valeursNegatives)
def aireNulle():
    """Aire Nulle"""
    check_debug(largeur="0", longueur="100", aire="0.00")
    check_debug(largeur="100", longueur="0", aire="0.00")



# Helpers
def check_debug(largeur: str, longueur: str, aire: str):2
    actual = check50.run("./rectangle").stdin(largeur).stdin(longueur).stdout(f"L'aire du rectangle est de {aire}")

def check_negative(largeur: str, longueur: str):
    actual = check50.run("./rectangle").stdin(largeur).stdin(longueur).stdout(f"ERREUR : Valeur negative interdite.")