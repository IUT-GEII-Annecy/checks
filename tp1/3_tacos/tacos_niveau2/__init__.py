import check50
import check50.c
import re

PRIX_TACOS = 6.30
PRIX_KEBAB = 5.50

STOCK_TACOS = 10
STOCK_KEBAB = 5

check50.import_checks("../tacos_niveau1")
from tacos_niveau1 import *

@check50.check(tacos_compile)
def tacos_hors_stock():
    """Hors stock Tacos"""
    check(11,3)

@check50.check(tacos_compile)
def tacos_hors_stock_kebab():
    """Hors stock Kebab"""
    check(3, 6)

@check50.check(tacos_compile)
def tacos_valeurs_negatives():
    """Valeurs négatives interdites"""
    check(-1, 2)
    check(2, -1)

@check50.check(tacos_compile)
def tacos_hors_stock_tout():
    """Hors stock Tacos et Kebab"""
    check(11, 6)






# Helpers
def check(nombre_de_tacos:int,  nombre_de_kebab:int):
    actual = check50.run("./tacos").stdout("Bonjour, bienvenu chez ")
    actual = actual.stdin(str(nombre_de_tacos)).stdin(str(nombre_de_kebab))

    if ((nombre_de_kebab < 0) or (nombre_de_tacos < 0)):
        actual = actual.stdout("ERREUR : Valeurs négatives interdites.").exit(1)
        return 
    elif ((nombre_de_tacos > STOCK_TACOS) and (nombre_de_kebab > STOCK_KEBAB)):
        actual = actual.stdout("Désolé, nous n'avons pas assez de Tacos, ni de Kebab")
    elif (nombre_de_tacos > STOCK_TACOS):
        actual = actual.stdout("Désolé, nous n'avons pas assez de Tacos")
    elif (nombre_de_kebab > STOCK_KEBAB):
        actual = actual.stdout("Désolé, nous n'avons pas assez de Kebab")
    else:
        montant_total = nombre_de_tacos * PRIX_TACOS + nombre_de_kebab * PRIX_KEBAB
        actual = actual.stdout(f"Montant total : {total:.2f} euros")
    
    actual = actual.stdout(f"Merci pour votre commande chez (.*)", regex=True)

