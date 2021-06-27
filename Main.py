# import time.sleep for AI "delay"
from time import sleep

# import AI functionalities from another file
import Ai

# import board structure and score checks from another file
import Board

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

# function loop to keep the game going, checks after each turn for score and possible draw situation
def game_loop(board, difficulty, win_score):
	while True:
		print ("Your turn")
		player_input(board)
		Board.print_board(board)
		if Board.score_checker(board, 'X', win_score) == 1:
			print ("You win!")
			break
		if Board.draw_check(board) == 1:
			break
			
		print ("AI's turn...")
		sleep(2) # 2-second delay to make it seem like the AI is "thinking"
		Ai.ai_input(board, difficulty, win_score)
		Board.print_board(board)
		if Board.score_checker(board, 'O', win_score) == 1:
			print ("You lose!")
			break
		if Board.draw_check(board) == 1:
			break

# game initialization function and exit text	
def main():
	game_board = []
	print ("Welcome to Tic-Tack-Toes")
	win_score = Board.init_board(game_board, "-")
	difficulty = diff_check() * 5 # defines difficulty variable which is sent to AI
	Board.print_board(game_board)
	game_loop(game_board, difficulty, win_score)
	print ("Game over man, game over!")
	new_game = input("Enter Y to play again, any other key to quit:")
	if new_game == "Y" or new_game == "y":
		main()
	else:
		quit()
			
# execution actually begins here
main()