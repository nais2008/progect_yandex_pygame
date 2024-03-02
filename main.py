import pygame
import sys
import os
import const_value


def main():
    pygame.init()
    screen = pygame.display.set_mode((const_value.WINDOW_WIDTH, const_value.WINDOW_HEIGHT))
    pygame.display.set_caption(const_value.CAPTION)
    pygame.display.set_icon(const_value.ICON)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.display.quit()


if __name__ == "__main__":
    main()