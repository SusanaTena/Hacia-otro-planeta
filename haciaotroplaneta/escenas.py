import os
import pygame as pg
from random import *
from .entidades import Nave
from . import ALTO, ANCHO, FPS
from .entidades import Colision, Meteorito, Nave, Planeta

pg.font.init()
pg.font.get_init()

# pygame.transform.rotozoom(Surface, angle, scale): return Surface -- para rotar la nave (http://www.losersjuegos.com.ar/traducciones/pygame/transform#rotate)

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
        mensaje = "Pulsa Enter."
        texto = self.tipografia.render(mensaje, True, (0, 0, 0))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO/4
        self.pantalla.blit(texto, (pos_x, pos_y))


class Instrucciones(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
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
            self.pintar_texto()
            pg.display.flip()
        return False

    def pintar_texto(self):
        mensaje = "¡Esquiva para llegar al planeta!"
        texto = self.tipografia.render(mensaje, True, (0, 0, 0))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO/4
        self.pantalla.blit(texto, (pos_x, pos_y))

        mensaje = "Pulsa flecha arriba o abajo para moverte."
        texto = self.tipografia.render(mensaje, True, (0, 0, 0))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO/4+70
        self.pantalla.blit(texto, (pos_x, pos_y))

        mensaje = "Tienes tres vidas, y perderás una por cada 5 impactos."
        texto = self.tipografia.render(mensaje, True, (0, 0, 0))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO/4+140
        self.pantalla.blit(texto, (pos_x, pos_y))

        mensaje = "Pulsa Enter para comenzar."
        texto = self.tipografia.render(mensaje, True, (0, 0, 0))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO/4+210
        self.pantalla.blit(texto, (pos_x, pos_y))

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "nasa.jpg")
        self.fondo = pg.image.load(ruta)
        self.jugador = Nave()
        self.num_meteoritos = 2000
        self.tiempo_partida = 20000
        self.meteoritos = pg.sprite.Group()
        self.crear_meteoritos()
        self.colision = Colision()
        self.planeta = Planeta((ANCHO, ALTO))
        
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        show_time = 20
        show_colision = False
        num_colisiones = 0
        num_vidas = 3
        fuente = pg.font.SysFont('freesanbold.ttf', 50)
        
        while not salir:
            self.reloj.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pintar_fondo()

            pg.time.get_ticks()

            if pg.time.get_ticks() <= self.tiempo_partida:
                self.jugador.update()
                self.pantalla.blit(self.jugador.image, self.jugador.rect)

            golpeados = pg.sprite.spritecollide(
                self.jugador, self.meteoritos, True)

            if len(golpeados) > 0 or show_colision == True:
                if show_time == 20:
                    self.colision.reproducir()
                
                show_colision = True
                show_time = show_time - 1
                self.pantalla.blit(self.colision.image, self.jugador.rect)
                                     
            if show_time == 0:
                num_colisiones = num_colisiones + 1
                show_time = 20
                show_colision = False

            textoColisiones = fuente.render(
                    "Colisiones: " + str(num_colisiones), True, (255, 200, 0))
            textoColisionesRect = textoColisiones.get_rect()
            textoColisionesRect.center = (ANCHO/2 - 300, 25)

            self.pantalla.blit(textoColisiones, textoColisionesRect)

            if pg.time.get_ticks() < self.tiempo_partida:
                for meteorito in self.meteoritos.sprites():
                    meteorito.update()
                    self.pantalla.blit(meteorito.image, meteorito.rect)

            if num_colisiones > 5:
                num_colisiones = 0
                num_vidas = num_vidas - 1 

            textoVidas = fuente.render(str(num_vidas) + " vida(s)", True, (255, 200, 0))
            textoVidasRect = textoVidas.get_rect()
            textoVidasRect.center = (ANCHO/2 + 100, 25)
            self.pantalla.blit(textoVidas, textoVidasRect)

            if num_vidas == 0:
                salir = True

            if pg.time.get_ticks() > self.tiempo_partida:
                self.pantalla.blit(self.planeta.image, self.planeta.rect)
                textoFin = fuente.render ("¡¡FELICIDADES!!", True, (255,255,255))
                textoFinRect = textoFin.get_rect()
                textoFinRect.center = (ANCHO/2, ALTO/2)
                self.pantalla.blit(textoFin, textoFinRect)
                textoFin = fuente.render("HAS LLEGADO AL PLANETA SIRIUS :)", True, (255, 255, 255))
                textoFinRect = textoFin.get_rect()
                textoFinRect.center = (ANCHO/2, ALTO/1.75)
                self.pantalla.blit(textoFin, textoFinRect)
                self.jugador.aterrizar()
                self.planeta.reproducir()
                self.pantalla.blit(self.jugador.image, self.jugador.rect)

            pg.display.flip()
        return False

    def pintar_fondo(self):
        self.pantalla.fill((25, 120, 200))
        self.pantalla.blit(self.fondo, (0,0))
        self.pantalla.blit(self.fondo, (1200, 0))

    def crear_meteoritos(self):

        margen_derecho = +100

        for i in range(self.num_meteoritos):
            # randint devuelve un valor aleatorio entre el primer y el segundo entero
            meteorito = Meteorito(
                (ANCHO + randint(0, 100000), randint(1, ALTO)))
            self.meteoritos.add(meteorito)



