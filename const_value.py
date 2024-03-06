import pygame

# data pygame
pygame.font.init()

COUNT = 0

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

met1 = [
    "img/anim_met1/0.png",
    "img/anim_met1/1.png",
    "img/anim_met1/2.png",
    "img/anim_met1/3.png",
    "img/anim_met1/4.png",
    "img/anim_met1/5.png"
]
met2 = [
    "img/anim_met2/0.png",
    "img/anim_met2/1.png",
    "img/anim_met2/2.png",
    "img/anim_met2/3.png",
    "img/anim_met2/4.png",
    "img/anim_met2/5.png",
    "img/anim_met2/6.png"
]

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (105, 105, 105)
EXIT_RED = (255, 100, 100)
START_GREEN = (100, 255, 100)