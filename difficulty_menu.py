from GLOBALS import *


def draw_difficulty_menu():

    # set screen title
    pygame.display.set_caption("Choose difficulty")

    # set screen image
    difficulty_image = pygame.image.load("assets/difficulty.png")

    # creating buttons
    button_easy = Button(230, 235, pygame.image.load(
        "assets/button_easy.png"), 1.2)
    button_medium = Button(230, 360, pygame.image.load(
        "assets/button_medium.png"), 1.2)
    button_hard = Button(230, 480, pygame.image.load(
        "assets/button_hard.png"), 1.2)
    button_back = Button(440, 685, pygame.image.load(
        "assets/button_back.png"), 1.2)

    # menu lopp
    while True:
        screen.blit(difficulty_image, (0, 0))

        if pygame.event.poll().type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # buttons logic
        if button_easy.draw(screen):
            GAME_DIFFICULTY = 0
            from game_loop import loop
            loop(GAME_DIFFICULTY)
        if button_medium.draw(screen):
            GAME_DIFFICULTY = 1
            from game_loop import loop
            loop(GAME_DIFFICULTY)
        if button_hard.draw(screen):
            GAME_DIFFICULTY = 2
            from game_loop import loop
            loop(GAME_DIFFICULTY)
        if button_back.draw(screen):
            from main_menu import draw_main_menu
            draw_main_menu()

        # Update the display
        pygame.display.update()


