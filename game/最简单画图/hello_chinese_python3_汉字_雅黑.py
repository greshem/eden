#coding: utf-8
#! /usr/bin/env python
############################################################################
# File name : hello.py
# Purpose : A Small Demo Practice Hello World Prgram using Pygame API
# Usages : Displays Hello World In Visual Mode. Considered as the first step of learning pygame API
# Start date : 17/12/2011
# End date : 17/12/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Dependency: simple.jpg
############################################################################


#import modules
import pygame
from pygame.locals import *
import os
from sys import exit
WHITE = (255, 255, 255)

#initalizing variables (setting up the stage) 
pygame.init()
screen=pygame.display.set_mode((640,480),0,24)

screen.fill(WHITE)  		#屏幕 填充   白色 

if not os.path.isfile("msyh.ttf"):
    print("微软雅黑文件不存在  搜索  msyh.ttf 文件拷贝到当前目录就可以了");
pygame.display.set_caption("Hello World")
#create=pygame.font.SysFont("msyh.ttf",30)
create = pygame.font.Font('msyh.ttf', 100)
f=create.render("你好",True,(0,0,0),(255,255,255))
#img=pygame.image.load("simple.jpg").convert()


#main loop which displays the hello world in visual mode
while True:
 for i in pygame.event.get():
  if i.type==QUIT:
   exit()

 #screen.blit(img,(0,0))
 screen.blit(f,(200,200))
 pygame.display.update()

