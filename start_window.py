import pygame
import os
import sys
import const_value


pygame.init()
screen = pygame.display.set_mode((const_value.WINDOW_WIDTH, const_value.WINDOW_HEIGHT))
pygame.display.set_caption(const_value.CAPTION)
pygame.display.set_icon(const_value.ICON)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def start_window():
    intro_text = ["Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('img/fon.jpg'), (const_value.WINDOW_WIDTH, const_value.WINDOW_HEIGHT + 80))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    clock = pygame.time.Clock()
    for line in intro_text:
        string_rendered = font.render(line, 1, const_value.BLACK)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = const_value.WINDOW_WIDTH // 2 - 150
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                main()  # начинаем игру
        pygame.display.flip()
        clock.tick(const_value.FPS)
    pygame.quit()
    sys.exit()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.display.quit()