# functions relevant for controlling graphics output

import sdl2.ext

# initialize  SDL2 objects & variables
sdl2.ext.init()
width = 640
height = 480
window = sdl2.ext.Window("Hello World!", size=(width, height))      
renderer = sdl2.ext.Renderer(window)

def draw_rectangle(renderer, x, y, w, h, r ,g ,b):
    for y_pixel in range(h):
        for x_pixel in range(w):
            renderer.draw_point([x+x_pixel,y+y_pixel], sdl2.ext.Color(r, g, b))

def draw_cross(renderer, x, y):
    cross_size_x = 40
    cross_size_y = 6
    cross_col_r = 255
    cross_col_g = 0
    cross_col_b = 0
    draw_rectangle(renderer, x, y+17, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
    draw_rectangle(renderer, x+17, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)
    
def draw_square(renderer, x, y):
    cross_size_x = 40
    cross_size_y = 6
    cross_col_r = 255
    cross_col_g = 0
    cross_col_b = 0
    draw_rectangle(renderer, x, y, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
    draw_rectangle(renderer, x, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)
    draw_rectangle(renderer, x, y+34, cross_size_x, cross_size_y, cross_col_r, cross_col_g, cross_col_b)
    draw_rectangle(renderer, x+34, y, cross_size_y, cross_size_x, cross_col_r, cross_col_g, cross_col_b)

def visual_feedback(board, renderer):
    draw_x = 0
    draw_y = 0
    for row in range(0,len(board)):
        for column in range(0,len(board[0])):
            if board[row][column] == 'X':
                draw_x = int(column)*42
                draw_y = int(row)*42
                draw_cross(renderer, draw_x, draw_y)
            elif board[row][column] == 'O':
                draw_x = int(column)*42
                draw_y = int(row)*42
                draw_square(renderer, draw_x, draw_y)
    renderer.present()