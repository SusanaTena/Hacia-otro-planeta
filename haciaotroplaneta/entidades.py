import os
import pygame as pg
from haciaotroplaneta import ALTO, ANCHO, FPS
from pygame.sprite import Sprite
from random import *


class Nave(Sprite):

    margen_izquierdo = 120
    velocidad = 5
    fps_animacion = 12
    limite_animacion = FPS // fps_animacion
    iteracion = 0

    def __init__(self):
        super().__init__()
        self.velocidad_x = self.velocidad

        self.image=pg.image.load(os.path.join("resources", "images", "nave.png"))
        self.rect = self.image.get_rect(
            midbottom=(self.margen_izquierdo, ALTO/2))

    def update(self):
        teclas = pg.key.get_pressed()
        if teclas[pg.K_DOWN]:
            self.rect.y += self.velocidad
            if self.rect.height > ALTO:
                self.rect.height = ALTO
        if teclas[pg.K_UP]:
            self.rect.y -= self.velocidad
            if self.rect.height < 0:
                self.rect.height = 0

    def aterrizar(self):

        if self.rect.x >= ANCHO - 210:
            self.rect.y = ALTO / 1.75
            self.rect.x = ANCHO - 180
            self.image = pg.image.load(os.path.join(   
                "resources", "images", "nave-rotada.png"))
            self.rect = self.image.get_rect(
                midbottom=(self.rect.x, self.rect.y))
            
        else:
            self.rect.x += 5
            self.rect.y = ALTO/2

    


class Meteorito(Sprite):

    def __init__(self, posicion):
        super().__init__()
        self.image = pg.image.load(
            os.path.join("resources", "images", "meteo.png")
        )
        self.rect = self.image.get_rect(
            midbottom=posicion)
        self.tipoImage = randint (1,3)
        if self.tipoImage == 1:
            self.image = pg.image.load(
                os.path.join("resources", "images", "meteo.png")
            )
        elif self.tipoImage == 2:
            self.image = pg.image.load(
                os.path.join("resources", "images", "meteo1.png")
            )
        else:
            self.image = pg.image.load(
                os.path.join("resources", "images", "meteo2.png")
        )

        self.velocidadMet = randint (1,3)
        if self.velocidadMet == 1:
            self.velocidadMet = -15
        elif self.velocidadMet == 2:
            self.velocidadMet = -6
        else:
            self.velocidadMet = -8

        self.velocidad_x = self.velocidadMet


    def update(self):
        # calculo de la posición de la nave en movimiento
        self.rect.x += self.velocidad_x

        # llegar a la parte izquierda
        if self.rect.width <= 0:
            self.velocidad_x = -self.velocidad_x

class Colision(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(
            os.path.join("resources", "images", "explosion.png"))
        self.sonido_colision = pg.mixer.Sound(os.path.join("resources", "sounds", "impacto.mp3"))
    
    def reproducir(self):
      pg.mixer.Sound.play(self.sonido_colision)
        

class Planeta:
    def __init__(self, posicion):
        super().__init__()
        self.image = pg.image.load(
            os.path.join("resources", "images", "mercury.png"))
        self.rect = self.image.get_rect(
            midbottom=posicion)
        self.sonido_llegada = pg.mixer.Sound(
            os.path.join("resources", "sounds", "fin.mp3"))

    def reproducir(self):
      pg.mixer.Sound.play(self.sonido_llegada)
    
    

        
