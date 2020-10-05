#OBJETO - ¿Qúe es?

# Objeto (Auto):
#   - Tiene propiedades (Atributos):
#       . Color
#       . Peos
#       . Alto
#       . Largo
#
#   - Tiene un comportamiento (¿Qué es capaz de hacer?)
#       . Arrancar
#       . Frenar
#       . Girar
#       . Acelerar


# Clase.- Modelo donde se redactan las características comunes de un grupo de objetos.
#   .Chasis, ruedas.

# Instanciar clase.- Un ejemplar pertenenciente a una clase
#   . Auto Peugeot y Citröen - Ambos compartes el mismo chasis y ruedas
#   . El Peugeot es un objeto perteneciente a una clase,  ejmplar de la clase y una instancia de clase.

# Modularización.- Aplicación formada por varias clases, ejemplo de equipos de sonido HiFi vs moderno.

class Auto():
    # Propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False
    
    # Comportamientos son "Métodos"
    # SELF hace referencia a la instancia perteneciente a la clase
    # SELF es equivalente al THIS
    def arrancar(self):
        self.enMarcha = True
    
    def estado(self):
        if(self.enMarcha):
            return "El auto está en marcha."
        else:
            return "El auto está parado."


# Esto es instanciar una clase
miAuto = Auto()
print(f"El largo de auto es {miAuto.largoChasis}")
print(f"El auto tiene {miAuto.ruedas} ruedas")
#miAuto.arrancar()
print(miAuto.estado())