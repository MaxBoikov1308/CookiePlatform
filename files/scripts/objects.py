import pygame as pg
from files.scripts.variables import *


class Object:
    def __init__(self, x, y, w, h, object_type):
        self.x, self.y, self.w, self.h, self.Object_type = x, y, w, h, object_type
        self.distance = 1000000
        self.color = (255, 255, 255)
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.sprite = None
        self.ISCOLLIDE = False

        self.ISACTIVE = False

    def draw(self, screen):
        # make active next comment to show blocks with collision
        # if self.ISCOLLIDE:
            # pg.draw.rect(screen, self.color, self.rect)
            # return
        screen.blit(self.sprite, (self.x, self.y))
    
    def set_active(self):
        if self.distance < 3 * GRID_SIZE:
            self.ISACTIVE = True
        else:
            self.ISACTIVE = False
            self.ISCOLLIDE = False


class Block(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (100, 100, 100)
        self.sprite = pg.transform.scale(pg.image.load("files/images/objects/block.png"), (GRID_SIZE, GRID_SIZE))


class Enemy(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (255, 0, 0)
        self.sprite = pg.transform.scale(pg.image.load("files/images/objects/enemy1.png"), (GRID_SIZE, GRID_SIZE))


class Cookie(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (255, 255, 0)
        self.sprite = pg.transform.scale(pg.image.load("files/images/objects/cookie.png"), (GRID_SIZE, GRID_SIZE))


class Spike(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (255, 0, 0)
        self.sprite = pg.transform.scale(pg.image.load("files/images/objects/spike.png"), (GRID_SIZE, GRID_SIZE))


class Finish(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (0, 0, 0)
        self.sprite = pg.transform.scale(pg.image.load("files/images/objects/finish.png"), (GRID_SIZE, GRID_SIZE))


class Start(Object):
    def __init__(self, x, y, w, h, object_type):
        super().__init__(x, y, w, h, object_type)
        self.color = (255, 255, 255)
        self.sprite = pg.transform.scale(pg.image.load("files/images/objects/start.png"), (GRID_SIZE, GRID_SIZE))