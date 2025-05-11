import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 1080, 520
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простий Лабіринт")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WALL_COLOR = (50, 50, 200)

# Параметри лабіринту
WALL_WIDTH = 300
PASSAGE_WIDTH = 100
WALL_HEIGHT = 30
NUM_WALLS = HEIGHT // WALL_HEIGHT

# Функція для створення лабіринту
def draw_maze():
    screen.fill(WHITE)
    direction = "right"
    
    for i in range(NUM_WALLS):
        y = HEIGHT - (i + 1) * WALL_HEIGHT

        if direction == "right":
            # Стінка зліва
            pygame.draw.rect(screen, WALL_COLOR, (0, y, WIDTH - PASSAGE_WIDTH, WALL_HEIGHT))
            direction = "left"
        else:
            # Стінка справа
            pygame.draw.rect(screen, WALL_COLOR, (PASSAGE_WIDTH, y, WIDTH - PASSAGE_WIDTH, WALL_HEIGHT))
            direction = "right"

# Основний цикл
def main():
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_maze()
        pygame.display.flip()
        clock.tick(60)

main()
