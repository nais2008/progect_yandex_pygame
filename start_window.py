import os
import sys
from const_value import *
from load_image import load_image
from button import Button


pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(CAPTION)
pygame.display.set_icon(ICON)


# Начало игры
def play():
    pass


# Правила
def rules():
    running = True

    while running:
        pos = pygame.mouse.get_pos()
        screen.fill(BLACK)

        rules_text = get_font(48).render("This is the RULES screen.", True, WHITE)
        rules_rect = rules_text.get_rect(center=(640, 260))
        screen.blit(rules_text, rules_rect)

        rules_back_button = Button(image=None, pos=(640, 460),
                                   text_input="Back", font=get_font(36),
                                   base_color=BLACK, hover_color=GRAY)
        rules_back_button.change_color(pos)
        rules_back_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rules_back_button.check_for_input(pos):
                    start_window()


# Выход
def quit_game():
    pygame.quit()
    sys.exit(1)


# стартовая страница
def start_window():
    running = True
    while running:
        screen.blit(BG_START, (0, 0))

        pos = pygame.mouse.get_pos()
        menu_text = get_font(100).render("Меню", True, WHITE)
        menu_rect = menu_text.get_rect(center=(590, 100))
        play_button = Button(image=None, pos=(590, 250),
                             text_input="Играть", font=get_font(75),
                             base_color=pygame.color.Color("#8f8f8f"),
                             hover_color=WHITE)
        rules_button = Button(image=None, pos=(590, 400),
                              text_input="Правила", font=get_font(75),
                              base_color=pygame.color.Color("#8f8f8f"),
                              hover_color=WHITE)
        quit_button = Button(image=None, pos=(590, 600),
                             text_input="Выйти", font=get_font(75),
                             base_color=pygame.color.Color("#8f8f8f"),
                             hover_color=WHITE)
        screen.blit(menu_text, menu_rect)

        for button in [play_button, rules_button, quit_button]:
            button.change_color(pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(pos):
                    play()
                if rules_button.check_for_input(pos):
                    rules()
                if quit_button.check_for_input(pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
    sys.exit()