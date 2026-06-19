import pygame
from pygame.math import Vector2
from settings import Settings

class Snake(Settings):
    
    def __init__(self):
        super().__init__()
        self.body = [Vector2(5, 10), Vector2(6,10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
    
    def draw_snake(self):
        cell_size = self.cell_size
        for block in self.body:
            x_position = int(block.x * cell_size)
            y_position = int(block.y * cell_size)
            block_rectangle = pygame.Rect(x_position, y_position, cell_size, cell_size)
            pygame.draw.rect(self.screen, (183, 111, 122), block_rectangle)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True