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

    def draw(self, screen):
        """
        Функция прорисовки и движения пули
        """
        bullet_image_rotate = pg.transform.rotate(self.bullet_image, self.angle)    # поворачиваем оригинал
        rect_bullet = bullet_image_rotate.get_rect(center=(self.x, self.y))         # область с координатами в центре
        screen.blit(bullet_image_rotate, rect_bullet)

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
