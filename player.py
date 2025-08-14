import pygame
from bullet import Bullet

class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = 5
        self.weapon = None
    
    def move(self, keys, max_width, max_height):
        if keys[pygame.K_a] and self.rect.x - self.speed > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x + self.speed < max_width - self.rect.width:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.y - self.speed > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y + self.speed < max_height - self.rect.height:
            self.rect.y += self.speed
    
    def pick_weapon(self, weapon):
        self.weapon = weapon
    
    def shoot(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return Bullet(self.rect.centerx, self.rect.centery, mouse_x, mouse_y)
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        if self.weapon:
            pygame.draw.circle(win, (255, 215, 0), self.rect.center, 5)