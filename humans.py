import pygame as pg
from settings import *
from math import sqrt, pi, acos


class Humans:
    """
    Класс, занимающийся главным героем
    """
    def __init__(self):
        self.x = WIDTH / 2          # координаты главного героя (ГГ) выравниваются по центру экрана игры
        self.y = HEIGHT / 2
        self.width = WIDTH_HUMAN             # размеры главного героя
        self.height = HEIGHT_HUMAN
        self.move_left = False      # параметр для движения главного героя при зажатой кнопке
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.angle = 0              # угол между мышкой и положением главного героя

    def draw(self, screen):
        """
        Функция, отвечающая за движение главного героя
        screen: экран главной игры
        """
        if self.move_left:
            self.x -= 1
        elif self.move_right:
            self.x += 1
        elif self.move_up:
            self.y -= 1
        elif self.move_down:
            self.y += 1

        # отрисовка главного героя
        main_hero = pg.Surface((self.width, self.height))                           # новая поверхность для героя
        main_hero.fill(WHITE)                                                       # цвет поверхности
        main_hero.set_colorkey((1, 1, 1))                                           # скрывает ненужные поверхности..
        # отрисовывает поверхность в полученных координатах под углом (angle) к курсору
        # TODO https: // www.cyberforum.ru / python - pygame / thread2261270.html
        screen.blit(pg.transform.rotate(main_hero, self.angle), (self.x, self.y))
        # проверка ветвления номер два

    def mouse_angle(self, mouse_position):
        """
        Функция, которая высчитывает угол между курсором и главным героем
        mouse_position: координаты мышки в формате (x, y)
        """
        mouse_x, mouse_y = mouse_position
        mouse_x -= self.x                                               # делаем начало координат в центре героя
        mouse_y -= self.y

        # вычисляем сосинус угола по координатам
        if mouse_x != 0 or mouse_y != 0:
            cos_angle = mouse_x / sqrt(mouse_x * mouse_x + mouse_y * mouse_y)
        else:
            cos_angle = 1

        # вычисляем угол и переводим из радиан в градусы
        if mouse_y <= 0:
            self.angle = acos(cos_angle) / pi * 180
        if mouse_y > 0:
            self.angle = 360 - acos(cos_angle) / pi * 180
