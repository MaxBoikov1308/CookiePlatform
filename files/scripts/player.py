from files.scripts.variables import *
import pygame as pg

class Player:
    def __init__(self, x0, y0):
        self.JUMP_SOUND = pg.mixer.Sound("files/sounds/jump_sound.mp3")
        self.JUMP_SOUND.set_volume(VOLUME)
        self.X0 = x0
        self.Y0 = y0
        self.X_POSITION, self.Y_POSITION = self.X0, self.Y0
        
        self.DELTA_X = SPEED
        self.XR, self.XL = 0, 0

        self.ISJUMP = False
        self.JUMP_PHASE = 0
        self.ISSPRINT = False
        self.PHASE = 0
        self.ISSTAND = True
        self.Y_GRAVITY = 1
        self.JUMP_HEIGHT = 15 
        self.Y_VELOCITY = self.JUMP_HEIGHT

        self.ISRIGHT = True

        self.STANDING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("files/images/player/walk_1_r.png"), (60, 80))
        self.STANDING_SURFACE_LEFT = pg.transform.scale(pg.image.load("files/images/player/walk_1_l.png"), (60, 80))
        self.JUMPING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("files/images/player/jump_1_r.png"), (60, 80))
        self.JUMPING_SURFACE_LEFT = pg.transform.scale(pg.image.load("files/images/player/jump_1_l.png"), (60, 80))
        self.RUNNING_SURFACE_RIGHT = pg.transform.scale(pg.image.load("files/images/player/run_1_r.png"), (60, 80))
        self.RUNNING_SURFACE_LEFT = pg.transform.scale(pg.image.load("files/images/player/run_1_l.png"), (60, 80))
        self.STANDING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("files/images/player/walk_2_r.png"), (60, 80))
        self.STANDING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("files/images/player/walk_2_l.png"), (60, 80))
        self.JUMPING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("files/images/player/jump_2_r.png"), (60, 80))
        self.JUMPING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("files/images/player/jump_2_l.png"), (60, 80))
        self.RUNNING_SURFACE_RIGHT_1 = pg.transform.scale(pg.image.load("files/images/player/run_2_r.png"), (60, 80))
        self.RUNNING_SURFACE_LEFT_1 = pg.transform.scale(pg.image.load("files/images/player/run_2_l.png"), (60, 80))

    def move(self):
        keys = pg.key.get_pressed()
        self.x_old = self.X_POSITION
        if self.ISSTAND:
                self.XR = 0
                self.XL = 0
        if keys[pg.K_a] and self.X_POSITION > self.DELTA_X:
            self.XL += 1
            self.XR = 0
            if self.XL >= 25:
                self.ISSPRINT = True
                self.X_POSITION -= 2 * self.DELTA_X
            else:
                self.X_POSITION -= self.DELTA_X

        if keys[pg.K_d] and self.X_POSITION < 1920 - self.DELTA_X - 50:
            self.XR += 1
            self.XL = 0
            if self.XR >= 25:
                self.ISSPRINT = True
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

        self.player_rect = self.JUMPING_SURFACE_RIGHT.get_rect(center=(self.X_POSITION + 30, self.Y_POSITION + 40))
        
        if self.X_POSITION > self.x_old:
            self.ISSTAND = False
            self.ISRIGHT = True
        elif self.X_POSITION == self.x_old:
            self.ISSTAND = True
            self.ISSPRINT = False
            if not self.ISRIGHT:
                self.ISRIGHT = False
            else:
                self.ISRIGHT = True
        else:
            self.ISSTAND = False
            self.ISRIGHT = False


    def draw(self, screen):
        screen.blit(self.select_sprite(self.PHASE, self.ISRIGHT, self.ISSTAND, self.ISJUMP,
                                       self.JUMP_PHASE, self.ISSPRINT), self.player_rect)
        # print(self.player_rect)


    def respawn(self):
        self.X_POSITION, self.Y_POSITION = self.X0, self.Y0
        self.ISFALL = False
        self.ISJUMP = False
        self.Y_VELOCITY = self.JUMP_HEIGHT
        self.IS_SPRINT = False
        self.ISSTAND = True
        self.PHASE = 0
        self.move()
    
    def select_sprite(self, phase=0, isright=True, isstand=True, isjump=False, jumpphase=0, issprint=False):
        if isright:
            if phase < 10:
                if isjump:
                    if jumpphase <= 15:
                        return self.JUMPING_SURFACE_RIGHT
                    else:
                        return self.JUMPING_SURFACE_RIGHT_1
                
                if not issprint or isstand:
                    return self.STANDING_SURFACE_RIGHT
                else:
                    return self.RUNNING_SURFACE_RIGHT
            else:
                if not issprint or isstand:
                    if phase >= 10 and isstand:
                        return self.STANDING_SURFACE_RIGHT
                    return self.STANDING_SURFACE_RIGHT_1
                else:
                    return self.RUNNING_SURFACE_RIGHT_1
        else:
            if phase < 10:
                if isjump:
                    if jumpphase <= 15:
                        return self.JUMPING_SURFACE_LEFT
                    else:
                        return self.JUMPING_SURFACE_LEFT_1
                if not issprint or isstand:
                    return self.STANDING_SURFACE_LEFT
                else:
                    return self.RUNNING_SURFACE_LEFT
            else:
                if not issprint or isstand:
                    if phase >= 10 and isstand:
                        return self.STANDING_SURFACE_LEFT
                    return self.STANDING_SURFACE_LEFT_1
                else:
                    return self.RUNNING_SURFACE_LEFT_1
        