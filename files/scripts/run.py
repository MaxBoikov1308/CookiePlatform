from files.scripts.variables import *
import pygame as pg
from files.scripts.builder import Builder
from files.scripts.player import Player
from files.scripts.main_menue import Menue
from files.scripts.interface import Interface
from random import randint


class Game:
    def __init__(self):
        pg.init()

        pg.font.init()
        self.font = pg.font.SysFont('Comic Sans MS', 70)
        self.SCREEN = pg.display.set_mode((1920, 1080))
        pg.display.set_caption("Cookie Platform")
        self.FPS_CLOCK = pg.time.Clock()
        self.FPS = FPS
        self.BUTTON_SOUND = pg.mixer.Sound("files/sounds/button_sound.mp3")
        self.BUTTON_SOUND.set_volume(VOLUME * 10)
        self.pause_button = pg.transform.scale(pg.image.load("files/images/buttons/exit.png"), (400, 110))
        self.pause_rect = self.pause_button.get_rect(center=(960, 600))

        self.builder = Builder(self.SCREEN)
        self.menue = Menue(self.SCREEN, self.BUTTON_SOUND)
        self.player = Player(self.builder.get_start_coords()[0], self.builder.get_start_coords()[1], self.SCREEN)
        self.interface = Interface(self.SCREEN)
        self.bg = self.builder.choose_bg(randint(1, 3))

        self.IS_PAUSE = False
        self.change_music(self.menue.ISGAME)
        self.mousepos = None
    
    def run(self):
        while True:
            if self.menue.ISGAME == True:
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        pg.quit()
                        quit()
                    if e.type == pg.KEYDOWN:
                        if e.key == pg.K_ESCAPE:
                            if self.IS_PAUSE:
                                self.IS_PAUSE = False
                            else:
                                self.IS_PAUSE = True
                        elif e.key == pg.K_p:
                            if self.IS_PAUSE:
                                self.IS_PAUSE = False
                            else:
                                self.IS_PAUSE = True
                        elif e.key == pg.K_r:
                            self.player.respawn()
                            self.player.hp -= 1
                            self.player.draw()
                    if e.type == pg.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            self.mousepos = pg.Rect(e.pos[0], e.pos[1], 1, 1)
                            if self.IS_PAUSE:
                                if pg.Rect.colliderect(self.pause_rect, self.mousepos):
                                    self.BUTTON_SOUND.play()
                                    self.change_to_menu()

                if not self.IS_PAUSE:
                    self.update_distance()
                    self.check_collision()
                    self.player.move()
                    if self.player.hp < 1:
                        self.change_to_menu()
                    if self.player.PHASE == 19:
                        self.player.PHASE = 0
                    self.player.PHASE += 1

                self.SCREEN.fill((0, 0, 0))
                self.SCREEN.blit(self.bg, (0, 0))
                self.builder.draw()
                self.player.draw()
                self.interface.draw(self.player.hp)

                if self.IS_PAUSE:
                    text = self.font.render('PAUSE', False, (0, 0, 0))
                    self.SCREEN.blit(text, (840, 400))
                    self.SCREEN.blit(self.pause_button, self.pause_rect)

            else:
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        pg.quit()
                        quit()
                    if e.type == pg.KEYDOWN:
                        if e.key == pg.K_ESCAPE:
                            pg.quit()
                            quit()
                    if e.type == pg.MOUSEBUTTONDOWN:
                        if e.button == 1:
                            self.mousepos = pg.Rect(e.pos[0], e.pos[1], 1, 1)
                            if pg.Rect.colliderect(self.menue.start_rect, self.mousepos):
                                self.menue.button_sound.play()
                                self.menue.ISGAME = True
                                self.bg = self.builder.choose_bg(randint(1, 3))
                                self.change_music(self.menue.ISGAME)
                            if pg.Rect.colliderect(self.menue.exit_rect, self.mousepos):
                                self.menue.button_sound.play()
                                pg.quit()
                                quit()
                            
                self.SCREEN.fill((0, 0, 0))
                self.menue.draw()

            pg.display.flip()
            self.FPS_CLOCK.tick(self.FPS)
            self.mousepos = None

    def change_music(self, isgame=False):
        if isgame:
            pg.mixer.music.load("files/sounds/background1.mp3")
        else:
            pg.mixer.music.load("files/sounds/menue_background.mp3")
        pg.mixer.music.set_volume(VOLUME)
        pg.mixer.music.play(-1)
    
    def update_distance(self):
        playerrect = self.player.player_rect
        x1 = playerrect[0]
        y1 = playerrect[1]
        for obj in self.builder.objects:
            if obj.Object_type == "enemy":
                obj.PHASE = self.player.PHASE
            x2 = obj.x
            y2 = obj.y
            obj.distance = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
            obj.set_active()
    
    def change_to_menu(self):
        if self.builder.level_number == 1 and not self.IS_PAUSE and self.player.hp > 0:
            self.builder.level_number = 2
            self.builder.objects = self.builder.load_objects_from_db()
            self.player.X0, self.player.Y0 = self.builder.get_start_coords()[0], self.builder.get_start_coords()[1]
            self.bg = self.builder.choose_bg(randint(1, 3))
            self.player.respawn()
        else:
            self.menue.ISGAME = False
            self.player.respawn()
            self.player.hp = 3
            self.IS_PAUSE = False
            self.change_music(self.menue.ISGAME)
            self.builder.objects = self.builder.load_objects_from_db()
            self.builder.level_number = 1

    def check_collision(self):
        for i in self.builder.objects:
            if i.ISACTIVE:
                if self.player.check_collision(i):
                    i.ISCOLLIDE = True
                    if i.Object_type == "finish":
                        self.change_to_menu()
                    elif i.Object_type == "enemy":
                        self.player.respawn()
                        self.player.hp -= 1
                    elif i.Object_type == "spike":
                        self.player.respawn()
                        self.player.hp -= 1
                    elif i.Object_type == "cookie":
                        if self.player.hp != 3:
                            self.player.hp += 1
                            self.builder.objects.remove(i)
                    elif i.Object_type == "block":
                        if not self.player.ISJUMP:
                            if self.player.Y_POSITION + PLAYER_H + 1 > i.y and i.y + i.h > self.player.Y_POSITION + PLAYER_H:
                                self.player.BOTTOM_COLLISION = True
                                self.player.Y_POSITION = i.y - PLAYER_H + 1
                                continue

                            if i.x + i.w >= self.player.X_POSITION and i.x < self.player.X_POSITION:
                                self.player.LEFT_COLLISION = True
                                self.player.X_POSITION = i.x + GRID_SIZE
                                continue

                            if self.player.X_POSITION + PLAYER_W >= i.x and i.x + i.w > self.player.X_POSITION + PLAYER_W:
                                self.player.RIGHT_COLLISION = True
                                self.player.X_POSITION = i.x - PLAYER_W + 1
                                continue
                        else:
                            if i.x + i.w >= self.player.X_POSITION and i.x < self.player.X_POSITION:
                                self.player.LEFT_COLLISION = True
                                self.player.X_POSITION = i.x + GRID_SIZE
                                continue

                            if self.player.X_POSITION + PLAYER_W >= i.x and i.x + i.w > self.player.X_POSITION + PLAYER_W:
                                self.player.RIGHT_COLLISION = True
                                self.player.X_POSITION = i.x - PLAYER_W + 1
                                continue

                            if self.player.Y_POSITION + PLAYER_H + 1 > i.y and i.y + i.h > self.player.Y_POSITION + PLAYER_H:
                                self.player.BOTTOM_COLLISION = True
                                self.player.Y_POSITION = i.y - PLAYER_H + 1
                                continue

                            if self.player.Y_POSITION - self.player.Y_VELOCITY <= i.y + GRID_SIZE and i.y + GRID_SIZE > self.player.Y_POSITION - PLAYER_H:
                                self.player.TOP_COLLISION = True
                                self.player.Y_VELOCITY = 0
                                self.player.Y_POSITION = i.y + GRID_SIZE + 1
                                continue
                else:
                    i.ISCOLLIDE = False
