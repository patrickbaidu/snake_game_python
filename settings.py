import pygame

class Settings:
    
    def __init__(self):
        self.cell_size = 40
        self.cell_number = 20
        self.screen = pygame.display.set_mode((self.cell_number * self.cell_size, self.cell_number * self.cell_size))
        self.clock = pygame.time.Clock()