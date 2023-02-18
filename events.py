import pygame as pg


def events(human):
    """
    Функция, отвечающая за события в игре
    human: класс главного героя
    """
    for event in pg.event.get():
        # выход из игры
        if event.type == pg.QUIT:
            exit()
        # события при нажатой клавише
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                human.move_left = True
            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                human.move_right = True
            elif event.key == pg.K_UP or event.key == pg.K_w:
                human.move_up = True
            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                human.move_down = True
        # события при отжатии клавиши
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                human.move_left = False
            elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                human.move_right = False
            elif event.key == pg.K_UP or event.key == pg.K_w:
                human.move_up = False
            elif event.key == pg.K_DOWN or event.key == pg.K_s:
                human.move_down = False
        if event.type == pg.MOUSEBUTTONDOWN:
            human.shot()
