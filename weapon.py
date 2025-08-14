import pygame

class Weapon:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.color = (255, 215, 0)
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)