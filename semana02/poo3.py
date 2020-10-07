#Encapsulación de Métodos
# Encapsular cuando tu objeto, tu clase y eso depende del comportamiento y criterio como program

class Auto():

    #Constructor
    # __ es para encapsular
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # Declarar dentro de la clase
        self.__enMarcha = False


    # Métodos que cambia la variable de arranque
    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha:
            chequeo = self.__cheque_interno()
        if self.__enMarcha and chequeo:
            return "El auto está en marcha."
        if self.__enMarcha and chequeo == False:
            return "Algo salío mal en el chequeo."
        else:
            return "El auto está parado."    


    # Método imprimir el estado del auto
    def estado(self):
        print(f"El auto tiene {self.__ruedas} ruedas. Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}")


    # Método no se encuentra encapsulado
    # Se encapsula método
    def __cheque_interno(self):
        print("Realizando chequeo interno")
        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"

        if self.gasolina == "Ok" and self.aceite =="Ok" and self.puertas == "Cerradas":
            return True
        else:
            return False

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
miAuto2.estado()
