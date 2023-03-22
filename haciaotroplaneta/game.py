import pygame
from haciaotroplaneta import ALTO, ANCHO
from haciaotroplaneta.escenas import Portada, Partdida, MejoresJugadores


class HaciaOtroPlaneta:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

        self.escenas = [
            Portada (self.pantalla),
            Partdida (self.pantalla),
            MejoresJugadores (self.pantalla)
        ]

    def comienzo(self):
        for escena in self.escenas:
            escena.bucle_principal()



