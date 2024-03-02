import pygame

# data pygame
pygame.font.init()

SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 720
CAPTION = "game которая заслуживает 100 баллов"
ICON = pygame.image.load("data/img/logo.jpg")


def get_font(font_size):
    return pygame.font.Font("data/font/font.otf", font_size)


FPS = 120
BG_START = pygame.image.load("data/img/fon.png")

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (175, 175, 175)