import pygame as pg
from player import Player
from math import pi, sin
from levels import Level1

pg.init()

SCREEN = pg.display.set_mode((1920, 1080))
FPS_CLOCK = pg.time.Clock()
FPS = 30
DELTA_MOVE = 10
ISJUMP = False
jumpCount = 10
level = Level1()
N = 0
BLOCKS = [(x0, y0, w, h) for x0, y0, w, h in level.objects.values()]
white = (255, 255, 255)
black = (0, 0, 0)
player = Player()
player.x = 500
player.y = 500

def dt():
    return 1 / FPS

def check_collision(r1, r2):  # (x0, y0, w, h), (x0, y0, w, h)
    return r1[0] < r2[0] + r2[2] and r1[0] + r1[2] > r2[0] and r1[1] < r2[1] + r2[3] and r1[3] + r1[1] > r2[1]

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            quit()

    player.move()

    # drawing the screen
    SCREEN.fill(black)
    level.draw(SCREEN, white)
    player.draw(SCREEN, white)

    pg.display.flip()
    # N =+ 1
    # FPS_CLOCK.tick(5 + 40 * sin(N / 100 * 2 * pi) ** 2)
    FPS_CLOCK.tick(FPS)