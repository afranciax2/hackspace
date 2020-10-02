import math

# Bucle indeterminado

"""
i = 1

while i <= 10:
    print(f"Ejecución: {i}")
    i = i + 1
print("Termina aquí")


edad = int(input("Ingresar edad: "))

while edad < 1 or edad > 100:
    print("Ingresar edad correctamente")
    edad = int(input("Ingresar edad: "))

print("Gracias por colaborar")
"""

# Hallar la raíz cuadrada de un número

print("Programa de cálculo de raíz cuadrada")

numero = int(input("Ingresar número: "))
intentos = 0

while numero < 0:
    print("No sé puede hallar la raíz de un número negativo")

    if intentos == 2:
        print("Has alcanzado tu máximos númenos de intentos")
        break

    numero = int(input("Ingresar número: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {solucion}")
