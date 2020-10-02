# Continue
"""
for letra in "Python":

    if letra == "h":
        continue

    print("Viendo la letra:" + letra)


nombre = "píldoras informáticas"
contador = 0

for i in nombre:

    if i == " ":
        continue
    contador += 1

print(contador)
"""

correo = input("email: ")

for i in correo:
    if i == "@":
        arroba = True
        break

else:
    arroba = False

print(arroba)