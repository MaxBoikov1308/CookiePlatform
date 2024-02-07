import pygame as pg
from variables import *

class Menue:
    def __init__(self, screen, sound):
        self.ISGAME = False
        self.SCREEN = screen
        self.bg = pg.image.load("../images/backgrounds/city_background.png")
        self.logo = pg.transform.scale(pg.image.load("../images/cookie.png"), (300, 300))
        self.font = pg.font.SysFont('Comic Sans MS', 80)
        self.text_logo = self.font.render('Cookie Platform', True, (0, 0, 0))
        self.button_sound = sound

        self.start_button = [pg.transform.scale(pg.image.load("../images/buttons/start.png"), (400, 110)),
                             pg.transform.scale(pg.image.load("../images/buttons/start_pressed.png"), (400, 110))]
        self.start_rect = self.start_button[0].get_rect(center=(960, 400))

        self.levels_button = [pg.transform.scale(pg.image.load("../images/buttons/levels.png"), (400, 110)),
                             pg.transform.scale(pg.image.load("../images/buttons/levels_pressed.png"), (400, 110))]
        self.levels_rect = self.start_button[0].get_rect(center=(960, 520))

        self.settings_button = [pg.transform.scale(pg.image.load("../images/buttons/settings.png"), (400, 110)),
                             pg.transform.scale(pg.image.load("../images/buttons/settings_pressed.png"), (400, 110))]
        self.settings_rect = self.start_button[0].get_rect(center=(960, 640))

        self.redactor_button = [pg.transform.scale(pg.image.load("../images/buttons/redactor.png"), (400, 110)),
                             pg.transform.scale(pg.image.load("../images/buttons/redactor_pressed.png"), (400, 110))]
        self.redactor_rect = self.start_button[0].get_rect(center=(960, 760))

        self.scores_button = [pg.transform.scale(pg.image.load("../images/buttons/scores.png"), (400, 110)),
                             pg.transform.scale(pg.image.load("../images/buttons/scores_pressed.png"), (400, 110))]
        self.scores_rect = self.start_button[0].get_rect(center=(960, 880))

        self.exit_button = [pg.transform.scale(pg.image.load("../images/buttons/exit.png"), (400, 110)),
                             pg.transform.scale(pg.image.load("../images/buttons/exit_pressed.png"), (400, 110))]
        self.exit_rect = self.exit_button[0].get_rect(center=(960, 1000))
    
    def draw(self):
        self.SCREEN.blit(self.bg, (0, 0))
        self.SCREEN.blit(self.logo, (800, 20))
        self.SCREEN.blit(self.text_logo, (680, 250))

        self.SCREEN.blit(self.start_button[0], self.start_rect)
        self.SCREEN.blit(self.levels_button[0], self.levels_rect)
        self.SCREEN.blit(self.settings_button[0], self.settings_rect)
        self.SCREEN.blit(self.redactor_button[0], self.redactor_rect)
        self.SCREEN.blit(self.scores_button[0], self.scores_rect)
        self.SCREEN.blit(self.exit_button[0], self.exit_rect)
