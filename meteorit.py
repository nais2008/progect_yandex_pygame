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

        self.anim = animation_images
        self.count = 0

    def update(self):
        if self.rect.y < WINDOW_HEIGHT - 20:
            self.rect.y += self.speed
        else:
            self.rect.y = 0 - self.rect.height
            self.rect.x = random.randrange(0, WINDOW_WIDTH - self.rect.width)
            self.speed = random.randrange(3, 12)

    def animation(self):
        screen.blit(self.anim[(self.count // 2) % 3],
                    (self.rect.x, self.rect.y))
        self.count += 1