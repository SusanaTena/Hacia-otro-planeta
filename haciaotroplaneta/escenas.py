import os
import pygame as pg
from random import *
from .entidades import Nave
from . import ALTO, ANCHO, FPS
from .entidades import Colision, Meteorito, Nave

pg.font.init()


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass


class Marcador:

        def __init__(self, centro_h, color):
            self.letra_marcador = pg.font.SysFont("arial", 100)
            self.color = color
            self.centro_h = pg.display.get_surface().get_width() / 2

        texto_uno = pg.font.SysFont("comic", 32)
        texto_dos = pg.font.SysFont("arial black", 50)

        #texto = texto_uno.render("SCORE = ")

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



class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "sky_test_front.png")
        self.fondo = pg.image.load(ruta)
        self.jugador = Nave()
        self.num_meteoritos = 1000
        self.tiempo = 60

        self.meteoritos = pg.sprite.Group()

        self.crear_meteoritos()

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        colision = Colision
        while not salir:
            self.reloj.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pintar_fondo()
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            #self.jugador.hay_colision(self.jugador)

            golpeados = pg.sprite.spritecollide(
                self.jugador, self.meteoritos, True)

            if len(golpeados) > 0:
                self.pantalla.blit(colision.image, self.jugador.rect)
                #########pintar imagen explosion, borrar meteorito

            # sumar la puntuación de todos los Meteoritos esquivados

            if pg.time.get_ticks() < 100000:
                for meteorito in self.meteoritos.sprites():
                    meteorito.update()
                    self.pantalla.blit(meteorito.image, meteorito.rect)
            
            self.tiempo = self.tiempo * 10

            print("tiempo", pg.time.get_ticks())

            #añadir duracion explosion
            pg.display.flip()
        return False

    def pintar_fondo(self):
        self.pantalla.fill((25, 120, 200))
        # pintar la imagen de fondo en la pantalla
        self.pantalla.blit(self.fondo, (0,0))
        self.pantalla.blit(self.fondo, (1200, 0))

    def crear_meteoritos(self):

        margen_derecho = +100

        for i in range(self.num_meteoritos):
            # randint devuelve un valor aleatorio entre el primer y el segundo entero
            meteorito = Meteorito(
                (ANCHO + randint(0, 100000), randint(1, ALTO)), -7)
            self.meteoritos.add(meteorito)


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
