import pygame


WHITE = (254, 254, 254)
BLACK = (0, 0, 0)


class Human:
    def __init__(self):
        self.health = 100
        self.x, self.y = pygame.display.get_surface().get_size()
        self.x = int(self.x/2)
        self.y = int(self.y/2)
        self.moveleft = False


    def draw(self, sc):
        if self.moveleft:
            self.x -= 1
        pygame.draw.rect(sc, WHITE, (self.x, self.y, 10, 10))



def run_game():
    pygame.init()
    size_game = (1000, 800)
    screen = pygame.display.set_mode((size_game))
    pygame.display.set_caption('Zombies in the city')

    game_over = False
    blackbond = Human()     # создаем главного героя
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    blackbond.moveleft = True
            elif event.type == pygame.KEYUP:
                blackbond.moveleft = False

        blackbond.draw(screen)   # должно вызываться в отдельном классе

        pygame.display.flip()
        screen.fill(BLACK)


run_game()
