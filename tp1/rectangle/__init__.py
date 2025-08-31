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
def aire6x5():
    """Un rectangle de 6 par 5 a une aire de 30.00"""
    check_debug(largeur="6", longueur="5", aire="30.00")


@check50.check(compiles)
def aire2x8():
    """Un rectangle de 2 par 8 a une aire de 16.00"""
    check_debug(largeur="2", longueur="8", aire="16.00")

@check50.check(compiles)
def aire1150():
    """Un rectangle de 11.5 par 100 a une aire de 1150.00"""
    check_debug(largeur="11.5", longueur="100", aire="1150.00")


# Helpers
def check_debug(largeur: str, longueur: str, aire: str):
    actual = check50.run("./rectangle").stdin(largeur).stdin(longueur).stdout(f"L'aire du rectangle est de {aire}")
    