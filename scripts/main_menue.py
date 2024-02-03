import pygame as pg
from variables import *

class Menue:
    def __init__(self, screen, sound):
        self.ISGAME = False
        self.SCREEN = screen
        self.bg = pg.image.load("../images/city_background.png")
        self.button_sound = sound
        self.start_coords = self.get_coords("start")
        self.start_coords_list = self.get_coords_list(self.start_coords)
    
    def draw(self):
        self.SCREEN.blit(self.bg, (0, 0))
        pg.draw.rect(self.SCREEN, (240, 0, 0), self.start_coords)
    
    def get_coords(self, name):
        if name == "start":
            return (800, 400, 320, 70)
    
    def get_coords_list(self, n):
        s = []
        for x in range(n[0], n[0] + n[2]):
            for y in range(n[1], n[1] + n[3]):
                s.append((x, y))
        return s
