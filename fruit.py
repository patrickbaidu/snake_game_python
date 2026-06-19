import pygame, random
from pygame.math import Vector2
from settings import Settings

class Fruit(Settings):
    
    def __init__(self):
        super().__init__()
        self.randomize()
    
    def draw_fruit(self):
        cell_size = self.cell_size
        screen = self.screen
        fruit_rectangle = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rectangle)
    
    def randomize(self):
        self.x_position = random.randint(0, self.cell_number - 1)
        self.y_position = random.randint(0, self.cell_number - 1)
        self.position = Vector2(self.x_position, self.y_position)