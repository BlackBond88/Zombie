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

    # human_image_name = 'Images/human.png'

    human_image_names = []
    for i in range(19):
        name = 'Images/Top_Down_Survivor/rifle/idle/survivor-idle_rifle_' + str(i) + '.png'
        human_image_names.append(name)

    human = Humans(human_image_names, HUMAN_SPEED, screen, draw, zombies)  # создаем главного героя

    # pistol = Weapons(human)                             # создаем оружие (пистолет)

    # главный цикл игры
    game_over = False
    game_pause = False
    while not game_over:
        clock.tick(FPS)
        game_pause = events(human, game_pause)               # модуль, отвечающий за события в игре
        screen.blit(background_image, (0, 0))       # отрисовывается фон игры

        for zombie in zombies:
            zombie.move(draw, human.x, human.y)

        human.move()                # прорисовка главного героя

        # цикл, когда в игре нажата пауза
        while game_pause:
            draw.writes_text('Pause')
            for event in pg.event.get():
                # выход из игры
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                        game_pause = False
                events_keys(event, human)

        my_mouse.draw()       # прорисовка курсора
        # pistol.draw(human, screen)  # прорисовка оружия

        pg.display.flip()


run_game()
