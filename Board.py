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
    max_cols = check_columns(board, character)
    max_diag = check_diagonal(board, character)
    max_straight = max(max_rows, max_cols, max_diag)
    
    return max_straight
    
def getMax_open(board, character, win_score):
    max_rows = check_rows_open(board, character, win_score)
    max_cols = check_columns_open(board, character, win_score)
    max_diag = check_diag_open(board, character, win_score)
    max_straight = max(max_rows, max_cols, max_diag)
    
    return max_straight
    
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

def check_columns_open(board, character, win_score):
    final_score = 0
    
    for column in range(0,len(board[0])):
        score = 0
        max_score = 0
        open_len = 0
        
        for row in range(0,len(board)):
            if board[row][column] == character:
                score +=1
                open_len +=1
                if score > max_score:
                    max_score = score
            elif board[row][column] == "-":
                score = 0
                open_len +=1
            else:
                score = 0
                open_len = 0
                max_score = 0
            
            if open_len >= win_score and score > max_score:
                max_score = score
                
            if open_len >= win_score and max_score > final_score:
                final_score = max_score 
                
    return final_score

def check_rows_open(board, character, win_score):
    final_score = 0
    
    for row in range(0,len(board)):
        score = 0
        max_score = 0
        open_len = 0
        
        for column in range(0,len(board[0])):
            if board[row][column] == character:
                score +=1
                open_len +=1
                if score > max_score:
                    max_score = score
            elif board[row][column] == "-":
                score = 0
                open_len +=1
            else:
                score = 0
                open_len = 0
                max_score = 0
            
            if open_len >= win_score and score > max_score:
                max_score = score
                
            if open_len >= win_score and max_score > final_score:
                final_score = max_score 
                
    return final_score

def check_diagonal(board, character):
    max_down = check_downwards(board, character)
    max_up = check_upwards(board, character)
    if max_down > max_up:
        return max_down
    else:
        return max_up
    
def check_diag_open(board, character, win_score):
    max_down = check_down_open(board, character, win_score)
    max_up = check_up_open(board, character, win_score)
    if max_down > max_up:
        return max_down
    else:
        return max_up
    
def check_downwards(board, character):
    
    max_score = 0
    score = 0
    
    # upper triangle
    diagonal = 0 # horizontal or vertical starting point
    x = 0
    y = 0
    
    while True:
        # break function after the starting point has reached the last horizontal cell
        if diagonal >= len(board[0]):
            break
        
        # increase score if character found in square
        if board[y][x] == character:
            score += 1
            if score > max_score:
                max_score = score
        # otherwise combo break, 0
        else:
            score = 0
        
        # move diagonally downwards
        x += 1
        y += 1
        
        # if reached the end of the row, reset row and move horizontal start point by 1
        if x >= len(board[0]):
            diagonal += 1
            y = 0
            x = diagonal
            score = 0            
            continue
        # same as above but with columns   
        elif y >= len(board):
            diagonal += 1
            y = 0
            x = diagonal   
            score = 0        
            continue
        
    # lower triangle
    diagonal = 1
    x = 0
    y = 1
    
    while True:
        
        if diagonal >= len(board):
            break
        
        # increase score if character found in square
        if board[y][x] == character:
            score += 1
            if score > max_score:
                max_score = score
        # otherwise combo break, 0
        else:
            score = 0

        x += 1
        y += 1
        
        if x >= len(board[0]):
            diagonal += 1
            y = diagonal
            x = 0            
            score = 0
            continue
            
        elif y >= len(board):
            diagonal += 1
            y = diagonal
            x = 0       
            score = 0    
            continue
        
    return max_score

def check_upwards(board, character):
    
    max_score = 0
    score = 0
    
    # lower triangle
    diagonal = 0 # horizontal or vertical starting point
    x = 0
    y = len(board)-1
    
    while True:
        # break function after the starting point has reached the last horizontal cell
        if diagonal >= len(board[0]):
            break
        
        # increase score if character found in square
        if board[y][x] == character:
            score += 1
            if score > max_score:
                max_score = score
        # otherwise combo break, 0
        else:
            score = 0
        
        # move diagonally upwards
        x += 1
        y -= 1
        
        # if reached the end of the row, reset row and move horizontal start point by 1
        if x >= len(board[0]):
            diagonal += 1
            y = len(board)-1
            x = diagonal     
            score = 0       
            continue
        # same as above but with columns   
        elif y < 0:
            diagonal += 1
            y = len(board)-1
            x = diagonal    
            score = 0       
            continue
        
    # upper triangle
    diagonal = len(board)-1
    number = 1
    x = 0
    y = len(board)-2
    
    while True:
        
        if diagonal < 0:
            break
        
        # increase score if character found in square
        if board[y][x] == character:
            score += 1
            if score > max_score:
                max_score = score
        # otherwise combo break, 0
        else:
            score = 0

        x += 1
        y -= 1
        
        if x >= len(board[0]):
            diagonal -= 1
            y = diagonal
            x = 0   
            score = 0       
            continue
            
        elif y < 0:
            diagonal -= 1
            y = diagonal
            x = 0   
            score = 0    
            continue
        
    return max_score

def check_down_open(board, character, win_score):
    
    final_score = 0
    
    score = 0
    open_len = 0
    max_score = 0
    
    # upper triangle
    diagonal = 0 # horizontal or vertical starting point
    x = 0
    y = 0
    
    while True:        
        # break function after the starting point has reached the last horizontal cell
        if diagonal >= len(board[0]):
            break
        
        # increase score if character found in square
        if board[y][x] == character:
            score += 1
            open_len += 1
            if score > max_score:
                max_score = score
                
        elif board[y][x] == "-":
            score = 0
            open_len += 1
            
        # otherwise combo break, 0
        else:
            score = 0
            open_len = 0
            max_score = 0
            
        if open_len >= win_score:
            if score > max_score:
                max_score = score      
            if max_score > final_score:
                final_score = max_score
        
        # move diagonally downwards
        x += 1
        y += 1
        
        # if reached the end of the row, reset row and move horizontal start point by 1
        if x >= len(board[0]):
            diagonal += 1
            y = 0
            x = diagonal
            score = 0
            open_len = 0    
            continue
        # same as above but with columns   
        elif y >= len(board):
            diagonal += 1
            y = 0
            x = diagonal   
            score = 0
            open_len = 0   
            continue
        
    # lower triangle
    diagonal = 1
    x = 0
    y = 1
    
    while True:
        
        if diagonal >= len(board):
            break
        
        # increase score if character found in square
        if board[y][x] == character:
            score += 1
            open_len += 1
            if score > max_score:
                max_score = score
                
        elif board[y][x] == "-":
            score = 0
            open_len += 1
            
        # otherwise combo break, 0
        else:
            score = 0
            open_len = 0
            max_score = 0
            
        if open_len >= win_score:
            if score > max_score:
                max_score = score      
            if max_score > final_score:
                final_score = max_score
        
        x += 1
        y += 1
        
        if x >= len(board[0]):
            diagonal += 1
            y = diagonal
            x = 0            
            score = 0
            open_len = 0
            continue
            
        elif y >= len(board):
            diagonal += 1
            y = diagonal
            x = 0       
            score = 0
            open_len = 0
            continue
        
    return final_score

def check_up_open(board, character, win_score):
    
    final_score = 0
    
    score = 0
    open_len = 0
    max_score = 0
    
    # lower triangle
    diagonal = 0 # horizontal or vertical starting point
    x = 0
    y = len(board)-1
    
    while True:
        # break function after the starting point has reached the last horizontal cell
        if diagonal >= len(board[0]):
            break
        
        # increase score if character found in square
        if board[y][x] == character:
            score += 1
            open_len += 1
            if score > max_score:
                max_score = score
                
        elif board[y][x] == "-":
            score = 0
            open_len += 1
            
        # otherwise combo break, 0
        else:
            score = 0
            open_len = 0
            max_score = 0
            
        if open_len >= win_score:
            if score > max_score:
                max_score = score      
            if max_score > final_score:
                final_score = max_score
        
        # move diagonally upwards
        x += 1
        y -= 1
        
        # if reached the end of the row, reset row and move horizontal start point by 1
        if x >= len(board[0]):
            diagonal += 1
            y = len(board)-1
            x = diagonal     
            score = 0
            open_len = 0
            continue
        # same as above but with columns   
        elif y < 0:
            diagonal += 1
            y = len(board)-1
            x = diagonal    
            score = 0
            open_len = 0
            continue
        
    # upper triangle
    diagonal = len(board)-1
    number = 1
    x = 0
    y = len(board)-2
    
    while True:
        
        if diagonal < 0:
            break
        
        # increase score if character found in square
        if board[y][x] == character:
            score += 1
            open_len += 1
            if score > max_score:
                max_score = score
                
        elif board[y][x] == "-":
            score = 0
            open_len += 1
            
        # otherwise combo break, 0
        else:
            score = 0
            open_len = 0
            max_score = 0
            
        if open_len >= win_score:
            if score > max_score:
                max_score = score      
            if max_score > final_score:
                final_score = max_score

        x += 1
        y -= 1
        
        if x >= len(board[0]):
            diagonal -= 1
            y = diagonal
            x = 0   
            score = 0
            open_len = 0
            continue
            
        elif y < 0:
            diagonal -= 1
            y = diagonal
            x = 0   
            score = 0
            open_len = 0
            continue
        
    return max_score
    
# checks if either player has the required score
def score_checker(board, character, win_score):
    if check_rows(board, character) >= win_score or check_columns(board, character) >= win_score or check_diagonal(board, character) >= win_score:
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