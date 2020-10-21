# Pilimorfismos

class Coche():

    def desplazamiento(self):
        print("Me desplazo en 4 ruedas")


class Moto():

    def desplazamiento(self):
        print("Me desplazo en 2 ruedas")


class Camion():
    
    def desplazamiento(self):
        print("Me desplazo en 6 ruedas")


def desplazamiento_vehicualo(vehiculo):
    vehiculo.desplazamiento()

#moto1 = Moto()
#moto1.desplazamiento()

#coche1 = Coche()
#coche1.desplazamiento()

#camion1 = Camion()
#camion1.desplazamiento()

miVehiculo = Camion()
desplazamiento_vehicualo(miVehiculo)