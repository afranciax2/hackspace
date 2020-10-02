# Función de tipo 'f'

valido = False
email = input("Ingresar e-mail: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email es incorrecto")

#Ejercicio 1:
#Crea un programa que muestre los números impares del 1 al 100. Los números deberán
#aparecer una al lado del otro sin salto de línea.

for i in range(1,100,2):
    print(i, end=" ")

#Ejercicio 2:
#Crea un programa que pida por teclado introducir una contraseña. La contraseña no
#podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
#el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña errónea”

contrasena = input("Ingresar contraseña: ")
contador = 0

for i in range(len(contrasena)):
    if contrasena[i] == " ":
        contador = 1

if len(contrasena) < 8 or contador > 0:
    print("Contraseña incorrecta")
else:
    print("Contraseña correcta")


#Ejercicio 3:
# Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
#función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
#correcta si solo tiene una “@” y si tiene uno o más “.”

correo = input("Ingresar correo: ")
arroba = 0
punto = 0

for i in range(len(correo)):
    if correo[i] == "@":
        arroba = arroba + 1
    if punto[i] == "."
        punto = punto + 1

if arroba != 1 or punto == 0:
    print("Correo Incorrecto")
else:
    print("Correo Correcto")