from peewee import SqliteDatabase, Model, TextField, IntegerField


db = SqliteDatabase("files/levels/level1.db")


class Level1(Model):
    Object_type = TextField()
    x = IntegerField()
    y = IntegerField()
    h = IntegerField()
    w = IntegerField()

    class Meta:
        database = db