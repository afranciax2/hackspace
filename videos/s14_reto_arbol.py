import time

"""
Imprimir árbol

    *
   ***
  *****
 *******
*********

"""

VECES = 1
NIVEL = 7

while NIVEL >= 1:
    print(" "*(NIVEL-1), "*"*VECES)
    VECES += 2
    NIVEL -= 1
    time.sleep(0.5)