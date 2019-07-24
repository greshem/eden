#!/usr/bin/env python

# Instructions: Draw the planets into the black hole controlled by the mouse.
# Avoid the red things because they cause the planets you've collected to be
# ejected. Watch out when you have collected a lot because you will be
# very massive and things will come at you fast. Have fun!

"""
gravity.py - the game
  for the pygame.draw competition
Copyright (C) 2006  Seth Yastrov

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import pygame, sys, random
from pygame.locals import *
from math import sin, cos, pi, sqrt
import random

pygame.init()

# Configuration
FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
FULLSCREEN = True

background_color = (0, 0, 0)
planet_color = (255, 255, 255)
planet_radius = 100

planet_pos = (SCREEN_WIDTH/2.0, SCREEN_HEIGHT/2.0)

videoFlags = 0
if 0: #FULLSCREEN:
  videoFlags |= pygame.FULLSCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), videoFlags)
pygame.display.set_caption("pygame.draw - Gravity")
screen = pygame.display.get_surface()

screen.fill(background_color)

class Planet:
  def __init__(self, color, pos, size):
    self.color = color
    self.pos = pos
    self.size = size
    self.mass = size
  
  def draw(self):
    pygame.draw.circle(screen, self.color, self.pos, self.size, 2)
    
class Chunk:
  def __init__(self, color, pos, size, bad):
    self.color = color
    self.pos = pos
    self.size = size
    self.mass = size
    
    self.acceleration = (0.0, 0.0)
    self.velocity = (0.0, 0.0)
    
    self.bad = bad
    
    if self.bad:
      self.color = [255, 0, 0]
      self.size = 10
    
    self.attach = False
    self.dead = False
  
  def draw(self):
    if self.bad:
      pygame.draw.rect(screen, self.color, pygame.Rect(int(self.pos[0]), int(self.pos[1]), int(self.size), int(self.size)), 0)
    elif not self.attach:
      pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.size, 0)
    
  def update(self):
    if self.dead:
      return
    if self.attach:
      self.pos = planet.pos[0] + self.attach[0], planet.pos[1] + self.attach[1]
      return
    
    dist = sqrt((planet.pos[0] - self.pos[0])**2 + (planet.pos[1] - self.pos[1])**2)
    
    if dist < planet.size + self.size:
      global score
      if self.bad:
        for c in chunks:
          if c.attach:
            c.acceleration = -c.acceleration[0], -c.acceleration[1]
            c.velocity = c.velocity[0] + c.acceleration[0] * elapsed * 10, c.velocity[1] + c.acceleration[1] * elapsed * 10
            c.pos = c.pos[0] + c.velocity[0] * elapsed * 10, c.pos[1] + c.velocity[1] * elapsed * 10
            #c.pos = c.pos[0] + c.attach[0], c.pos[1] + c.attach[1]
            c.attach = False
            planet.mass -= c.mass
            score -= 1
        chunks.remove(self)
        # Spawn another
        chunks.append(Chunk(color, randomPosition(), 8 + random.randint(-3, 3), True))
      else:
        # attach to the planet
        self.attach = self.pos[0] - planet.pos[0], self.pos[1] - planet.pos[1]
        planet.mass += self.mass
        score += 1
      return
    
    G = 50000.0
    accel = (G * planet.mass) / dist**2
    
    xcomp = cos((planet.pos[0] - self.pos[0]) / dist)
    ycomp = sin((planet.pos[1] - self.pos[1]) / dist)
    
    if (planet.pos[0] < self.pos[0]):
      xcomp *= -1
    
    speedlimit = 50.0
    speed = sqrt(self.velocity[0]**2 + self.velocity[1]**2)
    # Limit the speed when the chunk isn't near
    if speed > speedlimit and dist > SCREEN_WIDTH / 5:
      self.velocity = self.velocity[0] / speed * speedlimit, self.velocity[1] / speed * speedlimit
    
    self.acceleration = accel * xcomp, accel * ycomp
    self.velocity = self.velocity[0] + self.acceleration[0] * elapsed, self.velocity[1] + self.acceleration[1] * elapsed
    
    """
    speedlimit = 200.0
    if (self.velocity[0] > speedlimit):
      self.velocity = speedlimit, self.velocity[1] - self.velocity[0]-self.speedlimit
    if (self.velocity[1] > speedlimit):
      self.velocity = self.velocity[0], speedlimit
    if (self.velocity[0] < -speedlimit):
      self.velocity = -speedlimit, self.velocity[1]
    if (self.velocity[1] < -speedlimit):
      self.velocity = self.velocity[0], -speedlimit
    """
    
    self.pos = self.pos[0] + self.velocity[0] * elapsed, self.pos[1] + self.velocity[1] * elapsed
    
    # Wrap around
    if self.pos[0] > SCREEN_WIDTH:
      self.pos = self.pos[0] - SCREEN_WIDTH, self.pos[1]
    if self.pos[1] > SCREEN_HEIGHT:
      self.pos = self.pos[0], self.pos[1] - SCREEN_HEIGHT
    if self.pos[0] < 0:
      self.pos = SCREEN_WIDTH - self.pos[0], self.pos[1]
    if self.pos[1] < 0:
      self.pos = self.pos[0], SCREEN_HEIGHT - self.pos[1]
    
    #print xcomp, ycomp, elapsed, dist
    
    #print "a: %f %f v: %f %f d: %f %f" % (self.acceleration[0], self.acceleration[1], self.velocity[0], self.velocity[1], self.pos[0], self.pos[1])
    

def randomPosition():
  return random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)

def main():
  startGame(20)

def startGame(numChunks):
  global planet_pos, planet, chunks, elapsed
  clock = pygame.time.Clock()
  
  planet = Planet(planet_color, planet_pos, planet_radius)
  
  font = pygame.font.SysFont("Arial", 36)
  
  chunks = []
  grey = [160, 160, 160]
  for i in range(numChunks):
    color = [c + random.randint(-64, 64) for c in grey]
    chunks.append(Chunk(color, randomPosition(), 8 + random.randint(-3, 3), random.random() < 0.1))
  
  global score
  score = 0
  
  start = True
  
  while 1:
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == KEYDOWN and event.key == K_ESCAPE:
        return
      if event.type == MOUSEBUTTONDOWN:
        if start:
          start = False
          elapsed = 0.0
        """else:
          # Restart
          startGame(numChunks)
          return"""
    
    # Update
    
    planet.pos = pygame.mouse.get_pos()
    
    if not start:
      for c in chunks:
        c.update()
    
    
    # Draw
    
    screen.fill(background_color)
    
    for c in chunks:
      c.draw()
      
    planet.draw()
    
    if not start:
      s = font.render("%s" % score, True, [255, 255, 255])
      #screen.blit(s, (SCREEN_WIDTH-s.get_width()-20, 20))
      screen.blit(s, (planet.pos[0]+20, planet.pos[1]+20))
    
    if start:      
      s = font.render("Collect %d" % (numChunks * .5), True, [255, 255, 255])
      screen.blit(s, (SCREEN_WIDTH/2 - s.get_width()/2, SCREEN_HEIGHT/2 - s.get_height()))
      
      s2 = font.render("Click to start", True, [255, 255, 255])
      screen.blit(s2, (SCREEN_WIDTH/2 - s2.get_width()/2, SCREEN_HEIGHT/2 + s.get_height() + 10))
    
    if score >= numChunks * .5:
      startGame(numChunks + 20)
      return
    
    pygame.display.flip()
    elapsed = clock.tick(FPS) / 1000.0
    #print clock.get_fps()

if __name__ == '__main__':
    main()

