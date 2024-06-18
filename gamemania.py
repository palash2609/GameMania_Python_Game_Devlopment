import pygame
import sys
import subprocess
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
FONT_SIZE = 40
ARROW_SIZE = 30
ARROW_OFFSET_X = 370
HEADING_SIZE = 80
SPACING = 200 

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game Mania by Palash')
font = pygame.font.Font(None, FONT_SIZE)
heading_font = pygame.font.Font(None, HEADING_SIZE)
clock = pygame.time.Clock()

# Load images
tic_tac_toe_img = pygame.image.load('tictactoe1.jpg')  
snake_img = pygame.image.load('snake1.png') 

# Resize images if necessary
tic_tac_toe_img = pygame.transform.scale(tic_tac_toe_img, (180, 180))
snake_img = pygame.transform.scale(snake_img, (150, 190))

# Load background music
# pygame.mixer.music.load('assets/background_music.mp3')
# pygame.mixer.music.play(-1)

# Menu Options
menu_options = ['Tic-Tac-Toe Game', 'Snake Game']
menu_images = [tic_tac_toe_img, snake_img]
selected_option = 0

# Arrow Position
arrow_y = SCREEN_HEIGHT // 1

# Animation variables
color_phase = 0

def draw_menu():
    screen.fill(BLACK)
    
    # Draw heading with color fade animation
    heading_color = (abs(int(255 * math.sin(color_phase))), 
                     abs(int(255 * math.sin(color_phase + 2 * math.pi / 3))), 
                     abs(int(255 * math.sin(color_phase + 4 * math.pi / 3))))
    heading_text = heading_font.render('Welcome To Game Mania!', True, heading_color)
    heading_rect = heading_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(heading_text, heading_rect)
    
    for i, (option, image) in enumerate(zip(menu_options, menu_images)):
        color = WHITE if i == selected_option else (100, 100, 100)
        text = font.render(option, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + i * SPACING))
        screen.blit(text, text_rect)
        # Position image to the left of the text
        image_rect = image.get_rect(center=(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + i * SPACING))
        screen.blit(image, image_rect)

def draw_arrow(y):
    arrow_points = [(ARROW_OFFSET_X, y), 
                    (ARROW_OFFSET_X - ARROW_SIZE, y - ARROW_SIZE // 2), 
                    (ARROW_OFFSET_X - ARROW_SIZE, y + ARROW_SIZE // 2)]
    pygame.draw.polygon(screen, RED, arrow_points)

def run_game(game_script):
    subprocess.run(['python', game_script])

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    run_game('g1.py')
                elif selected_option == 1:
                    run_game('g2.py')

    # Update Arrow Position
    target_y = SCREEN_HEIGHT // 2 + selected_option * SPACING
    if arrow_y < target_y:
        arrow_y = min(arrow_y + 10, target_y)
    elif arrow_y > target_y:
        arrow_y = max(arrow_y - 10, target_y)
    
    # Update color phase for heading animation
    color_phase += 0.01

    # Draw everything
    draw_menu()
    draw_arrow(arrow_y)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
