import time
import numpy as np
import sys

# Imprimir cada letra con un retraso de 0.05 décimas
def imprimir_con_retraso(palabra):
    for letra in palabra:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.05)


# Clases
class Pokemon:
    def __init__(self, nombre, tipo, movimientos, ivs, hp="■■■■■■■■■■■■■■■■■■■■"):
        self.nombre = nombre
        self.tipo = tipo
        self.movimientos = movimientos
        self.ataque = ivs['ataque']
        self.defensa = ivs['defensa']
        self.hp = hp
        self.barras = 20
    

    def info_batalla(self, enemigo):
        print("\n-----BATALLA POKÉMON-----")
        print(f"\n{self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Nivel: {3*(1+np.mean([self.ataque, self.defensa]))}")
        print("\nVS")
        print(f"\n{enemigo.nombre}")
        print(f"Tipo: {enemigo.tipo}")
        print(f"Ataque: {enemigo.ataque}")
        print(f"Defensa: {enemigo.defensa}")
        print(f"Nivel: {3*(1+np.mean([enemigo.ataque, enemigo.defensa]))}")
        time.sleep(2) # Visualización con una demora de 2 seg


    def ventaja(self, enemigo):
        # Fuego tiene ventaja sobre Planta
        # Planta tiene ventaja sobre Agua
        # Agua tiene ventaja sobre Fuego
        tipo_pokemon = ['fuego', 'agua', 'planta']

        for i,k in enumerate(tipo_pokemon):

            # Pokémon del mismo tipo
            if self.tipo == k:
                if enemigo.tipo == k:
                    cadena_1_ataque = "\nNo es muy efectivo..."
                    cadena_2_ataque = "\nNo es muy efectivo..."

            # Pokémon 2 tiene ventaja
            if enemigo.tipo == tipo_pokemon[(i+1)%3]:
                enemigo.ataque *= 2
                enemigo.defensa *=2
                self.ataque /= 2
                self.defensa /= 2
                cadena_1_ataque = "\nNo es muy efectivo..."
                cadena_2_ataque = "\n¡Es muy eficaz!"

            # Pokémon 1 tiene ventaja
            if enemigo.tipo == tipo_pokemon[(i+2)%3]:
                self.ataque *= 2
                self.defensa *=2
                enemigo.ataque /= 2
                enemigo.defensa /= 2
                cadena_1_ataque = "\n¡Es muy eficaz!" 
                cadena_2_ataque = "\nNo es muy efectivo..."
            return cadena_1_ataque, cadena_2_ataque
    
    # Inicia Pokémon 1, elige ataque y calcula los nuevos HP
    # Se realiza lo mismo con Pokémos 2 hasta que los HP de unos de los pokes < 0
    # Se actualiza los datos
    def turno(self, enemigo, cadena_1_ataque, cadena_2_ataque):
        
        while (self.barras > 0) and (enemigo.barras > 0):
            print(f"\n{self.nombre}\t\tHP\t{self.hp}")
            print(f"{enemigo.nombre}\t\tHP\t{enemigo.hp}")
            
            print(f"\n¡Adelante {self.nombre}!")
            for i,x in enumerate (self.movimientos):
                print(f"{i+1}.", x)
            index = int(input("Elige un movimiento: "))
            imprimir_con_retraso(f"\n¡{self.nombre} usó {self.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            # Determinar Daño
            enemigo.barras -= self.ataque
            enemigo.hp = ""

            # Agregar barras adicionales
            for j in range(int(enemigo.barras+.1*enemigo.defensa)):
                enemigo.hp += "■"
            
            time.sleep(1)
            print(f"\n{self.nombre}\t\tHP\t{self.hp}")
            print(f"{enemigo.nombre}\t\tHP\t{enemigo.hp}\n")
            time.sleep(5)

            # Comprobar si Pokémon se debilitó
            if enemigo.barras <= 0:
                imprimir_con_retraso("\n..." + enemigo.nombre + " pierde la batalla")
                break

            print(f"¡Adelante {enemigo.nombre}!")
            for i,x in enumerate (enemigo.movimientos):
                print(f"{i+1}.", x)
            index = int(input("Elige un movimiento: "))
            imprimir_con_retraso(f"\n¡{enemigo.nombre} usó {enemigo.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            # Determinar Daño
            self.barras -= enemigo.ataque
            self.hp = ""

            # Agregar barras adicionales
            for j in range(int(self.barras+.1*self.defensa)):
                self.hp += "■"
            
            time.sleep(1)
            print(f"\n{self.nombre}\t\tHP\t{self.hp}")
            print(f"{enemigo.nombre}\t\tHP\t{enemigo.hp}\n")
            time.sleep(5)

            # Comprobar si Pokémon se debilitó
            if self.barras <= 0:
                imprimir_con_retraso("..." + self.nombre + " pierde la batalla")
                break
    

    def batalla(self, enemigo):
        self.info_batalla(enemigo)
        cadena_1_ataque, cadena_2_ataque = self.ventaja(enemigo)
        self.turno(enemigo, cadena_1_ataque, cadena_2_ataque)
    
if __name__ == "__main__":
    charizard = Pokemon('Charizard', 'fuego', ['Lanza Llamas', 'Pirotecnia', 'Giro Fuero', 'Ascuas'], {'ataque':13, 'defensa':9})
    blastoise = Pokemon('Blastoise', 'agua', ['Pistola Agua', 'Burbuja', 'Hidropulso', 'Hidrobomba'], {'ataque':10, 'defensa':10})
    venusaur = Pokemon('Venusaur', 'planta', ['Latigo Ceoa', 'Hoja Afilada', 'Rayo Solar', 'Abatidora'], {'ataque':8, 'defensa':12})
    #charizard.batalla(blastoise)
    blastoise.batalla(charizard)