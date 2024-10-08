import pygame
import sys

from button import Button

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7


# define square size
SQUARESIZE = 100

# define circle radius
RADIUS = int(SQUARESIZE / 2 - 5)

# define width and height of board
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 2) * SQUARESIZE

# initalize pygame, screen
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
