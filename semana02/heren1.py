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
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo caballito"
    

    # Sobre escritura de métodos
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acele} \nFrenando: {self.frena} \nCaballito: {self.hcaballito}")


class Furgoneta(Vehiculos):

    def carga(self, carga):
        self.cargado = carga
        if self.cargado:
            return "La furgoneta está cargada."
        else:
            return "La furgoneta no está cargada."


class VElectricos(Vehiculos):
    def __init__(self):
        super().__init__(marca, modelo)
        self.autonimia = 100
    
    def cargar_energia(self):
        self.cargando = True


# Herencia múltiples
class BiciElectrica(Vehiculos, VElectricos):
    pass


# Zona de Instancias
#--------------------
miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()
print("")

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
print("")

miBici = BiciElectrica("Orbea", "HC1030")