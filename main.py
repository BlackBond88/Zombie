from settings import *
from events import *


class Humans:
    def __init__(self):
        self.health = 100
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
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
        pygame.draw.rect(sc, WHITE, (self.x, self.y, 10, 10))


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(NAME)

    human = Humans()  # создаем главного героя
    while True:
        events(human)

        screen.fill(BLACK)

        human.draw(screen)  # должно вызываться в отдельном классе

        pygame.display.flip()


run_game()
