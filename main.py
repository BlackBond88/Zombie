from cursor import *
from events import *
from weapons import *
from humans import *



def run_game():
    """
    Функция, отвечающая за запуск игры
    """
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))   # главный экран игры
    pg.display.set_caption(NAME)

    my_mouse = Mouse()                              # создаем свой курсор мышки
    human = Humans()                                # создаем главного героя
    pistol = Weapons(human)                         # создаем оружие (пистолет)

    # главный цикл игры
    while True:
        events(human)               # модуль, отвечающий за события в игре

        screen.fill(BLACK)          # заливает экран черным цветом

        my_mouse.draw(screen)       # прорисовка курсора
        human.draw(screen)          # прорисовка главного героя
        # pistol.draw(human, screen)  # прорисовка оружия

        pg.display.flip()


run_game()
