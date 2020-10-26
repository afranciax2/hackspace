# Métodos especiales

# --- Constructor ---

class Galleta:
    chispas = False

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
    
    def __str__(self):
        return f"Soy una galleta {self.color} y {self.sabor}."

galleta_1 = Galleta("blanca", "dulce")

print(galleta_1)
print(str(galleta_1))
print(galleta_1.__str__())

# --- Destructor ---

class Chocolate:

    def __del__(self):
        print("El chocolate se está borrando de la memoria")

chocolate_1 = Chocolate()
#del(chocolate_1)
#chocolate_1.__del__()


# --- Length ---
class Cancion:
    def __init__(self, autor, titulo, duracion):
        self.duracion = duracion
    
    def __len__(self):
        return self.duracion

cancion = Cancion("Queen", "Don't Stop Me Now", 210)
print(len(cancion))
print(cancion.__len__())