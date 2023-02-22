import pygame as pg
from settings import *
from math import cos, sin
from count import *


class Bullets:
    """
    Класс, отвечающий за пули
    """
    def __init__(self, human):
        self.angle = human.angle - 180

        # Пересчитываем координаты вылета пули относительно положения главного героя
        self.x = human.x - 59 * cos(self.angle * pi / 180)
        self.y = human.y + 59 * sin(self.angle * pi / 180)
        self.size = BULLET_SIZE
        self.bullet_image = pg.image.load('Images/bullet.png')
        self.delete = False
        self.human_class = human
        self.rect = 0

    def draw(self):
        """
        Функция прорисовки и движения пули
        """
        self.rect = self.human_class.draw.rotation(self.x, self.y, self.size, self.bullet_image, self.angle)

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

    def killing_zombie_test(self, zombies):
        # проверяем попадает ли пуля в зомби
        i = 0
        for zombie in zombies:
            if self.rect.colliderect(zombie.rect):
                dist = count_distance(self.x, self.y, zombie.x, zombie.y)
                if dist <= self.size + zombie.size:  # проверяем по радиусу от центров объектов
                    del zombies[i]
                    self.delete = True
                    self.human_class.delete_bullet()
            i += 1
