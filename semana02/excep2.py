def divide():

    try:
        op1 = float(input("Ingresar primer número: "))
        op2 = float(input("Ingresar segundo número: "))
        print(f"La división es: {op1/op2}")
    except ValueError:
        print("El valor introducido es erróneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    finally:
        print(f"Cálculo finalizado")
divide()

# Sentencia Finally
def divide1():

    try:
        op1 = float(input("Ingresar primer número: "))
        op2 = float(input("Ingresar segundo número: "))
        print(f"La división es: {op1/op2}")
 
    finally:
        print(f"Cálculo finalizado")

divide1()