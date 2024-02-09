from peewee import *

db = SqliteDatabase("../levels/level2.db")


class Level(Model):
    Object_type = TextField()
    x = IntegerField()
    y = IntegerField()
    h = IntegerField()
    w = IntegerField()

    class Meta:
        database = db
