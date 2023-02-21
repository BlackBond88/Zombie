from math import pi, atan2


def count_angle(x_2, y_2, x_1, y_1):
    """
    Функция, которя считает угол между объектами
    """
    x = x_2 - x_1
    y = y_2 - y_1
    angle = (180 / pi) * atan2(x, y) - 90
    return angle
