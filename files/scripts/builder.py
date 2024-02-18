from files.scripts.objects import *
from files.levels.level1 import Level1
from files.levels.level2 import Level2
import pygame as pg


class Builder:
    def __init__(self, screen):
        self.screen = screen
        self.level_number = 1
        self.objects = self.load_objects_from_db()
        self.bg1 = pg.transform.scale(pg.image.load("files/images/backgrounds/jungle_background.png"), (1920, 1080))
        self.bg2 = pg.transform.scale(pg.image.load("files/images/backgrounds/forest_background.png"), (1920, 1080))
        self.bg3 = pg.transform.scale(pg.image.load("files/images/backgrounds/forest_background.png"), (1920, 1080))

    def load_objects_from_db(self):
        objects = []
        if self.level_number == 1:
            for obj in Level1.select():
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
        else:
            for obj in Level2.select():
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
                return obj.x + 5, obj.y - 25
    
    def choose_bg(self, n):
        if n == 1:
            for obj in self.objects:
                if obj.Object_type == "block":
                    obj.active_sprite = obj.sprite1
            return self.bg1
        elif n == 2:
            for obj in self.objects:
                if obj.Object_type == "block":
                    obj.active_sprite = obj.sprite2
            return self.bg2
        elif n == 3:
            for obj in self.objects:
                if obj.Object_type == "block":
                    obj.active_sprite = obj.sprite3
            return self.bg3