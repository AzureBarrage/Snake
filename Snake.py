import pygame
import sys
import random
import time

pygame.font.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
snake_size = 25
snake_speed = 25
snake_pos = [[100, 50], [90, 50], [80, 50]]

# Food settings
food_size = 25
food_pos = [random.randrange(1, WIDTH // 20) * 20, random.randrange(1, HEIGHT // 20) * 20]


def draw_objects():
    screen.fill(WHITE)
    for pos in snake_pos:
        pygame.draw.circle(screen, GREEN, (pos[0] + snake_size // 2, pos[1] + snake_size // 2), snake_size // 2)
    pygame.draw.circle(screen, RED, (food_pos[0] + food_size // 2, food_pos[1] + food_size // 2), food_size // 2)


def move_snake():
    for i in range(len(snake_pos) - 1, 0, -1):
        snake_pos[i] = list(snake_pos[i - 1])

    if direction == 'RIGHT':
        snake_pos[0][0] += snake_speed
    elif direction == 'LEFT':
        snake_pos[0][0] -= snake_speed
    elif direction == 'UP':
        snake_pos[0][1] -= snake_speed
    elif direction == 'DOWN':
        snake_pos[0][1] += snake_speed


def check_collision():
    head_x, head_y = snake_pos[0]

    # Check if the snake's head overlaps any part of its body
    for segment in snake_pos[1:]:
        seg_x, seg_y = segment
        if head_x + snake_size > seg_x and head_x < seg_x + snake_size and \
                head_y + snake_size > seg_y and head_y < seg_y + snake_size:
            return True

    # Check if the snake's head goes outside the screen boundaries
    if head_x >= WIDTH or head_x < 0 or head_y >= HEIGHT or head_y < 0:
        return True

    return False


def generate_food():
    global food_pos
    food_pos = [random.randrange(1, WIDTH // 20) * 20, random.randrange(1, HEIGHT // 20) * 20]


def eat_food():
    head_x, head_y = snake_pos[0]
    food_x, food_y = food_pos

    if head_x >= food_x and head_x < food_x + food_size and head_y >= food_y and head_y < food_y + food_size:
        snake_pos.append([0, 0])
        return True
    return False


def display_message(text, pos, font_size=24, color=(0, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)


def reset_game():
    global snake_pos, direction
    snake_pos = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    generate_food()


clock = pygame.time.Clock()


# Main loop
def game_loop():
    global direction  # Add this line to define the 'direction' variable as global

    direction = 'RIGHT'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        move_snake()
        if check_collision():
            break

        if eat_food():
            generate_food()

        draw_objects()
        pygame.display.flip()
        clock.tick(10)


    display_message("You lost! Press R to try again or Q to quit", (50, HEIGHT // 2))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


# Main loop
while True:
    game_loop()
    time.sleep(1)
