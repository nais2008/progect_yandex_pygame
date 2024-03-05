from spaceship import *
from meteorit import *
import sys


def start_play():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    sp = Player("img/anim_sp/0.png", 20)

    meteorits = pygame.sprite.Group()
    meteorits.add(Meteorit("img/anim_met1/0.png"))
    meteorits.add(Meteorit("img/anim_met1/0.png"))
    meteorits.add(Meteorit("img/anim_met2/0.png"))
    meteorits.add(Meteorit("img/anim_met2/0.png"))

    running = True
    while running:
        clock = pygame.time.Clock()
        screen.blit(load_image("img/fon.jpg"), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bullets.update()

        sp.update()
        sp.animation()

        meteorits.draw(screen)
        meteorits.update()

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()