import os
import pygame as pg
from random import *
from .entidades import Nave
from . import ALTO, ANCHO, FPS
from .entidades import Colision, Meteorito, Nave, Planeta

pg.font.init()
pg.font.get_init()

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
        self.colision = Colision()
        self.planeta = Planeta((ANCHO, ALTO/4))

        
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        show_time = 20
        show_colision = False
        num_colisiones = 0

        font1 = pg.font.SysFont('freesanbold.ttf', 50)
        
        while not salir:
            self.reloj.tick(FPS)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pintar_fondo()

            pg.time.get_ticks()

            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            #self.jugador.hay_colision(self.jugador)

            golpeados = pg.sprite.spritecollide(
                self.jugador, self.meteoritos, True)

            if len(golpeados) > 0 or show_colision == True:
                show_colision = True
                show_time = show_time - 1
                self.pantalla.blit(self.colision.image, self.jugador.rect)

            self.pantalla.blit(self.planeta.image, self.planeta.rect)
            
            if show_time == 0:
                num_colisiones = num_colisiones + 1
                show_time = 20
                show_colision = False

            # sumar la puntuación de todos los Meteoritos esquivados
            # todos los que pasen de la y suman 10 pts
            # vidas = 5
            # 
            text1 = font1.render(
                    "Colisiones: " + str(num_colisiones), True, (0, 50, 0))
            textRect1 = text1.get_rect()
            textRect1.center = (ANCHO/2, 25)

            self.pantalla.blit(text1, textRect1)

            if pg.time.get_ticks() < 100000:
                for meteorito in self.meteoritos.sprites():
                    meteorito.update()
                    self.pantalla.blit(meteorito.image, meteorito.rect)
            
            #borrar? self.tiempo = self.tiempo * 10

            if num_colisiones > 5:
                mensaje = "Has perdido una vida"
                texto = font1.render(mensaje, True, (0, 0, 0))
                pos_x = ANCHO/2 - texto.get_width()/2
                pos_y = ALTO/4
                self.pantalla.blit(texto, (pos_x, pos_y))

        
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

