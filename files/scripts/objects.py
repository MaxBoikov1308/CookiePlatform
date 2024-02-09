import pygame as pg
from files.scripts.variables import *


class Object:
    def __init__(self, x, y, w, h, object_type):
        self.x, self.y, self.w, self.h, self.Object_type = x, y, w, h, object_type
        self.distance = 1000000
        self.color = (255, 255, 255)
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)

        self.ISACTIVE = False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
    
    def set_active(self):
        if self.distance < 2 * GRID_SIZE:
            self.ISACTIVE = True
        else:
            self.ISACTIVE = False
    
    def action(self):
        pass


class Block(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (100, 100, 100)


class Enemy(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (255, 0, 0)


class Cookie(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (255, 255, 0)


class Spike(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (255, 0, 0)


class Finish(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (0, 0, 0)


class Start(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (255, 255, 255)