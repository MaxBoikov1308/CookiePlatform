from variables import *
import pygame as pg


class Player:
    def __init__(self):
        self.JUMP_SOUND = pg.mixer.Sound("../sounds/jump_sound.mp3")
        self.JUMP_SOUND.set_volume(VOLUME)

        self.X_POSITION, self.Y_POSITION = 400, 660
        
        self.DELTA_X = SPEED

        self.XR, self.XL = 0, 0

        self.ISJUMP = False
        self.JUMP_PHASE = 0
        self.IS_SPRINT = False
        self.PHASE = 0
        self.ISSTANDING = True
        self.ROTATION = 'r'
        self.Y_GRAVITY = 1
        self.JUMP_HEIGHT = 15 
        self.Y_VELOCITY = self.JUMP_HEIGHT

        
        self.STANDING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("../images/walk_1_r.png"), (60, 80))
        self.STANDING_SURFACE_LEFT = pg.transform.scale(pg.image.load("../images/walk_1_l.png"), (60, 80))
        self.JUMPING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("../images/jump_1_r.png"), (60, 80))
        self.JUMPING_SURFACE_LEFT = pg.transform.scale(pg.image.load("../images/jump_1_l.png"), (60, 80))
        self.RUNNING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("../images/run_1_r.png"), (60, 80))
        self.RUNNING_SURFACE_LEFT = pg.transform.scale(pg.image.load("../images/run_1_l.png"), (60, 80))
        self.STANDING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("../images/walk_2_r.png"), (60, 80))
        self.STANDING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("../images/walk_2_l.png"), (60, 80))
        self.JUMPING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("../images/jump_2_r.png"), (60, 80))
        self.JUMPING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("../images/jump_2_l.png"), (60, 80))
        self.RUNNING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("../images/run_2_r.png"), (60, 80))
        self.RUNNING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("../images/run_2_l.png"), (60, 80))


    def move(self):
        keys = pg.key.get_pressed()
        self.x_old = self.X_POSITION
        if keys[pg.K_a] and self.X_POSITION > self.DELTA_X:
            self.ROTATION = 'l'
            self.IS_SPRINT = False
            self.XL += 1
            self.XR = 0
            if self.XL >= 25:
                self.IS_SPRINT = True
                self.ROTATION = 'l'
            if self.IS_SPRINT and self.ROTATION == 'l':
                self.X_POSITION -= 2 * self.DELTA_X
            else:
                self.X_POSITION -= self.DELTA_X

        if keys[pg.K_d] and self.X_POSITION < 1920 - self.DELTA_X - 50:
            self.ROTATION = 'r'
            self.IS_SPRINT = False
            self.XR += 1
            self.XL = 0
            if self.XR >= 25:
                self.IS_SPRINT = True
                self.ROTATION = 'r'
            if self.IS_SPRINT and self.ROTATION == 'r':
                self.X_POSITION += 2 * self.DELTA_X
            else:
                self.X_POSITION += self.DELTA_X
            
        if not(self.ISJUMP):
            if keys[pg.K_SPACE] or keys[pg.K_w]:
                self.ISJUMP = True
                self.JUMP_SOUND.play()
        if self.ISJUMP:
            self.JUMP_PHASE += 1
            self.Y_POSITION -= self.Y_VELOCITY
            self.Y_VELOCITY -= self.Y_GRAVITY
            if self.Y_VELOCITY < -self.JUMP_HEIGHT:
                self.JUMP_PHASE == 0
                self.ISJUMP = False
                self.Y_VELOCITY = self.JUMP_HEIGHT

        if self.ISJUMP:
            if self.ROTATION == 'r':
                self.player_rect = self.JUMPING_SURFACE_RIGHT.get_rect(center=(self.X_POSITION, self.Y_POSITION))
            else:
                self.player_rect = self.JUMPING_SURFACE_LEFT.get_rect(center=(self.X_POSITION, self.Y_POSITION))
        else:
            if self.ROTATION == 'r':
                self.player_rect = self.STANDING_SURFACE_RIGHT.get_rect(center=(self.X_POSITION, self.Y_POSITION))
            else:
                self.player_rect = self.STANDING_SURFACE_LEFT.get_rect(center=(self.X_POSITION, self.Y_POSITION))
        
        if self.X_POSITION > self.x_old:
            self.ROTATION = 'r'
            self.ISSTANDING = False
        elif self.X_POSITION == self.x_old:
            self.ROTATION = self.ROTATION
            self.ISSTANDING = True
        else:
            self.ISSTANDING = False
            self.ROTATION = 'r'


    def draw(self, screen):
        if self.PHASE < 10:
            if self.ISJUMP:
                if self.ROTATION == 'r':
                    screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                else:
                    screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
            else:
                if self.ISSTANDING:
                    if self.ISJUMP:
                        if self.JUMP_PHASE <= 15:
                            if self.ROTATION == 'r':
                                screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
                        else:
                            if self.ROTATION == 'r':
                                screen.blit(self.JUMPING_SURFACE_RIGHT_1, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_LEFT_1, self.player_rect)
                else:
                    if self.IS_SPRINT:
                        if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                if self.ROTATION == 'r':
                                    screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                                else:
                                    screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
                            else:
                                if self.ROTATION == 'r':
                                    screen.blit(self.JUMPING_SURFACE_RIGHT_1, self.player_rect)
                                else:
                                    screen.blit(self.JUMPING_SURFACE_LEFT_1, self.player_rect)
                        else:
                            if self.ROTATION == 'r':
                                screen.blit(self.RUNNING_SURFACE_RIGHT, self.player_rect)
                            else:
                                screen.blit(self.RUNNING_SURFACE_LEFT, self.player_rect)
                    else:
                        if self.ROTATION == 'r':
                            screen.blit(self.STANDING_SURFACE_RIGHT, self.player_rect)
                        else:
                            screen.blit(self.STANDING_SURFACE_LEFT, self.player_rect)
        else:
            if self.ISSTANDING:
                if self.ISJUMP:
                    if self.JUMP_PHASE <= 15:
                        if self.ROTATION == 'r':
                            screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                        else:
                            screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
                    else:
                        if self.ROTATION == 'r':
                            screen.blit(self.JUMPING_SURFACE_RIGHT_1, self.player_rect)
                        else:
                            screen.blit(self.JUMPING_SURFACE_LEFT_1, self.player_rect)
                else:
                    if self.ROTATION == 'r':
                            screen.blit(self.STANDING_SURFACE_RIGHT, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_LEFT, self.player_rect)           
            else:
                if self.IS_SPRINT:
                    if self.ISJUMP:
                        if self.JUMP_PHASE <= 15:
                            if self.ROTATION == 'r':
                                screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
                        else:
                            if self.ROTATION == 'r':
                                screen.blit(self.JUMPING_SURFACE_RIGHT_1, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_LEFT_1, self.player_rect)
                else:
                    if self.ROTATION == 'r':
                        screen.blit(self.STANDING_SURFACE_RIGHT_1, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_LEFT_1, self.player_rect)


    def respawn(self, x0, y0):
        self.X_POSITION, self.Y_POSITION = x0, y0
        self.ISFALL = False
        self.ISJUMP = False
        self.Y_VELOCITY = self.JUMP_HEIGHT
        self.IS_SPRINT = False
        self.move()