import pygame
from . import ALTO, ANCHO
from .escenas import Portada, Partdida, MejoresJugadores


class HaciaOtroPlaneta:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Hacia otro Planeta")

        self.escenas = [
            Portada(self.pantalla),
            Partdida(self.pantalla),
            MejoresJugadores(self.pantalla)
        ]

    def comienzo(self):
        for escena in self.escenas:
            he_acabado = escena.bucle_principal()
            if he_acabado:
                break
        print("He acabado el for")
        pygame.quit()
