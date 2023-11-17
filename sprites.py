import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *
from math import *
# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        # self.image = pg.Surface((50, 50))
        # self.image.fill(GREEN)
        # use an image for player sprite...
        self.game = game
        self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0) 
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)
        if hits:
            print("i can jump")
            self.vel.y = -PLAYER_JUMP
    def fire(self):
        mpos = pg.mouse.get_pos()
        targetx = mpos[0]
        targety = mpos[1]
        distance_x = targetx - self.rect.x
        distance_y = targety = self.rect.y
        angle = atan2(distance_y, distance_x)
        speed_x = 10 * cos(angle)
        speed_y = 10 * sin(angle)


# platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h, img_file ,kind):
        Sprite.__init__(self)
        self.img_file=img_file 
        self.image = pg.image.load(os.path.join(img_folder, 'platform.png')).convert()
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.speed=3
    def update(self):
        if self.kind == "moving":
            self.pos = self.rect.x
            self.rect.x = self.pos + 2
        if self.kind == "bounce":
            self.image.fill(WHITE)
    
class Ice_plat(Platform):
    def __init__(self, x, y, w, h, kind):
        Platform.__init__(self, x, y, w, h, kind)
        self.image = pg.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print("i made an ice plat")
           

           
class Mob(Sprite):
    def __init__(self, game, x, y, w, h, kind):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.image.set_colorkey(BLACK)
        self.image = pg.image.load(os.path.join(img_folder, 'mob.png')).convert()
        self.rect.x = x
        self.rect.y = y
        self.kind = kind
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.tagged = False
        self.aggro_range = 300
        self.is_seeking = True
    def seeking(self, obj):
        if abs(self.rect.x - obj.rect.x) < self.aggro_range and abs(self.rect.y - obj.rect.y) < self.aggro_range:
            if self.rect.x < obj.rect.x:
                self.rect.x +=1
            if self.rect.x > obj.rect.x:
                self.rect.x -=1
            if self.rect.y < obj.rect.y:
                self.rect.y +=1
            if self.rect.y > obj.rect.y:
                self.rect.y -=1
    def update(self):
        if self.is_seeking:
            self.seeking(self.game.Player)
        self.cd.ticking()
        if self.cd.delta > 0.2 and self.tagged:
            self.kill()

    def update(self):
        pass
        