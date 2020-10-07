# Creación de segunda instancia
# Estado inicial, cuando se crea una instancia ya cuenta con un estado inical, como un estado de fabrica
# Constructos --> Métod especial que le da estado a los objetos
# Estado inical <-- Constructor

class Auto():

    #Constructor, estado inicial a los objetos de la clase
    #Está es la nomenclatura
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # Declarar dentro de la clase
        self.__enMarcha = False
    

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        if self.__enMarcha:
            return "El auto está en marcha."
        else:
            return "El auto está parado."    


    def estado(self):
        print(f"El auto tiene {self.__ruedas} ruedas. Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}")

# Primera instancia
miAuto = Auto()
print(miAuto.arrancar(True))
miAuto.estado()

print("")
print("------A continuación creamos el segundo objeto------")
print("")

# Segunda instancia
miAuto2 = Auto()
print(miAuto2.arrancar(False))
miAuto2.ruedas = 2 # Evitar declarar fuera de la clase
miAuto2.estado()