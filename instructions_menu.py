from GLOBALS import *


def draw_instructions_menu():

    # set screen title
    pygame.display.set_caption("Instructions")

    # set screen image
    instructions_image = pygame.image.load("assets/instructions.png")

    # creating buttons
    button_back = Button(440, 685, pygame.image.load("assets/button_back.png"), 1.2)

    # menu lopp
    while True:
        screen.blit(instructions_image, (0, 0))

        # check if exit button is clicked
        if pygame.event.poll().type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # buttons logic
        if button_back.draw(screen):
            from main_menu import draw_main_menu
            draw_main_menu()

        # Update the display
        pygame.display.update()


