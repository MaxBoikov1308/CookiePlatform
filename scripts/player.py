import pygame as pg


class Player:
    def __init__(self):
        self.JUMP_SOUND = pg.mixer.Sound("sounds/jump_sound.mp3")

        self.X_POSITION, self.Y_POSITION = 400, 660
        
        self.DELTA_X = 10

        self.ISJUMP = False

        self.Y_GRAVITY = 0.6
        self.JUMP_HEIGHT = 20
        self.Y_VELOCITY = self.JUMP_HEIGHT

        self.STANDING_SURFACE = pg.transform.scale(pg.image.load("images/mario_standing.png"), (48, 64))
        self.ISJUMP_SURFACE = pg.transform.scale(pg.image.load("images/mario_jumping.png"), (48, 64))

        self.mario_rect = self.STANDING_SURFACE.get_rect(center=(self.X_POSITION, self.Y_POSITION))

    def move(self):
        keys = pg.key.get_pressed()
    
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
            self.mario_rect = self.ISJUMP_SURFACE.get_rect(center=(self.X_POSITION, self.Y_POSITION))
        else:
            self.mario_rect = self.STANDING_SURFACE.get_rect(center=(self.X_POSITION, self.Y_POSITION))

    def draw(self, screen, color):
        # pg.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        screen.blit(self.ISJUMP_SURFACE, self.mario_rect)
        screen.blit(self.STANDING_SURFACE, self.mario_rect)
    
    def respawn(self, x0, y0):
        self.x, self.y = x0, y0
        self.ISFALL = False
        self.ISJUMP = False
