from cursor import *
from events import *
from weapons import *
from humans import *
from zombie import *
import random


def run_game():
    """
    Функция, отвечающая за запуск игры
    """
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))   # главный экран игры
    background_image = pg.image.load('Images/background.jpg')
    pg.display.set_caption(NAME)
    clock = pg.time.Clock()                         # скорость игры (FPS)

    my_mouse = Mouse('Images/cursor.png')               # создаем свой курсор мышки
    human = Humans('Images/human.png', HUMAN_SPEED, screen)     # создаем главного героя

    zombies = []
    for i in range(20):
        x_zombi = random.random() * WIDTH
        y_zombi = random.random() * HEIGHT
        zombie = Zombies(human, x_zombi, y_zombi)
        zombies.append(zombie)

    pistol = Weapons(human)                             # создаем оружие (пистолет)

    # главный цикл игры
    while True:
        clock.tick(FPS)

        events(human)               # модуль, отвечающий за события в игре

        screen.blit(background_image, (0, 0))       # отрисовывается фон игры

        for zombie in zombies:
            zombie.draw(screen)

        my_mouse.draw(screen)       # прорисовка курсора
        human.draw()                # прорисовка главного героя

        # pistol.draw(human, screen)  # прорисовка оружия

        pg.display.flip()


run_game()
