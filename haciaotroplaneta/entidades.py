import os
import pygame as pg
from pygame.sprite import Sprite
from haciaotroplaneta import ALTO, ANCHO, FPS


class Nave(Sprite):

    margen_inferior = 20
    velocidad = 5
    fps_animacion = 12
    limite_animacion = FPS // fps_animacion
    iteracion = 0

    def __init__(self):
        super().__init__()
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
            midbottom=(ANCHO/2, ALTO-self.margen_inferior))
        print("rect: ", self.rect)
