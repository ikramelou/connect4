from game_logic import *
from GLOBALS import *


def draw_board(board):

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (0, SQUARESIZE, width, SQUARESIZE), 4)

    # drawing a blue rectangle with white cirles inside
    for c in range(COLUMN_COUNT):
        for r in range(1, ROW_COUNT + 1):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r *
                                            SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, WHITE, (int(
                c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    # drawing the red and yellow played circles
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(
                    c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(
                    c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
