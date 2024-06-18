import numpy as np
import pygame 
import math

# Constants
ROWS=3
COLUMNS=3

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)

WIDTH=600
HEIGHT=600
SIZE=(WIDTH,HEIGHT)

CIRCLE=pygame.image.load('circle.png')
CROSS=pygame.image.load('x.png')

def mark(row,col,player):
	board[row][col]=player

def is_valid_mark(row,col):
	return board[row][col]==0

def is_board_full():
	for c in range(COLUMNS):
		for r in range(ROWS):
			if board[r][c]==0:
				return False
	return True
def draw_board():
	for c in range(COLUMNS):
		for r in range(ROWS):
			if board[r][c]==1:
				window.blit(CIRCLE,((c*200)+50,(r*200)+50))
			elif board[r][c]==2:
				window.blit(CROSS,((c*200)+50,(r*200)+50))
	pygame.display.update()
def draw_lines():
	#Vertical Lines
	pygame.draw.line(window,BLACK,(200,0),(200,600),10)
	pygame.draw.line(window,BLACK,(400,0),(400,600),10)
	#Horizontal Lines
	pygame.draw.line(window,BLACK,(0,200),(600,200),10)
	pygame.draw.line(window,BLACK,(0,400),(600,400),10)


def is_winning_move(player):
	if player==1:
		winning_color=BLUE
	else:
		winning_color=RED
	#Vertical Check
	for r in range(ROWS):  
		if board[r][0]== player and board[r][1]== player and board[r][2]==player:
			pygame.draw.line(window,winning_color,(10,(r*200)+100),(WIDTH-10,(r*200)+100),10)
			return True
	#Horizontal Check
	for c in range(COLUMNS): 
		if board[0][c]== player and board[1][c]== player and board[2][c]==player:
			pygame.draw.line(window,winning_color,((c*200)+100,10),((c*200)+100,HEIGHT-10),10)
			return True

	# +ve diagonal
	if board[0][0]== player and board[1][1]== player and board[2][2]==player:
		pygame.draw.line(window,winning_color,(10,10),(590,590),10)
		return True
	# -ve diagonal
	if board[2][0]== player and board[1][1]== player and board[0][2]==player:
		#print(announcement)
		pygame.draw.line(window,winning_color,(590,10),(10,590),10)
		return True

board=np.zeros((ROWS,COLUMNS))

game_over=False

Turn =0


pygame.init()
window=pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic Tac Toe")
window.fill(WHITE)
draw_lines()
pygame.display.update()
pygame.time.wait(2000)


while not game_over:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			print(event.pos)
			if Turn %2==0: #Even
				#Player 1
				# row=int(input("Player 1: Choose row number(0-2): "))
				# col=int(input("Player 1: Choose col number(0-2): "))
				row=math.floor(event.pos[1]/200)
				col=math.floor(event.pos[0]/200)
				if is_valid_mark(row,col):
					mark(row,col,1)
					if is_winning_move(1):
						game_over=True
				else:
					Turn-=1
			else:  #Odd
				#Player2
				# row=int(input("Player 2: Choose row number(0-2): "))
				# col=int(input("Player 2: Choose col number(0-2): "))
				row=math.floor(event.pos[1]/200)
				col=math.floor(event.pos[0]/200)
				if is_valid_mark(row,col):
					mark(row,col,2)
					if is_winning_move(2):
						game_over=True
				else:
					Turn-=1
			Turn+=1

			print(board)
			draw_board()

	if is_board_full():
		game_over=True

	if game_over==True:
		print("Game Over")
		pygame.time.wait(2000) #Delay of 2000 ms
		board.fill(0) #Board rsest conditions
		window.fill(WHITE)
		draw_lines()
		draw_board()
		game_over=False
		pygame.display.update()
