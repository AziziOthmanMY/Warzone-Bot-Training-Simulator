import pygame
import random
from player import Player
from bot import Bot
from map import GameMap
from bullet import Bullet
from weapon import Weapon

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warzone Bot Training Simulator")

game_map = GameMap(WIDTH, HEIGHT)

player = Player(400, 300, 40, 40, (0, 0, 255))
bots = [Bot(random.randint(0, WIDTH-40), random.randint(0, HEIGHT-40), 40, 40, (255, 0, 0)) for _ in range(5)]
bullets = []
weapons = [Weapon(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)) for _ in range(3)]

score = 0
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)
    win.fill((34, 139, 34))
    game_map.draw(win)
    
    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH, HEIGHT)
    player.draw(win)
    
    for bot in bots:
        bot.move_towards_player(player)
        bot.draw(win)
    
    for bullet in bullets[:]:
        bullet.move()
        bullet.draw(win)
        for bot in bots[:]:
            if bullet.rect.colliderect(bot.rect):
                bots.remove(bot)
                bullets.remove(bullet)
                score += 1
    
    for weapon in weapons:
        weapon.draw(win)
        if player.rect.colliderect(weapon.rect):
            player.pick_weapon(weapon)
            weapons.remove(weapon)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player.weapon:
                bullets.append(player.shoot())

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()