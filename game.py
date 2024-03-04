import sys
from spaceship import *
from meteorit import *


def start_play():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    sp = Player("img/anim_sp/0.png", 20)
    meteorits = pygame.sprite.Group()
    meteorits.add(Meteorit("img/anim_met1/0.png", 10))
    meteorits.add(Meteorit("img/anim_met2/6.png", 12))
    meteorits.add(Meteorit("img/anim_met2/0.png", 8))
    running = True
    while running:
        clock = pygame.time.Clock()
        screen.blit(load_image("img/fon.jpg"), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        sp.update()
        sp.animation()
        meteorits.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()