# OneDaySimulator
# 'Whatever I feel like simulating on a given day'
# By: Luka David

from pygame import *

init()
backColour = (0,0,0)
(width, height) = (800, 600)

screen = display.set_mode((width, height))

display.set_caption('Today\'s Simulation')
screen.fill(backColour)
display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

# ERROR: not sure when to use init, couldn't convert to using normal import
# Old code had pygame. in front of line 8 and 10
