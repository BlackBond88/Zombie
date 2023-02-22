import pygame as pg
from count import *
from settings import *
from math import pi, cos, sin
import random


class Zombies:
    """
    Класс, отвечающий за зомби в игре
    """

    def __init__(self):
        self.x = random.random() * WIDTH
        self.y = random.random() * HEIGHT
        self.size = ZOMBIE_SIZE
        self.zombie_image = pg.image.load('Images/zombie.png')

    def move(self, draw, human):
        # вычисляем угол между главным героем и зомби
        angle = count_angle(human.x, human.y, self.x, self.y)

        # отрисовка зомби
        rect = draw.rotation(self.x, self.y, self.size, self.zombie_image, angle)

        # двигаем замби к главному герою
        self.x += ZOMBIE_SPEED * cos(angle * pi / 180)
        self.y -= ZOMBIE_SPEED * sin(angle * pi / 180)

        # проверяем соприкосновение зомби с главным героем
        if rect.colliderect(human.rect):
            dist = count_distance(self.x, self.y, human.x, human.y)
            if dist <= self.size + human.size:      # проверяем по радиусу от центров объектов
                exit()
