from random import randint

board = []

def init_board(char):
	for square in range(5):
		board.append([char] * 5)

def print_board(board):
	for row in board:
		print (" ".join(row))

def getMax(character):
	max_rows = check_rows(board, character)
	max_cols = check_columns (board, character)
	if max_rows > max_cols:
		return max_rows
	else:
		return max_cols

def player_input(board):
	while True:
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
		
		if not ((player_row >= 0 and player_row <= 4) and (player_col >= 0 and player_col <= 4)):
			print ("Please enter a valid number (1-5).")
			continue
		elif board[player_row][player_col] != "-":
			print ("Already in use!")
			continue
		else:
			board[player_row][player_col] = "X"
			break
		
def ai_input(board):
	attempts = 0
	ai_max = getMax('O')
	while True:
		ai_y = randint(0, len(board) - 1)
		ai_x = randint(0, len(board[0]) - 1)
		if board[ai_y][ai_x] != "-":
			continue
		else:
			board[ai_y][ai_x] = "O"
			attempts += 1
		if getMax('O') > ai_max or attempts >= 100:
			break
		else:
			board[ai_y][ai_x] = "-"

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

def score_checker(board, character):
	if check_rows(board, character) == 4 or check_columns(board, character) == 4:
		return 1
	
def count_chars(char, board):
	count = 0
	for row in board:
		count += row.count(char)
	return count
	
def draw_check():
	if count_chars('-', board) == 0:
		print ("Board full, it's a draw!")
		return 1
	else:
		return 0

def game_loop(board):
	while True:
		print ("Your turn")
		player_input(board)
		print_board(board)
		if score_checker(board, 'X') == 1:
			print ("You win!")
			break
		if draw_check() == 1:
			break
			
		print ("AI's turn")
		ai_input(board)
		print_board(board)
		if score_checker(board, 'O') == 1:
			print ("You lose!")
			break
		if draw_check() == 1:
			break
	
def main():
	board = []
	init_board(board) # modify init_board() function to 
	print ("Welcome to Tic-Tack-Toes")
	print_board(board)
	game_loop(board)
	print ("Fuck You xD")
			
# execution actually begins here
main()
