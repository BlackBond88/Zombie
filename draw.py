import pygame as pg
from math import pi, cos, sin


class Draw:
    """
    Класс отечает за прорисовку объектов в игре
    """
    def __init__(self, screen):
        self.screen = screen

    def rotation(self, x, y, rect_width, rect_hieght, image_original, angle):
        """
        Поворачиваем картинку и отображаем ее
        :param x: координаты центра картинки, во круг которой будет происходить поворот
        :param y: координата
        :param image_original: изображение, которое нужно повернуть
        :param angle: угол поворота
        """
        image_rotate = pg.transform.rotate(image_original, angle)
        rect = image_rotate.get_rect(center=(x, y), size=(rect_width, rect_hieght))

        # x = x + rect_width / 2
        # y = y + rect_hieght / 2
        #rect_width = rect_hieght * sin(angle)
       # rect_hieght = rect_hieght * cos(angle)
        self.screen.blit(image_rotate, rect)

        # тест соприкосновения прямоугольников
        x = x - image_rotate.get_width() / 2
        y = y - image_rotate.get_height() / 2
        pg.draw.rect(self.screen, (255, 0, 0), (x, y, rect_width, rect_hieght), 1)

        return rect
