# functions needed to create a board and check scores

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
        
    # define max value for score based on shortest board axis
    min_points = 3
    
    if board_width < board_height:
        max_points = board_width
    else:
        max_points = board_height
        
    # take required score
    while True:
        try:
            win_score = int(input("Enter required score to win (" + str(min_points) + "-" + str(max_points) +"):"))
        except ValueError:
            print ("Please enter a number.")
            continue
        if not (win_score >= min_points and win_score <= max_points):
            print ("Please enter a number between " + str(min_points) + " and " + str(max_points))
            continue
        else:
            return win_score

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
def score_checker(board, character, win_score):
    if check_rows(board, character) >= win_score or check_columns(board, character) >= win_score:
      print(character + " wins!")
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