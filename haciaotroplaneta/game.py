import pygame as pg
from . import ALTO, ANCHO
from .escenas import Portada, Partida, Instrucciones, Fin
from .entidades import Nave


class HaciaOtroPlaneta:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Hacia otro Planeta")

        self.escenas = [
            Portada(self.pantalla),
            Instrucciones(self.pantalla),
            Partida(self.pantalla)
        ]

    def comienzo(self):
        for escena in self.escenas:
            he_acabado = escena.bucle_principal()
            if he_acabado:
                break
        print("He acabado el for")
        pg.quit()


if __name__ == "__main__":
    juego = HaciaOtroPlaneta()
    juego.comienzo()
