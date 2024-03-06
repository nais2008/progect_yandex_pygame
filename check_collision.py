from meteorit import *
from spaceship import *
import const_value


def check_collisions(bullets, meteors):
    collisions = pygame.sprite.groupcollide(bullets, meteors, True, True)
    # Обработка столкновений
    for bullet, meteorites in collisions.items():
        for met in meteorites:
            met.animation()
            new_meteor = [Meteorit("img/anim_met1/0.png", met1),
                          Meteorit("img/anim_met2/0.png", met2)]
            meteors.add(new_meteor[random.randrange(0, 2)])
            const_value.COUNT += 1