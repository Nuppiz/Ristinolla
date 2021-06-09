#import functionality for random integer
from random import randint

# creates a 25-cell board, MODIFY at some point so user can decide size
def init_board(board, char):
	for square in range(5):
		board.append([char] * 5)

# splits the 25 cells into even rows
def print_board(board):
	for row in board:
		print (" ".join(row))

# used by AI to check for longest current straight
def getMax(board, character):
	max_rows = check_rows(board, character)
	max_cols = check_columns (board, character)
	if max_rows > max_cols:
		return max_rows
	else:
		return max_cols

# while-loop function for player's turn
def player_input(board):
	while True:
		#try-excepts to make sure player enters a number and not some other character, MODIFY for board size
		try:
			player_row = int(input("Enter Row (1-5): "))-1
		except ValueError:
			print ("Please enter a valid number.")
			continue
		
		try:
			player_col = int(input("Enter Column (1-5): "))-1
		except ValueError:		
			print ("Please enter a valid number.")
			continue
		
		#checks that player enters a number within the range of the board, MODIFY for board size
		if not ((player_row >= 0 and player_row <= 4) and (player_col >= 0 and player_col <= 4)):
			print ("Please enter a valid number (1-5).")
			continue
		#checks if the selected cell is already used up
		elif board[player_row][player_col] != "-":
			print ("Already in use!")
			continue
		#if all conditions are met, cell is filled with an X
		else:
			board[player_row][player_col] = "X"
			break

# rudimentary AI, takes a random cell, checks if it's in use and then tries to go for the currently longest straight
def ai_input(board): 
	attempts = 0
	ai_max = getMax(board, 'O')
	while True:
		ai_y = randint(0, len(board) - 1)
		ai_x = randint(0, len(board[0]) - 1)
		if board[ai_y][ai_x] != "-":
			continue
		else:
			board[ai_y][ai_x] = "O"
			attempts += 1
		if getMax(board, 'O') > ai_max or attempts >= 100:
			break
		else:
			board[ai_y][ai_x] = "-"

# functions to check each row and column for consecutive characters (X or O), MODIFY for board size
def check_rows(board, character):
	max_score = 0
	for row in range(0,5):
		score = 0
		for column in range(0,5):
			if board[row][column] == character:
				score +=1
				if score > max_score:
					max_score = score
			else:
				score = 0
	return max_score

def check_columns(board, character):
	max_score = 0
	for column in range(0,5):
		score = 0
		for row in range(0,5):
			if board[row][column] == character:
				score +=1
				if score > max_score:
					max_score = score
			else:
				score = 0
	return max_score

# checks if either player has the required score, MODIFY for board size
def score_checker(board, character):
	if check_rows(board, character) == 4 or check_columns(board, character) == 4:
		return 1

# helper function to count the amount of empty cells left on the board
def count_chars(char, board):
	count = 0
	for row in board:
		count += row.count(char)
	return count
	
# if no empty cells are left and neither player has the required score, game ends in a draw
def draw_check(board):
	if count_chars('-', board) == 0:
		print ("Board full, it's a draw!")
		return 1
	else:
		return 0

# function loop to keep the game going, checks after each turn for score and possible draw situation
def game_loop(board):
	while True:
		print ("Your turn")
		player_input(board)
		print_board(board)
		if score_checker(board, 'X') == 1:
			print ("You win!")
			break
		if draw_check(board) == 1:
			break
			
		print ("AI's turn")
		ai_input(board)
		print_board(board)
		if score_checker(board, 'O') == 1:
			print ("You lose!")
			break
		if draw_check(board) == 1:
			break

#game initialization function and exit text	
def main():
	game_board = []
	init_board(game_board, "-") # MODIFY init_board() function to change board size
	print ("Welcome to Tic-Tack-Toes")
	print_board(game_board)
	game_loop(game_board)
	print ("Fuck You xD")
			
# execution actually begins here
main()