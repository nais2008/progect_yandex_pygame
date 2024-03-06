from spaceship import *
from meteorit import *
import sys
from check_collision import check_collisions
import const_value
from end_window import end_window


# начало игры
def start_play():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    sp = Player("img/anim_sp/0.png", 20)
    const_value.COUNT = 5

    global bullets

    meteorits = pygame.sprite.Group()
    meteorits.add(Meteorit("img/anim_met1/0.png", met1))
    meteorits.add(Meteorit("img/anim_met1/0.png", met1))
    meteorits.add(Meteorit("img/anim_met2/0.png", met2))
    meteorits.add(Meteorit("img/anim_met2/0.png", met2))

    running = True
    while running:
        clock = pygame.time.Clock()
        screen.blit(load_image("img/fon.jpg"), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        check_collisions(bullets, meteorits)

        bullets.draw(screen)
        bullets.update()

        sp.update()
        sp.animation()

        meteorits.draw(screen)
        meteorits.update()

        collisions = pygame.sprite.spritecollide(sp, meteorits, False)
        for meteorite in collisions: #
            if meteorite.rect.colliderect(sp.rect):
                sp.decrease_lives()
                # При наличии нескольких жизней и желании остановить столкновение после первого удара, можно добавить:
                meteorite.rect.y = -100
                const_value.COUNT -= 1
        if sp.lives <= 0:
            end_window()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()