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

def visual_feedback(board, grid_sq_size):
    draw_x = 1
    draw_y = 1
    grid_size_x = (len(board[0])) * grid_sq_size
    grid_size_y = (len(board)) * grid_sq_size
    grid_x = 0
    grid_y = 0
    grid_color = sdl2.ext.Color(0, 0, 0)
    
    # draw grid
    for row in range(len(board) + 1):
        sdl2.ext.line(window_surface, grid_color, (0, grid_y, grid_size_x, grid_y))
        grid_y += grid_sq_size
    
    for column in range(len(board[0]) + 1): 
        sdl2.ext.line(window_surface, grid_color, (grid_x, 0, grid_x, grid_size_y))
        grid_x += grid_sq_size
              
    # draw crosses or circles (actually squares) for each player
    for row in range(0,len(board)):
        for column in range(0,len(board[0])):
            if board[row][column] == 'X':
                draw_x = int(column) * grid_sq_size + 2
                draw_y = int(row) * grid_sq_size + 2
                draw_cross(draw_x, draw_y)
            elif board[row][column] == 'O':
                draw_x = int(column) * grid_sq_size + 2
                draw_y = int(row) * grid_sq_size + 2
                draw_square(draw_x, draw_y)
    window.refresh()
