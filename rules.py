from const_value import *
import sys
from button import Button
import start_window


# Страница правил
def rules():
    running = True

    while running:
        pos = pygame.mouse.get_pos()
        screen.fill(BLACK)

        rules_text = get_font(64).render("This is the RULES screen.", True, WHITE)
        rules_rect = rules_text.get_rect(center=(WINDOW_WIDTH // 2, 260))
        screen.blit(rules_text, rules_rect)

        rules_back_button = Button(image=None, pos=(WINDOW_WIDTH // 2, 500),
                                   text_input="Назад", font=get_font(36),
                                   base_color=GRAY, hover_color=WHITE)

        rules_back_button.change_color(pos)
        rules_back_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rules_back_button.check_for_input(pos):
                    start_window.start_window()
        pygame.display.flip()