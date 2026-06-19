import pygame, sys
from pygame.math import Vector2
from settings import Settings
from main_event import MainEvent

pygame.init()

main_game = MainEvent()
settings = Settings()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)

    settings.screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    settings.clock.tick(60)