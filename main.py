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

    zombies = []
    for i in range(ZOMBIE_NUMBER):
        zombie = Zombies()
        zombies.append(zombie)

    human = Humans('Images/human.png', HUMAN_SPEED, screen, draw, zombies)  # создаем главного героя

    # pistol = Weapons(human)                             # создаем оружие (пистолет)

    # главный цикл игры
    game_over = False
    while not game_over:
        clock.tick(FPS)

        events(human)               # модуль, отвечающий за события в игре

        screen.blit(background_image, (0, 0))       # отрисовывается фон игры

        for zombie in zombies:
            zombie.move(draw, human.x, human.y)

        human.move()                # прорисовка главного героя

        my_mouse.draw()       # прорисовка курсора

        # pistol.draw(human, screen)  # прорисовка оружия

        pg.display.flip()


run_game()
