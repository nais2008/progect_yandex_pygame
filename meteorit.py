from load_image import load_image
from const_value import *
import random


# логика метеорита
class Meteorit(pygame.sprite.Sprite):
    def __init__(self, image, animation_images):
        super().__init__()
        self.image = load_image(image)

        self.speed = random.randrange(3, 7)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = 0

        self.animation_images = [load_image(image) for image in animation_images]
        self.animation_index = 0
        self.exploding = False

    def update(self):
        if self.rect.y < WINDOW_HEIGHT - 20:
            self.rect.y += self.speed
        else:
            self.rect.y = 0 - self.rect.height
            self.rect.x = random.randrange(0, WINDOW_WIDTH - self.rect.width)
            self.speed = random.randrange(3, 12)

    def check_collision_with_spaceship(self, spaceship):
        if pygame.sprite.collide_rect(self, spaceship):
            spaceship.decrease_lives()