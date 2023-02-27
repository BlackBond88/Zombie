import pygame as pg
from settings import *


class Draw:
    """
    Класс отечает за прорисовку объектов в игре
    """
    def __init__(self, screen):
        self.screen = screen

    def rotation(self, x, y, image_original, angle):
        """
        Поворачиваем картинку и отображаем ее
        """
        image_rotate = pg.transform.rotate(image_original, angle)
        rect = image_rotate.get_rect(center=(x, y))

        self.screen.blit(image_rotate, rect)

        # pg.draw.circle(self.screen, (255, 0, 0), (x, y), 4, 3)

        return rect

    def writes_text(self, text):
        temp_font = pg.font.Font(None, 206)
        text = temp_font.render(text, True, RED)
        text_rect = text.get_rect()
        text_rect.centerx = WIDTH // 2
        text_rect.y = HEIGHT * 0.4
        self.screen.blit(text, text_rect)
        pg.display.flip()
