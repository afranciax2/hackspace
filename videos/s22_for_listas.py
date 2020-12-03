from random import randint
from time import sleep

#i = 1
#while i <= 10:
#    print(i)
#    i += 1
#print("")


#for i in range(1, 10 +1):
#    print(i)


"""
RANDOM_MIN = 1
RANDOM_MAX = 6
ACUM_MIN = 100
ELEMENTO_NEUTRO = 0
PAUSA = 0.25

acum = ELEMENTO_NEUTRO

vueltas = 0
while acum < ACUM_MIN:
    vueltas += 1
    munero_aleatorio = randint(RANDOM_MIN, RANDOM_MAX)
    acum += munero_aleatorio
    print("Núnero_aleatorio: %d - Acúmulado: %d - Vueltas: %d" % (munero_aleatorio, acum, vueltas))
    sleep(PAUSA)
print("Acumulador: %d" % acum)
print("Vueltas: %d" % vueltas)
"""

NUMERO = 1
NUMERO_MAX = 100
acum = 0

while NUMERO <= NUMERO_MAX:
    if NUMERO % 2 != 0:
        print(f'Número impar: {NUMERO}')
        ACU += NUMERO
    NUMERO += 1
print(f'Total acúmulado: {ACU}')
