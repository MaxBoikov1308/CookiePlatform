from variables import *
import pygame as pg
from builder import Builder
from player import Player

class Game:
    def __init__(self):
        pg.init()

        self.SCREEN = pg.display.set_mode((1920, 1080))
        self.FPS_CLOCK = pg.time.Clock()
        self.FPS = FPS
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.player = Player()
        self.player.x = 500
        self.player.y = 500
        self.builder = Builder(self.SCREEN)
        pg.mixer.music.load("sounds/background1.mp3")
        pg.mixer.music.set_volume(VOLUME)
        pg.mixer.music.play(-1)
        self.bg = pg.image.load("images/cave_background.png")
        self.IS_PAUSE = False
    
    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    quit()
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        pg.quit()
                        quit()
                    elif e.key == pg.K_p:
                        if self.IS_PAUSE:
                            self.IS_PAUSE = False
                        else:
                            self.IS_PAUSE = True
                    elif e.key == pg.K_r:
                        self.player.respawn(500, 500)


            if not self.IS_PAUSE:
                self.player.move()

            # drawing the screen
            self.SCREEN.fill(self.black)
            self.SCREEN.blit(self.bg, (0, 0))
            self.builder.draw(self.white)
            self.player.draw(self.SCREEN)
            if self.IS_PAUSE:
                pg.draw.rect(self.SCREEN, self.red, (300, 300, 20, 20))

            pg.display.flip()
            self.FPS_CLOCK.tick(self.FPS)
