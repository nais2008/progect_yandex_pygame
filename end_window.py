import const_value
from rules import *
import game
from load_image import load_image
import pygame
from button import Button
import sys


def end_window():
    running = True

    while running:
        const_value.screen.blit(load_image("img/fon.jpg"), (0, 0))

        pos = pygame.mouse.get_pos()
        menu_text = const_value.get_font(100).render(f"Конец. Счет: {str(const_value.COUNT)}", True, const_value.WHITE)
        menu_rect = menu_text.get_rect(center=(const_value.WINDOW_WIDTH // 2, 60))
        play_button = Button(image=None, pos=(const_value.WINDOW_WIDTH // 2, 250),
                             text_input="Играть", font=const_value.get_font(75),
                             base_color=const_value.GRAY,
                             hover_color=const_value.START_GREEN)
        rules_button = Button(image=None, pos=(const_value.WINDOW_WIDTH // 2, 350),
                              text_input="Правила", font=const_value.get_font(75),
                              base_color=const_value.GRAY,
                              hover_color=const_value.WHITE)
        quit_button = Button(image=None, pos=(const_value.WINDOW_WIDTH // 2, 680),
                             text_input="Выйти", font=const_value.get_font(48),
                             base_color=const_value.GRAY,
                             hover_color=const_value.EXIT_RED)
        const_value.screen.blit(menu_text, menu_rect)

        for button in [play_button, rules_button, quit_button]:
            button.change_color(pos)
            button.update(const_value.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(pos):
                    game.start_play()
                    const_value.COUNT = 0
                if rules_button.check_for_input(pos):
                    rules()
                if quit_button.check_for_input(pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()
    pygame.quit()
    sys.exit()