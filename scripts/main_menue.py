import pygame as pg
from variables import *

class Menue:
    def __init__(self, screen, sound):
        self.ISGAME = False
        self.SCREEN = screen
        self.bg = pg.image.load("../images/city_background.png")
        self.logo = pg.image.load("../images/icon.ico")
        self.button_sound = sound
        self.start_coords = self.get_coords("start")
        self.start_coords_list = self.get_coords_list(self.start_coords)
        self.level_coords = self.get_coords("level")
        self.level_coords_list = self.get_coords_list(self.level_coords)
        self.score_coords = self.get_coords("score")
        self.score_coords_list = self.get_coords_list(self.start_coords)
        self.redactor_coords = self.get_coords("redactor")
        self.redactor_coords_list = self.get_coords_list(self.level_coords)
        self.exit_coords = self.get_coords("exit")
        self.exit_coords_list = self.get_coords_list(self.exit_coords)
        self.pause_coords = self.get_coords("pause")
        self.pause_coords_list = self.get_coords_list(self.pause_coords)
    
    def draw(self):
        self.SCREEN.blit(self.bg, (0, 0))
        self.SCREEN.blit(self.logo, (830, 100))
        pg.draw.rect(self.SCREEN, (0, 240, 0), (760, 290, 400, 70))
        pg.draw.rect(self.SCREEN, (240, 0, 0), self.start_coords)
        pg.draw.rect(self.SCREEN, (240, 0, 0), self.level_coords)
        pg.draw.rect(self.SCREEN, (240, 0, 0), self.score_coords)
        pg.draw.rect(self.SCREEN, (240, 0, 0), self.redactor_coords)
        pg.draw.rect(self.SCREEN, (240, 0, 0), self.exit_coords)
    
    def get_coords(self, name):
        if name == "start":
            return (800, 400, 320, 70)
        elif name == "level":
            return (800, 500, 320, 70)
        elif name == "score":
            return (800, 600, 320, 70)
        elif name == "redactor":
            return (800, 700, 320, 70)
        elif name == "exit":
            return (800, 800, 320, 70)
        elif name == "pause":
            return (910, 550, 100, 100)
    
    def get_coords_list(self, n):
        s = []
        for x in range(n[0], n[0] + n[2]):
            for y in range(n[1], n[1] + n[3]):
                s.append((x, y))
        return s
