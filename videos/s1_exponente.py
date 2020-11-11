print("Exponente 2 - V.1")
print("=================")
base = 2
exponente = 0
MAX_NUM = 5
INCREMENTO = 1

while exponente <= MAX_NUM:
    print("{} ** {}".format(base,exponente),"es =", base ** exponente)
    exponente += INCREMENTO

print("Exponente: ",exponente)
print("")


print("Exponente 2 - V.2")
print("=================")
BASE = 2
EXPONENTE_INI = 0
EXPONENTE_FIN = 5
INCREMENTO_EXP = 1
ELEMENTO_NEUTRO = 1
p = ELEMENTO_NEUTRO
e = EXPONENTE_INI

while e <= EXPONENTE_FIN :
    print("%d elevado al exponente %d = %d" % (BASE, e, p))
    p *= BASE
    e += INCREMENTO_EXP