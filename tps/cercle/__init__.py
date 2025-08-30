import check50
import check50.c


@check50.check()
def exists():
    """cercle.c existe"""
    check50.exists("cercle.c")


@check50.check(exists)
def compiles():
    """cercle.c compile sans erreur"""
    check50.c.compile("cercle.c", lcs50=True)


@check50.check(compiles)
def rayon6():
    """Cercle de rayon 6"""
    check_debug(rayon="6", circonference="37.70", aire="113.10")


@check50.check(compiles)
def rayon100():
    """Cercle de rayon 100"""
    check_debug(rayon="100", circonference="628.319", aire="31415.93")

@check50.check(compiles)
def cercle0():
    """Cercle de rayon nul"""
    check_debug(rayon="0", circonference="0.00", aire="0.00")


# Helpers
def check_debug(rayon: str, circonference: str, aire: str):
    actual = check50.run("./cercle").stdin(rayon).stdout(f"Aire : {aire}").stdout(f"Perimetre : {perimetre}")
    