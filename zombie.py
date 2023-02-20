import pygame as pg
from settings import *
from math import pi, cos, sin, atan2


class Zombies:
    """
    Класс, отвечающий за зомби в игре
    """
    def __init__(self, human, x, y):
        self.x = x
        self.y = y
        self.human_class = human
        self.angle = human.angle
        self.zombie_image = pg.image.load('Images/zombie.png')

    def draw(self, screen):
        self.move()
        zombie_image_rotate = pg.transform.rotate(self.zombie_image, self.angle)  # поворачиваем оригинал
        rect_zombie = zombie_image_rotate.get_rect(center=(self.x, self.y))  # область с координатами в центре
        screen.blit(zombie_image_rotate, rect_zombie)
        self.x += ZOMBIE_SPEED * cos(self.angle * pi / 180)
        self.y -= ZOMBIE_SPEED * sin(self.angle * pi / 180)

    def move(self):
        x = self.human_class.x
        y = self.human_class.y
        # делаем начало координат в центре героя
        coord_x = x - self.x
        coord_y = y - self.y
        # вычисляем угол между точками в градусах
        self.angle = (180 / pi) * atan2(coord_x, coord_y) - 90