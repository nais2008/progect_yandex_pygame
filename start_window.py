from rules import *
from game import start_play


# стартовая страница
def start_window():
    running = True

    while running:
        screen.blit(load_image("img/fon.jpg"), (0, 0))

        pos = pygame.mouse.get_pos()
        menu_text = get_font(100).render("Меню", True, WHITE)
        menu_rect = menu_text.get_rect(center=(WINDOW_WIDTH // 2, 60))
        play_button = Button(image=None, pos=(WINDOW_WIDTH // 2, 250),
                             text_input="Играть", font=get_font(75),
                             base_color=GRAY,
                             hover_color=START_GREEN)
        rules_button = Button(image=None, pos=(WINDOW_WIDTH // 2, 350),
                              text_input="Правила", font=get_font(75),
                              base_color=GRAY,
                              hover_color=WHITE)
        quit_button = Button(image=None, pos=(WINDOW_WIDTH // 2, 680),
                             text_input="Выйти", font=get_font(48),
                             base_color=GRAY,
                             hover_color=EXIT_RED)
        screen.blit(menu_text, menu_rect)

        for button in [play_button, rules_button, quit_button]:
            button.change_color(pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(pos):
                    start_play()
                if rules_button.check_for_input(pos):
                    rules()
                if quit_button.check_for_input(pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()
    pygame.quit()
    sys.exit()