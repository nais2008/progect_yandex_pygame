import pygame
from load_image import load_image


class Spaceship(pygame.sprite.Sprite):
    image = load_image("")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Spaceship.image
        self.rect = self.image.get_rect()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    s