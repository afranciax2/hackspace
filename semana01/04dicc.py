mi_dicc ={
    "Alemania": "Berlin",
    "Francia": "Paris",
    "Peru": "Lima",
    "España": "Madrid" 
}

#Agregar elemento
print(mi_dicc)
print(mi_dicc["Francia"])

mi_dicc['Italia'] = 'Lisboa'
print(mi_dicc)

#Modificar valor nuevo
mi_dicc["Italia"] = "Roma"
print(mi_dicc)

#Eliminar valores
del mi_dicc['Alemania']
print(mi_dicc)


mi_dicc_2 ={
    "Alemania": "Berlín",
    23: "Jordan",
    "Mosqueteros": 3
}
print(mi_dicc_2)

#Diccionario por tupla
mi_tupla = ["Espana", "Francia", "Perú"]
mi_dicc_tup ={mi_tupla[0]:"Madrid", mi_tupla[1]:"París", mi_tupla[2]:"Lima"}
print(mi_dicc_tup)

jugador = {
    23: "Jordan",
    "Nombre": "Michael",
    "Equipo": "Chicago",
    "Anillos": {"Temporadas": [1991, 1992, 1993, 1996, 1997, 1998]}
}
print(jugador["Anillos"])
print(jugador)

#Métodos

#Método de llaves
print(jugador.keys())

print(jugador.values())

print(len(jugador))