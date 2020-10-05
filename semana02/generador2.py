# Función Generador que devuleve ciudades

def devolver_ciudades(*ciudades): # * --> número indeterminado de argumentos
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento


ciudades_devueltas = devolver_ciudades("Madrid", "Barcelona", "Lima", "Trujillo")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))