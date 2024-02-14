import pygame as pg
from files.scripts.variables import *


class Interface:
    def __init__(self, screen):
        self.color1 = (255, 0, 0)
        self.color2 = (0, 0, 0)
        self.screen = screen
        self.coords = ((855, 900), (925, 900), (995, 900))

    def draw(self, hp):
        if hp >= 1:
            pg.draw.rect(self.screen, self.color1, (self.coords[0][0], self.coords[0][1], 50, 50))
            if hp >= 2:
                pg.draw.rect(self.screen, self.color1, (self.coords[1][0], self.coords[1][1], 50, 50))
                if hp == 3:
                    pg.draw.rect(self.screen, self.color1, (self.coords[2][0], self.coords[2][1], 50, 50))
                else:
                    pg.draw.rect(self.screen, self.color2, (self.coords[2][0], self.coords[2][1], 50, 50))
            else:
                pg.draw.rect(self.screen, self.color2, (self.coords[1][0], self.coords[1][1], 50, 50))
                pg.draw.rect(self.screen, self.color2, (self.coords[2][0], self.coords[2][1], 50, 50))
        else:
            pg.draw.rect(self.screen, self.color2, (self.coords[0][0], self.coords[0][1], 50, 50))
            pg.draw.rect(self.screen, self.color2, (self.coords[1][0], self.coords[1][1], 50, 50))
            pg.draw.rect(self.screen, self.color2, (self.coords[2][0], self.coords[2][1], 50, 50))
