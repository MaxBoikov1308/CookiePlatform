import pygame as pg
from peewee import SqliteDatabase, Model, TextField, IntegerField

db = SqliteDatabase("levels/level2.db")

class Level(Model):
    name = TextField()
    x = IntegerField()
    y = IntegerField()
    h = IntegerField()
    w = IntegerField()

    class Meta:
        database = db


class Builder:
    def __init__(self, screen):
        self.level = Level
        self.objects = self.load_objects_from_db()
        self.screen = screen
        self.objects = self.load_objects_from_db()

    def load_objects_from_db(self):
        objects = []
        for obj in Level.select():
            objects.append([obj.x, obj.y, obj.w, obj.h])
        return objects

    def draw(self, color):
        for obj_coords in self.objects:
            x0, y0, w, h = obj_coords
            pg.draw.rect(self.screen, color, (x0, y0, w, h))
