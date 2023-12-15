import pygame as pg


class Level():
    def __init__(self):
        self.objects = {}
        self.names = self.objects.keys()
    
    def draw(self, screen, color):
        for obj in self.names:
            x0 = self.objects[obj][0]
            y0 = self.objects[obj][1]
            w = self.objects[obj][2]
            h = self.objects[obj][3]
            pg.draw.rect(screen, color, (x0, y0, w, h))


class Level1(Level):
    def __init__(self):
        super().__init__()
        self.objects = {
            "block1": (600, 1080 - 100, 100, 100),
        }
        self.names = self.objects.keys()