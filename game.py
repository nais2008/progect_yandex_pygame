import sys
from spaceship import *


def start_play():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    sp = Player("img/anim_sp/0.png", 20)
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
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    sys.exit()