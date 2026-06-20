import pygame, sys
from pygame.math import Vector2
from fruit import Fruit
from snake import Snake
from main_functions import MainFunction

class MainEvent(Snake, Fruit, MainFunction):
    
    def __init__(self):
        super().__init__()
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
    
    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        self.snake.reset()
    
    def draw_grass(self):
        grass_color = (167, 209, 61)
        
        for row in range(self.cell_number):
            if row % 2 == 0:
                for column in range(self.cell_number):
                    if column % 2 == 0:
                        grass_rectangle = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rectangle)
                    
                    else:
                        for column in range(self.cell_number):
                            if column % 2 != 0:
                                grass_rectangle = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                                pygame.draw.rect(self.screen, grass_color, grass_rectangle)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        game_font = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 40)
        score_rectangle = score_surface.get_rect(center = (score_x, score_y))
        apple_rectangle = self.apple.get_rect(midright = (score_rectangle.left, score_rectangle.centery))
        background_rectangle = pygame.Rect(apple_rectangle.left, apple_rectangle.top, apple_rectangle.width + score_rectangle.width + 6, apple_rectangle.height)
        
        pygame.draw.rect(self.screen, (167, 209, 61), background_rectangle)
        self.screen.blit(score_surface, score_rectangle)
        self.screen.blit(self.apple, apple_rectangle)
        pygame.draw.rect(self.screen, (56, 74, 12), background_rectangle, 2)