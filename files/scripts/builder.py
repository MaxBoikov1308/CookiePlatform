import pygame as pg
from peewee import SqliteDatabase, Model, TextField, IntegerField
from files.scripts.objects import *

db = SqliteDatabase("files/levels/level1.db")

class Level(Model):
    Object_type = TextField()
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

    def load_objects_from_db(self):
        objects = []
        for obj in Level.select():
            if obj.Object_type == "block":
                objects.append(Block(obj.x, obj.y, obj.w, obj.h, obj.Object_type))
            elif obj.Object_type == "enemy":
                objects.append(Enemy(obj.x, obj.y, obj.w, obj.h, obj.Object_type))
            elif obj.Object_type == "cookie":
                objects.append(Cookie(obj.x, obj.y, obj.w, obj.h, obj.Object_type))
            elif obj.Object_type == "spike":
                objects.append(Spike(obj.x, obj.y, obj.w, obj.h, obj.Object_type))
            elif obj.Object_type == "start":
                objects.append(Start(obj.x, obj.y, obj.w, obj.h, obj.Object_type))
            elif obj.Object_type == "finish":
                objects.append(Finish(obj.x, obj.y, obj.w, obj.h, obj.Object_type))
        return objects

    def draw(self):
        for obj in self.objects:
            obj.draw(self.screen)

    def get_start_coords(self):
        for obj in self.objects:
            if obj.Object_type == "start":
                return obj.x + 5, obj.y - 30