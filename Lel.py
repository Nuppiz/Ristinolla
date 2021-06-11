#known issues: "Already in use!" loops forever (!), AI is... confused

# import functionality for random integer
from random import randint

# creates a board with custom width and length
def init_board(board, char):
	min_value = 5
	max_value = 20
	
	# take width
	while True:
		try:
			board_width = int(input("Enter board width (" + str(min_value) + "-" + str(max_value) +"):"))
		except ValueError:
			print ("Please enter a number.")
			continue
		if not (board_width >= min_value and board_width <= max_value):
			print ("Please enter a number between " + str(min_value) + " and " + str(max_value))
			continue
		else:
			break
		
	# take height
	while True:
		try:
			board_height = int(input("Enter board height (" + str(min_value) + "-" + str(max_value) +"):"))
		except ValueError:
			print ("Please enter a number.")
			continue
		if not (board_height >= min_value and board_height <= max_value):
			print ("Please enter a number between " + str(min_value) + " and " + str(max_value))
			continue
		else:
			break
		
	# create board
	for row in range(board_height):
		board.append([char] * (board_width))

# splits the cells into rows
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
# try-excepts to make sure player enters a number and not some other character
	# column first
	while True:	
		try:
			player_col = int(input("Enter Column: "))-1
		except ValueError:
			print ("Please enter a valid number.")
			continue
		#checks that player enters a number within the range of the board
		if not ((player_col >= 0 and player_col <= len(board[0])-1)):
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
		if not ((player_row >= 0 and player_row <= len(board)-1)):
			print ("Please enter a valid number.")
			continue
		else:
			break
	
	# checks if the selected cell is already used up
	while True:
		if not board[player_row][player_col] == "-":
			print ("Already in use!")
			continue
	
	# if all conditions are met, cell is filled with an X
		else:
			board[player_row][player_col] = "X"
			break

# rudimentary AI
def ai_input(board): 
	attempts = 0
	ai_max = getMax(board, 'O')
	while True:
		# randint to generate a random pair of coordinates
		ai_y = randint(0, len(board) - 1)
		ai_x = randint(0, len(board[0]) - 1)
		# checks that the cell is empty, if not, try again with new coords
		if board[ai_y][ai_x] != "-":
			continue
		else:
			board[ai_y][ai_x] = "O"
			attempts += 1
		# AI functionality that prioritizes going for the longest straight rather than just a random cell, attempt limit to prevent an infinite loop
		if getMax(board, 'O') > ai_max or attempts >= 100:
			break
		else:
			board[ai_y][ai_x] = "-"

# functions to check each row and column for consecutive characters (X or O)
def check_rows(board, character):
	max_score = 0
	for row in range(0,len(board)):
		score = 0
		for column in range(0,len(board[0])):
			if board[row][column] == character:
				score +=1
				if score > max_score:
					max_score = score
			else:
				score = 0
	return max_score

def check_columns(board, character):
	max_score = 0
	for column in range(0,len(board[0])):
		score = 0
		for row in range(0,len(board)):
			if board[row][column] == character:
				score +=1
				if score > max_score:
					max_score = score
			else:
				score = 0
	return max_score

# checks if either player has the required score
def score_checker(board, character):
	if check_rows(board, character) == len(board[0])-1 or check_columns(board, character) == len(board)-1:
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

# game initialization function and exit text	
def main():
	game_board = []
	init_board(game_board, "-")
	print ("Welcome to Tic-Tack-Toes")
	print_board(game_board)
	game_loop(game_board)
	print ("Fuck You xD")
			
# execution actually begins here
main()