# Función para generar números pares

def generar_pares(limite):
    num = 1
    pares = []

    while num < limite:
        pares.append(num*2)
        num += 1
    return pares

print(generar_pares(10))


# Números pares con GENERADORES

def generar_pares_gen(limite):
    num = 1

    while num < limite:
        yield num*2
        num += 1

devuelve_pares = generar_pares_gen(10)

print(next(devuelve_pares))
print("Aquí podría ir más código...")
print(next(devuelve_pares))
print("Aquí podría ir más código...")
print(next(devuelve_pares))
print("Aquí podría ir más código...")