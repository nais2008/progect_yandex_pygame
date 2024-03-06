import rules
from const_value import *
from load_image import *
from button import Button
import game


def escape_window():
    running = True

    while running:
        screen.blit(load_image("img/fon.jpg"), (0, 0))

        pos = pygame.mouse.get_pos()
        menu_text = get_font(100).render("Пауза", True, WHITE)
        menu_rect = menu_text.get_rect(center=(WINDOW_WIDTH // 2, 60))
        play_button = Button(image=None,
                             pos=(WINDOW_WIDTH // 2, 350),
                             text_input="Продолжить", font=get_font(75),
                             base_color=GRAY,
                             hover_color=START_GREEN)
        rules_button = Button(image=None,
                              pos=(WINDOW_WIDTH // 2, 450),
                              text_input="Правила", font=get_font(75),
                              base_color=GRAY,
                              hover_color=WHITE)
        screen.blit(menu_text, menu_rect)

        for button in [play_button, rules_button]:
            button.change_color(pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(pos):
                    game.start_play()
                if rules_button.check_for_input(pos):
                    rules.rules()
        pygame.display.flip()
    pygame.quit()
    sys.exit()