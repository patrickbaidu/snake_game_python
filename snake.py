import pygame
from pygame.math import Vector2
from settings import Settings

class Snake(Settings):
    
    def __init__(self):
        super().__init__()
        self.body = [Vector2(5, 10), Vector2(4,10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self._crunch_sound = pygame.mixer.Sound('sound/crunch.wav')

        self.__head_up = pygame.image.load('graphics/head_up.png').convert_alpha()
        self.__head_down = pygame.image.load('graphics/head_down.png').convert_alpha()
        self.__head_right = pygame.image.load('graphics/head_right.png').convert_alpha()
        self.__head_left = pygame.image.load('graphics/head_left.png').convert_alpha()
        
        self.__tail_up = pygame.image.load('graphics/tail_up.png').convert_alpha()
        self.__tail_down = pygame.image.load('graphics/tail_down.png').convert_alpha()
        self.__tail_right = pygame.image.load('graphics/tail_right.png').convert_alpha()
        self.__tail_left = pygame.image.load('graphics/tail_left.png').convert_alpha()
        
        self.__body_vertical = pygame.image.load('graphics/body_vertical.png').convert_alpha()
        self.__body_horizontal = pygame.image.load('graphics/body_horizontal.png').convert_alpha()
        
        self.__body_top_right = pygame.image.load('graphics/body_top_right.png').convert_alpha()
        self.__body_top_left = pygame.image.load('graphics/body_top_left.png').convert_alpha()
        self.__body_bottom_right = pygame.image.load('graphics/body_bottom_right.png').convert_alpha()
        self.__body_bottom_left = pygame.image.load('graphics/body_bottom_left.png').convert_alpha()
    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        cell_size = self.cell_size
        screen = self.screen
        
        for index, block in enumerate(self.body):
            x_position = int(block.x * cell_size)
            y_position = int(block.y * cell_size)
            block_rectangle = pygame.Rect(x_position, y_position, self.cell_size, self.cell_size)
            
            if index == 0:
                screen.blit(self.head, block_rectangle)
            
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rectangle)
            
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                
                if previous_block.x == next_block.x:
                    screen.blit(self.__body_vertical, block_rectangle)
                
                elif previous_block.y == next_block.y:
                    screen.blit(self.__body_horizontal, block_rectangle)
            
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.__body_top_left, block_rectangle)
                    
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.__body_bottom_left, block_rectangle)
                    
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.__body_top_right, block_rectangle)
                    
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.__body_bottom_right, block_rectangle)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.__head_left
        elif head_relation == Vector2(-1, 0): self.head = self.__head_right
        elif head_relation == Vector2(0, 1): self.head = self.__head_up
        elif head_relation == Vector2(0, -1): self.head = self.__head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.__tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.__tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.__tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.__tail_down
    
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
    
    def play_crunch_sound(self):
        self._crunch_sound.play()
    
    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)