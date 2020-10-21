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
    

    def info_batalla(pokemon_1, pokemon_2):
        print("\n-----BATALLA POKÉMON-----")
        print(f"\n{pokemon_1.nombre}")
        print(f"Tipo: {pokemon_1.tipo}")
        print(f"Ataque: {pokemon_1.ataque}")
        print(f"Defensa: {pokemon_1.defensa}")
        print(f"Nivel: {3*(1+np.mean([pokemon_1.ataque, pokemon_1.defensa]))}")
        print("\nVS")
        print(f"\n{pokemon_2.nombre}")
        print(f"Tipo: {pokemon_2.tipo}")
        print(f"Ataque: {pokemon_2.ataque}")
        print(f"Defensa: {pokemon_2.defensa}")
        print(f"Nivel: {3*(1+np.mean([pokemon_2.ataque, pokemon_2.defensa]))}")
        time.sleep(2) # Visualización con una demora de 2 seg


    def ventaja(pokemon_1, pokemon_2):
        tipo_pokemon = ['fuego', 'agua', 'planta']

        for i,k in enumerate(tipo_pokemon):

            # Pokémon del mismo tipo
            if pokemon_1.tipo == k:
                if pokemon_2.tipo == k:
                    cadena_1_ataque = "\nNo es muy efectivo..."
                    cadena_2_ataque = "\nNo es muy efectivo..."
            
            # Pokémon 1 tiene ventaja
            if pokemon_2.tipo == tipo_pokemon[(i+2)%3]:
                pokemon_1.ataque *= 2
                pokemon_1.defensa *=2
                pokemon_2.ataque /= 2
                pokemon_2.defensa /= 2
                cadena_1_ataque = "\n¡Es muy eficaz!" 
                cadena_2_ataque = "\nNo es muy efectivo..."

            # Pokémon 2 tiene ventaja
            if pokemon_2.tipo == tipo_pokemon[(i+1)%3]:
                pokemon_2.ataque *= 2
                pokemon_2.defensa *=2
                pokemon_1.ataque /= 2
                pokemon_1.defensa /= 2
                cadena_1_ataque = "\nNo es muy efectivo..."
                cadena_2_ataque = "\n¡Es muy eficaz!"
            return cadena_1_ataque, cadena_2_ataque
    

    # Inicia Pokémon 1, elige ataque y calcula los nuevos HP
    # Se realiza lo mismo con Pokémos 2 hasta que los HP de unos de los pokes < 0
    # Se actualiza los datos
    def turno(pokemon_1, pokemon_2, cadena_1_ataque, cadena_2_ataque):
        
        while (pokemon_1.barras > 0) and (pokemon_2.barras > 0):
            print(f"\n{pokemon_1.nombre}\t\tHP\t{pokemon_1.hp}")
            print(f"{pokemon_2.nombre}\t\tHP\t{pokemon_2.hp}")
            
            print(f"\n¡Adelante {pokemon_1.nombre}!")
            for i,x in enumerate (pokemon_1.movimientos):
                print(f"{i+1}.", x)
            index = int(input("Elige un movimiento: "))
            imprimir_con_retraso(f"\n¡{pokemon_1.nombre} usó {pokemon_1.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_1_ataque)

            # Determinar Daño
            pokemon_2.barras -= pokemon_1.ataque
            pokemon_2.hp = ""

            # Agregar barras adicionales
            for j in range(int(pokemon_2.barras+.1*pokemon_2.defensa)):
                pokemon_2.hp += "■"
            
            time.sleep(1)
            print(f"\n{pokemon_1.nombre}\t\tHP\t{pokemon_1.hp}")
            print(f"{pokemon_2.nombre}\t\tHP\t{pokemon_2.hp}\n")
            time.sleep(5)

            # Comprobar si Pokémon se debilitó
            if pokemon_2.barras <= 0:
                imprimir_con_retraso("\n..." + pokemon_2.nombre + " pierde la batalla")
                break

            print(f"¡Adelante {pokemon_2.nombre}!")
            for i,x in enumerate (pokemon_2.movimientos):
                print(f"{i+1}.", x)
            index = int(input("Elige un movimiento: "))
            imprimir_con_retraso(f"\n¡{pokemon_2.nombre} usó {pokemon_2.movimientos[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            # Determinar Daño
            pokemon_1.barras -= pokemon_2.ataque
            pokemon_1.hp = ""

            # Agregar barras adicionales
            for j in range(int(pokemon_1.barras+.1*pokemon_1.defensa)):
                pokemon_1.hp += "■"
            
            time.sleep(1)
            print(f"\n{pokemon_1.nombre}\t\tHP\t{pokemon_1.hp}")
            print(f"{pokemon_2.nombre}\t\tHP\t{pokemon_2.hp}\n")
            time.sleep(5)

            # Comprobar si Pokémon se debilitó
            if pokemon_1.barras <= 0:
                imprimir_con_retraso("..." + pokemon_1.nombre + " pierde la batalla")
                break
    

    def batalla(pokemon_1, pokemon_2):
        pokemon_1.info_batalla(pokemon_2)
        cadena_1_ataque, cadena_2_ataque = pokemon_1.ventaja(pokemon_2)
        pokemon_1.turno(pokemon_2, cadena_1_ataque, cadena_2_ataque)
        money = np.random.choice(5000)
    
if __name__ == "__main__":
    charizard = Pokemon('Charizard', 'fuego', ['Lanza Llamas', 'Pirotecnia', 'Giro Fuero', 'Ascuas'], {'ataque':13, 'defensa':9})
    blastoise = Pokemon('Blastoise', 'agua', ['Pistola Agua', 'Burbuja', 'Hidropulso', 'Hidrobomba'], {'ataque':10, 'defensa':10})
    venusaur = Pokemon('Venusaur', 'planta', ['Latigo Ceoa', 'Hoja Afilada', 'Rayo Solar', 'Abatidora'], {'ataque':8, 'defensa':12})
    charizard.batalla(blastoise)
    #blastoise.batalla(venusaur)