import pygame as pg
from math import pi, cos, sin


class Bullets:
    def __init__(self, human):
        self.x = human.x
        self.y = human.y
        self.bullet_image = pg.image.load('Images/bullet.png')
        self.angle = human.angle - 180

    def drow(self, screen):
        bullet_image_rotate = pg.transform.rotate(self.bullet_image, self.angle)
        rect_bullet = bullet_image_rotate.get_rect(center=(self.x, self.y))
        screen.blit(bullet_image_rotate, rect_bullet)

        self.angle_rota = self.angle * pi / 180

        self.x -= 20 * cos(self.angle_rota)
        self.y += 20 * sin(self.angle_rota)
