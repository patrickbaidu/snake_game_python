import pygame, sys
from pygame.math import Vector2
from fruit import Fruit
from snake import Snake

class MainEvent(Snake, Fruit):
    
    def __init__(self):
        super().__init__()
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()