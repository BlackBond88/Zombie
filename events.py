import pygame


def events(human):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                human.move_left = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                human.move_right = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                human.move_up = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                human.move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                human.move_left = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                human.move_right = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                human.move_up = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                human.move_down = False
