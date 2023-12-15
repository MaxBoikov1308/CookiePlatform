import pygame as pg


class Player:
    def __init__(self):
        self.width = 50
        self.height = 100
        self.DELTA_MOVE = 10
        self.ISJUMP = False
        self.jumpCount = 10
        self.x = 0
        self.y = 0

    def move(self):
        keys = pg.key.get_pressed()
    
        if keys[pg.K_a] and self.x > self.DELTA_MOVE: 
            self.x -= self.DELTA_MOVE 

        if keys[pg.K_d] and self.x < 1920 - self.DELTA_MOVE - 50:  
            self.x += self.DELTA_MOVE
            
        if not(self.ISJUMP): 
            if keys[pg.K_SPACE]:
                self.ISJUMP = True
        else:
            if self.jumpCount >= -10:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else: 
                self.jumpCount = 10
                self.ISJUMP = False

    def draw(self, screen, color):
        pg.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
