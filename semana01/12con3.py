# Switch no existe
# Para evaluar muchas condiciones encadenadas
"""
edad = 145

if 0 < edad < 100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")
"""

# Evaluar salario de diferentes roles de una empresa.
salario_presidente = float(input("Ingresar salario presidente (S/.): "))
print("Salario presidente: S/." + str(salario_presidente))

salario_director = float(input("Ingresar salario director(S/.): "))
print("Salario director: S/." + str(salario_director))

salario_jefe = float(input("Ingresar salario jefe (S/.): "))
print("Salario jefe: S/." + str(salario_jefe))

salario_admi = float(input("Ingresar salario administrativo (S/.): "))
print("Salario administrativo: S/." + str(salario_admi))

if salario_admi < salario_jefe < salario_director < salario_presidente:
    print("Salario asignado correctamente")
else:
    print("Salario incorrecto")