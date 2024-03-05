import escape_window
from const_value import *
import sys
from button import Button
import start_window
from load_image import load_image


# Страница правил
def rules():
    running = True

    while running:
        pos = pygame.mouse.get_pos()
        screen.blit(load_image("img/fon.jpg"), (0, 0))

        rules_text = ["Правила", "",
                      "Их покачто нету",
                      "Играем во что дано",]
        text_coord = 60
        for line in rules_text:
            str_render = get_font(74).render(line, 1, WHITE)
            intro_rect = str_render.get_rect()
            intro_rect.top = text_coord
            intro_rect.x = WINDOW_WIDTH // 2 - intro_rect.width // 2
            text_coord += intro_rect.height
            screen.blit(str_render, intro_rect)
            text_coord += 10

        rules_start_button = Button(image=None, pos=(WINDOW_WIDTH // 3, 600),
                                    text_input="На главную", font=get_font(48),
                                    base_color=GRAY, hover_color=EXIT_RED)
        rules_pause_button = Button(image=None, pos=(WINDOW_WIDTH // 1.5, 600),
                                    text_input="Пауза", font=get_font(48),
                                    base_color=GRAY, hover_color=EXIT_RED)

        rules_start_button.change_color(pos)
        rules_start_button.update(screen)

        rules_pause_button.change_color(pos)
        rules_pause_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rules_start_button.check_for_input(pos):
                    start_window.start_window()
                if rules_pause_button.check_for_input(pos):
                    escape_window.escape_window()
        pygame.display.flip()