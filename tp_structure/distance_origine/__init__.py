import check50
import check50.c

MAIN = "distance_origine.c"
HEADER = "headers/geometrie.h"
SOURCE = "sources/geometrie.c"


@check50.check()
def distance_origine_exists():
    """distance_origine.c existe"""
    check50.exists(MAIN)


@check50.check(distance_origine_exists)
def geometrie_header_exists():
    """headers/geometrie.h existe"""
    check50.exists(HEADER)


@check50.check(distance_origine_exists)
def geometrie_source_exists():
    """sources/geometrie.c existe"""
    check50.exists(SOURCE)


@check50.check(geometrie_header_exists, geometrie_source_exists)
def distance_origine_compiles():
    """distance_origine.c compile sans erreur avec la bibliothèque géométrie (avec -lm)"""
    check50.c.compile(MAIN, SOURCE, cc_flags=["-I", "headers"], lcs50=True, lm=True)


@check50.check(distance_origine_compiles)
def test_triangle_3_4():
    """Distance du point (3, 4) = 5.00"""
    check_distance(x="3", y="4", expected="Distance: 5.00")


@check50.check(distance_origine_compiles)
def test_origine():
    """Distance du point (0, 0) = 0.00"""
    check_distance(x="0", y="0", expected="Distance: 0.00")


@check50.check(distance_origine_compiles)
def test_decimal():
    """Distance du point (1.5, 2.5) ≈ 2.92"""
    check_distance(x="1.5", y="2.5", expected="Distance: 2.92")


# Helper function
def check_distance(x: str, y: str, expected: str):
    """Teste le calcul de distance pour des coordonnées spécifiques"""
    actual = check50.run("./distance_origine").stdin(x).stdin(y).stdout()

    # Vérifier que la sortie correspond
    if expected not in actual:
        raise check50.Mismatch(expected=expected + "\n", actual=actual)
