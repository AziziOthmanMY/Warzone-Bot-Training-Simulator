import pygame

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self, win):
        pygame.draw.rect(win, (139, 69, 19), (200, 150, 100, 50))
        pygame.draw.rect(win, (139, 69, 19), (500, 400, 150, 50))