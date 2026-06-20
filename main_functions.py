from abc import ABC, abstractmethod

class MainFunction:
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def draw_elements(self):
        pass
    
    @abstractmethod
    def check_collisions(self):
        pass
    
    @abstractmethod
    def check_fail(self):
        pass
    
    @abstractmethod
    def game_over(self):
        pass
    
    @abstractmethod
    def draw_grass(self):
        pass
    
    @abstractmethod
    def draw_score(self):
        pass