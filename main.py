from settings import *
from events import *


class Humans:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.width = 12
        self.height = 12
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def draw(self, sc):
        if self.move_left:
            self.x -= 1
        if self.move_right:
            self.x += 1
        if self.move_up:
            self.y -= 1
        if self.move_down:
            self.y += 1
        pygame.draw.rect(sc, WHITE, (self.x, self.y, self.width, self.height))


class Weapons:
    def __init__(self, human):
        self.width = 4
        self.height = 4
        self.x = human.x + human.width
        self.y = human.y + human.height / 2 - self.height / 2


    def draw(self, human, sc):
        self.x = human.x + human.width
        self.y = human.y + human.height / 2 - self.height / 2
        pygame.draw.rect(sc, RED, (self.x, self.y, self.width, self.height))


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(NAME)

    human = Humans()  # создаем главного героя
    pistol = Weapons(human)
    while True:
        events(human)

        screen.fill(BLACK)

        human.draw(screen)  # должно вызываться в отдельном классе
        pistol.draw(human, screen)

        pygame.display.flip()


run_game()
