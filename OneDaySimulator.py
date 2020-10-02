# OneDaySimulator
# 'Whatever I feel like simulating on a given day'
# By: Luka David

import pygame
from pygame.locals import*

pygame.init()
backColour = (0,0,0)
(width, height) = (800, 600)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Today\'s Simulation')
screen.fill(backColour)
pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


