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
        self.IS_RIGHT_SPRINT = False
        self.IS_LEFT_SPRINT = False
        self.PHASE = 0
        self.ISSTANDING = True
        self.Y_GRAVITY = 1
        self.JUMP_HEIGHT = 15 
        self.Y_VELOCITY = self.JUMP_HEIGHT

        self.ISRIGHT = True

        self.STANDING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("../images/player/walk_1_r.png"), (60, 80))
        self.STANDING_SURFACE_LEFT = pg.transform.scale(pg.image.load("../images/player/walk_1_l.png"), (60, 80))
        self.JUMPING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("../images/player/jump_1_r.png"), (60, 80))
        self.JUMPING_SURFACE_LEFT = pg.transform.scale(pg.image.load("../images/player/jump_1_l.png"), (60, 80))
        self.RUNNING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("../images/player/run_1_r.png"), (60, 80))
        self.RUNNING_SURFACE_LEFT = pg.transform.scale(pg.image.load("../images/player/run_1_l.png"), (60, 80))
        self.STANDING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("../images/player/walk_2_r.png"), (60, 80))
        self.STANDING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("../images/player/walk_2_l.png"), (60, 80))
        self.JUMPING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("../images/player/jump_2_r.png"), (60, 80))
        self.JUMPING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("../images/player/jump_2_l.png"), (60, 80))
        self.RUNNING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("../images/player/run_2_r.png"), (60, 80))
        self.RUNNING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("../images/player/run_2_l.png"), (60, 80))
    def move(self):
        keys = pg.key.get_pressed()
        self.x_old = self.X_POSITION
        if self.ISSTANDING:
                self.XR = 0
                self.XL = 0
        if keys[pg.K_a] and self.X_POSITION > self.DELTA_X:
            self.IS_RIGHT_SPRINT = False
            self.XL += 1
            self.XR = 0
            if self.XL >= 25:
                self.IS_LEFT_SPRINT = True
            if self.IS_LEFT_SPRINT:
                self.X_POSITION -= 2 * self.DELTA_X
            else:
                self.X_POSITION -= self.DELTA_X

        if keys[pg.K_d] and self.X_POSITION < 1920 - self.DELTA_X - 50:
            self.IS_LEFT_SPRINT = False
            self.XR += 1
            self.XL = 0
            if self.XR >= 25:
                self.IS_RIGHT_SPRINT = True
            if self.IS_RIGHT_SPRINT:
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
            self.player_rect = self.JUMPING_SURFACE_RIGHT.get_rect(center=(self.X_POSITION, self.Y_POSITION))
        else:
            self.player_rect = self.STANDING_SURFACE_RIGHT.get_rect(center=(self.X_POSITION, self.Y_POSITION))
        
        if self.X_POSITION > self.x_old:
            self.ISSTANDING = False
            self.ISRIGHT = True
        elif self.X_POSITION == self.x_old:
            self.ISSTANDING = True
            self.IS_LEFT_SPRINT = False
            self.IS_RIGHT_SPRINT = False
            if not self.ISRIGHT:
                self.ISRIGHT = False
            else:
                self.ISRIGHT = True
        else:
            self.ISSTANDING = False
            self.ISRIGHT = False


    def draw(self, screen):
        if self.PHASE < 10:
            if self.ISRIGHT:
                if self.ISSTANDING:
                    if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_RIGHT_1, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_RIGHT, self.player_rect)
                else:
                    if self.IS_RIGHT_SPRINT:
                        if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_RIGHT_1, self.player_rect)
                        else:
                            screen.blit(self.RUNNING_SURFACE_RIGHT, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_RIGHT, self.player_rect)
            else:
                if self.ISSTANDING:
                    if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_LEFT_1, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_LEFT, self.player_rect)
                else:
                    if self.IS_LEFT_SPRINT:
                        if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_LEFT_1, self.player_rect)
                        else:
                            screen.blit(self.RUNNING_SURFACE_LEFT, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_LEFT, self.player_rect)
        else:
            if self.ISRIGHT:
                if self.ISSTANDING:
                    if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_RIGHT_1, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_RIGHT, self.player_rect)
                else:
                    if self.IS_RIGHT_SPRINT:
                        if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                screen.blit(self.JUMPING_SURFACE_RIGHT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_RIGHT_1, self.player_rect)
                        else:
                            screen.blit(self.RUNNING_SURFACE_RIGHT_1, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_RIGHT_1, self.player_rect)
            else:
                if self.ISSTANDING:
                    if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_LEFT_1, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_LEFT, self.player_rect)
                else:
                    if self.IS_LEFT_SPRINT:
                        if self.ISJUMP:
                            if self.JUMP_PHASE <= 15:
                                screen.blit(self.JUMPING_SURFACE_LEFT, self.player_rect)
                            else:
                                screen.blit(self.JUMPING_SURFACE_LEFT_1, self.player_rect)
                        else:
                            screen.blit(self.RUNNING_SURFACE_LEFT_1, self.player_rect)
                    else:
                        screen.blit(self.STANDING_SURFACE_LEFT_1, self.player_rect)


    def respawn(self, x0, y0):
        self.X_POSITION, self.Y_POSITION = x0, y0
        self.ISFALL = False
        self.ISJUMP = False
        self.Y_VELOCITY = self.JUMP_HEIGHT
        self.IS_SPRINT = False
        self.move()