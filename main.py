import pygame as pg
from player import Player

pg.init()

SCREEN = pg.display.set_mode((1920, 1080))
FPS_CLOCK = pg.time.Clock()
FPS = 60
x = 0
y = 0
white = (255, 255, 255)
black = (0, 0, 0)
player = Player()

def dt():
    return 1 / FPS

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            quit()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_w:
                y -= 1
            if e.key == pg.K_s:
                y += 1
            if e.key == pg.K_a:
                x -= 1
            if e.key == pg.K_d:
                x += 1
    
    SCREEN.fill(black)
    player.draw(SCREEN, x, y, white)

    pg.display.flip()
    FPS_CLOCK.tick(FPS)