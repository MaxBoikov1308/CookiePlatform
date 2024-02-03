from variables import *
import pygame as pg
from builder import Builder
from player import Player
from main_menue import Menue


class Game:
    def __init__(self):
        pg.init()

        pg.font.init()
        self.font = pg.font.SysFont('Comic Sans MS', 70)
        self.SCREEN = pg.display.set_mode((1920, 1080))
        self.FPS_CLOCK = pg.time.Clock()
        self.FPS = FPS
        self.BUTTON_SOUND = pg.mixer.Sound("../sounds/button_sound.mp3")
        self.bg = pg.image.load("../images/jungle_background.png")
        self.BUTTON_SOUND.set_volume(VOLUME)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.player = Player()
        self.builder = Builder(self.SCREEN)
        self.menue = Menue(self.SCREEN, self.BUTTON_SOUND)
        self.player.x = 500
        self.player.y = 500
        self.IS_PAUSE = False
        self.change_music(self.menue.ISGAME)
    
    def run(self):
        while True:
            if self.menue.ISGAME == True:
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        pg.quit()
                        quit()
                    if e.type == pg.KEYDOWN:
                        if e.key == pg.K_ESCAPE:
                            self.menue.ISGAME = False
                            self.player.respawn(500, 500)
                            self.IS_PAUSE = False
                            self.change_music(self.menue.ISGAME)
                            self.player.XL = self.player.XR = 0
                        elif e.key == pg.K_p:
                            if self.IS_PAUSE:
                                self.IS_PAUSE = False
                            else:
                                self.IS_PAUSE = True
                        elif e.key == pg.K_r:
                            self.player.respawn(500, 500)
                            self.player.draw(self.SCREEN)
                    if e.type == pg.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            if self.IS_PAUSE:
                                if self.menue.pause_coords_list.__contains__(e.pos):
                                    self.menue.ISGAME = False
                                    self.player.respawn(500, 500)
                                    self.IS_PAUSE = False
                                    self.change_music(self.menue.ISGAME)
                                    self.player.XL = self.player.XR = 0

                if not self.IS_PAUSE:
                    self.player.move()

                # drawing the screen
                self.SCREEN.fill(self.black)
                self.SCREEN.blit(self.bg, (0, 0))
                self.builder.draw(self.white)
                self.player.draw(self.SCREEN)
                if self.IS_PAUSE:
                    text = self.font.render('PAUSE', False, (0, 0, 0))
                    self.SCREEN.blit(text, (840, 400))
                    pg.draw.rect(self.SCREEN, (240, 0, 0), (910, 550, 100, 100))

                pg.display.flip()
                self.FPS_CLOCK.tick(self.FPS)
            else:
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        pg.quit()
                        quit()
                    if e.type == pg.KEYDOWN:
                        if e.key == pg.K_ESCAPE:
                            pg.quit()
                            quit()
                    if e.type == pg.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            if self.menue.start_coords_list.__contains__(e.pos):
                                self.menue.ISGAME = True
                                self.menue.button_sound.play()
                                self.change_music(self.menue.ISGAME)
                            if self.menue.exit_coords_list.__contains__(e.pos):
                                self.menue.button_sound.play()
                                pg.quit()
                                quit()
                            
                self.SCREEN.fill(self.black)
                self.menue.draw()
                pg.display.flip()
                self.FPS_CLOCK.tick(self.FPS)

    def change_music(self, isgame=False):
        if isgame:
            pg.mixer.music.load("../sounds/background1.mp3")
        else:
            pg.mixer.music.load("../sounds/menue_background.mp3")
        pg.mixer.music.set_volume(VOLUME)
        pg.mixer.music.play(-1)