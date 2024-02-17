import pygame as pg
from files.scripts.variables import *


class Interface:
    def __init__(self, screen):
        self.heart = pg.transform.scale(pg.image.load("files/images/interface/heart_full.png"), (50, 50))
        self.heart_hollow = pg.transform.scale(pg.image.load("files/images/interface/heart_hollow.png"), (50, 50))
        self.screen = screen
        self.coords = ((855, 900), (925, 900), (995, 900))

    def draw(self, hp):
        if hp >= 1:
            self.screen.blit(self.heart, (self.coords[0][0], self.coords[0][1], 50, 50))
            if hp >= 2:
                self.screen.blit(self.heart, (self.coords[1][0], self.coords[1][1], 50, 50))

                if hp == 3:
                    self.screen.blit(self.heart, (self.coords[2][0], self.coords[2][1], 50, 50))
                else:
                    self.screen.blit(self.heart_hollow, (self.coords[2][0], self.coords[2][1], 50, 50))
            else:
                self.screen.blit(self.heart_hollow, (self.coords[1][0], self.coords[1][1], 50, 50))
                self.screen.blit(self.heart_hollow, (self.coords[2][0], self.coords[2][1], 50, 50))
        else:
            self.screen.blit(self.heart_hollow, (self.coords[0][0], self.coords[0][1], 50, 50))
            self.screen.blit(self.heart_hollow, (self.coords[1][0], self.coords[1][1], 50, 50))
            self.screen.blit(self.heart_hollow, (self.coords[2][0], self.coords[2][1], 50, 50))
