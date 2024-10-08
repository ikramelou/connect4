import random
from GLOBALS import COLUMN_COUNT, ROW_COUNT
from game_logic import is_valid_location, get_next_open_row, winning_move, drop_piece
import math


def easy(board):
    c = random.randint(0, COLUMN_COUNT - 1)
    while not is_valid_location(board, c):
        c = random.randint(0, COLUMN_COUNT - 1)
    return c


def ai_answer(board, human_piece, ai_piece, GAME_DIFFICULTY):
    if GAME_DIFFICULTY == 0:
        return easy(board)
    elif GAME_DIFFICULTY == 1:
        return minimax(board, 1, -math.inf, math.inf, True,human_piece, ai_piece)[0]
    elif GAME_DIFFICULTY == 2:
        return minimax(board, 5, -math.inf, math.inf, True,human_piece, ai_piece)[0]


def evaluate_window(window, piece, human_piece, ai_piece):
	score = 0
	opp_piece = human_piece
	if piece == human_piece:
		opp_piece = ai_piece

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(0) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(0) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(0) == 1:
		score -= 4

	return score

def score_position(board, piece, human_piece, ai_piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_COUNT-3):
			window = row_array[c:c+4]
			score += evaluate_window(window, piece, human_piece, ai_piece)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_COUNT-3):
			window = col_array[r:r+4]
			score += evaluate_window(window, piece, human_piece, ai_piece)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+i][c+i] for i in range(4)]
			score += evaluate_window(window, piece, human_piece, ai_piece)

	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+3-i][c+i] for i in range(4)]
			score += evaluate_window(window, piece, human_piece, ai_piece)

	return score

def is_terminal_node(board, human_piece, ai_piece):
	return winning_move(board, human_piece) or winning_move(board, ai_piece) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer, human_piece, ai_piece):
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board, human_piece, ai_piece)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(board, ai_piece):
				return (None, 100000000000000)
			elif winning_move(board, human_piece):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(board, ai_piece, human_piece, ai_piece))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, ai_piece)
			new_score = minimax(b_copy, depth-1, alpha, beta, False, human_piece, ai_piece)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, human_piece)
			new_score = minimax(b_copy, depth-1, alpha, beta, True, human_piece, ai_piece)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value

def get_valid_locations(board):
	valid_locations = []
	for col in range(COLUMN_COUNT):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations

