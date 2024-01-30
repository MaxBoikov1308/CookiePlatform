import pygame as pg
from peewee import *

db = SqliteDatabase("levels/level2.db")


class Level(Model):
    name = TextField()
    x = IntegerField()
    y = IntegerField()
    h = IntegerField()
    w = IntegerField()

    class Meta:
        database = db


