# import time.sleep for AI "delay"
from time import sleep

# import AI functionalities from another file
import Ai

# import board structure and score checks from another file
import Board

# import graphics from another file
import Graphics

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
def turn(board, difficulty, win_score, character):
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
def game_loop(board, difficulty, win_score):
  whose_turn = "X"

  while True:
    # Check for window events
    events = Graphics.sdl2.ext.get_events()
    for event in events:
      if event.type == Graphics.sdl2.SDL_QUIT:
        break
        
    # Display board
    Board.print_board(board)
    Graphics.visual_feedback(board)

    # Execute turn
    if turn(board, difficulty, win_score, whose_turn) == 1:
      break
    
    # Swap turn
    if whose_turn == "X":
      whose_turn = "O"
    else:
      whose_turn = "X"
  
  # Display board last time after game ends / while loop is over
  Board.print_board(board)
  Graphics.visual_feedback(board)

# game initialization function and exit text	  
def main():
  
  # configure game
  game_board = []
  print ("Welcome to Tic-Tack-Toes")
  win_score = Board.init_board(game_board, "-")
  difficulty = diff_check() * 5 # defines difficulty variable which is sent to AI
  
  # show window
  Graphics.window.show()
  color = Graphics.sdl2.ext.Color(0, 128, 0)
  Graphics.sdl2.ext.fill(Graphics.window_surface, color, (0, 0, Graphics.width, Graphics.height))
  color = Graphics.sdl2.ext.Color(0, 0, 0)
  Graphics.sdl2.ext.line(Graphics.window_surface, color, (0, 0, 100, 100))

  # begin the actual game
  game_loop(game_board, difficulty, win_score)
  
  # game over, quit/restart
  print ("Game over man, game over!")
  new_game = input("Enter Y to play again, any other key to quit:")
  if new_game == "Y" or new_game == "y":
    main()
  else:
    quit()
	
# execution actually begins here
main()
