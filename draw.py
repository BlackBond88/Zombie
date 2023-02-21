import pygame as pg


class Draw:
    """
    Класс отечает за прорисовку объектов в игре
    """
    def __init__(self, screen):
        self.screen = screen

    def draw(self, x, y, image_original, angle):
        image_rotate = pg.transform.rotate(image_original, angle)
        rect = image_rotate.get_rect(center=(x, y))
        self.screen.blit(image_rotate, rect)
