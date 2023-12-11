import pygame as pg


class Player:
    def __init__(self):
        self.width = 50
        self.height = 100

    def jump(self):
        pass

    def draw(self, screen, x0, y0, color):
        pg.draw.rect(screen, color, (x0, y0, self.width, self.height))

