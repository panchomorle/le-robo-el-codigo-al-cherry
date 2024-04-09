import random
import time

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = random.randint(1, 100)
        self.defensa = random.randint(1, 100)
        self.media = random.randint(1, 100)

    def __str__(self):
        return f"{self.nombre} | Ataque: {self.ataque}, Defensa: {self.defensa}, Media: {self.media}"

#Equipos de jugadores
equipo1 = [Jugador("BLOCK ERNST"), Jugador("ORDOÑEZ"), Jugador("STESSENS"), Jugador("GIORDANA"), Jugador("PAVÓN")]
equipo2 = [Jugador("thunder_1"), Jugador("thunder_2"), Jugador("thunder_3"), Jugador("thunder_4"), Jugador("thunder_5")]

#Simular el partido
def simular_partido(equipo1, equipo2):
    marcador_equipo1 = 0
    marcador_equipo2 = 0
    for i in range(5):
        print(f"Jugada {i+1}:")
        time.sleep(3)
        jugador_equipo1 = equipo1[i]
        jugador_equipo2 = equipo2[i]
        print(f"{jugador_equipo1} vs {jugador_equipo2}")

        #Condiciones de LAGE para que llegue al GOOOL
        if jugador_equipo1.media > jugador_equipo2.defensa: #PVP
            print(f"Arranca por la derecha el genio de LAGE del fútbol mundial.")
            time.sleep(3)
            if jugador_equipo1.ataque > jugador_equipo2.defensa: #Comparación atributos de media para ver si se da el gol.
                print(f"Gol de {jugador_equipo1.nombre}!")
                marcador_equipo1 += 1
                time.sleep(3)
            else:
                print("Que bien defiende Thunder")
        """else:
            print(f"{jugador_equipo2.nombre} de SAMAR recupera la pelota.")"""
            
        #Condiciones de SAMAR para que llegue al GOOOL
        if jugador_equipo2.media > jugador_equipo1.defensa: #PVP
            print(f"Madre mía como avanza Thunder")
            time.sleep(3)
            if jugador_equipo2.ataque > jugador_equipo1.defensa: #Comparación atributos de media para ver si se da el gol.
                print(f"Gol de {jugador_equipo2.nombre}!")
                marcador_equipo2 += 1
                time.sleep(3)
            else:
                print("Que bien defiende LAGE")
        """else: 
            print(f"{jugador_equipo1.nombre} de LAGE recupera la pelota")"""

        print(f"Marcador: LAGE ({marcador_equipo1}) - Thunder ({marcador_equipo2})")
        print()

    # Mostrar marcador final
    print("=== Marcador Final ===")
    print(f"LAGE: {marcador_equipo1}")
    print(f"Thunder: {marcador_equipo2}")

# Simular el partido
print("=== LAGE vs Thunder ===")
simular_partido(equipo1, equipo2)
