import os
import pygame as pg
from pygame.sprite import Sprite
from haciaotroplaneta import ALTO, ANCHO, FPS



class Nave(Sprite):

    margen_izquierdo = 120
    velocidad = 5
    fps_animacion = 12
    limite_animacion = FPS // fps_animacion
    iteracion = 0

    def __init__(self):
        super().__init__()
        self.velocidad_x = self.velocidad
        self.imagenes = [
            pg.image.load(
                os.path.join("resources", "images", "nave.png")
            ),
            pg.image.load(
                os.path.join("resources", "images", "nave.png")
            ),
            pg.image.load(
                os.path.join("resources", "images", "airship.png")
            )]
        self.siguiente_imagen = 0
        self.image = self.imagenes[self.siguiente_imagen]
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

    def hay_colision(self, otro):
        if self.rect.colliderect(otro):
            # hay_colision
            self.velocidad_x = -self.velocidad_x
        self.image = pg.image.load(
            os.path.join("resources", "images", "nave.png"))

class Meteorito(Sprite):

    def __init__(self, posicion, velocidad):
        super().__init__()
        self.velocidad_x = velocidad
        self.image = pg.image.load(
            os.path.join("resources", "images", "meteo.png")
        )
        self.rect = self.image.get_rect(
            midbottom=posicion)

    def update(self):

        # calculo de la posición de la pelota
        # en movimiento
        self.rect.x += self.velocidad_x

        # self.rect.x += self.velocidad_x
        # llegar a la parte izquierda
        if self.rect.width <= 0:
            self.velocidad_x = -self.velocidad_x

    def pierdes(self):
        print("Has perdido una vida")

    def reset(self):
        print("Volvemos a poner la pelota en la posición inicial")

    def hay_colision(self, otro):
        if self.rect.colliderect(otro):
            # hay_colision
            self.velocidad_x = -self.velocidad_x
        self.image = pg.image.load(
            os.path.join("resources", "images", "explosion.png")
        )
        
