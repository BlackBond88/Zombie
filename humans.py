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
        self.counter_idle = 0
        self.counter_shoot = 0
        self.counter_move = 0
        self.counter_feet = 0
        self.shots_animation = False

        self.image_humans = load_image('rifle', 'idle', 20)  # загружает картинки
        self.image_humans_shoot = load_image('rifle', 'shoot', 3)
        self.image_humans_move = load_image('rifle', 'move', 20)
        self.image_humans_feet = load_image('feet', 'run', 20)

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

        self.animation()

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

    def animation(self):
        n_image_humans_idle = 20 - 1
        n_image_humans_shoot = 3 - 1
        n_image_humans_move = 20 - 1
        speed_animation_idle = 10
        speed_animation_shoot = 4
        speed_animation_move = 4

        if self.move_up or self.move_down or self.move_left or self.move_right:
            self.rect = self.draw.rotation(self.x, self.y,
                                           self.image_humans_feet[self.counter_feet // speed_animation_move],
                                           self.angle)
            if self.counter_feet == n_image_humans_move * speed_animation_move:
                self.counter_feet = 0
            else:
                self.counter_feet += 1
        if self.shots_animation:    # TODO

            self.rect = self.draw.rotation(self.x, self.y, self.image_humans_shoot[self.counter_shoot // speed_animation_shoot], self.angle)

            if self.counter_shoot == n_image_humans_shoot * speed_animation_shoot:
                self.counter_shoot = 0
                self.shots_animation = False
            else:
                self.counter_shoot += 1
        elif self.move_up or self.move_down or self.move_left or self.move_right:
            self.rect = self.draw.rotation(self.x, self.y,
                                           self.image_humans_move[self.counter_move // speed_animation_move],
                                           self.angle)
            if self.counter_move == n_image_humans_move * speed_animation_move:
                self.counter_move = 0
            else:
                self.counter_move += 1
        else:
            self.rect = self.draw.rotation(self.x, self.y, self.image_humans[self.counter_idle // speed_animation_idle], self.angle)
            if self.counter_idle == n_image_humans_idle * speed_animation_idle:
                self.counter_idle = 0
            else:
                self.counter_idle += 1
