from peewee import SqliteDatabase, Model, TextField, IntegerField


db = SqliteDatabase("files/levels/level2.db")


class Level2(Model):
    Object_type = TextField()
    x = IntegerField()
    y = IntegerField()
    h = IntegerField()
    w = IntegerField()

    class Meta:
        database = db