import check50
import check50.c
import re
from pathlib import Path
from contextlib import chdir, nullcontext  # <-- standard lib

EXER_DIR = "0_hello"
MAIN = "hello.c"

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
def hello_exists():
    check50.log("ICI")
    """hello.c existe"""
    with exercise_cwd():
        check50.exists(MAIN)



@check50.check(hello_exists)
def hello_compiles():
    """hello.c compiles"""
    with exercise_cwd():
        check50.c.compile(MAIN, lcs50=True)


@check50.check(hello_compiles)
def mario():
    """responds to name Mario"""
    check_name("Mario")


@check50.check(hello_compiles)
def peach():
    """responds to name Peach"""
    check_name("Peach")


@check50.check(hello_compiles)
def bowser():
    """responds to name Bowser"""
    check_name("Bowser")


def check_name(name):
    # Define expected, actual outputs
    expected = f"hello, {name}\n"
    with exercise_cwd():
        actual = check50.run("./hello").stdin(name).stdout()

    # Check output
    if not re.match(regex(name), actual):
        try:
            last_character = actual[-1]
        except IndexError:
            raise check50.Mismatch(expected=expected, actual=actual)

        if last_character != "\n":
            raise check50.Mismatch(
                expected=expected,
                actual=actual,
                help=r"Forgot to print a newline at the end of your output?",
            )
        raise check50.Mismatch(expected=expected, actual=actual)


def regex(string):
    return f"^[Hh]ello, {re.escape(string)}\n$"
