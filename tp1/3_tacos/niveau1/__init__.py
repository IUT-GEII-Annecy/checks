import check50
import check50.c
import re

PRIX_TACOS = 6.30
PRIX_KEBAB = 5.50

@check50.check()
def tacos_exists():
    """tacos.c existe"""
    check50.exists("tacos.c")

@check50.check(tacos_exists)
def tacos_compile():
    """tacos.c compile sans erreur"""
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



# Helpers
def check(tacos:int, kebab:int):
    total = tacos * PRIX_TACOS + kebab * PRIX_KEBAB

    actual = check50.run("./tacos").stdout("Bonjour, bienvenu chez ")

    actual = actual.stdin(str(tacos)).stdin(str(kebab))

    actual = actual.stdout(f"Montant total : {total:.2f} euros")
    actual = actual.stdout(f"Merci pour votre commande chez (.*)", regex=True)
    