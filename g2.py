import pygame
import random

# Define colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (160, 32, 240)
ORANGE = (255,151, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Screen dimensions
WIDTH = 600
HEIGHT = 400

# Snake attributes
snake_block = 10
snake_speed = 15

# Initialize game
pygame.init()
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game by Palash")

# Fonts
font_style = pygame.font.SysFont("Arial", 30)
lost_mssg = font_style.render("Oops...You Lost! Press P-To Play Again or Q-To Quit", True, RED)


clock = pygame.time.Clock()

def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        color = GREEN if i == len(snake_list) - 1 else RED
        pygame.draw.rect(dis, color, (x[0], x[1], snake_block, snake_block))
        if i == len(snake_list) - 1:  # Draw eyes for the head
            pygame.draw.circle(dis, BLACK, (x[0] + 3, x[1] + 3), 2)
            pygame.draw.circle(dis, BLACK, (x[0] + 7, x[1] + 3), 2)

def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, YELLOW)
    dis.blit(value, [0, 0])

def game_loop():
    game_over = False
    game_close = False
    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0
    x_food = snake_block * random.randint(0, (WIDTH // snake_block - 1)) #b/w 0 and 590
    y_food = snake_block * random.randint(0, (HEIGHT // snake_block - 1)) #b/w 0 and 390
    snake_list = []
    snake_length = 1

    while not game_over:
        while game_close:
            dis.fill(WHITE)
            lost_mssg_rect = lost_mssg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            dis.blit(lost_mssg, lost_mssg_rect)
            pygame.display.update() #To the refresh the display
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #Click q=Quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p: #Click p=Play again
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #For x close button to work
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0: #Defining boundary of the game
            game_close = True
        x += x_change
        y += y_change
        dis.fill(BLACK) #To fill the background
        our_snake(snake_block, snake_list) #Snake
        pygame.draw.rect(dis, YELLOW, (x_food, y_food, snake_block, snake_block)) #Food
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:  #snake eats its own body
            if segment == snake_head:
                game_close = True

        if x == x_food and y == y_food: # food generating and snake body growing
            snake_length += 1
            x_food = snake_block * random.randint(0, (WIDTH // snake_block - 1))
            y_food = snake_block * random.randint(0, (HEIGHT // snake_block - 1))

        display_score(snake_length - 1) #for score
        pygame.display.update()
        clock.tick(snake_speed) #15 frames/sec

    pygame.quit()

game_loop()
