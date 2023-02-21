import pygame as pg
from settings import *
from math import pi, cos, sin


class Bullets:
    """
    Класс, отвечающий за пули
    """
    def __init__(self, human):
        self.angle = human.angle - 180

        # Пересчитываем координаты вылета пули относительно положения главного героя
        self.x = human.x - 59 * cos(self.angle * pi / 180)
        self.y = human.y + 59 * sin(self.angle * pi / 180)

        self.bullet_image = pg.image.load('Images/bullet.png')
        self.delete = False
        self.human_class = human

    def draw(self):
        """
        Функция прорисовки и движения пули
        """
        self.human_class.draw.rotation(self.x, self.y, self.bullet_image, self.angle)

        self.x -= BULLET_SPEED * cos(self.angle * pi / 180)
        self.y += BULLET_SPEED * sin(self.angle * pi / 180)

        self.test_position()

    def test_position(self):
        """
        Если пуля покидает экран - удалеет ее
        """
        if self.x > WIDTH or self.x < 0 or self.y > HEIGHT or self.y < 0:
            self.delete = True
            self.human_class.delete_bullet()
