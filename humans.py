import pygame as pg
from settings import *
from math import pi, atan2


class Humans:
    """
    Класс, занимающийся главным героем
    """
    def __init__(self, image_name, speed):
        self.x = WIDTH / 2              # координаты главного героя (ГГ) выравниваются по центру экрана игры
        self.y = HEIGHT / 2
        self.width = WIDTH_HUMAN        # размеры главного героя
        self.height = HEIGHT_HUMAN
        self.move_left = False          # параметр для движения главного героя при зажатой кнопке
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.angle = 0                  # угол между мышкой и положением главного героя
        self.image_human = pg.image.load(image_name)        # загружаем изображение героя
        self.speed = speed

    def draw(self, screen):
        """
        Функция, отвечающая за движение главного героя
        screen: экран главной игры
        """
        if self.move_left:
            self.x -= self.speed
        if self.move_right:
            self.x += self.speed
        if self.move_up:
            self.y -= self.speed
        if self.move_down:
            self.y += self.speed

        # отрисовка главного героя
        self.mouse_angle()
        image_human_rotate = pg.transform.rotate(self.image_human, self.angle)
        rect_human = image_human_rotate.get_rect(center=(self.x, self.y))
        screen.blit(image_human_rotate, rect_human)

    def mouse_angle(self):
        """
        Функция, которая высчитывает угол между курсором и главным героем
        """
        mouse_x, mouse_y = pg.mouse.get_pos()
        # делаем начало координат в центре героя
        coord_x = mouse_x - self.x
        coord_y = mouse_y - self.y
        # вычисляем угол между точками в градусах
        self.angle = (180 / pi) * atan2(coord_x, coord_y) - 90
