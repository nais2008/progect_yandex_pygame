from load_image import load_image
from const_value import *
import random


class Meteorit(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()
        self.image = load_image(image)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = 0

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.rect.y = 0 - self.rect.height