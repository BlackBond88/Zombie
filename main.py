from cursor import *
from events import *
# from weapons import *
from humans import *
from zombie import *


def run_game():
    """
    Функция, отвечающая за запуск игры
    """
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))   # главный экран игры
    background_image = pg.image.load('Images/background.jpg')
    pg.display.set_caption(NAME)
    clock = pg.time.Clock()                         # скорость игры (FPS)

    my_mouse = Mouse(screen, 'Images/cursor.png')               # создаем свой курсор мышки
    draw = Draw(screen)
    human = Humans('Images/human.png', HUMAN_SPEED, screen, draw)     # создаем главного героя

    zombies = []
    for i in range(1):
        zombie = Zombies()
        zombies.append(zombie)

    # pistol = Weapons(human)                             # создаем оружие (пистолет)

    # главный цикл игры
    game_over = False
    while not game_over:
        clock.tick(FPS)

        events(human)               # модуль, отвечающий за события в игре

        screen.blit(background_image, (0, 0))       # отрисовывается фон игры

        human.move()                # прорисовка главного героя

        for zombie in zombies:
            zombie.move(human.x, human.y, draw, human)

        my_mouse.draw()       # прорисовка курсора


        # pistol.draw(human, screen)  # прорисовка оружия

        pg.display.flip()


run_game()
