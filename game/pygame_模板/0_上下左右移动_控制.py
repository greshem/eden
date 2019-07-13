# Pygame 模板基于这个模块 进一步的添加功能
import pygame
import random
import pygame
from pygame.locals import *
import random
import time


WIDTH = 360
HEIGHT = 480
FPS = 30

# 常见的颜色定义一下
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 初始化pygame环境
pygame.init()
pygame.mixer.init()  #初始化音效系统
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #设置窗口大小
pygame.display.set_caption("My Game")   #设置游戏的名称
clock = pygame.time.Clock()     #获取游戏的时钟


#pygame.mixer.music.load( "K:\_xfile_backup\朗读\光盘_cd_钱奕程\2014_04_15_冰雪奇缘_列那狐\我要就出贝里奥_巴赫：G弦上的咏叹调.ogg")
#pygame.mixer.music.set_volume(0.1)
#pygame.mixer.music.play(loops=-1)

class Plane(pygame.sprite.Sprite):
    def __init__(self, image=None):
        pygame.sprite.Sprite.__init__(self, self.containers)
        red=pygame.Surface([50, 50])
        red.fill((255, 0, 0))
    
        self.image = red
        self.cooldown=1
        self.rect=self.image.get_rect()
        self.rect.centerx = screen.get_width() / 2
        self.distancefromcenter=25
        self.rect.centery=screen.get_height()-self.distancefromcenter-40
        self.dx=19
        self.dy=19

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

       
allSprites = pygame.sprite.Group()     #所有运动的精灵
Plane.containers = allSprites

plane=Plane()


# 游戏循环
running = True          #游戏是否是运行状态
while running:
    # 使游戏跑在正确的状态 
    clock.tick(FPS)
    # 处理输入事件
    for event in pygame.event.get():
        # 假如事件是 退出, 那么游戏运行状态为关闭
        if event.type == pygame.QUIT:
            running = False

    # 更新所有的运动精灵的状态
    allSprites.update()

    # 用黑色填充窗口
    screen.fill(BLACK)
    #每个精灵在窗口上画出来
    allSprites.draw(screen)
    # 开始 flip 整个画面
    pygame.display.flip()

pygame.quit()
