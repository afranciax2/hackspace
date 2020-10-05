
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

# Capturamos la exceción
def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"

while True:
    try:
        op1 = int(input("Ingresar primer número: "))
        op2 = int(input("Ingresar segundo número: "))
        break
    except ValueError:
        print("Deben ingresar números. Intentar de nuevo")

operacion = input("Ingresa la operación a realizar (suma, resta, multiplica o divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplicar(op1, op2))

elif operacion == "divide":
    print(dividir(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa.")

# Debemos realizar una captura o control de excepción