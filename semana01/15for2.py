#

contador = 0
email = input("Ingresar e-mail: ")
for i in email:
    if (i == "@" or i == "."):
        contador = contador + 1

if contador == 2:
    print("Email correcto")
else:
    print("Email es incorrecto")


# Tipo Range
for i in range(5):
    print(i)