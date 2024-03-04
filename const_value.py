import pygame

# data pygame
pygame.font.init()

SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
CAPTION = "game которая заслуживает 100 баллов"
ICON = pygame.image.load("data/img/logo.jpg")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.init()
pygame.display.set_caption(CAPTION)
pygame.display.set_icon(ICON)


def get_font(font_size):
    return pygame.font.Font("data/font/font.otf", font_size)


FPS = 20

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (105, 105, 105)
EXIT_RED = (255, 100, 100)
START_GREEN = (100, 255, 100)