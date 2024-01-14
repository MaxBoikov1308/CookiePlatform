import pygame as pg
from builder import Builder
from player import Player

class Game:
    def __init__(self):
        pg.init()

        self.SCREEN = pg.display.set_mode((1920, 1080))
        self.FPS_CLOCK = pg.time.Clock()
        self.FPS = 30
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.player = Player()
        self.player.x = 500
        self.player.y = 500
        self.builder = Builder()
    
    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    quit()

            self.player.move()

            # drawing the screen
            self.SCREEN.fill(self.black)
            self.builder.build(self.SCREEN, self.white)
            self.player.draw(self.SCREEN, self.white)

            pg.display.flip()
            self.FPS_CLOCK.tick(self.FPS)
