# Instrucciones Raise -- > A futuros excepciones propias
import math

def evaluar_edad(edad):

    if edad < 0:
        raise ZeroDivisionError("No se permiten edad negativas")

    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres adulto"
    elif edad < 100:
        return "Eres adulto mayor"

#print(evaluar_edad(-15))

def calcular_raiz (num1):
    if num1 < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

op1 = int(input("Ingresa número: "))

try:
    print(calcular_raiz(op1))
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)

print("Programa finalizado")
