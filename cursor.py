import pygame as pg


class Mouse:
    """
    Класс, занимающийся курсором мыши
    """
    def __init__(self, screen, image_name):
        self.image_cursor = pg.image.load(image_name).convert_alpha()
        self.screen = screen

    def draw(self):
        """
        Функция рисует картинку на месте курсора
        """
        pg.mouse.set_visible(False)     # скрывает курсор

        mouse_x, mouse_y = pg.mouse.get_pos()

        image_height, image_width = self.image_cursor.get_size()         # определяем размер изображения
        center_cursor_x = mouse_x - image_width / 2                      # определяем центр изображения в курсор
        center_cursor_y = mouse_y - image_height / 2
        self.screen.blit(self.image_cursor, (center_cursor_x, center_cursor_y))
