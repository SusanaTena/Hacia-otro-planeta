import os
import pygame as pygame
from . import ALTO, ANCHO


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "portada.jpg")
        self.logo = pygame.image.load(ruta)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
            self.pantalla.fill((25, 80, 99))
            self.pintar_logo()
            pygame.display.flip()

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO/20
        self.pantalla.blit(self.logo, (pos_x, pos_y))


class Partdida(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
            self.pantalla.fill((0, 25, 0))
            pygame.display.flip()


class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
            self.pantalla.fill((30, 50, 70))
            pygame.display.flip()
