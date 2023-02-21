import pygame as pg
from settings import *
from math import pi, cos, sin, atan2


class Zombies:
    """
    Класс, отвечающий за зомби в игре
    """
    def __init__(self, human, x, y):
        self.x = x
        self.y = y
        self.human_class = human
        self.angle = human.angle
        self.zombie_image = pg.image.load('Images/zombie.png')

    def draw(self):
        self.move()
        self.human_class.draw_human.draw(self.x, self.y, self.zombie_image, self.angle)
        self.x += ZOMBIE_SPEED * cos(self.angle * pi / 180)
        self.y -= ZOMBIE_SPEED * sin(self.angle * pi / 180)

    def move(self):
        x = self.human_class.x
        y = self.human_class.y
        # делаем начало координат в центре героя
        coord_x = x - self.x
        coord_y = y - self.y
        # вычисляем угол между точками в градусах
        self.angle = (180 / pi) * atan2(coord_x, coord_y) - 90
