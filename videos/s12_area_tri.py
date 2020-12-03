print("Área del triángulo")
print("==================")
print()

try:
    base = float(input("Ingrese la base: "))
except ValueError:
    print("ERROR: La base debe ser un número de punto flotante.")
    exit(1)

try:
    altura = float(input("Ingrese la altu: "))
except ValueError:
    print("ERROR: La altura debe ser un número de punto flotante.")
    exit(1)

area = (base * altura) / 2.0

print("Base: %.2f" % base)
print("Altura: %.2f" % altura)
print("Área: %.2f" % area)