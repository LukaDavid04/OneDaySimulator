# OneDaySimulator
# 'Whatever I feel like simulating on a given day'
# By: Luka David


import os
import pygame
from random import*
from pygame.locals import*
import pygame.gfx

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,150)

pygame.init()
backColour = (255,255,255)
(width, height) = (800, 600)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Today\'s Simulation')
screen.fill(backColour)
pygame.display.flip()



def rain():
  raining = True
  while raining:
    a = randint(0, 800)


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_SPACE:
        rain()
    if event.type == pygame.QUIT:
      running = False

pygame.quit()


