
# Code for chapter 02 - Exceptions in Python

# WITH BUGS!
# This code contains at least 9 defects.
# Try to fix them all based on the error messages.

import pygame #Error 1 syntax imprt <- import
#Error 9 missing Surface
from pygame import image, Rect, Surface #Error 5 Syntax imagge <- image


TILE_POSITIONS = [ #Error 2 no closing bracket
    ('#', 0, 0),  # wall
    (' ', 0, 1),  # floor Error 4 was missing EOL comma
    ('.', 2, 0),  # dot
    # missing key value '*'
    ('*', 3, 0), # player
]
SIZE = 32

#image = '../images/tiles.xpm'

def get_tile_rect(x,y):
    """
    Converts tile indices to a pygame.RECT
    :param x:
    :param y:
    :return:
    """
    return  Rect(x*SIZE, y*SIZE, SIZE, SIZE)
def load_tiles(): #Error 3 EOL colon was missing
    """
    Load tiles from an image file into a dictionary.
    Returns a tuple of (image, tile_dict)
    """
    tiles = {}
    tile_img = image.load('../images/tiles.xpm') #Error 6 Syntax loaad<-load, tiless<-tiles file path
    for symbol, x, y in TILE_POSITIONS: #Error 7 syntax TILEPOSITIONS<-TILE_POSITIONS
        #rect = Rect(x*SIZE, y*SIZE, SIZE, SIZE) #Error 8 Too many arguements needed function call
        tiles[symbol] = get_tile_rect(x,y) #need to call new function written for omitted line above
    return tile_img, tiles


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    m = Surface((96, 32))
    m.blit(tile_img, get_tile_rect(0, 0), tiles['#'])
    m.blit(tile_img, get_tile_rect(1, 0), tiles[' '])
    m.blit(tile_img, get_tile_rect(2, 0), tiles['*'])
    image.save(m, 'tile_combo.png')


# ----------------------------

# Optional exercise:
# make the print statement below work
# by modifying the class
# so that it prints the char attribute


class Tile:

    def __init__(self, achar, x, y):
        char = achar

t = Tile('#', 0, 0)

#print(t.char)
