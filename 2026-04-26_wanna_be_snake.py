import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
FPS = 10

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = COLOR_GREEN

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = cur
        
        if self.direction == pygame.K_UP:
            y -= GRID_SIZE
        elif self.direction == pygame.K_DOWN:
            y += GRID_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= GRID_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += GRID_SIZE

        # Wrap around screen (Intermediate feature)
        new = (x % SCREEN_WIDTH, y % SCREEN_HEIGHT)
        
        # Check if snake hit itself
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, COLOR_BLACK, r, 1)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = COLOR_RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, COLOR_BLACK, r, 1)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Intermediate Snake OOP')

    snake = Snake()
    food = Food()
    font = pygame.font.SysFont("arial", 24)

    while True:
        screen.fill(COLOR_BLACK)
        
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != pygame.K_DOWN:
                    snake.direction = event.key
                elif event.key == pygame.K_DOWN and snake.direction != pygame.K_UP:
                    snake.direction = event.key
                elif event.key == pygame.K_LEFT and snake.direction != pygame.K_RIGHT:
                    snake.direction = event.key
                elif event.key == pygame.K_RIGHT and snake.direction != pygame.K_LEFT:
                    snake.direction = event.key

        # 2. Logic
        snake.update()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        # 3. Rendering
        snake.draw(screen)
        food.draw(screen)
        
        score_text = font.render(f"Score: {snake.length - 1}", True, COLOR_WHITE)
        screen.blit(score_text, (5, 5))
        
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()