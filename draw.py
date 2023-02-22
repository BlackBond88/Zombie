import pygame as pg
from math import pi, cos, sin


class Draw:
    """
    Класс отечает за прорисовку объектов в игре
    """
    def __init__(self, screen):
        self.screen = screen

    def rotation(self, x, y, radius, image_original, angle):
        """
        Поворачиваем картинку и отображаем ее
        """
        image_rotate = pg.transform.rotate(image_original, angle)
        rect = image_rotate.get_rect(center=(x, y))

        self.screen.blit(image_rotate, rect)

        # pg.draw.circle(self.screen, (255, 0, 0), (x, y), radius, 3)

        return rect
