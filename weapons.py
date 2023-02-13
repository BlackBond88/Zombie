import pygame as pg
from settings import *


class Weapons:
    """
    Класс, отвечающий за оружие главного героя
    """
    def __init__(self, human):
        self.width = 4
        self.height = 4
        self.x = human.x + human.width
        self.y = human.y + human.height / 2 - self.height / 2

    def draw(self, human, sc):
        self.x = human.x + human.width
        self.y = human.y + human.height / 2 - self.height / 2
        pg.draw.rect(sc, RED, (self.x, self.y, self.width, self.height))
