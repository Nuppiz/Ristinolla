# import functionality for random integer
from random import randint

# import time.sleep for AI "delay"
from time import sleep

# import AI functionalities from another file
import Ai

# import board structure and score checks from another file
import Board

import sdl2.ext

# necessary checks for correct difficulty input
def diff_check():
	while True:
		try:
			diff_input = int(input("Enter AI difficulty (1-5):"))
		except ValueError:
			print ("Please enter a number.")
			continue
		if not (diff_input >= 1 and diff_input <= 5):
			print ("Please enter a number between 1 and 5.")
			continue
		else:
			return diff_input

# while-loop function for player's turn
def player_input(board):
# try-excepts to make sure player enters a number and not some other character
	# column first
	while True:	
		try:
			player_col = int(input("Enter Column: "))-1
		except ValueError:
			print ("Please enter a valid number.")
			continue
		#checks that player enters a number within the range of the board
		if not ((player_col >= 0 and player_col < len(board[0]))):
			print ("Please enter a valid number.")
			continue
		else:
			break
		
	# then row
	while True:	
		try:
			player_row = int(input("Enter Row: "))-1
		except ValueError:		
			print ("Please enter a valid number.")
			continue
		if not ((player_row >= 0 and player_row < len(board))):
			print ("Please enter a valid number.")
			continue
		else:
			break
	
	# checks if the selected cell is already used up
	if not board[player_row][player_col] == "-":
		print ("Already in use!")
		player_input(board)
	
	# if all conditions are met, cell is filled with an X
	else:
		board[player_row][player_col] = "X"
		
# generalized turn function
def turn(board, difficulty, win_score, character, renderer):
  # Prompt for input
  print(character + "'s turn")
  if character == "X":
    player_input(board)
  else:
  	sleep(2) # 2-second delay to make it seem like the AI is "thinking"
  	Ai.ai_input(board, difficulty, win_score)
  
  # Check for victory conditions, return 1 if game ends, 0 if not
  if Board.score_checker(board, character, win_score) == 1:
    return 1
  if Board.draw_check(board) == 1:
    return 1
  else:
    return 0

# function loop to keep the game going, checks after each turn for score and possible draw situation
def game_loop(board, difficulty, win_score, window, renderer):
  whose_turn = "X"

  while True:
    # Check for window events
    events = sdl2.ext.get_events()
    for event in events:
      if event.type == sdl2.SDL_QUIT:
        break
        
    # Display board & refresh window
    Board.print_board(board)
    visual_feedback(board, renderer)
    window.refresh()

    # Execute turn
    if turn(board, difficulty, win_score, whose_turn, renderer) == 1:
      break
    
    # Swap turn
    if whose_turn == "X":
      whose_turn = "O"
    else:
      whose_turn = "X"
  
  # Display board last time after game ends / while loop is over
  Board.print_board(board)
  visual_feedback(board, renderer)

# game initialization function and exit text	  
def main():
  # initialize  SDL2 objects & variables
  sdl2.ext.init()
  width = 640
  height = 480
  window = sdl2.ext.Window("Hello World!", size=(width, height))      
  renderer = sdl2.ext.Renderer(window)
  
  # configure game
  game_board = []
  print ("Welcome to Tic-Tack-Toes")
  win_score = Board.init_board(game_board, "-")
  difficulty = diff_check() * 5 # defines difficulty variable which is sent to AI

  # show window
  window.show()

  # begin the actual game
  game_loop(game_board, difficulty, win_score, window, renderer)
  
  # game over, quit/restart
  print ("Game over man, game over!")
  new_game = input("Enter Y to play again, any other key to quit:")
  if new_game == "Y" or new_game == "y":
    main()
  else:
    quit()

def draw_rectangle(renderer, x, y, w, h, r ,g ,b):
	for y_pixel in range(h):
		for x_pixel in range(w):
			renderer.draw_point([x+x_pixel,y+y_pixel], sdl2.ext.Color(r, g, b))

def draw_cross(renderer, x, y):
	cross_size_x = 40
	cross_size_y = 6
	cross_col_r = 255
	cross_col_g = 0
	cross_col_b = 0
	draw_rectangle(renderer, x, y+17, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
	draw_rectangle(renderer, x+17, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)
	
def draw_square(renderer, x, y):
	cross_size_x = 40
	cross_size_y = 6
	cross_col_r = 255
	cross_col_g = 0
	cross_col_b = 0
	draw_rectangle(renderer, x, y, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
	draw_rectangle(renderer, x, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)
	draw_rectangle(renderer, x, y+34, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
	draw_rectangle(renderer, x+34, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)

def visual_feedback(board, renderer):
	draw_x = 0
	draw_y = 0
	for row in range(0,len(board)):
		for column in range(0,len(board[0])):
			if board[row][column] == 'X':
				draw_x = int(column)*42
				draw_y = int(row)*42
				draw_cross(renderer, draw_x, draw_y)
			elif board[row][column] == 'O':
				draw_x = int(column)*42
				draw_y = int(row)*42
				draw_square(renderer, draw_x, draw_y)
	renderer.present()
	
# execution actually begins here
main()
