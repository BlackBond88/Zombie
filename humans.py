from bullets import *
from draw import *
from count import *
from load import *
import time


class Humans:
    """
    Класс, занимающийся главным героем
    """
    def __init__(self, speed, screen, human_draw, zombies):
        self.x = WIDTH / 2  # координаты главного героя (ГГ) выравниваются по центру экрана игры
        self.y = HEIGHT / 2
        self.size = HUMAN_SIZE  # размеры главного героя
        self.move_left = False  # параметр для движения главного героя при зажатой кнопке
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.speed = speed
        self.screen = screen
        self.shots = False
        self.rect = 0
        self.angle = 0
        self.bullet_list = []
        self.draw = human_draw
        self.zombies = zombies
        self.image_humans = []
        self.i = 0
        self.j = 0
        self.shots_animation = False

        self.image_humans = load_image('rifle', 'idle', 20)  # загружает картинки
        self.image_humans_shoot = load_image('rifle', 'shoot', 3)

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

        if self.shots_animation:    # TODO
            n = 4  # анимация выстрела со скоростью n (без движения)
            self.rect = self.draw.rotation(self.x, self.y, self.image_humans_shoot[self.j // n], self.angle)
            if self.j == 2 * n:
                self.i = 0
                self.j = 0
                self.shots_animation = False
            else:
                self.j += 1
        else:
            n = 10  # анимация героя со скоростью n (без движения)
            self.rect = self.draw.rotation(self.x, self.y, self.image_humans[self.i // n], self.angle)
            if self.i == 19 * n:
                self.i = 0
                self.j = 0
            else:
                self.i += 1

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
        self.shots_animation = True
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
        pass
        for zombie in self.zombies:
            if self.rect.colliderect(zombie.rect):
                dist = count_distance(self.x, self.y, zombie.x, zombie.y)
                if dist <= self.size + zombie.size:  # проверяем по радиусу от центров объектов
                    self.draw.writes_text('YOU LOSE')
                    time.sleep(2)
                    exit()
