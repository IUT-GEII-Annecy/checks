import check50
import check50.c

MAIN = "point_simple.c"
HEADER = "headers/geometrie.h"
SOURCE = "sources/geometrie.c"


@check50.check()
def point_simple_exists():
    """point_simple.c existe"""
    check50.exists(MAIN)


@check50.check(point_simple_exists)
def geometrie_header_exists():
    """headers/geometrie.h existe"""
    check50.exists(HEADER)


@check50.check(point_simple_exists)
def geometrie_source_exists():
    """sources/geometrie.c existe"""
    check50.exists(SOURCE)


@check50.check(geometrie_header_exists, geometrie_source_exists)
def point_simple_compiles():
    """point_simple.c compile sans erreur avec la bibliothèque géométrie"""
    check50.c.compile(MAIN, SOURCE, cc_flags=["-I", "headers"], lcs50=True)


@check50.check(point_simple_compiles)
def test_positive_values():
    """Point avec valeurs positives (3.5, 2.8)"""
    check_point(x="3.5", y="2.8", expected="Point: (3.5, 2.8)")


@check50.check(point_simple_compiles)
def test_zero_values():
    """Point à l'origine (0, 0)"""
    check_point(x="0", y="0", expected="Point: (0.0, 0.0)")


@check50.check(point_simple_compiles)
def test_negative_values():
    """Point avec valeurs négatives (-1.5, -2.3)"""
    check_point(x="-1.5", y="-2.3", expected="Point: (-1.5, -2.3)")


# Helper function
def check_point(x: str, y: str, expected: str):
    """Teste un point avec des coordonnées spécifiques"""
    actual = check50.run("./point_simple").stdin(x).stdin(y).stdout()

    # Vérifier que la sortie correspond
    if expected not in actual:
        raise check50.Mismatch(expected=expected + "\n", actual=actual)
