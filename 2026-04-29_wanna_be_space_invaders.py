import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player Setup
player_width = 50
player_height = 40
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - 70
player_speed = 5

# Bullet Setup
bullet_width = 5
bullet_height = 10
bullet_speed = -7
bullets = []

# Enemy Setup
enemy_width = 50
enemy_height = 40
enemy_speed = 2
enemies = []

def spawn_enemy():
    x = random.randint(0, SCREEN_WIDTH - enemy_width)
    y = random.randint(50, 150)
    enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

# Spawn initial enemies
for _ in range(6):
    spawn_enemy()

# Game Loop
running = True
clock = pygame.time.Clock()
score = 0

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Shooting logic
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player_x + player_width//2, player_y, bullet_width, bullet_height)
                bullets.append(bullet)

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Update Bullets
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Update Enemies
    for enemy in enemies[:]:
        enemy.x += enemy_speed
        # Bounce off walls
        if enemy.right >= SCREEN_WIDTH or enemy.left <= 0:
            enemy_speed *= -1
            for e in enemies:
                e.y += 10 # Move down

    # Collision Detection
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                spawn_enemy() # Replace the enemy
                break

    # Draw Player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    
    # Draw Bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
        
    # Draw Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()