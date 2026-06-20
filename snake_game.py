import pygame, sys
from pygame.math import Vector2
from settings import Settings
from main_event import MainEvent

pygame.mixer.pre_init(44100, -16, 2, 512)
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
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    settings.screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    settings.clock.tick(60)