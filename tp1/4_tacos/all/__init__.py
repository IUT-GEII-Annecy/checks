import check50
import check50.c
import re
from pathlib import Path
from contextlib import chdir, nullcontext  # <-- standard lib


PRIX_TACOS = 6.30
PRIX_KEBAB = 5.50

STOCK_TACOS = 10
STOCK_KEBAB = 5


EXER_DIR = "4_tacos/"
MAIN = "tacos.c"

def exercise_cwd():
    """
    Si hello.c est à la racine → pas de cd.
    Si hello.c est dans 0_hello/ → cd 0_hello.
    Sinon → erreur explicite.
    """
    if Path(MAIN).exists():
        return nullcontext()
    elif Path(EXER_DIR, MAIN).exists():
        return chdir(EXER_DIR)   # <-- au lieu de check50.cd(...)
    else:
        raise check50.Failure(f"{MAIN} introuvable (./{MAIN} ou ./{EXER_DIR}/{MAIN}).")
    


@check50.check()
def tacos_exists():
    """tacos.c existe"""
    with exercise_cwd():
        check50.exists("tacos.c")

@check50.check(tacos_exists)
def tacos_compile():
    """tacos.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile("tacos.c", lcs50=True)

@check50.check(tacos_compile)
def queDesTacos():
    """1 Tacos, 0 Kebab"""
    check(1,0);

@check50.check(tacos_compile)
def queDesKebab():
    """0 Tacos, 1 Kebab"""
    check(0,1);

@check50.check(tacos_compile)
def rien():
    """rien du tout"""
    check(0,0);
    
@check50.check(tacos_compile)
def beaucoup():
    """9 Tacos, 4 Kebabs"""
    check(9,4);

    
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

@check50.check(tacos_compile)
def tacos_reduction_appliquee():
    """Réduction de 10% appliquée au-delà de 5 articles"""
    check_reduction(4, 3)  # 7 articles

@check50.check(tacos_compile)
def tacos_pas_de_reduction_a_cinq():
    """Pas de réduction pour exactement 5 articles"""
    check(2, 3)  # 5 articles, montant plein attendu


REDUCTION = 0.9  # -10% au-delà de 5 articles au total

def check_reduction(nombre_de_tacos: int, nombre_de_kebab: int):
    montant_plein = nombre_de_tacos * PRIX_TACOS + nombre_de_kebab * PRIX_KEBAB
    montant_reduit = montant_plein * REDUCTION
    with exercise_cwd():
        actual = check50.run("./tacos").stdout("Bonjour, bienvenu chez ")
        actual = actual.stdin(str(nombre_de_tacos)).stdin(str(nombre_de_kebab))
        actual = actual.stdout(f"Montant total : {montant_reduit:.2f} euros")
        actual = actual.stdout(f"Merci pour votre commande chez (.*)", regex=True)


# Helpers
def check(nombre_de_tacos:int,  nombre_de_kebab:int):
    with exercise_cwd():
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
            if nombre_de_tacos + nombre_de_kebab > 5:
                montant_total *= REDUCTION
            actual = actual.stdout(f"Montant total : {montant_total:.2f} euros")
        
        actual = actual.stdout(f"Merci pour votre commande chez (.*)", regex=True)

