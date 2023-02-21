import pygame as pg


class Draw:
    """
    Класс отечает за прорисовку объектов в игре
    """
    def __init__(self, screen):
        self.screen = screen

    def rotation(self, x, y, image_original, angle):
        """
        Поворачиваем картинку и отображаем ее
        :param x: координаты центра картинки, во круг которой будет происходить поворот
        :param y: координата
        :param image_original: изображение, которое нужно повернуть
        :param angle: угол поворота
        """
        image_rotate = pg.transform.rotate(image_original, angle)
        rect = image_rotate.get_rect(center=(x, y))
        self.screen.blit(image_rotate, rect)
