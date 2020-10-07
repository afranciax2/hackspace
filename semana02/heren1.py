# Herencia
# POO Trasladar los objetos de la vida real
# Trasladar el comportamiento de las personas que ocurre en la vida real en programación

class Vehiculos():

    # Constructor se aplica para todos los vehículos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acele = False
        self.frena = False


    # Definimos comportarmientos
    def arrancar(self):
        self.enmarcha = True
    

    def acelerar(self):
        self.acele = True
    

    def frenar(self):
        self.frena = True

    
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acele} \nFrenando: {self.frena}")


# sintaxis para heredar clases
# class name(Clase padre)

class Moto(Vehiculos):
    pass

miMoto = Moto("Bajaj", "Torito")
miMoto.estado()