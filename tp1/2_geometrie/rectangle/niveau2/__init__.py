import check50
import check50.c

check50.import_checks("../../rectangle/niveau1")
from niveau1 import *

@check50.check(compiles)
def largeurNegative():
    """Rectangle : Largeur négative"""
    check_negative(largeur="-0.5", longueur="100")

@check50.check(largeurNegative)
def longueurNegative():
    """Rectangle : Longueur négative"""
    check_negative(largeur="0.5", longueur="-100")  

@check50.check(longueurNegative)
def valeursNegatives():
    """Rectangle : Les deux valeurs négative"""
    check_negative(largeur="-0.5", longueur="-100") 

@check50.check(valeursNegatives)
def aireNulle():
    """Rectangle : Aire Nulle"""
    check_debug(largeur="0", longueur="100", aire="0.00")
    check_debug(largeur="100", longueur="0", aire="0.00")



# Helpers
def check_debug(largeur: str, longueur: str, aire: str):
    actual = check50.run("./rectangle").stdin(largeur).stdin(longueur).stdout(f"L'aire du rectangle est de {aire}")

def check_negative(largeur: str, longueur: str):
    actual = check50.run("./rectangle").stdin(largeur).stdin(longueur).stdout(f"ERREUR : Valeur negative interdite.")