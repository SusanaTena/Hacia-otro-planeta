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

        ruta_fuente = os.path.join(
            "resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pygame.font.Font(ruta_fuente, 35)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                    salir = True

            self.pantalla.fill((25, 80, 99))
            self.pintar_logo()
            self.pintar_texto()
            pygame.display.flip()
        return False

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO/20
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_texto(self):
        mensaje = "Pulsa Enter para comenzar la partida"
        texto = self.tipografia.render(mensaje, True, (0, 0, 0))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO/4
        self.pantalla.blit(texto, (pos_x, pos_y))


class Partdida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "saturn.jpg")
        self.fondo = pygame.image.load(ruta)

    def bucle_principal(self):
        super().bucle_principal()
        return False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir = True
            self.pintar_fondo()
            pygame.display.flip()
        return False

    def pintar_fondo(self):
        self.pantalla.fill((25, 120, 200))
        # pintar la imagen de fondo en la pantalla
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.fondo, (600, 0))


class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
            self.pantalla.fill((30, 50, 70))
            pygame.display.flip()
        return False
