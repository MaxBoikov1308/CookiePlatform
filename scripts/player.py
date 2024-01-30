from copy import copy
from variables import *
import pygame as pg


class Player:
    def __init__(self):
        self.JUMP_SOUND = pg.mixer.Sound("sounds/jump_sound.mp3")
        self.JUMP_SOUND.set_volume(VOLUME)

        self.X_POSITION, self.Y_POSITION = 400, 660
        
        self.DELTA_X = SPEED


        self.ISJUMP = False

        self.Y_GRAVITY = 0.6
        self.JUMP_HEIGHT = 20
        self.Y_VELOCITY = self.JUMP_HEIGHT

        self.STANDING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("images/player_r.png"), (28, 60))
        self.JUMPING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("images/player_r_j.png"), (28, 60))
        self.STANDING_SURFACE_LEFT = pg.transform.scale(pg.image.load("images/player_l.png"), (28, 60))
        self.JUMPING_SURFACE_LEFT = pg.transform.scale(pg.image.load("images/player_l_j.png"), (28, 60))

        self.mario_rect = self.STANDING_SURFACE_RIGHT.get_rect(center=(self.X_POSITION, self.Y_POSITION))


    def move(self):
        keys = pg.key.get_pressed()
        self.x_old = copy(self.X_POSITION)
        if keys[pg.K_a] and self.x > self.DELTA_X: 
            self.X_POSITION -= self.DELTA_X 

        if keys[pg.K_d] and self.x < 1920 - self.DELTA_X - 50:  
            self.X_POSITION += self.DELTA_X
            
        if not(self.ISJUMP): 
            if keys[pg.K_SPACE]:
                self.ISJUMP = True
                self.JUMP_SOUND.play()
        if self.ISJUMP:
            self.Y_POSITION -= self.Y_VELOCITY
            self.Y_VELOCITY -= self.Y_GRAVITY
            if self.Y_VELOCITY < -self.JUMP_HEIGHT:
                self.ISJUMP = False
                self.Y_VELOCITY = self.JUMP_HEIGHT

        if self.ISJUMP:
            self.player_rect = self.JUMPING_SURFACE_RIGHT.get_rect(center=(self.X_POSITION, self.Y_POSITION))
        else:
            self.player_rect = self.STANDING_SURFACE_RIGHT.get_rect(center=(self.X_POSITION, self.Y_POSITION))


    def draw(self, screen, color):
        # pg.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        if self.X_POSITION > self.x_old:
            if self.ISJUMP:
                screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
            else:
                screen.blit(self.STANDING_SURFACE_RIGHT, self.player_rect)
        else:
            if self.ISJUMP:
                screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
            else:
                screen.blit(self.STANDING_SURFACE_LEFT, self.player_rect)





    def respawn(self, x0, y0):
        self.x, self.y = x0, y0
        self.ISFALL = False
        self.ISJUMP = False
