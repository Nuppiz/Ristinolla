# functions needed for the AI

# import functionality for random integer
from random import randint

# import getMax function from Board.py
import Board

def ai_try_win(board, difficulty, win_score):
  attempts = 0
  max_attempts = len(board[0]) * len(board) * difficulty

  while True:
    ai_y = randint(0, len(board) - 1)
    ai_x = randint(0, len(board[0]) - 1)

    if board[ai_y][ai_x] != "-":
      continue
    else:
      board[ai_y][ai_x] = "O"
      attempts += 1

    if Board.getMax(board, 'O') >= win_score:
      return True
    elif attempts >= max_attempts:
      return False
    else:
      board[ai_y][ai_x] = "-"

def ai_prevent_player_win(board, difficulty, win_score):
  attempts = 0
  max_attempts = len(board[0]) * len(board) * difficulty

  while True:
    ai_y = randint(0, len(board) - 1)
    ai_x = randint(0, len(board[0]) - 1)

    if board[ai_y][ai_x] != "-": # checks that the cell is empty, if not, try again with new coords
      continue
    else:
      board[ai_y][ai_x] = "X" # put a temporary X in the chosen cell
      attempts += 1
      
    # if that X would result in a player win, switch it to O to prevent it
    if Board.getMax(board, 'X') >= win_score:
      board[ai_y][ai_x] = "O"
      return True
    # if out of attempts, end this function
    elif attempts >= max_attempts:
      return False
    # else erase the temporary X and try again
    else:
      board[ai_y][ai_x] = "-"
  
def ai_think(board, difficulty, ai_max):
    attempts = 0
    max_attempts = len(board[0]) * len(board) * difficulty # determines max attempts by board size and difficulty
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
        if Board.getMax(board, 'O') > ai_max or attempts >= max_attempts:
            break
        else:
            board[ai_y][ai_x] = "-"
            
def ai_input(board, difficulty, win_score):
    ai_max = Board.getMax(board, 'O')
    player_max = Board.getMax(board, 'X')
    success = False
    
    # check if almost winning, and try to place last O
    if ai_max == win_score-1:
          success = ai_try_win(board, difficulty, win_score)
    
    # check if player is almost winning
    if not success and player_max == win_score-1:
          success = ai_prevent_player_win(board, difficulty, win_score)

    # finally, just try to add an O somewhere
    if not success:
          ai_think(board, difficulty, ai_max)