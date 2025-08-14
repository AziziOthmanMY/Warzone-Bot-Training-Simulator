import pygame
import math

class Bullet:
    def __init__(self, x, y, target_x, target_y):
        self.rect = pygame.Rect(x, y, 8, 8)
        self.color = (255, 255, 0)
        angle = math.atan2(target_y - y, target_x - x)
        self.dx = math.cos(angle) * 10
        self.dy = math.sin(angle) * 10
    
    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)