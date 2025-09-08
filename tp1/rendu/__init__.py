import check50
from pathlib import Path


# 0_hello
check50.import_checks("../0_hello/variable")
check50.log("--- Test Hello ---")
from variable import *

# 1_fixme
check50.import_checks("../1_fixme/fixme")
check50.log("--- Test Fixme ---")
from fixme import *

# 2_geometrie/geometrie/all
check50.import_checks("../2_geometrie/cercle/all")
check50.log("--- Test Cercle ---")
from all import *

check50.import_checks("../2_geometrie/rectangle/all")
check50.log("--- Test Rectangle ---")
from all import *

# 3_age
check50.import_checks("../3_age/niveau2")
check50.log("--- Test Age ---")
from niveau2 import *  # si ton dossier est un package, sinon from __init__ import *

# 4_tacos
check50.import_checks("../4_tacos/all")
check50.log("--- Test Tacos Niveau 1 ---")
from all import *

# check50.import_checks("../4_tacos/niveau2")
# check50.log("--- Test Tacos Niveau 2 ---")
# from niveau2 import *

