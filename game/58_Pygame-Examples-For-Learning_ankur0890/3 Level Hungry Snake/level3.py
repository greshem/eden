#! /usr/bin/env python
############################################################################
# Purpose : A very small,basic and my first game
# Usages : Learning purpose
# Start date : 12/04/2011
# End date : 2/05/2011
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
# Version : 0.0.2
# Modification history : Level3 - Stone Fall 
############################################################################



import pygame
from  pygame.locals import *
from sys import exit
from random import randint

counter=0
def main():
 while True:
  b=[]
  def update():
   global counter
   counter=(counter+1)%7
  def blast(w,h):
   image=pygame.image.load("explosed-sprite.png").convert_alpha()
   width,height=image.get_size()
   for i in xrange(int(width/w)):
    b.append(image.subsurface((i*w,0,w,h)))
   #print a
  up=1
  down=2
  right=3
  left=4
  step=20
  block=[20,20]
  x=randint(1,20)
  y=randint(2,22)
  applexy=[]
  x3=randint(1,25)
  check=[x3*20,-20]
  snakexy=[int(x*20),int(y*20)]
  snakelist=[[x*20,y*20],[(x-20)*20,(y*20)]]
  apple=0
  dead=0
  grow=0
  direction=right
  score=0
  start=0
  draw=[]
  screen=pygame.display.set_mode((640,480),0,24)
  clock=pygame.time.Clock()

#game loop
  while not dead:
   pressed=pygame.key.get_pressed()
   for i in pygame.event.get():
    if i.type==QUIT or pressed[K_q]:
     exit()
   image2=pygame.image.load("stone.png").convert_alpha()
   pygame.transform.scale(image2,(20,20))
   check[1]=check[1]+step
   if check[1]>480:
    x2=randint(1,25)
    check[0]=x2*20
    check[1]=0
  
   if pressed[K_LEFT] and direction!=right:
     direction=left
   elif pressed[K_RIGHT] and direction!=left:
      direction=right
   elif pressed[K_UP] and direction!=down:
      direction=up
   elif pressed[K_DOWN] and direction!=up:
      direction=down
   if direction==right:
    snakexy[0]=snakexy[0]+step
    if snakexy[0]>=640:
     snakexy[0]=0

   elif direction==left:
    snakexy[0]=snakexy[0]-step
    if snakexy[0]<0:
     snakexy[0]=620

   elif direction==up:
    snakexy[1]=snakexy[1]-step
    if snakexy[1]<0:
     snakexy[1]=460
   elif direction==down:
    snakexy[1]=snakexy[1]+step
    if snakexy[1]>=480:
     snakexy[1]=0

   if snakelist.count(snakexy)>0:
    for i in snakelist:
     if i==snakexy:
      draw.append(i)
      break
    dead=1
   if apple==0:
    x1=randint(1,31)
    y1=randint(2,22)
    applexy=[int(x1*step),int(y1*step)]
    apple=1

   snakelist.insert(0,list(snakexy))
   if snakexy[0]==applexy[0] and snakexy[1]==applexy[1]:
    apple=0
    score=score+1
   else:
    snakelist.pop()

   if snakelist.count(check)>0:
    for i in snakelist:
     if i==check:
      draw.append(i)
      break
    dead=1

#display on the screen
   screen.fill((0,0,0))
   scr=pygame.font.SysFont("comicsansms",20)
   text4=scr.render("Score : %d"%score,True,(0,255,0))
   screen.blit(text4,(500,10))
   screen.blit(image2,check)
   pygame.draw.rect(screen,(255,0,0),Rect(applexy,block),0)
   for i in snakelist:
    pygame.draw.rect(screen,(0,255,0),Rect(i,block))
   pygame.display.flip()
   clock.tick(15)

  if dead==1:
   blast(20,20)
   for i in xrange(7):
    screen.blit(b[counter],(tuple(draw)))
    update()
    pygame.display.update()
    clock.tick(10)

# Game over display

   screen.fill((0,0,0))
   over=pygame.font.SysFont("comicsansms",40)
   s1=pygame.font.SysFont("comicsansms",30)
   s2=pygame.font.SysFont("comicsansms",30)
   text5=over.render("GAME OVER",True,(0,255,0))
   screen.blit(text5,(50,50))
   screen.blit(text4,(200,200))
   screen.blit(s1.render("Press s To Play Again",True,(0,255,0)),(50,250))
   screen.blit(s2.render("Press l For Level Selection ",True,(0,255,0)),(50,300))

   pygame.display.flip()
   while True:
    for i in pygame.event.get():
     if i.type==QUIT:
      exit()
    pressed=pygame.key.get_pressed()
    if pressed[K_q]:
     exit()
    if pressed[K_s]:
     main()
    if pressed[K_l]:
     break
   break



if __name__=='__main__':
 main()

















