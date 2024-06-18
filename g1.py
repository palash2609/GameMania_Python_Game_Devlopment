import numpy as np
import pygame 
import math

# Constants
ROWS = 3
COLUMNS = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH = 600
HEIGHT = 700  # Increased height for the status bar otherwise 600
SIZE = (WIDTH, HEIGHT)

CIRCLE = pygame.image.load('circle.png')
CROSS = pygame.image.load('x.png')

def mark(row, col, player):
    board[row][col] = player

def is_valid_mark(row, col):
    return board[row][col] == 0

def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0:
                return False
    return True

def draw_board():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 1:
                window.blit(CROSS, ((c * 200) + 50, (r * 200) + 50))
            elif board[r][c] == 2:
                window.blit(CIRCLE, ((c * 200) + 50, (r * 200) + 50))
    pygame.display.update()

def draw_lines():
    # Vertical Lines
    pygame.draw.line(window, BLACK, (200, 0), (200, 600), 10)
    pygame.draw.line(window, BLACK, (400, 0), (400, 600), 10)
    # Horizontal Lines
    pygame.draw.line(window, BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(window, BLACK, (0, 400), (600, 400), 10)

def is_winning_move(player):
    if player == 1:
        winning_color = RED
    else:
        winning_color = BLUE
    # Vertical Check
    for r in range(ROWS):  
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            pygame.draw.line(window, winning_color, (10, (r * 200) + 100), (WIDTH - 10, (r * 200) + 100), 10)
            return True
    # Horizontal Check
    for c in range(COLUMNS): 
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            pygame.draw.line(window, winning_color, ((c * 200) + 100, 10), ((c * 200) + 100, HEIGHT - 100), 10)
            return True

    # +ve diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(window, winning_color, (10, 10), (590, 590), 10)
        return True
    # -ve diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        pygame.draw.line(window, winning_color, (590, 10), (10, 590), 10)
        return True

def draw_status(message):
    font = pygame.font.SysFont(None, 36)
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, 650))  
    pygame.draw.rect(window, BLACK, (0, 600, WIDTH, 100))
    window.blit(text,text_rect)
    pygame.display.update()

board = np.zeros((ROWS, COLUMNS))

game_over = False
Turn = 0

pygame.init() #To initialize pygame's function and modules
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic-Tac-Toe by Palash")
window.fill(WHITE)
draw_lines()
draw_status("Player 1's turn")
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # event that represent clicking on the mouse
            if Turn % 2 == 0: # Even->Player 1
                row = math.floor(event.pos[1] / 200)
                col = math.floor(event.pos[0] / 200)
                if row < 3 and col < 3 and is_valid_mark(row, col):
                    mark(row, col, 1)
                    if is_winning_move(1):
                        game_over = True
                        draw_status("Player 1 won!")
                    else:
                        draw_status("Player 2's turn")
                else:
                    Turn -= 1
            else:  # Odd ->Player 2
                row = math.floor(event.pos[1] / 200)
                col = math.floor(event.pos[0] / 200)
                if row < 3 and col < 3 and is_valid_mark(row, col):
                    mark(row, col, 2)
                    if is_winning_move(2):
                        game_over = True
                        draw_status("Player 2 won!")
                    else:
                        draw_status("Player 1's turn")
                else:
                    Turn -= 1
            Turn += 1

            draw_board()

            if is_board_full() and not game_over:
                game_over = True
                draw_status("It's a draw!")

    if game_over:
        pygame.time.wait(2000)  #Delay of 2000 ms
        board.fill(0)  #Board rsest conditions
        window.fill(WHITE)
        draw_lines()
        draw_board()
        game_over = False
        Turn = 0
        draw_status("Player 1's turn")
        pygame.display.update()
