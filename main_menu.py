from GLOBALS import *


def draw_main_menu():

    # set screen title
    pygame.display.set_caption("Main menu")

    # set screen image
    menu_image = pygame.image.load("assets/menu.png")

    # creating buttons
    button_play = Button(440, 210, pygame.image.load(
        "assets/button_play.png"), 1.2)
    button_instructions = Button(
        440, 375, pygame.image.load("assets/button_instructions.png"), 1.2)
    button_exit = Button(440, 540, pygame.image.load(
        "assets/button_exit.png"), 1.2)

    # menu lopp
    while True:
        screen.blit(menu_image, (0, 0))

        # check if exit button is clicked
        if button_exit.draw(screen) or pygame.event.poll().type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # buttons logic
        if button_instructions.draw(screen):
            from instructions_menu import draw_instructions_menu
            draw_instructions_menu()
        if button_play.draw(screen):
            from difficulty_menu import draw_difficulty_menu
            draw_difficulty_menu()

        # Update the display
        pygame.display.update()
