print("Hola"[0])
print("Hola"[1])
print("Hola"[2])
print("Hola"[3])

# Interpolación de variables
print("%s %.2f" % ("Us$", 9.986))
print("%05d" % 1)
print("{} pueden ser {}".format("strings", "interpolados"))

nombre = "Juan"
print("¡Hola %s!" % nombre)
print("¡Hola {}!".format(nombre))
print("¡Hola {nombre}!".format(nombre=nombre))
print(f"¡Hola {nombre}!")

tu_nombre = input("Ingresa su nombre: ")
print("¡Hola {}".format(tu_nombre))