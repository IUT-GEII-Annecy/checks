import check50
import check50.c
import re

PRIX_TACOS = 6.30
PRIX_KEBAB = 5.50

STOCK_TACOS = 10
STOCK_KEBAB = 5

REDUCTION = 0.9  # -10% au-delà de 5 articles au total

# NB: le dossier de checks du niveau 2 s'appelle "niveau2" (et non
# "tacos_niveau2" comme le fait niveau2/__init__.py pour niveau1) : on importe
# ici depuis le nom de dossier réel.
check50.import_checks("../niveau2")
from niveau2 import *


@check50.check(tacos_compile)
def beaucoup():
    """9 Tacos, 4 Kebabs"""
    # Redéfini par rapport à niveau1/niveau2 : à partir du niveau3, 13
    # articles (9+4) dépassent le seuil de 5 et déclenchent la réduction.
    check_reduction(9, 4)

@check50.check(tacos_compile)
def tacos_reduction_appliquee():
    """Réduction de 10% appliquée au-delà de 5 articles"""
    check_reduction(4, 3)  # 7 articles

@check50.check(tacos_compile)
def tacos_pas_de_reduction_a_cinq():
    """Pas de réduction pour exactement 5 articles"""
    check(2, 3)  # 5 articles, montant plein attendu


# Helpers
def check_reduction(nombre_de_tacos: int, nombre_de_kebab: int):
    montant_plein = nombre_de_tacos * PRIX_TACOS + nombre_de_kebab * PRIX_KEBAB
    montant_reduit = montant_plein * REDUCTION

    actual = check50.run("./tacos").stdout("Bonjour, bienvenu chez ")
    actual = actual.stdin(str(nombre_de_tacos)).stdin(str(nombre_de_kebab))
    actual = actual.stdout(f"Montant total : {montant_reduit:.2f} euros")
    actual = actual.stdout(f"Merci pour votre commande chez (.*)", regex=True)
