# Listas inmutables, no cambia.

mi_tupla = ("Juan", 13, 1.0, 1995)
print(mi_tupla[1])
print(mi_tupla)

# Tuplas a Listas
mi_lista = list(mi_tupla)
print(mi_lista)


# Listas a Tuplas
mi_lista_2 = ["Ann", 13, 1, 2000, 13]
print(mi_lista_2)
mi_tupla_2 = tuple(mi_lista_2)
print(mi_tupla_2)
print("Juan" in mi_tupla_2)

#Count, cuantós elementos tiene la tupla
print(mi_tupla_2.count(13))
print(len(mi_tupla_2))

# Tuplas unitarias
tupla_uni = ("Anthony", 3, 4, 1988) # --> Se recomiedao
# tupla_uni = "Anthony", # Empaquetado de tupla
nombre, dia, mes, anio = tupla_uni
print(nombre)
print(dia)
print(mes)
print(anio)


