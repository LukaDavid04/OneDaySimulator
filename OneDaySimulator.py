# OneDaySimulator
# 'Whatever I feel like simulating on a given day'
# By: Luka David



import os
import pygame
from pygame.locals import*

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,150)

pygame.init()
backColour = (255,255,255)
(width, height) = (800, 600)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Today\'s Simulation')
screen.fill(backColour)
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
    if event.type == pygame.QUIT:
      running = False

pygame.quit()


