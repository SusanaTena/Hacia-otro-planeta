import pygame
from haciaotroplaneta import ALTO, ANCHO


class HaciaOtroPlaneta:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))

    def comienzo(self):
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
            self.pantalla.fill((25, 80, 99))
            pygame.display.flip()



