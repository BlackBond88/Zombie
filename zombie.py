import pygame as pg
from settings import *
from math import pi, cos, sin, atan2


class Zombies:
    """
    Класс, отвечающий за зомби в игре
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.zombie_image = pg.image.load('Images/zombie.png')

    def move(self, human_x, human_y, draw):
        # вычисляем угол между главным героем и зомби
        coord_x = human_x - self.x
        coord_y = human_y - self.y
        angle = (180 / pi) * atan2(coord_x, coord_y) - 90

        draw.rotation(self.x, self.y, self.zombie_image, angle)     # отрисовываем зомби

        # двигаем замби к главному герою
        self.x += ZOMBIE_SPEED * cos(angle * pi / 180)
        self.y -= ZOMBIE_SPEED * sin(angle * pi / 180)
