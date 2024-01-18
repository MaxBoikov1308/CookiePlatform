import pygame as pg
from peewee import *

db = SqliteDatabase("levels/level1.db")


class Level(Model):
    name = TextField()
    x = IntegerField()
    y = IntegerField()
    h = IntegerField()
    w = IntegerField()

    class Meta:
        database = db


class Level1(Level):
    def __init__(self):
        super().__init__()
        self.objects = {}
        self.write()
        self.names = self.objects.keys()
    
    def draw(self, screen, color):
        for obj in self.names:
            x0 = self.objects[obj][0]
            y0 = self.objects[obj][1]
            w = self.objects[obj][2]
            h = self.objects[obj][3]
            pg.draw.rect(screen, color, (x0, y0, w, h))
    
    def add(self, name, x, y, w, h):
        self.objects[name] = (x, y, w, h)
    
    def write(self):
        for i in Level.select():
            self.add(i.name, i.x, i.y, i.h, i.w)
    


# Level.create_table()
# cube = Level(name="cube", x=500, y=500, h=100, w=100)
# cube.save()