# Pygame 模板基于这个模块 进一步的添加功能
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# 常见的颜色定义一下
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#tgfcoder-FrozenJam-SeamlessLoop
# 初始化pygame环境
pygame.init()
pygame.mixer.init()  #初始化音效系统
screen = pygame.display.set_mode((WIDTH, HEIGHT))  #设置窗口大小
pygame.display.set_caption("My Game")	#设置游戏的名称
clock = pygame.time.Clock()		#获取游戏的时钟


pygame.mixer.music.load( "打飞机\\shmup\\snd\\tgfcoder-FrozenJam-SeamlessLoop.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)

all_sprites = pygame.sprite.Group()     #所有运动的精灵
# 游戏循环
running = True			#游戏是否是运行状态
while running:
	# 使游戏跑在正确的状态 
    clock.tick(FPS)
    # 处理输入事件
    for event in pygame.event.get():
        # 假如事件是 退出, 那么游戏运行状态为关闭
        if event.type == pygame.QUIT:
            running = False

    # 更新所有的运动精灵的状态
    all_sprites.update()

    # 用黑色填充窗口
    screen.fill(BLACK)
	#每个精灵在窗口上画出来
    all_sprites.draw(screen)
    # 开始 flip 整个画面
    pygame.display.flip()

pygame.quit()
