import check50
import check50.c
import re
from pathlib import Path
from contextlib import chdir, nullcontext  # <-- standard lib


EXER_DIR = "3_age"
MAIN = "age.c"

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
def age_exists():
    """age.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)

@check50.check(age_exists)
def age_compile():
    """age.c compile sans erreur"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)

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
    with exercise_cwd():
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

    