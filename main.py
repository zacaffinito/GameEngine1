# This file was created by Zac Affinito

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *

vec = pg.math.Vector2

# setup asset folders with images and folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')


# create on screen text with font
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

class Player(Sprite):
    # init method with class properties
    def __init__(self):
        # call the super class
        Sprite.__init__(self)
        # use image for player sprite
        self.image = pg.image.load(os.path.join(img_folder, 'theBell.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = -0.3
        self.hitpoints = 100
    def controls(self):
        # create WASD + space bar controls
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_SPACE]:
            self.jump()
    def jump(self):
        # create jumps at contacts w platforms
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            self.vel.y = -PLAYER_JUMP
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # friction + gravity 
        self.acc.x += self.vel.x * self.cofric

        # equations for sprite motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos
        # check to see if sprite fell through the bottom
        if self.rect.y > HEIGHT:
            self.pos = vec(WIDTH/2, HEIGHT/2)
            


# platform sprites

class Platform(Sprite):
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image = pg.image.load(os.path.join(img_folder, 'platform.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect.center)
        self.category = category
        self.speed = 3
        # not in use
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
        if self.category == "stagnant":
            if self.category == "ice":
                self.image.fill(WHITE)


class Mob(Sprite):
    # create new class for mobs and allow them to be collected for points
    def __init__(self, x, y, w, h, category):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image = pg.image.load(os.path.join(img_folder, 'mob.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print(self.rect.center)
        self.category = category
        self.speed = 1
    def update(self):
        if self.category == "moving":
            self.rect.x += self.speed
            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:
                self.speed = -self.speed
                self.rect.y += 25
        if self.category == "ice":
            self.image.fill(WHITE)

        if self.rect.y > HEIGHT:
            self.rect.y = 0
            print(all_mobs)
     



# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()

# create a group for all sprites
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()
all_mobs = pg.sprite.Group()
mob_count =20

# instantiate classes
player = Player()
# add instances to groups
all_sprites.add(player)

for i in range (0, 13):
    p = Platform(randint(0,WIDTH),randint(0,HEIGHT),30,30,"bounce")
    all_sprites.add(p)
    all_platforms.add(p)

for i in range(0,mob_count):
    m = Mob(randint(0,WIDTH),randint(0,HEIGHT),25,25,"moving")
    all_sprites.add(m)
    all_mobs.add(m)
range =0
all_mobs.add(m)

# Game loop
running = True

while running:
    # keep the loop running using clock
    currentfps = clock.tick(FPS)
        
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    #Game Update Loop Section 
    # update all sprites
    all_sprites.update()
    
    # this is what prevents the player from falling through the platform when falling down...
    if player.vel.y > 0:
            hits = pg.sprite.spritecollide(player, all_platforms, False)
            if hits:
                if hits[0].category == "moving":
                    player.vel.x = hits[0].speed*1.75

                player.pos.y = hits[0].rect.top
                player.vel.y = 0

                
                
    # platform interactions
    if player.vel.y < 0:
        hits = pg.sprite.spritecollide(player, all_platforms, False)
        if hits:
            SCORE += 2
            if player.rect.bottom >= hits[0].rect.top - 5:
                player.rect.top = hits[0].rect.bottom
                player.acc.y = 5
                player.vel.y = 0
# points system on mob collect
    mhits = pg.sprite.spritecollide(player, all_mobs, True)
    if mhits:
        mob_count -= 1
        SCORE += 1
    
    while mob_count <= 20:
        m = Mob(randint(0,WIDTH),randint(0,HEIGHT),25,25,"moving")
        all_sprites.add(m)
        all_mobs.add(m)
        mob_count += 1

   
    screen.fill(SKYBLUE)
    all_sprites.draw(screen)
    # Displays score
    draw_text("Score: " + str(SCORE), 22, BLACK, WIDTH/2, HEIGHT/10)

    pg.display.flip()

pg.quit()