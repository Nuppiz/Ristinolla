# functions relevant for controlling graphics output

import sdl2.ext

# initialize  SDL2 objects & variables
sdl2.ext.init()
width = 640
height = 480
window = sdl2.ext.Window("Tic-Tac-Toes", size=(width, height))
window_surface = window.get_surface()      

def draw_rectangle(x,y,  w,h,  r,g,b):
  color = sdl2.ext.Color(r,g,b)
  sdl2.ext.fill(window_surface, color, (x,y,  w,h))
  
def draw_cross(x, y):
    cross_size_x = 40
    cross_size_y = 6
    cross_col_r = 255
    cross_col_g = 255
    cross_col_b = 255
    draw_rectangle(x, y+17, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
    draw_rectangle(x+17, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)
    
def draw_square(x, y):
    cross_size_x = 40
    cross_size_y = 6
    cross_col_r = 255
    cross_col_g = 0
    cross_col_b = 0
    draw_rectangle(x, y, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
    draw_rectangle(x, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)
    draw_rectangle(x, y+34, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
    draw_rectangle(x+34, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)

def visual_feedback(board):
    draw_x = 0
    draw_y = 0
    for row in range(0,len(board)):
        for column in range(0,len(board[0])):
            if board[row][column] == 'X':
                draw_x = int(column)*42
                draw_y = int(row)*42
                draw_cross(draw_x, draw_y)
            elif board[row][column] == 'O':
                draw_x = int(column)*42
                draw_y = int(row)*42
                draw_square(draw_x, draw_y)
    window.refresh()
