#! /usr/bin/env python
############################################################################
# Purpose : A very small,basic and my first game
# Usages : Learning purpose
# Start date : 12/04/2011
# End date : 2/05/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Version : 0.0.2
# Modification history : Start of the game takes place by running this script
############################################################################


import pygame
from  pygame.locals import *
from sys import exit
from random import randint
import level1
import level2
import level3


# making out the starting screen

while True:
 pygame.init()
 screen=pygame.display.set_mode((640,480),0,24)
 caption=pygame.display.set_caption("Hungry Snake")
 f=pygame.font.SysFont("comicsansms",50)
 text1=f.render("Hungry Snake",True,(0,255,0))
 clock=pygame.time.Clock()
 start=pygame.font.SysFont("comicsansms",30)
 text2=start.render("Press s to start",True,(0,255,0))
 q=pygame.font.SysFont("comicsansms",30)
 text3=q.render("Press q to quit",True,(0,255,0))
 s=[[300,200],[280,200],[260,200],[240,200],[220,200],[200,200],[180,200],[180,220],[160,220],[140,220],[120,220],[120,240],[100,240]]
 a=[100,240]
 pygame.draw.rect(screen,(255,0,0),Rect(a,[20,20]),0)
 screen.blit(text1,(60,60))
 screen.blit(text2,(300,300))
 screen.blit(text3,(300,350))
 for i in s:
  pygame.draw.rect(screen,(0,255,0),Rect(i,[20,20]),0)
  pygame.display.flip()
  clock.tick(10)
 pygame.display.flip()

#event handling (Key events)
 while True:
  for i in pygame.event.get():
   if i.type==QUIT:
    exit()
  pressed=pygame.key.get_pressed()
  if pressed[K_q]:
   exit()
  if pressed[K_s]:
   break
 break

# Level screen
while True:
 press=pygame.key.get_pressed()
 for i in pygame.event.get():
  if i.type==QUIT or  press[K_q]:
   exit()
 screen.fill((0,0,0))
 mousepress=pygame.mouse.get_pressed()
 l1=pygame.font.SysFont("comicsansms",50)
 l2=pygame.font.SysFont("comicsansms",30)
 l3=pygame.font.SysFont("comicsansms",30)
 l4=pygame.font.SysFont("comicsansms",30)
 r2=Rect((100,200),l2.size("Press 1 for Level 1 "))
 r3=Rect((100,250),l3.size("Press 2 for Level 2 "))
 r4=Rect((100,300),l3.size("Press 3 for Level 3 "))
 screen.blit(l1.render("Select Your Level",True,(0,255,0)),(100,100))
 screen.blit(l2.render("Press 1 for Level 1 ",True,(0,255,0)),(100,200))
 screen.blit(l3.render("Press 2 for level 2 ",True,(0,255,0)),(100,250))
 screen.blit(l4.render("Press 3 for level 3 ",True,(0,255,0)),(100,300))
 pygame.display.update()
 
 if press[K_1] or  (r2.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
  level1.main()
 if press[K_2] or  (r3.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
  level2.main()
 if press[K_3] or  (r4.collidepoint(pygame.mouse.get_pos()) and mousepress[0]):
  level3.main()
  
