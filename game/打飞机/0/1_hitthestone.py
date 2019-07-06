#! /usr/bin/env python

import pygame
from pygame.locals import *
import random
import time

pygame.init()
screen=pygame.display.set_mode([640, 480],0,24)
pygame.display.set_caption("Hit The Stone")
background=pygame.Surface(screen.get_size())
background=background.convert()
screen.blit(background,(0,0))

class Plane(pygame.sprite.Sprite):
    def __init__(self, image=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = image or Plane._default_image
        self.cooldown=15
        self.rect=self.image.get_rect()
        self.rect.centerx = screen.get_width() / 2
        self.distancefromcenter=30
        self.rect.centery=screen.get_height()-self.distancefromcenter-40
        self.dx=3
        self.dy=3

    def update(self):
        self.pressed=pygame.key.get_pressed()
        if self.pressed[K_DOWN]:
            self.rect.centery+=self.dy
        elif self.pressed[K_UP]:
            self.rect.centery-=self.dy
        if self.pressed[K_LEFT]:
            self.rect.centerx-=self.dx
        elif self.pressed[K_RIGHT]:
            self.rect.centerx+=self.dx

        if self.rect.bottom>=screen.get_height():
            self.rect.bottom=screen.get_height()
        elif self.rect.top<=0:
            self.rect.top=0

        if self.rect.centerx>=screen.get_width()-self.distancefromcenter:
            self.rect.centerx=screen.get_width()-self.distancefromcenter
        elif self.rect.centerx<=self.distancefromcenter:
            self.rect.centerx=self.distancefromcenter

        self.cooldown = max(0, self.cooldown-1)


class Stone(pygame.sprite.Sprite):
    def __init__(self, image=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image=image or Stone._default_image
        self.rect=self.image.get_rect()
        self.rect.centerx=random.randint(5,630)
        self.rect.centery=0
        self.dy=4

    def update(self):
        self.rect.centery+=self.dy
        if self.rect.bottom>=screen.get_height():
            self.rect.centerx=random.randint(5,630)
            self.rect.centery=0


class Bullet(pygame.sprite.Sprite):

    def __init__(self, posx, posy, image=None):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = image or Bullet._default_image
        self.rect=self.image.get_rect()        
        self.rect.center=(posx,posy-30)
        self.dy=5
        

    def update(self):
        self.rect.centery-=self.dy
        self.rect.center=(self.rect.centerx,self.rect.centery)
        if self.rect.top<=0:
            self.kill()

class Score(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = 'SCORE: {}'.format(SCORE)
            self.image = self.font.render(msg, 0, self.color)
       

def main():
    allSprites=pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    stones = pygame.sprite.Group()

    Plane.containers = allSprites
    Stone.containers = allSprites, stones
    Bullet.containers = allSprites, bullets

    red=pygame.Surface([10, 10])
    red.fill((255, 0, 0))

    yellow=pygame.Surface([36, 54])
    yellow.fill((255, 255, 0))

    blue=pygame.Surface([36, 54])
    blue.fill((0, 0, 255))
	
    Plane._default_image = pygame.image.load('plane.gif').convert()
    Bullet._default_image = pygame.image.load('geometrybullet.png').convert()
    Stone._default_image = pygame.image.load('stone.png').convert_alpha()

    clock=pygame.time.Clock()

    max_stones = 10;
    stone_spawn_delay = 40;
    stone_spawn_cooldown = 0;

    global SCORE
    SCORE = 0
    allSprites.add(Score())

    plane=Plane(yellow)

    while True:
        pressed=pygame.key.get_pressed()
        for i in pygame.event.get():
            if i.type==QUIT or pressed[K_q]:
                exit()
        if pressed[K_SPACE] and plane.cooldown == 0:
            Bullet(plane.rect.centerx,plane.rect.centery,red) 
            plane.cooldown=15

        for stone in stones:
            for bullet in bullets:
               if bullet.rect.colliderect(stone):
                   bullet.kill()
                   stone.kill()
                   SCORE += 500
            if stone.rect.colliderect(plane):
                plane.kill()
                stone.kill()

        stone_spawn_cooldown -= 1
        if len(stones) < max_stones and stone_spawn_cooldown <= 0:
            Stone(blue)
            stone_spawn_cooldown = stone_spawn_delay
       
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__=='__main__':
    main()
        
        

