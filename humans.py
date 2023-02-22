from bullets import *
from draw import *
from count import *


class Humans:
    """
    Класс, занимающийся главным героем
    """

    def __init__(self, image_name, speed, screen, human_draw, zombies):
        self.x = WIDTH / 2  # координаты главного героя (ГГ) выравниваются по центру экрана игры
        self.y = HEIGHT / 2
        self.size = HUMAN_SIZE  # размеры главного героя
        self.move_left = False  # параметр для движения главного героя при зажатой кнопке
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.angle = 0  # угол между мышкой и положением главного героя
        self.image_human = pg.image.load(image_name)  # загружаем изображение героя
        self.speed = speed
        self.screen = screen
        self.shots = False
        self.bullet_list = []
        self.draw = human_draw
        self.rect = 0
        self.zombies = zombies

    def move(self):
        """
        Функция, отвечающая за движение главного героя
        screen: экран главной игры
        """
        self.move_ban()

        if self.move_left:
            self.x -= self.speed
        if self.move_right:
            self.x += self.speed
        if self.move_up:
            self.y -= self.speed
        if self.move_down:
            self.y += self.speed

        # отрисовка главного героя
        mouse_x, mouse_y = pg.mouse.get_pos()

        self.angle = count_angle(mouse_x, mouse_y, self.x, self.y)

        self.rect = self.draw.rotation(self.x, self.y, self.size, self.image_human, self.angle)

        self.zombie_attack_test()

        if self.shots:
            for bullet in self.bullet_list:
                bullet.draw()  # отрисовка пули
                # проверяем, попала ли пуля в зомби
                bullet.killing_zombie_test(self.zombies)

    def shot(self):
        """
        Функция, которая создает пули
        """
        self.shots = True
        bullet = Bullets(self)
        self.bullet_list.append(bullet)

    def delete_bullet(self):
        """
        Функция пробегает весь список пуль и удаляет те, которые с меткой Delete
        """
        i = 0
        for bullet in self.bullet_list:
            if bullet.delete:
                del self.bullet_list[i]
            i += 1

    def move_ban(self):
        if self.x > WIDTH - self.size:
            self.move_right = False
        if self.x < self.size:
            self.move_left = False
        if self.y > HEIGHT - self.size:
            self.move_down = False
        if self.y < self.size:
            self.move_up = False

    def zombie_attack_test(self):
        # проверяем соприкосновение зомби с главным героем
        for zombie in self.zombies:
            if self.rect.colliderect(zombie.rect):
                dist = count_distance(self.x, self.y, zombie.x, zombie.y)
                if dist <= self.size + zombie.size:  # проверяем по радиусу от центров объектов
                    exit()
