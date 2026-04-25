import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.25
FLAP_STRENGTH = -6
PIPE_SPEED = 3
PIPE_GAP = 150

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
GREEN = (34, 139, 34)

# Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Derpy Square: The Flapping")
clock = pygame.time.Clock()

# Game Variables
bird_rect = pygame.Rect(50, SCREEN_HEIGHT // 2, 30, 30)
bird_movement = 0
pipes = []
score = 0
game_active = True

def create_pipe():
    random_pipe_pos = random.randint(150, 450)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, random_pipe_pos, 50, SCREEN_HEIGHT)
    top_pipe = pygame.Rect(SCREEN_WIDTH, random_pipe_pos - PIPE_GAP - SCREEN_HEIGHT, 50, SCREEN_HEIGHT)
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= PIPE_SPEED
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= SCREEN_HEIGHT:
        return False
    return True

# Spawn first pipe
pipes.extend(create_pipe())
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement += FLAP_STRENGTH
            if event.key == pygame.K_SPACE and not game_active:
                # Reset Game
                game_active = True
                pipes.clear()
                bird_rect.center = (50, SCREEN_HEIGHT // 2)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE and game_active:
            pipes.extend(create_pipe())

    screen.fill(SKY_BLUE)

    if game_active:
        # Bird Physics
        bird_movement += GRAVITY
        bird_rect.centery += bird_movement
        pygame.draw.rect(screen, YELLOW, bird_rect)

        # Pipes
        pipes = move_pipes(pipes)
        draw_pipes(pipes)

        # Collision
        game_active = check_collision(pipes)
    else:
        # Game Over Screen
        font = pygame.font.SysFont('Arial', 32)
        text = font.render("GAME OVER - Press SPACE", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text, text_rect)

    pygame.display.update()
    clock.tick(60)