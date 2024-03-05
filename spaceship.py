from escape_screen import escape_screen
from bullet import *


walk_left = [
    load_image("img/anim_sp/2.png"),
    load_image("img/anim_sp/1.png"),
    load_image("img/anim_sp/0.png")
]
walk_right = [
    load_image("img/anim_sp/0.png"),
    load_image("img/anim_sp/1.png"),
    load_image("img/anim_sp/2.png")
]
bullets = pygame.sprite.Group()


# параметры карабля
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__()
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH // 2 - self.rect.width // 2
        self.rect.y = 525
        self.left = False
        self.right = False
        self.count = 0
        self.speed = speed
        self.xp = 100


# управление караблем
class Player(Spaceship):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            print("esc")
            escape_screen()
        elif keys[pygame.K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
            self.left = True
            self.right = False
        elif keys[pygame.K_RIGHT] and self.rect.x < WINDOW_WIDTH - (self.rect.width + 7):
            self.rect.x += self.speed
            self.left = False
            self.right = True
        elif keys[pygame.K_SPACE]:
            new_bullet = Bullet(self.rect.x)
            bullets.add(new_bullet)
        else:
            self.left = False
            self.right = False
            self.count = 0

    def animation(self):
        if self.count >= 20:
            self.count = 0
        if self.left == True:
            screen.blit(walk_left[(self.count // 10) % 3], (self.rect.x, self.rect.y))
            self.count += 1
        elif self.right == True:
            screen.blit(walk_right[(self.count // 10) % 3], (self.rect.x, self.rect.y))
            self.count += 1
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))