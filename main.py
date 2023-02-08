import pygame


Size_game = (1000, 800)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((Size_game))

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True


run_game()
