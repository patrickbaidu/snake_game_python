import pygame, sys
from fruit import Fruit
from settings import Settings

pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    Settings.screen.fill((175, 215, 70))
    pygame.display.update()
    Settings.clock.tick(60)