import math
from GLOBALS import *
from board import draw_board
from game_logic import *
from ai import ai_answer


def loop(GAME_DIFFICULTY):
    board = create_board()
    game_over = False
    tmp = first_to_play()
    human_color = tmp[0][0]
    human_piece = tmp[0][1]
    ai_color = tmp[1][0]
    ai_piece = tmp[1][1]

    turn = "HUMAN" if human_piece == 1 else "AI"
    posx = 4 + RADIUS

    # hotfix to draw the first dropped piece if the first to play is the AI
    if turn == "AI":
        mousepos = pygame.mouse.get_pos()
        pygame.mouse.set_pos(mousepos[0] + 1, mousepos[1])
        

    # set screen title
    pygame.display.set_caption("Connect 4")

    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)

    label = myfont.render("", 1, human_color)
    # creating buttons
    button_restart = Button(10, 10, pygame.image.load(
        "assets/button_restart.png"), 1.2)
    button_exit = Button(450, 10, pygame.image.load(
        "assets/button_exit.png"), 1.2)
    while not game_over:
        draw_board(board)

        # buttons logic
        if button_restart.draw(screen):
            label = myfont.render("", 1, human_color)
            board = create_board()
            game_over = False
            tmp = first_to_play()
            human_color = tmp[0][0]
            human_piece = tmp[0][1]
            ai_color = tmp[1][0]
            ai_piece = tmp[1][1]
            turn = "HUMAN" if human_piece == 1 else "AI"
            posx = 4 + RADIUS

            # hotfix to draw the first dropped piece if the first to play is the AI
            if turn == "AI":
                mousepos = pygame.mouse.get_pos()
                pygame.mouse.set_pos(mousepos[0] + 1, mousepos[1])

        for event in pygame.event.get():

            # check if exit button is clicked
            if button_exit.draw(screen) or event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(
                    screen, BLUE, (0, SQUARESIZE, width, SQUARESIZE), 4)
                pygame.draw.rect(
                    screen, WHITE, (4, SQUARESIZE + 4,
                                    width - 8, SQUARESIZE - 8)
                )
                if event.pos[0] < 4 + RADIUS:
                    posx = 4 + RADIUS
                elif event.pos[0] > width - (4 + RADIUS):
                    posx = width - (4 + RADIUS)
                else:
                    posx = event.pos[0]

            pygame.draw.circle(
                screen, human_color, (posx, int(3 * SQUARESIZE / 2)), RADIUS)
            pygame.display.update()
            if turn == "HUMAN":

                if event.type == pygame.MOUSEBUTTONDOWN and event.pos[1] > 100:
                    pygame.draw.rect(
                        screen, BLUE, (0, SQUARESIZE, width, SQUARESIZE), 4)

                    # Ask for Player Input
                    posx = event.pos[0]
                    posy = event.pos[1]
                    col = int(math.floor(posx / SQUARESIZE))
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, human_piece)

                        # hotfix to display the next circle
                        pygame.mouse.set_pos(posx + 1, posy)

                        # check if move lead to a win
                        if winning_move(board, human_piece):
                            label = myfont.render("YOU WON", 1, human_color)
                            game_over = True

                        # check if move lead to a draw
                        if not winning_move(board, human_piece) and np.all(board):
                            label = myfont.render("DRAW", 1, (0, 0, 0))
                            game_over = True

                        # change turn
                        turn = "AI"

                    # don't change turn if piece dropped in invalid col
                    else:
                        turn = "HUMAN"
                        pygame.mouse.set_pos(posx + 1, posy)
            # AI turn
            elif turn == "AI" and not game_over:
                col = ai_answer(board, ai_piece, human_piece, GAME_DIFFICULTY)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, ai_piece)
                # check if move lead to a win
                if winning_move(board, ai_piece):
                    label = myfont.render("YOU LOST", 1, ai_color)
                    game_over = True

                # check if move lead to a draw
                if not winning_move(board, ai_piece) and np.all(board):
                    label = myfont.render("DRAW", 1, (0, 0, 0))
                    game_over = True

                turn = "HUMAN"
    while game_over:
        # buttons logic
        button_exit.draw(screen)
        if button_restart.draw(screen):
            label = myfont.render("", 1, human_color)
            board = create_board()
            game_over = False
            tmp = first_to_play()
            human_color = tmp[0][0]
            human_piece = tmp[0][1]
            ai_color = tmp[1][0]
            ai_piece = tmp[1][1]
            turn = "HUMAN" if human_piece == 1 else "AI"
            posx = 4 + RADIUS
            loop(GAME_DIFFICULTY)

        for event in pygame.event.get():
            if button_exit.draw(screen) or event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(label, (190, 115))
        pygame.display.update()
        draw_board(board)
