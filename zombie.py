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
        self.zombie_image = pg.image.load('Images/zombie.png')

    def move(self, human_x, human_y, draw, human):
        # вычисляем угол между главным героем и зомби
        angle = count_angle(human_x, human_y, self.x, self.y)

        # отрисовка зомби
        self.rect = draw.rotation(self.x, self.y, ZOMBIE_WIDTH, ZOMBIE_HIEGHT, self.zombie_image, angle)

        # двигаем замби к главному герою
        self.x += ZOMBIE_SPEED * cos(angle * pi / 180)
        self.y -= ZOMBIE_SPEED * sin(angle * pi / 180)

        self.human = human  # временно
        if self.rect.colliderect(human.rect):
            exit()
