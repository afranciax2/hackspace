#print(1 < 2 and 2 < 3)
#print(1 < 2 < 3)
#print(3 > 2 > 1)

numero = 35
if numero >= 0 and numero <= 100:
    print("El número {} se encuentra entre 0 y 100".format(numero))
else:
    print("El número {} no se encuentra entre 0 y 100".format(numero))


numero_1 = 36
if 0 <= numero_1 <= 100:
    print("El número {} se encuentra entre 0 y 100".format(numero_1))
else:
    print("El número {} no se encuentra entre 0 y 100".format(numero_1))



# --- Comprensión de listas ---

# Método tradicional
lista = []
for letra in "casa":
    lista.append(letra)
print(lista)

# --- Comprensión de listas ---
lista_c = [letra for letra in "casa"]
print(lista_c)


# Método tradicional
lista_2 = []
for numero in range(0,11):
    lista_2.append(numero**2)
print(lista_2)

lista_22 = [numero**2 for numero in range(0,11)]
print(lista_22)


# Método tradicional
lista_3 = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista_3.append(numero)
print(lista_3)

lista_33 = [numero for numero in range(0,11) if numero % 2 == 0]
print(lista_33)


# Método tradicional
lista_4 = []
for numero in range (0,11):
    lista_4.append(numero**2)

pares = []
for numero in lista_4:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

lista_44 = [numero for numero in
                [numero**2 for numero in range(0,11)]
                    if numero % 2 == 0]
print(lista_44)