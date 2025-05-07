class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Torneo:
    def __init__(self, ganador):
        self.ganador = ganador

class Encuentro:
    def __init__(self, torneo, limite):
        self.torneo = torneo
        self.limite = limite

# Ejemplo
jugador1 = Jugador("Carlos")
torneo1 = Torneo(jugador1)
encuentro1 = Encuentro(torneo1, 10)

print("Ganador del torneo:", encuentro1.torneo.ganador.nombre)
print("Límite del encuentro:", encuentro1.limite)




