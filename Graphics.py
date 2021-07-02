# functions relevant for controlling graphics output

import sdl2.ext
import math

# initialize  SDL2 objects & variables
sdl2.ext.init()
width = 640
height = 480
window = sdl2.ext.Window("Tic-Tac-Toes", size=(width, height))
window_surface = window.get_surface()
pixelthing = sdl2.ext.PixelView(window_surface)


def draw_rectangle(x,y,  w,h,  r,g,b):
    color = sdl2.ext.Color(r,g,b)
    sdl2.ext.fill(window_surface, color, (x,y,  w,h))
  
def draw_cross(x, y, grid_sq_size):
    #dimensions
    margin = grid_sq_size / 10
    cross_size_x = grid_sq_size - (2 * margin + 1)
    cross_size_y = cross_size_x / 8
    line_width_scale = 1 / 8
    empty_space_scale = (1 - line_width_scale) / 2

    #color
    cr_col_r = 255
    cr_col_g = 255
    cr_col_b = 255

    # horizontal line
    draw_rectangle(x + margin + 1,                              # start point x
                   y + grid_sq_size * empty_space_scale + 1,    # start point y
                   cross_size_x,                                # width
                   cross_size_y,                                # height
                   # color
                   cr_col_r, cr_col_g, cr_col_b)
                   
    # vertical line
    draw_rectangle(x + grid_sq_size * empty_space_scale + 1,    # start point x
                   y + margin + 1,                              # start point y
                   cross_size_y,                                # width
                   cross_size_x,                                # height
                   # color
                   cr_col_r, cr_col_g, cr_col_b)
    
def draw_square(x, y, grid_sq_size):
    # dimensions
    margin = grid_sq_size / 10
    cross_size_x = grid_sq_size - (2 * margin + 1)
    cross_size_y = cross_size_x / 8
    line_width_scale = 1 / 8
    empty_space_scale = 1 - line_width_scale
    
    # color
    cr_col_r = 255
    cr_col_g = 0
    cr_col_b = 0
    
    # top line
    draw_rectangle(x + margin + 1,    # start point x
                   y + margin + 1,    # start point y
                   cross_size_x,      # width
                   cross_size_y,      # height
                   # color
                   cr_col_r, cr_col_g, cr_col_b) 
             
    # left line
    draw_rectangle(x + margin + 1,    # start point x
                   y + margin + 1,    # start point y
                   cross_size_y,      # width
                   cross_size_x,      # height
                   # color
                   cr_col_r, cr_col_g, cr_col_b) 
    
    # bottom line
    draw_rectangle(x + margin + 1,                                    # start point x
                   y - margin + grid_sq_size * empty_space_scale + 1, # start point y
                   cross_size_x,                                      # width
                   cross_size_y,                                      # height
                   # color
                   cr_col_r, cr_col_g, cr_col_b) 
    
    # right line
    draw_rectangle(x - margin + grid_sq_size * empty_space_scale + 1, # start point x
                   y + margin + 1,                                    # start point y
                   cross_size_y,                                      # width
                   cross_size_x,                                      # height
                   # color
                   cr_col_r, cr_col_g, cr_col_b)
    
def draw_circle(x, y, grid_sq_size):
    margin = grid_sq_size / 10
    radius = int((grid_sq_size - margin) / 2)
    radius2 = int(radius / 4)
    x = x + grid_sq_size // 2
    y = y + grid_sq_size // 2
    
    # color
    ci_col_r = 255
    ci_col_g = 0
    ci_col_b = 0
    
    for y_pix in range (-radius, radius):
        for x_pix in range (-radius, radius):
            if math.sqrt(y_pix**2 + x_pix**2) < radius and math.sqrt(y_pix**2 + x_pix**2) > radius-radius2:
                pixelthing[y + y_pix] [x + x_pix] = sdl2.ext.Color(ci_col_r, ci_col_g, ci_col_b)

def visual_feedback(board, grid_sq_size):
    draw_x = 0
    draw_y = 0
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
              
    # draw crosses or circles for each player
    for row in range(0,len(board)):
        for column in range(0,len(board[0])):
            if board[row][column] == 'X':
                draw_x = int(column) * grid_sq_size
                draw_y = int(row) * grid_sq_size
                draw_cross(draw_x, draw_y, grid_sq_size)
            elif board[row][column] == 'O':
                draw_x = int(column) * grid_sq_size
                draw_y = int(row) * grid_sq_size
                draw_circle(draw_x, draw_y, grid_sq_size)
    window.refresh()
