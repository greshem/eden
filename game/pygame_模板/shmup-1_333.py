# coding:utf-8
# KidsCanCode - Game Development with Pygame video series
# Shmup game - part 1
# Video link: https://www.youtube.com/watch?v=nGufy7weyGY
# Player sprite and movement
import pygame
import random  #随机 

WIDTH = 1000  #宽度
HEIGHT = 600
FPS = 60

# define colors 定义颜色 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()        # 
pygame.mixer.init()  #混音器 初始化 
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #显示器 设置高低
pygame.display.set_caption("EDEN!")                 #设置标题 
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((44, 44))  # 创建一个i额 50x40长方形
        self.image.fill(BLUE)                   #7用green 填充
        self.rect = self.image.get_rect()       #获取大小
        self.rect.centerx = WIDTH / 2           #  中心 为宽度的一半
        self.rect.bottom = HEIGHT - 10          # 高 10个
        self.speedx = 0                         #速度为0

def update(self):
        self.pressed=pygame.key.get_pressed()
        if self.pressed[K_DOWN]:
            self.rect.centery+=10
        elif self.pressed[K_UP]:
            self.rect.centery-=10
        if self.pressed[K_LEFT]:
            self.rect.centerx-=10
        elif self.pressed[K_RIGHT]:
            self.rect.centerx+10

        if self.rect.bottom>=screen.get_height():
            self.rect.bottom=screen.get_height()
        elif self.rect.top<=0:
            self.rect.top=0

all_sprites = pygame.sprite.Group()         # 敌人  初始化 
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:       #退出的时候 
            running = False

#    Update
    all_sprites.update()            #敌人更新

    # Draw / render
    #screen.fill(BLACK)
    screen.fill(BLACK)          #屏幕 填充   白色 
    all_sprites.draw(screen)        #画屏幕
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
