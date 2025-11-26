import check50
import check50.c

MAIN = "distance_deux_points.c"
HEADER = "headers/geometrie.h"
SOURCE = "sources/geometrie.c"


@check50.check()
def distance_deux_points_exists():
    """distance_deux_points.c existe"""
    check50.exists(MAIN)


@check50.check(distance_deux_points_exists)
def geometrie_header_exists():
    """headers/geometrie.h existe"""
    check50.exists(HEADER)


@check50.check(distance_deux_points_exists)
def geometrie_source_exists():
    """sources/geometrie.c existe"""
    check50.exists(SOURCE)


@check50.check(geometrie_header_exists, geometrie_source_exists)
def distance_deux_points_compiles():
    """distance_deux_points.c compile sans erreur avec la bibliothèque géométrie (avec -lm)"""
    check50.c.compile(MAIN, SOURCE, cc_flags=["-I", "headers"], lcs50=True, lm=True)


@check50.check(distance_deux_points_compiles)
def test_origine_to_3_4():
    """Distance entre A(0,0) et B(3,4) = 5.00"""
    check_distance(xa="0", ya="0", xb="3", yb="4", expected="Distance: 5.00")


@check50.check(distance_deux_points_compiles)
def test_general_case():
    """Distance entre A(1,1) et B(4,5) = 5.00"""
    check_distance(xa="1", ya="1", xb="4", yb="5", expected="Distance: 5.00")


@check50.check(distance_deux_points_compiles)
def test_same_points():
    """Distance entre points identiques = 0.00"""
    check_distance(xa="2", ya="3", xb="2", yb="3", expected="Distance: 0.00")


# Helper function
def check_distance(xa: str, ya: str, xb: str, yb: str, expected: str):
    """Teste le calcul de distance entre deux points"""
    actual = check50.run("./distance_deux_points").stdin(xa).stdin(ya).stdin(xb).stdin(yb).stdout()

    # Vérifier que la sortie correspond
    if expected not in actual:
        raise check50.Mismatch(expected=expected + "\n", actual=actual)
