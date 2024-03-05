from const_value import *
from load_image import load_image


# логика пули
class Bullet(pygame.sprite.Sprite):
    def __init__(self, coord_x):
        super().__init__()
        self.image = load_image("img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.x = coord_x + self.rect.width * 1.95
        self.rect.y = 500
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed