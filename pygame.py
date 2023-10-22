import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Snake properties
snake_block = 20
snake_speed = 15

# Initialize Snake position
x, y = width // 2, height // 2
x_change, y_change = 0, 0

# Initialize Snake body
snake = [(x, y)]
snake_length = 1

# Set up the food
food_x = random.randrange(1, (width - snake_block) // snake_block) * snake_block
food_y = random.randrange(1, (height - snake_block) // snake_block) * snake_block

# Score
score = 0

# Game over flag
game_over = False

# Game loop
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change == 0:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT and x_change == 0:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP and y_change == 0:
                x_change = 0
                y_change = -snake_block
            elif event.key == pygame.K_DOWN and y_change == 0:
                x_change = 0
                y_change = snake_block

    # Check if the snake eats the food
    if x == food_x and y == food_y:
        food_x = random.randrange(1, (width - snake_block) // snake_block) * snake_block
        food_y = random.randrange(1, (height - snake_block) // snake_block) * snake_block
        snake_length += 1
        score += 1

    # Update the snake's position
    x += x_change
    y += y_change

    # Game over conditions
    if x >= width or x < 0 or y >= height or y < 0:
        game_over = True

    # Check for self-collision
    if (x, y) in snake[:-1]:
        game_over = True

    snake.append((x, y))
    if len(snake) > snake_length:
        del snake[0]

    # Update the display
    win.fill(black)

    for segment in snake:
        pygame.draw.rect(win, green, [segment[0], segment[1], snake_block, snake_block])

    pygame.draw.rect(win, white, [food_x, food_y, snake_block, snake_block])

    pygame.display.update()

    clock.tick(snake_speed)

# Game over message
font = pygame.font.Font(None, 36)
game_over_text = font.render(f"Game Over - Score: {score}", True, white)
win.blit(game_over_text, (width // 3, height // 3))
pygame.display.update()

# Wait for a few seconds before exiting
pygame.time.delay(2000)

pygame.quit()
