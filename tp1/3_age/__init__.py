import check50
import check50.c
import re

@check50.check()
def age_exists():
    """age.c existe"""
    check50.exists("age.c")

@check50.check(age_exists)
def age_compile():
    """age.c compile sans erreur"""
    check50.c.compile("age.c", lcs50=True)

@check50.check(age_compile)
def enfant():
    """Enfant"""
    check(1);
    check(10);
    check(12);

@check50.check(age_compile)
def mineur():
    """Mineur"""
    check(13);
    check(17);

@check50.check(age_compile)
def adulte():
    """Adulte"""
    check(18);
    check(58);
    check(59);
    
@check50.check(age_compile)
def senior():
    """Senior"""
    check(60);
    check(90);

@check50.check(age_compile)
def menteur():
    """Menteur"""
    check(200);
    check(120);

@check50.check(age_compile)
def negatif():
    """Menteur car Negatif"""
    check(-1);
    check(-5);



# Helpers
def check(age:int):
    actual = check50.run("./age").stdin(str(age))
    if (age<0):
        actual.stdout("ERREUR : Valeurs n[eé]gatives interdites.",str_output="ERREUR : Valeurs négatives interdites.").exit()
    else:
        actual = actual.stdout("Vous [eê]tes un ",regex=True,str_output="Vous êtes un")
        if (age<12):
            actual.stdout("enfant.").exit()
        elif(age<18):
            actual.stdout("mineur.").exit()
        elif(age<60):
            actual.stdout("adulte.").exit()
        elif(age<120):
            actual.stdout("s[ée]nior.",regex=True,str_output="sénior").exit()
        else:
            actual.stdout("menteur.").exit()

    