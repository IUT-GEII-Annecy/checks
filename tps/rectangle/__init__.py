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
def harry():
    """Un rectangle de 5 par 5 a une aire de 25"""
    check_debug(largueur=5, longueur=5, aire=25)


@check50.check(compiles)
def dumbledore():
    """Input of \"Dumbledore\" and \"Mould-on-the-Wold\" produces output \"Hello, Dumbledore, from Mould-on-the-Wold!\""""
    check_debug(name="Dumbledore", place="Mould-on-the-Wold")


# Helpers
def check_debug(name: str, place: str):
    check50.run("./debug").stdin(largeur).stdin(longueur).stdout(f"L'aire du rectangle est de {aire}!")