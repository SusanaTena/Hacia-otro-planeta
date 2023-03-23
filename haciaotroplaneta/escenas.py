import os
import pygame as pg
from .entidades import Nave
from . import ALTO, ANCHO, FPS


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        ruta = os.path.join("resources", "images", "titulo.jpg")
        self.logo = pg.image.load(ruta)

        ruta_fuente = os.path.join(
            "resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(ruta_fuente, 35)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_KP_ENTER:
                    salir = True

            self.pantalla.fill((25, 80, 99))
            self.pintar_logo()
            self.pintar_texto()
            pg.display.flip()
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
        ruta = os.path.join("resources", "images", "sky_test_front.png")
        self.fondo = pg.image.load(ruta)
        self.jugador = Nave()
        #self.pelota = Meteorito(self.jugador.rect.midtop)
        #self.crear_muro()

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            self.reloj.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pintar_fondo()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            pg.display.flip()
        return False

    def pintar_fondo(self):
        self.pantalla.fill((25, 120, 200))
        # pintar la imagen de fondo en la pantalla
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.fondo, (1200, 0))


class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pantalla.fill((30, 50, 70))
            self.pantalla.blit(self.fondo(0, 0))
            pg.display.flip()
        return False
