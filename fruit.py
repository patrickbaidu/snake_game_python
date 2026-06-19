import pygame
from pygame.math import Vector2
from settings import Settings

class Fruit(Settings):
    
    def __init__(self):
        self.x_position = 5
        self.y_position = 4
        self.position = Vector2(self.x_position, self.y_position)
    
    def draw_fruit(self):
        fruit_rectangle = pygame.Rect(self.position.x_position, self.position.y_position, cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rectangle)