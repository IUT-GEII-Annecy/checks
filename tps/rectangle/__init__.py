import check50
import check50.c


@check50.check()
def exists():
    """debug.c exists"""
    check50.exists("rectangle.c")


@check50.check(exists)
def compiles():
    """debug.c compiles"""
    check50.c.compile("rectangle.c", lcs50=True)


@check50.check(compiles)
def aire5x5():
    """Un rectangle de 5 par 5 a une aire de 25"""
    check_debug(largeur=5, longueur=5, aire="25.00")


@check50.check(compiles)
def aire2x5():
    """Un rectangle de 2 par 5 a une aire de 25"""
    check_debug(largeur=2, longueur=5, aire="10.00")


# Helpers
def check_debug(largeur: float, longueur: float, aire: str):
    actual = check50.run("./rectangle").stdin(largeur).stdin(longueur).stdout(f"L'aire du rectangle est de {aire}\")
    