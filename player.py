import pygame as pg


class Player:
    def __init__(self):
        self.width = 50
        self.height = 100
        self.DELTA_MOVE = 15
        self.ISJUMP = False
        self.ISFALL = False
        self.jumpCount = 10
        self.fallCount = 0
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
            if self.jumpCount >= 0:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else: 
                self.jumpCount = 10
                self.ISJUMP = False
                self.ISFALL = True
        if self.ISFALL:
            if self.y + self.height < 1080:
                self.y -= (self.fallCount * abs(self.fallCount)) * 0.5
                print(self.y)
                self.fallCount -= 1
            else: 
                self.ISFALL = False
                self.fallCount = 0

    def draw(self, screen, color):
        pg.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
